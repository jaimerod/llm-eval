# LLM Evaluation Report: `nemotron-3-super:cloud`

**Date:** 2026-05-06  
**Overall Score:** 98.9 / 100

---

## Summary

| Category | Score | Questions |
|----------|------:|----------:|
| Reasoning | 93.3 | 5 |
| Mathematics | 100.0 | 5 |
| Knowledge | 100.0 | 5 |
| Code | 100.0 | 5 |
| Instruction Following | 100.0 | 5 |
| Agentic | 100.0 | 5 |

## Performance Metrics

| Metric | Value |
|--------|------:|
| Average latency | 24767 ms |
| Estimated tokens / sec | 1.2 |
| Total questions | 30 |

---

## Visualizations

![Category Scores](charts/category_scores.png)

![Capability Radar](charts/radar_chart.png)

![Latency Distribution](charts/latency_distribution.png)

---

## Detailed Results

### Reasoning

**Q1:** All cats are mammals. Some mammals are pets. Garfield is a cat. Is Garfield a mammal? Answer with just 'Yes' or 'No' and one sentence explanation.

> Yes Garfield is a cat, and all cats are mammals.

**Score:** `1.00` &nbsp; **Latency:** `27514 ms`

**Q2:** If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets? Answer with just the number and unit.

> 5 minutes

**Score:** `1.00` &nbsp; **Latency:** `20449 ms`

**Q3:** A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost? Answer with just the amount in cents.

> 5

**Score:** `1.00` &nbsp; **Latency:** `17451 ms`

**Q4:** You have two buckets: one holds 3 liters, one holds 5 liters. How do you measure exactly 4 liters using only these two buckets? Describe the steps briefly.

> 1. Fill the 5‑liter bucket completely.  
2. Pour from the 5‑liter bucket into the 3‑liter bucket until the latter is full.  
   → 5‑L bucket now has 2 L left, 3‑L bucket has 3 L.  
3. Empty the 3‑liter bucket.  
4. Transfer the 2 L from the 5‑liter bucket into the empty 3‑liter bucket.  
   → 5‑L bucket is empty, 3‑L bucket holds 2 L.  
5. Fill the 5‑liter bucket again.  
6. Pour from the 5‑liter bucket into the 3‑liter bucket until the latter is full (it needs only 1 L).  
   → 5‑L bucket now contains exactly 4 L, and the 3‑L bucket is full (3 L).  

You now have exactly 4 liters in the 5‑lit…

**Score:** `1.00` &nbsp; **Latency:** `26965 ms`

**Q5:** Three boxes contain: apples, oranges, and both. All labels are wrong. You may pick one fruit from one box. Which box label do you pick from to identify all three boxes? Name the mislabeled box you should pick from.

> Pick from the box labeled **“both.”** Since every label is wrong, that box cannot actually contain both fruits; it must hold only apples **or** only oranges. Seeing which fruit it contains lets you deduce the correct contents of the other two boxes. So the mislabeled box you should sample from is the one labeled **both**.

**Score:** `0.67` &nbsp; **Latency:** `19406 ms`


### Mathematics

**Q1:** What is 15% of 240? Answer with just the number.

> 36

**Score:** `1.00` &nbsp; **Latency:** `13290 ms`

**Q2:** A train travels at 60 mph. How far does it travel in 2 hours and 30 minutes? Answer with just the number in miles.

> 150

**Score:** `1.00` &nbsp; **Latency:** `27637 ms`

**Q3:** What is the square root of 144? Answer with just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `9678 ms`

**Q4:** A rectangle has a length of 8 cm and width of 5 cm. What is its area? Answer with just the number and unit.

> 40 cm²

**Score:** `1.00` &nbsp; **Latency:** `16078 ms`

**Q5:** Solve for x: 3x + 7 = 22. Answer with just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `15647 ms`


### Knowledge

**Q1:** What is the chemical symbol for gold? Answer with just the symbol.

> Au

