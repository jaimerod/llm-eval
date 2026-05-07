# llm-eval

Automated benchmark tool for evaluating locally-hosted LLM models via [Ollama](https://ollama.com). Runs a structured 300-question benchmark across 6 capability categories, generates visualizations, and writes a per-model Markdown report. Each run automatically updates this file with a link to the full report.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Make sure Ollama is running and the model is available
ollama pull llama3.2

# 3. Run the evaluation
python main.py --model llama3.2
```

Results land in `evaluations/llama3.2/` and this file is updated with a new row in the index below.

---

## CLI Reference

```
python main.py --model <name> [--output-dir <path>]
```

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--model` | Yes | — | Ollama model name exactly as it appears in `ollama list` |
| `--output-dir` | No | `evaluations` | Root folder where per-model result directories are written |

**Examples**

```bash
# Evaluate a specific model tag
python main.py --model llama3.2:3b

# Write results to a custom directory
python main.py --model mistral --output-dir /data/results

# Evaluate multiple models back-to-back
for model in llama3.2 mistral gemma2; do
    python main.py --model $model
done
```

Colons in model names (e.g. `llama3.2:3b`) are replaced with underscores in directory names (`evaluations/llama3.2_3b/`).

---

## Output Structure

After a run for `llama3.2`:

```
evaluations/
└── llama3.2/
    ├── report.md              ← full evaluation report
    └── charts/
        ├── category_scores.png    ← horizontal bar chart by category
        ├── radar_chart.png        ← spider/radar capability profile
        └── latency_distribution.png  ← box + jitter plot of response times
README.md                      ← updated with a new row in the index table
```

**`report.md`** contains:
- Overall score and per-category breakdown table
- Performance metrics (avg latency, estimated tokens/sec)
- Embedded chart images
- Full question-by-question detail with the model's raw response and per-question score

Charts are embedded in `report.md` using relative paths, so they render on GitHub when you navigate into the report.

---

## Evaluation Methodology

### Categories

The benchmark covers 6 categories with 50 questions each (300 total). All questions are sent with `temperature: 0` for deterministic, reproducible results.

| Category | Questions | What it tests |
|----------|-----------|---------------|
| **Reasoning** | 50 | Logical deduction, puzzles, causal inference, probability, combinatorics |
| **Mathematics** | 50 | Arithmetic, algebra, calculus, combinatorics, geometry, number theory |
| **Knowledge** | 50 | Factual recall across history, science, geography, literature, biology |
| **Code** | 50 | Python code generation and syntax validity, from basic to advanced algorithms |
| **Instruction Following** | 50 | Adherence to format constraints (word count, JSON, line count, exact strings) |
| **Agentic** | 50 | Multi-turn context retention, task decomposition, structured tool-call generation |

The **Overall Score** is the unweighted mean of all six category scores, scaled to 0–100.

### Scoring Functions

Each `Question` is assigned a `score_fn` that determines how its response is evaluated. All scorers return a float in `[0.0, 1.0]`.

| `score_fn` | Used by | Logic |
|------------|---------|-------|
| `keyword` | Reasoning, Knowledge | Splits `expected` on whitespace into keywords; score = fraction present (case-insensitive) in the response |
| `math` | Mathematics, Reasoning | Extracts all numbers from response via regex; score = 1.0 if any number matches `expected` within ±0.01, else 0.0 |
| `syntax` | Code | Strips fenced code blocks; 0.5 for valid `ast.parse()`, 0.5 for presence of expected identifier. Max 1.0 |
| `instruction` | Instruction Following | Dispatches on special sentinel values: `10_words` checks word count, `haiku_lines` checks line count, `{"french"` validates full JSON parse, else falls back to `keyword` |
| `agentic_context` | Agentic | Sends two turns; scores only the follow-up response for keyword recall. Penalises responses under 5 words |
| `agentic_decompose` | Agentic | 60% weight on numbered step count in first response (≥4 steps = full credit), 40% weight on whether follow-up references the plan |
| `agentic_tool` | Agentic | Extracts JSON from response; scores 1/3 each for correct `name`, `city`, and `units` fields |

### Agentic Category Detail

The Agentic category is specifically designed to surface failures common in autonomous task pipelines:

- **Context retention (Q1–Q10):** Seeds facts in turn 1, asks the model to recall them exactly in turn 2. Tests whether the model maintains conversation state across a wide range of domain contexts (configs, salaries, project specs, etc.). Sent as real multi-turn `ollama.chat()` calls with the full message history.
- **Task decomposition & follow-through (Q11–Q20):** Asks for a numbered plan in turn 1, then asks the model to execute or elaborate on a specific step in turn 2 while referencing its own plan. Tests self-consistency across a variety of engineering and operational scenarios.
- **Simulated tool use (Q21–Q50):** Provides a JSON tool schema and asks the model to produce a valid tool-call object for a described user request. Covers 30 diverse tools — weather, CRUD, finance, scheduling, messaging, infrastructure, and more — testing structured output capability and parameter inference under varied complexity.

### Score Interpretation

| Range | Rating | Meaning |
|-------|--------|---------|
| 70–100 | Good | Reliable for production use in this category |
| 40–69 | Fair | Usable with supervision; expect occasional errors |
| 0–39 | Poor | Unreliable for this capability; consider a different model |

---

## Repository Structure

```
llm-eval/
├── main.py              ← entire application (single file)
├── requirements.txt     ← pip dependencies
├── README.md            ← this file; auto-updated with evaluation index
├── RUNBOOK.md           ← deployment and operations guide
└── evaluations/         ← created on first run
    └── <model>/
        ├── report.md
        └── charts/
```

---

## Developer Guide

### Data Structures

**`Question`** (`main.py:33`) — one benchmark item.

| Field | Type | Description |
|-------|------|-------------|
| `category` | `str` | Display name; groups questions in the report |
| `prompt` | `str` | Text sent to the model as the user message |
| `expected` | `str` | Reference value used by the scorer |
| `score_fn` | `str` | Key that selects which scorer to call |
| `follow_up` | `str \| None` | If set, a second turn is sent with this text |
| `follow_up_expected` | `str \| None` | Reference value for the follow-up scorer |

**`QuestionResult`** (`main.py:43`) — outcome of one question execution.

| Field | Type | Description |
|-------|------|-------------|
| `question` | `Question` | The original question |
| `response` | `str` | Model's first-turn response |
| `score` | `float` | Final score `[0.0, 1.0]` |
| `latency_ms` | `float` | Wall-clock time for the first Ollama call |
| `follow_up_response` | `str \| None` | Model's second-turn response if applicable |

### Adding a Question

Append a `Question` to the `QUESTIONS` list (`main.py:55`). Pick the most appropriate existing `score_fn`. If the category is new, it will automatically appear in charts and the report — no other changes needed. With 50 questions per category the benchmark is already demanding; new questions should add coverage gaps rather than redundancy.

```python
Question(
    category="Reasoning",
    prompt="If all roses are flowers and some flowers fade quickly, can we conclude all roses fade quickly? Answer Yes or No.",
    expected="no",
    score_fn="keyword",
),
```

### Adding a Category

1. Add questions with the new `category` string to `QUESTIONS`.
2. No other code changes are required — `aggregate_results`, `generate_charts`, and `write_report` all derive categories dynamically from the question list.

Note: the radar chart works best with 5–8 categories. Beyond that, the axis labels start overlapping.

### Adding a Scoring Function

1. Write a function with signature `(response: str, ...) -> float` alongside the existing scorers (`main.py:353`).
2. Add a new `if fn == "your_fn_name":` branch in `compute_score` (`main.py:440`).
3. Use the new `score_fn` key in your `Question` definitions.

### How the README Index Works

`update_main_index` (`main.py:689`) reads `README.md`, finds any existing row for the model by regex, replaces it if found, or appends a new row at the end. The function is **idempotent** — re-running for the same model updates rather than duplicates the row. The table header at the bottom of this file is the anchor; rows are appended directly after it.

---

## Requirements

- Python 3.12+
- [Ollama](https://ollama.com) running locally (default: `http://localhost:11434`)
- The target model pulled via `ollama pull <name>`

Python packages (`requirements.txt`):

| Package | Purpose |
|---------|---------|
| `ollama` | Python client for the Ollama REST API |
| `matplotlib` | Chart generation (saved as PNG, never displayed) |
| `numpy` | Score averaging and radar chart geometry |
| `tqdm` | Progress bar during benchmark execution |

---

## Evaluation Index

| Model | Score | Tokens/sec | Date | Report |
|-------|------:|-----------:|------|--------|
| `gemma4:e4b` | 91.6 / 100 | 29.7 | 2026-05-06 | [Report](evaluations/gemma4_e4b/report.md) |
| `qwen3-coder-next:q4_K_M` | 95.2 / 100 | 5.2 | 2026-05-06 | [Report](evaluations/qwen3-coder-next_q4_K_M/report.md) |
| `deepseek-coder-v2:16b` | 93.3 / 100 | 166.2 | 2026-05-06 | [Report](evaluations/deepseek-coder-v2_16b/report.md) |
| `qwen3-coder:30b` | 96.0 / 100 | 24.4 | 2026-05-06 | [Report](evaluations/qwen3-coder_30b/report.md) |
| `nemotron-3-super:cloud` | 98.9 / 100 | 1.2 | 2026-05-06 | [Report](evaluations/nemotron-3-super_cloud/report.md) |
