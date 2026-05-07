# llm-eval Runbook

Operational guide for deploying, running, monitoring, and troubleshooting the `llm-eval` benchmark tool.

---

## Table of Contents

1. [System Requirements](#1-system-requirements)
2. [Installation](#2-installation)
3. [Running Evaluations](#3-running-evaluations)
4. [Output Artifacts](#4-output-artifacts)
5. [Batch & Scheduled Evaluation](#5-batch--scheduled-evaluation)
6. [Troubleshooting](#6-troubleshooting)
7. [Maintenance](#7-maintenance)
8. [CI/CD Integration](#8-cicd-integration)
9. [Security & Access Notes](#9-security--access-notes)

---

## 1. System Requirements

### Hardware

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 8 GB | 16 GB+ |
| GPU VRAM | — (CPU-only works) | 8 GB+ (NVIDIA/AMD/Apple Silicon) |
| Disk | 5 GB free | 20 GB+ for multiple large models |
| CPU | 4 cores | 8+ cores for CPU inference |

> Models are loaded and kept in memory by Ollama for a short period after use. Running multiple large models in sequence can cause OOM if RAM/VRAM is tight.

### Software

| Dependency | Version | Notes |
|------------|---------|-------|
| Python | 3.12+ | Uses `list[T]` and `match` syntax |
| Ollama | 0.1.38+ | Must be running as a service before invoking `main.py` |
| pip | Any recent | Used to install Python deps |
| git | Any | Optional; only needed if cloning the repo |

### Network

Ollama defaults to `http://localhost:11434`. No outbound internet is required at evaluation time. Internet is only needed to `ollama pull` a model for the first time.

---

## 2. Installation

### Step 1 — Install Ollama

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**macOS:**
Download from https://ollama.com and install the `.dmg`, or:
```bash
brew install ollama
```

**Windows:**
Download the installer from https://ollama.com/download/windows.

Verify:
```bash
ollama --version
```

### Step 2 — Start the Ollama service

```bash
# Linux (systemd)
sudo systemctl start ollama
sudo systemctl enable ollama   # start on boot

# macOS
ollama serve &                 # or use the menu bar app

# Verify it's listening
curl http://localhost:11434/api/tags
```

### Step 3 — Pull models to evaluate

```bash
ollama pull llama3.2
ollama pull mistral
ollama pull gemma2

# List all available local models
ollama list
```

### Step 4 — Set up the Python environment

```bash
cd /path/to/llm-eval

python3.12 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

Verify:
```bash
python main.py --help
```

---

## 3. Running Evaluations

### Single model

```bash
source .venv/bin/activate
python main.py --model llama3.2
```

Expected terminal output:

```
Model      : llama3.2
Output     : evaluations/llama3.2
Questions  : 30

Benchmarking: 100%|██████████| 30/30 [02:14<00:00]
  [Reasoning             ] score=0.80  latency=  3241 ms
  ...

──────────────────────────────────────────
  Overall Score : 74.3 / 100
──────────────────────────────────────────
  Reasoning                 80.0  ████████████████
  ...

Report : evaluations/llama3.2/report.md
Charts : evaluations/llama3.2/charts
Index  : /path/to/llm-eval/README.md
```

### Custom output directory

```bash
python main.py --model llama3.2 --output-dir /mnt/results
```

The model subdirectory is always created inside `--output-dir`. The `README.md` index is always written relative to `main.py`, regardless of `--output-dir`.

### Verifying a successful run

```bash
# Check report exists and is non-empty
ls -lh evaluations/llama3.2/report.md

# Check all three charts were generated
ls evaluations/llama3.2/charts/

# Verify README was updated
tail -5 README.md
```

---

## 4. Output Artifacts

| Path | Description | Regenerated on re-run? |
|------|-------------|----------------------|
| `evaluations/<model>/report.md` | Full Markdown report with scores, metrics, and Q&A detail | Yes, overwritten |
| `evaluations/<model>/charts/category_scores.png` | Horizontal bar chart | Yes, overwritten |
| `evaluations/<model>/charts/radar_chart.png` | Spider/radar capability profile | Yes, overwritten |
| `evaluations/<model>/charts/latency_distribution.png` | Box + jitter latency plot | Yes, overwritten |
| `README.md` | Root index; row is upserted (not duplicated) | Row updated in-place |

> Re-running for the same model **overwrites** the report and charts but only **updates** (not duplicates) the README row.

---

## 5. Batch & Scheduled Evaluation

### Evaluate all locally available models

```bash
#!/usr/bin/env bash
set -euo pipefail

cd /path/to/llm-eval
source .venv/bin/activate

ollama list --json 2>/dev/null \
  | python3 -c "import sys,json; [print(m['name']) for m in json.load(sys.stdin)['models']]" \
  | while read -r model; do
      echo "=== Evaluating: $model ==="
      python main.py --model "$model" || echo "FAILED: $model"
  done
```

### Cron job (Linux)

Run all models every Sunday at 2 AM:

```cron
0 2 * * 0 cd /path/to/llm-eval && /path/to/llm-eval/.venv/bin/python main.py --model llama3.2 >> /var/log/llm-eval.log 2>&1
```

Edit with:
```bash
crontab -e
```

### GitHub Actions (scheduled)

```yaml
# .github/workflows/eval.yml
name: LLM Evaluation

on:
  schedule:
    - cron: '0 2 * * 0'   # every Sunday at 2 AM UTC
  workflow_dispatch:        # allow manual trigger

jobs:
  evaluate:
    runs-on: self-hosted    # must be a runner with Ollama installed
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run evaluation
        run: python main.py --model llama3.2

      - name: Commit results
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add evaluations/ README.md
          git diff --staged --quiet || git commit -m "chore: evaluation results $(date -I)"
          git push
```

> **Important:** GitHub-hosted runners do not have Ollama or local models. Use a `self-hosted` runner on a machine where Ollama is installed and the target models are already pulled.

---

## 6. Troubleshooting

### Ollama not running

**Symptom:**
```
httpx.ConnectError: [Errno 111] Connection refused
```
or
```
ollama._types.ResponseError: ...
```

**Fix:**
```bash
# Check if Ollama is running
curl -s http://localhost:11434/api/tags | python3 -m json.tool

# Start it
ollama serve          # foreground
sudo systemctl start ollama   # Linux systemd
```

---

### Model not found

**Symptom:**
```
ollama._types.ResponseError: model "gemma4" not found, try pulling it first
```

**Fix:**
```bash
ollama pull gemma4

# List what's available
ollama list
```

---

### Out of memory / model crashes mid-evaluation

**Symptom:** Ollama process exits, questions after a certain point all score 0.0 with `ERROR` messages.

**Diagnosis:**
```bash
# Check system RAM
free -h

# Check GPU VRAM (NVIDIA)
nvidia-smi

# Check Ollama logs
journalctl -u ollama -n 50    # Linux systemd
```

**Fix options:**
- Use a quantised (smaller) model variant: `ollama pull llama3.2:3b` instead of the default 7B/8B
- Reduce concurrent processes (don't run Ollama + other GPU workloads simultaneously)
- Increase swap space as a last resort

---

### Charts not generated / matplotlib error

**Symptom:**
```
RuntimeError: cannot connect to X server
```
or matplotlib import fails on a headless server.

**Fix:** The script already calls `matplotlib.use("Agg")` before any other matplotlib import. If this error still appears, it means something else is importing matplotlib before `main.py` sets the backend.

```bash
# Verify the backend is set correctly
python -c "import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot; print('OK')"

# If using a display-enabled environment and want to suppress it
export MPLBACKEND=Agg
python main.py --model llama3.2
```

---

### `relative_to` ValueError (path resolution)

**Symptom:**
```
ValueError: 'evaluations/model/report.md' is not in the subpath of '/abs/path'
```

**Fix:** Run `main.py` from the repo root, or use an absolute path for `--output-dir`:

```bash
# From repo root (recommended)
cd /path/to/llm-eval
python main.py --model llama3.2

# Or with absolute output dir
python main.py --model llama3.2 --output-dir /path/to/llm-eval/evaluations
```

---

### Slow evaluation / high latency per question

**Diagnosis:**
```bash
# Check if GPU is being used by Ollama
nvidia-smi dmon -s u         # NVIDIA — watch GPU utilisation live
ollama ps                    # Shows currently loaded models and hardware
```

**Common causes and fixes:**

| Cause | Fix |
|-------|-----|
| CPU-only inference on a large model | Use a smaller model (`llama3.2:3b`) or enable GPU |
| Model is being re-loaded every question | Normal for first question; subsequent questions reuse loaded model |
| System swapping | Free RAM or use a quantised model |
| Ollama using wrong GPU | Set `CUDA_VISIBLE_DEVICES=0` or use `OLLAMA_GPU_LAYERS` env var |

---

### README.md evaluation table is malformed

**Symptom:** Rows appear outside the table or without a header after the first run.

**Cause:** The script appends rows to `README.md` at the file's end. If the `## Evaluation Index` table header was removed or the file was rearranged, the appended row has no header.

**Fix:** Ensure `README.md` ends with (no trailing blank lines after the last `|` line):
```markdown
## Evaluation Index

| Model | Score | Date | Report |
|-------|------:|------|--------|
```

The script will then append data rows directly after this header and the table will render correctly.

---

### Dependency installation fails

```bash
# Upgrade pip first
pip install --upgrade pip

# If ollama wheel fails to build
pip install --upgrade setuptools wheel
pip install ollama

# On ARM (Apple Silicon / Raspberry Pi)
pip install --extra-index-url https://pypi.org/simple/ -r requirements.txt
```

---

## 7. Maintenance

### Update a model to a newer version

```bash
ollama pull llama3.2      # pulls the latest tag
ollama list               # confirm new digest
python main.py --model llama3.2   # re-evaluate; README row is updated in place
```

### Remove old evaluation results

```bash
# Remove a specific model's results
rm -rf evaluations/old-model/

# Remove all evaluations
rm -rf evaluations/

# The README row for the removed model will still exist — clean it manually
# or re-run the evaluation to regenerate it
```

### Upgrade Python dependencies

```bash
pip install --upgrade ollama matplotlib numpy tqdm
pip freeze > requirements.txt   # optional: lock exact versions
```

### Check for Ollama updates

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh   # re-running the installer updates it
```

**macOS:**
```bash
brew upgrade ollama
```

---

## 8. CI/CD Integration

### Environment variables

No mandatory environment variables. Optional overrides:

| Variable | Default | Purpose |
|----------|---------|---------|
| `MPLBACKEND` | `Agg` (set in code) | Force non-interactive matplotlib backend |
| `OLLAMA_HOST` | `http://localhost:11434` | Point to a remote Ollama instance |
| `OLLAMA_GPU_LAYERS` | auto | Number of model layers to offload to GPU |

### Using a remote Ollama instance

```bash
export OLLAMA_HOST=http://192.168.1.100:11434
python main.py --model llama3.2
```

The `ollama` Python client reads `OLLAMA_HOST` automatically.

### Exit codes

`main.py` exits `0` on success. It exits non-zero only if Python itself raises an unhandled exception (e.g. import error, permission denied on output directory). Individual question failures are caught and logged as `ERROR` with a `0.0` score — the run still completes and exits `0`.

To fail CI when the overall score drops below a threshold, wrap the call:

```bash
#!/usr/bin/env bash
python main.py --model llama3.2

# Parse the overall score from the report
score=$(grep "Overall Score" evaluations/llama3.2/report.md | grep -oP '[\d.]+(?= / 100)')
threshold=60

if (( $(echo "$score < $threshold" | bc -l) )); then
    echo "Score $score is below threshold $threshold — failing build"
    exit 1
fi
```

---

## 9. Security & Access Notes

- **All inference is local.** No prompts, responses, or scores are sent to any external service.
- **Ollama listens on localhost** (`127.0.0.1:11434`) by default. Do not expose this port externally without authentication.
- **Output files are written to disk** in the repo directory. On shared systems, restrict directory permissions as needed.
- **No credentials are required.** The script uses no API keys or secrets.
- **Model weights** are stored by Ollama in `~/.ollama/models`. Restrict access if models are sensitive or proprietary.