**Score:** `1.00` &nbsp; **Latency:** `20820 ms`

**Q2:** In what year did World War II end? Answer with just the year.

> 1945

**Score:** `1.00` &nbsp; **Latency:** `11928 ms`

**Q3:** What is the capital of Australia? Answer with just the city name.

> Canberra

**Score:** `1.00` &nbsp; **Latency:** `15520 ms`

**Q4:** Who wrote the play 'Hamlet'? Answer with just the author's last name.

> Shakespeare

**Score:** `1.00` &nbsp; **Latency:** `14709 ms`

**Q5:** What is the approximate speed of light in a vacuum? Answer with just the value in km/s (round to nearest 1000).

> 300000

**Score:** `1.00` &nbsp; **Latency:** `14981 ms`


### Code

**Q1:** Write a Python function called `fibonacci` that takes an integer n and returns the nth Fibonacci number (0-indexed). Return only the function code, no explanation.

> def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

**Score:** `1.00` &nbsp; **Latency:** `14161 ms`

**Q2:** Write a Python one-liner that reverses a string variable called `s`. Return only the code, no explanation.

> s = s[::-1]

**Score:** `1.00` &nbsp; **Latency:** `16436 ms`

**Q3:** Write a Python function called `is_palindrome` that returns True if a string is a palindrome, False otherwise. Return only the function code.

> ```python
def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, False otherwise."""
    return s == s[::-1]
```

**Score:** `1.00` &nbsp; **Latency:** `20445 ms`

**Q4:** Write a Python list comprehension that creates a list of squares of even numbers from 1 to 20. Return only the expression.

> [x**2 for x in range(1, 21) if x % 2 == 0]

**Score:** `1.00` &nbsp; **Latency:** `87494 ms`

**Q5:** Write a Python function called `count_words` that takes a string and returns the number of words in it. Return only the function code.

> ```python
def count_words(s):
    return len(s.split())
```

**Score:** `1.00` &nbsp; **Latency:** `20516 ms`


### Instruction Following

**Q1:** List exactly 3 benefits of exercise. Format your response as a numbered list. Include no additional text before or after the list.

> 1. Improves cardiovascular health and reduces risk of heart disease.
2. Enhances mood and reduces symptoms of anxiety and depression.
3. Increases muscle strength, bone density, and overall functional fitness.

**Score:** `1.00` &nbsp; **Latency:** `25599 ms`

**Q2:** Respond to this message in exactly 10 words, no more, no less: 'What is the weather like today?'

> Today it's sunny, mild, light clouds, gentle breeze outside now

**Score:** `1.00` &nbsp; **Latency:** `33148 ms`

**Q3:** Translate the word 'hello' into French, Spanish, and German. Format your answer as JSON with keys 'french', 'spanish', 'german'.

> {
  "french": "bonjour",
  "spanish": "hola",
  "german": "hallo"
}

**Score:** `1.00` &nbsp; **Latency:** `18868 ms`

**Q4:** Write a haiku (5-7-5 syllable structure) about the ocean. Output only the haiku — no title, no explanation.

> Waves whisper low tide sigh  
Moon pulls the restless sea tonight  
Salt kisses the warm shore

**Score:** `1.00` &nbsp; **Latency:** `34583 ms`

**Q5:** List the days of the week in reverse order, one per line, using ALL CAPS. No other text.

> SUNDAY
SATURDAY
FRIDAY
THURSDAY
WEDNESDAY
TUESDAY
MONDAY

**Score:** `1.00` &nbsp; **Latency:** `18510 ms`


### Agentic

**Q1:** I'm planning a birthday party for my friend Alex who loves jazz music, is allergic to peanuts, and lives in Chicago. Please acknowledge these details — I'll ask you about them in a moment.

> Got it! I’ve noted that Alex loves jazz music, has a peanut allergy, and lives in Chicago. Feel free to ask about any of those details whenever you’re ready.

**Follow-up:** What are the three key facts I told you about Alex? List them.

> Here are the three key facts you shared about Alex:  
1. Alex loves jazz music.  
2. Alex is allergic to peanuts.  
3. Alex lives in Chicago.  

Let me know if you'd like to build on these details for the party planning! 🎷🥜🌆

**Score:** `1.00` &nbsp; **Latency:** `19295 ms`

**Q2:** My project has three requirements: it must use Python, it must be completed by Friday, and the budget is $500. Acknowledge these constraints.

> Understood. Your project requires:  
1. Implementation in Python  
2. Completion by Friday  
3. Adherence to a $500 budget  

I acknowledge all three constraints as stated. Let me know how you’d like to proceed within these parameters.

**Follow-up:** What are the three project requirements I gave you? List each one.

> Here are the three project requirements you specified, listed exactly as stated:  

1. It must use Python.  
2. It must be completed by Friday.  
3. The budget is $500.  

I confirm these constraints as acknowledged in our prior exchange. Let me know how you’d like to proceed.

**Score:** `1.00` &nbsp; **Latency:** `39969 ms`

**Q3:** I want to build a REST API that reads from a database and returns JSON. Give me a numbered step-by-step plan with exactly 5 steps.

> 1. Choose a language/framework (e.g., Python + FastAPI, Node.js + Express, Java + Spring Boot) and set up the project skeleton.  
2. Define the database schema and configure a connection (ORM or driver) to your chosen DB (SQL, NoSQL).  
3. Create API endpoints (routes) that map HTTP methods to functions which query the database and retrieve the needed data.  
4. Serialize the query results into JSON objects (using built‑in serializers or libraries) and return them as HTTP responses with appropriate status codes.  
5. Test the API locally (e.g., with curl, Postman, or automated tests), then dep…

**Follow-up:** Now execute step 1 from the plan you just gave me. Be specific and reference your plan.

> **Executing Step 1 of the plan**  
*(Step 1: “Choose a language/framework (e.g., Python + FastAPI, Node.js + Express, Java + Spring Boot) and set up the project skeleton.”)*  

I will select **Python + FastAPI** as the language/framework and create the initial project skeleton.

---

### 1.1 Create the project directory  
```bash
mkdir my-fastapi-api
cd my-fastapi-api
```

### 1.2 Initialize a vir…

**Score:** `1.00` &nbsp; **Latency:** `22389 ms`

**Q4:** I need to migrate a legacy monolithic application to microservices. Give me a numbered plan with exactly 4 steps.

> 1. **Map and Decompose the Monolith**: Analyze the existing codebase to identify business capabilities, data domains, and logical boundaries using techniques like domain-driven design (DDD) or event storming; define clear, loosely-coupled microservice boundaries based on high cohesion and low coupling, prioritizing services with minimal dependencies for initial extraction.  
2. **Implement the Strangler Pattern**: Gradually replace monolithic functionality with new microservices by routing specific requests (e.g., via API gateway or feature toggles) to the new services while keeping the legacy…

**Follow-up:** Based on the plan you just provided, what does step 2 involve? Reference your exact wording.

> Step 2 involves:  
"Implement the Strangler Pattern: Gradually replace monolithic functionality with new microservices by routing specific requests (e.g., via API gateway or feature toggles) to the new services while keeping the legacy system running; start with low-risk, high-value components (e.g., user authentication or product catalog) to validate the approach and reduce risk."

**Score:** `1.00` &nbsp; **Latency:** `60682 ms`

**Q5:** You have access to the following tool:  {   "name": "get_weather",   "description": "Get current weather for a city",   "parameters": {     "city": {"type": "string", "description": "City name"},     "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}   },   "required": ["city", "units"] }  A user says: "What's the weather in Tokyo in Celsius?"  Respond with ONLY a valid JSON object representing the tool call. No explanation.

> {
  "name": "get_weather",
  "arguments": {
    "city": "Tokyo",
    "units": "celsius"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `38835 ms`
