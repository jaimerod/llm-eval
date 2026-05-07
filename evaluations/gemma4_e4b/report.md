# LLM Evaluation Report: `gemma4:e4b`

**Date:** 2026-05-06  
**Overall Score:** 91.6 / 100

---

## Summary

| Category | Score | Questions |
|----------|------:|----------:|
| Reasoning | 85.8 | 50 |
| Mathematics | 93.0 | 50 |
| Knowledge | 84.0 | 50 |
| Code | 99.0 | 50 |
| Instruction Following | 90.6 | 50 |
| Agentic | 97.1 | 50 |

## Performance Metrics

| Metric | Value |
|--------|------:|
| Average latency | 2739 ms |
| Estimated tokens / sec | 29.7 |
| Total questions | 300 |

---

## Visualizations

![Category Scores](charts/category_scores.png)

![Capability Radar](charts/radar_chart.png)

![Latency Distribution](charts/latency_distribution.png)

---

## Detailed Results

### Reasoning

**Q1:** All cats are mammals. Some mammals are pets. Garfield is a cat. Is Garfield a mammal? Answer Yes or No.

> Yes

**Score:** `1.00` &nbsp; **Latency:** `1402 ms`

**Q2:** If it takes 5 machines 5 minutes to make 5 widgets, how long for 100 machines to make 100 widgets? Answer with the number and unit only.

> 5 minutes

**Score:** `1.00` &nbsp; **Latency:** `2852 ms`

**Q3:** A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost in cents? Answer with just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `2012 ms`

**Q4:** You have a 3-liter and a 5-liter bucket. How do you measure exactly 4 liters? Describe briefly.

> 1. **Fill the 3-liter bucket (B3).**
   *(State: B3 = 3L, B5 = 0L)*

2. **Pour B3 into the 5-liter bucket (B5).**
   *(State: B3 = 0L, B5 = 3L)*

3. **Fill the 3-liter bucket (B3) again.**
   *(State: B3 = 3L, B5 = 3L)*

4. **Carefully pour from B3 into B5 until B5 is full.** (B5 needs 2 more liters).
   *(State: B3 = 1L, B5 = 5L)*
   *(You have successfully isolated 1 liter in B3.)*

5. **Empty the 5-liter bucket (B5).**
   *(State: B3 = 1L, B5 = 0L)*

6. **Pour the 1 liter from B3 into B5.**
   *(State: B3 = 0L, B5 = 1L)*

7. **Fill the 3-liter bucket (B3) completely.**
   *(State: B3 = 3L, …

**Score:** `1.00` &nbsp; **Latency:** `10427 ms`

**Q5:** Three boxes are labeled Apples, Oranges, and Mixed — all labels are wrong. You pick one fruit from the Mixed box and it's an apple. What is in each box? Answer concisely.

> *   **Apples** box contains **Oranges**.
*   **Oranges** box contains **Mixed**.
*   **Mixed** box contains **Apples**.

**Score:** `0.67` &nbsp; **Latency:** `5416 ms`

**Q6:** A snail climbs 3 feet up a wall each day and slides 2 feet down each night. The wall is 10 feet tall. On which day does the snail reach the top? Just the number.

> 8

**Score:** `1.00` &nbsp; **Latency:** `4924 ms`

**Q7:** In a race you overtake the runner in 2nd place. What position are you now in? Answer with just the position.

> 2nd

**Score:** `0.50` &nbsp; **Latency:** `1014 ms`

**Q8:** How many months in a year have 28 days? Answer with just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `178 ms`

**Q9:** Mary's mother has four children: April, May, June, and one more. What is the fourth child's name?

> The fourth child's name is **Mary**.

**Score:** `1.00` &nbsp; **Latency:** `2836 ms`

**Q10:** An electric train is traveling north. The wind is blowing east. Which direction does the smoke blow from the train?

> This is a trick question!

Since the train is **electric**, it does not produce smoke.

***

**However, if we assume the train *were* a steam or diesel train producing smoke, here is the physics answer:**

The smoke would be blown **East**.

**Explanation:**

1. **Wind Dominance:** The wind is the primary force determining the direction of the smoke plume. Since the wind is blowing East, it will push the smoke in that direction.
2. **Relative Movement:** While the smoke is being pushed East by the wind, it is also being carried North by the train's movement. The resulting plume would travel ge…

**Score:** `1.00` &nbsp; **Latency:** `5315 ms`

**Q11:** A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have? Just the number.

> 9

**Score:** `1.00` &nbsp; **Latency:** `840 ms`

**Q12:** What comes next in the sequence: O, T, T, F, F, S, S, E, N, ? (Hint: think of number names)

> The next letter is **T**.

The sequence represents the first letter of the English names of consecutive numbers:

* **O** (One)
* **T** (Two)
* **T** (Three)
* **F** (Four)
* **F** (Five)
* **S** (Six)
* **S** (Seven)
* **E** (Eight)
* **N** (Nine)
* **T** (Ten)

**Score:** `1.00` &nbsp; **Latency:** `2509 ms`

**Q13:** Two mothers and two daughters go fishing. Each catches exactly one fish, yet only 3 fish are caught total. How is this possible?

> This is a classic riddle!

The key is that the people are not four distinct individuals. They are three people who fill the roles of two mothers and two daughters.

The group consists of:

1. **A Grandmother** (who is a mother)
2. **A Mother** (who is a daughter to the grandmother, and a mother herself)
3. **A Daughter** (who is a daughter to the mother)

**How the roles are filled:**

* **Two Mothers:** The Grandmother and the Mother.
* **Two Daughters:** The Mother (daughter to the Grandmother) and the Daughter (daughter to the Mother).

Since there are only **3 people**, and each person cat…

**Score:** `1.00` &nbsp; **Latency:** `5640 ms`

**Q14:** Rearrange the letters B, E, L, O, W to form a common English word.

> BELOW

**Score:** `0.00` &nbsp; **Latency:** `183 ms`

**Q15:** A lily pad doubles in size every day and covers the entire pond in 48 days. How many days does it take to cover half the pond? Just the number.

> 47

**Score:** `1.00` &nbsp; **Latency:** `1721 ms`

**Q16:** You have two ropes. Each burns in exactly 60 minutes but not at a uniform rate. How do you measure exactly 45 minutes? Explain briefly.

> This is a classic time-measurement puzzle. Since the rate is non-uniform, we cannot rely on physical length; we must rely on the total burn time.

Here is the explanation:

1. **Cut Rope A:** Cut Rope A into two pieces. The first piece must represent exactly **15 minutes** of burn time, and the second piece must represent the remaining **45 minutes** of burn time. (This step is necessary because 15 minutes is the key interval.)
2. **Start Timing:** Simultaneously light the 15-minute piece of Rope A and the entire Rope B.
3. **Wait:** Wait until the 15-minute piece of Rope A burns completely.

…

**Score:** `0.25` &nbsp; **Latency:** `11378 ms`

**Q17:** A clock shows 3:15. What is the exact angle in degrees between the hour and minute hands? Just the number.

> 7.5

**Score:** `1.00` &nbsp; **Latency:** `3088 ms`

**Q18:** You have 12 identical-looking balls; one is heavier. Using a balance scale, what is the minimum number of weighings to guarantee finding the heavy ball?

> The minimum number of weighings required is **3**.

This is a classic puzzle that relies on the fact that a balance scale has three possible outcomes (left side heavier, right side heavier, or balanced). Since each weighing can, at best, reduce the possibilities by a factor of three, we can use the formula $3^W \ge N$, where $N$ is the number of balls and $W$ is the number of weighings.

*   $3^1 = 3$ (Not enough for 12)
*   $3^2 = 9$ (Not enough for 12)
*   $3^3 = 27$ (Enough for 12)

Therefore, 3 weighings are sufficient.

***

### The Strategy (How it works in 3 weighings)

The goal is to e…

**Score:** `1.00` &nbsp; **Latency:** `13769 ms`

**Q19:** If you drive to work at 30 mph, how fast must you drive back to average 60 mph for the round trip?

> This is a classic physics problem involving average speed, and the key concept is that **average speed is calculated using the total distance divided by the total time**, not the average of the two speeds.

The mathematical answer is that **it is impossible** to achieve an average speed of 60 mph.

Here is the detailed explanation of why:

### 1. The Formula

Average Speed ($\bar{v}$) is calculated as:
$$\bar{v} = \frac{\text{Total Distance}}{\text{Total Time}}$$

### 2. Setting Up the Variables

Let:
*   $d$ = the distance to work (one way).
*   $v_1$ = speed going to work = 30 mph.
*   $v_2$…

**Score:** `0.67` &nbsp; **Latency:** `12084 ms`

**Q20:** The Monty Hall problem: you pick door 1, the host opens door 3 revealing a goat. Should you switch to door 2? Answer Yes/No and give the win probability if you switch.

> **Yes**

The win probability if you switch to door 2 is **2/3** (or approximately 66.7%).

***

### Explanation:

When you first pick Door 1, you have a 1/3 chance of being right and a 2/3 chance of being wrong (meaning the car is behind Door 2 or Door 3).

The host's action of opening Door 3 (and revealing a goat) is not random; it is an informative action that concentrates the initial 2/3 probability onto the single remaining unopened door (Door 2).

*   **If you stay (Door 1):** Your probability of winning remains the initial 1/3.
*   **If you switch (Door 2):** You are essentially betting …

**Score:** `0.67` &nbsp; **Latency:** `4871 ms`

**Q21:** If 2+3=10, 7+2=63, 6+5=66, 8+4=96, then 9+7=? Just the number.

> 144

**Score:** `1.00` &nbsp; **Latency:** `6380 ms`

**Q22:** How many squares are on a standard 8×8 chessboard? (Count all sizes, not just 1×1.) Just the number.

> 209

**Score:** `0.00` &nbsp; **Latency:** `193 ms`

**Q23:** Is this argument valid? 'All dogs are animals. All cats are animals. Therefore all dogs are cats.' Answer Yes or No and identify the fallacy.

> No.

**Fallacy:** Fallacy of the Undistributed Middle (or Non Sequitur).

**Explanation:** The argument incorrectly assumes that because two groups (dogs and cats) share a common characteristic or category (being animals), one group must be contained within the other. The middle term ("animals") is the undistributed middle, and the premises do not provide enough information to logically connect the two outer terms ("dogs" and "cats").

**Score:** `0.67` &nbsp; **Latency:** `4369 ms`

**Q24:** Three friends pay $30 for a hotel room. Manager refunds $5; bellhop keeps $2 and returns $1 each. Each friend paid $9 = $27 total; plus $2 = $29. Where is the missing dollar?

> This is a classic riddle designed to confuse you with faulty math. **There is no missing dollar.**

The error lies in how you are adding the numbers. You should not add the bellhop's $2 to the $27 the friends paid.

Here is the correct way to account for the money:

### The Correct Accounting

The $30 paid must be accounted for by three parties:

1. **The Hotel:** $25 (The actual cost of the room)
2. **The Bellhop:** $2 (What he kept)
3. **The Friends:** $3 (The total refund they received)

**$25 + $2 + $3 = $30**

***

### Why the Riddle's Math is Wrong

The riddle tries to trick you by makin…

**Score:** `0.50` &nbsp; **Latency:** `8731 ms`

**Q25:** How many times does the digit 1 appear in all integers from 1 to 100? Just the number.

> 21

**Score:** `1.00` &nbsp; **Latency:** `184 ms`

**Q26:** At what time between 3 and 4 o'clock are the hour and minute hands of a clock exactly coincident? Answer in minutes past 3, to 2 decimal places.

> This is a classic clock problem. We need to find the time $t$ minutes past 3:00 when the hour and minute hands are at the same angle.

1.  **Determine the speeds of the hands:**
    *   The minute hand (M) moves $360^\circ$ in 60 minutes, so its speed is $v_m = 6^\circ$ per minute.
    *   The hour hand (H) moves $360^\circ$ in 12 hours (720 minutes), so its speed is $v_h = 0.5^\circ$ per minute.

2.  **Determine the initial positions (at 3:00):**
    *   The minute hand is at $0^\circ$ (pointing at 12).
    *   The hour hand is at $3 \times 30^\circ = 90^\circ$ (pointing at 3).

3.  **Set up …

**Score:** `1.00` &nbsp; **Latency:** `10052 ms`

**Q27:** You have a 100-floor building and 2 eggs. You want to find the highest floor an egg survives from. What is the minimum worst-case number of drops needed?

> This is a classic problem in probability and algorithm design, often called the **Egg Drop Puzzle**.

The goal is to find the minimum number of drops ($D$) such that, no matter where the critical floor is, we can guarantee finding it within $D$ drops.

### The Optimal Strategy

To minimize the worst-case scenario, you must use a strategy that ensures that whether the egg breaks or survives, the remaining search space can be covered by the remaining drops. This means the intervals between drops must decrease sequentially.

If you have $D$ drops available, the maximum number of floors you can te…

**Score:** `1.00` &nbsp; **Latency:** `11420 ms`

**Q28:** A logician visits an island where everyone either always lies or always tells the truth. A native says: 'I am a liar.' Is the native a truth-teller, a liar, or is this impossible?

> This is a classic logical paradox, often called the **Liar Paradox**.

The answer is that **this scenario is logically impossible** given the rules of the island.

Here is the step-by-step breakdown of why:

### 1. Assume the native is a Truth-teller (T)

*   If the native is a truth-teller, everything they say must be true.
*   They say: "I am a liar."
*   If this statement is true, it means the native *is* a liar.
*   **Contradiction:** We assumed they were a truth-teller, but the statement proves they are a liar. Therefore, they cannot be a truth-teller.

### 2. Assume the native is a Liar …

**Score:** `1.00` &nbsp; **Latency:** `5576 ms`

**Q29:** What is the minimum number of moves to solve the Tower of Hanoi with 4 discs? Just the number.

> 15

**Score:** `1.00` &nbsp; **Latency:** `1023 ms`

**Q30:** A store reduces a price by 10% then reduces it by another 10%. Is the total reduction 20%? Answer Yes/No and give the actual percentage.

> No. The total reduction is 19%.

**Score:** `1.00` &nbsp; **Latency:** `237 ms`

**Q31:** What is the maximum number of regions a plane can be divided into by 5 straight lines? Just the number.

> 16

**Score:** `1.00` &nbsp; **Latency:** `4305 ms`

**Q32:** If you write all numbers from 1 to 1000, how many times do you write the digit 0? Just the number.

> 303

**Score:** `0.00` &nbsp; **Latency:** `6106 ms`

**Q33:** Look-and-Say sequence: 1, 11, 21, 1211, 111221. What is the next term?

> The Look-and-Say sequence works by describing the digits in the previous term.

Let's verify the steps provided:

1. **1**
2. **11** (One 1)
3. **21** (Two 1s)
4. **1211** (One 2, one 1)
5. **111221** (From 1211: Three 1s, two 2s, one 1)

To find the next term, we apply the rule to the last term, **111221**:

* **111** $\rightarrow$ Three 1s $\rightarrow$ **31**
* **22** $\rightarrow$ Two 2s $\rightarrow$ **22**
* **1** $\rightarrow$ One 1 $\rightarrow$ **11**

Concatenating these descriptions gives the next term:

**312211**

**Score:** `1.00` &nbsp; **Latency:** `10800 ms`

**Q34:** Albert is taller than Bob. Carlos is shorter than Albert. David is taller than Carlos but shorter than Bob. Who is the second tallest? Just the name.

> Bob

**Score:** `1.00` &nbsp; **Latency:** `3131 ms`

**Q35:** What is 1/3 of 3/4 of 48? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `210 ms`

**Q36:** Two children share the same parents, were born at the same time, but are not twins. How?

> This is a classic riddle that relies on lateral thinking! Here are the most common and clever answers:

**1. They are characters (or names).**
The "parents" are the authors, creators, or people who wrote them. For example, two characters in a book who were created by the same author, but were not born at the same time.

**2. They are dolls or toys.**
The "parents" are the people who bought or created them. They were "born" (made) at the same time, but are not biological twins.

**3. They are triplets (or quadruplets).**
While the riddle specifies "not twins," if the intent of the riddle is to …

**Score:** `1.00` &nbsp; **Latency:** `7786 ms`

**Q37:** How many prime numbers are there between 1 and 20? Just the number.

> 8

**Score:** `1.00` &nbsp; **Latency:** `183 ms`

**Q38:** Alice runs at 5 m/s and Bob at 3 m/s on a circular 400-meter track, both in the same direction. How many seconds until Alice laps Bob? Just the number.

> 200

**Score:** `1.00` &nbsp; **Latency:** `3143 ms`

**Q39:** If P(rain) = 0.3 on any day, what is P(no rain on two consecutive days)? Give as a decimal.

> This is a problem involving independent events.

1.  **Find the probability of no rain on a single day:**
    *   $P(\text{no rain}) = 1 - P(\text{rain})$
    *   $P(\text{no rain}) = 1 - 0.3 = 0.7$

2.  **Calculate the probability of no rain on two consecutive days:**
    *   Since the weather on one day is assumed to be independent of the weather on the next day, we multiply the probabilities:
    *   $P(\text{no rain on Day 1 and no rain on Day 2}) = P(\text{no rain}) \times P(\text{no rain})$
    *   $P(\text{no rain on two consecutive days}) = 0.7 \times 0.7 = 0.49$

**Answer:** 0.49

**Score:** `1.00` &nbsp; **Latency:** `5145 ms`

**Q40:** A doctor gives you 3 pills and says take one every 30 minutes. How many minutes until all pills are taken? Just the number.

> 60

**Score:** `1.00` &nbsp; **Latency:** `1859 ms`

**Q41:** What is wrong with this reasoning: 'I've flipped a coin 10 times and got heads every time, so tails is overdue.' Name the fallacy.

> The fallacy in this reasoning is the **Gambler's Fallacy** (or the Monte Carlo Fallacy).

---

### Explanation

**1. The Fallacy:**
The Gambler's Fallacy is the mistaken belief that if an event occurs more frequently than normal in the past, it is less likely to occur in the future (or vice versa). It assumes that past outcomes influence the probability of future outcomes.

**2. Why it is Wrong (The Concept of Independence):**
Coin flips are **independent events**. This means that the outcome of any single flip has absolutely no influence on the outcome of the next flip. The coin has no memory…

**Score:** `1.00` &nbsp; **Latency:** `4349 ms`

**Q42:** Four people cross a bridge at night with one torch: A=1 min, B=2 min, C=5 min, D=10 min. Max 2 per crossing. Minimum total time in minutes?

> This is a classic river crossing puzzle. The goal is to minimize the total time, where the time taken for any crossing is determined by the slowest person in the group.

The people are:
A = 1 minute
B = 2 minutes
C = 5 minutes
D = 10 minutes

We must use the fastest people (A and B) to handle the return trips, and we must ensure the two slowest people (C and D) cross together to minimize the time for that crossing.

Here is the optimal sequence of crossings:

**1. A and B cross.**
* Time taken: max(1, 2) = 2 minutes.
* Location: A and B are across. C and D remain.
* Total Time: 2 minutes.

**2…

**Score:** `1.00` &nbsp; **Latency:** `16022 ms`

**Q43:** Complete the pattern: 2, 3, 5, 7, 11, 13, ? (What rule governs this sequence?)

> The next number in the sequence is **17**.

**What rule governs this sequence?**

The sequence consists of **consecutive prime numbers**.

(A prime number is a whole number greater than 1 whose only divisors are 1 and itself.)

The sequence is: 2, 3, 5, 7, 11, 13, **17**, 19, 23, ...

**Score:** `1.00` &nbsp; **Latency:** `2559 ms`

**Q44:** You are in a room with two doors. One leads to freedom, one to a tiger. Two guards know which is which: one always lies, one always tells the truth. You can ask one guard one yes/no question. What do you ask?

> You should point to one of the doors (let's call it Door A) and ask either guard:

**"If I were to ask the other guard whether this door leads to freedom, would he say 'yes'?"**

***

### The Logic (Why this works):

This question is designed to neutralize the difference between the truth-teller and the liar, forcing them both to give the same, reliable answer.

**1. Assume Door A is the door to Freedom (F):**
*   The other guard (the Liar/Truth-teller) knows the answer is "Yes."
*   If you ask the **Truth-teller**: He knows the Liar would lie and say "No." Since he must tell the truth, he wil…

**Score:** `1.00` &nbsp; **Latency:** `15197 ms`

**Q45:** A number equals the sum of its proper divisors (divisors less than itself). What is the smallest such number greater than 1?

> This type of number is known as a **perfect number**.

To find the smallest such number greater than 1, we test the numbers sequentially:

*   **2:** Proper divisors: 1. Sum = 1. ($2 \neq 1$)
*   **3:** Proper divisors: 1. Sum = 1. ($3 \neq 1$)
*   **4:** Proper divisors: 1, 2. Sum = $1 + 2 = 3$. ($4 \neq 3$)
*   **5:** Proper divisors: 1. Sum = 1. ($5 \neq 1$)
*   **6:** Proper divisors: 1, 2, 3. Sum = $1 + 2 + 3 = 6$. ($6 = 6$)

The smallest such number greater than 1 is **6**.

**Score:** `1.00` &nbsp; **Latency:** `3949 ms`

**Q46:** If all Wumps are Mooks and half of all Mooks are Wumps, what fraction of Mooks are Wumps? Answer as a fraction.

> $$\frac{1}{2}$$

**Score:** `0.00` &nbsp; **Latency:** `1389 ms`

**Q47:** Which is larger: 2^(3^2) or (2^3)^2? State which and give both values.

> The larger value is **$2^{(3^2)}$**.

Here are the calculations for both values:

### 1. Calculate $2^{(3^2)}$

First, evaluate the exponent:
$$3^2 = 9$$
So, the expression becomes:
$$2^9$$
$$2^9 = 512$$

### 2. Calculate $(2^3)^2$

Use the rule of exponents $(a^m)^n = a^{m \times n}$:
$$(2^3)^2 = 2^{3 \times 2} = 2^6$$
$$2^6 = 64$$

***

### Summary

*   **$2^{(3^2)}$** = **512**
*   **$(2^3)^2$** = **64**

Since $512 > 64$, **$2^{(3^2)}$** is larger.

**Score:** `1.00` &nbsp; **Latency:** `4903 ms`

**Q48:** A frog is at the bottom of a 10-foot well. Each day it climbs 3 feet; each night it falls 1 foot. On what day does it escape? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `3722 ms`

**Q49:** You measure the height of a building by dropping a stone and timing its fall at 3 seconds. Using d = ½gt² and g = 9.8 m/s², how tall is the building in meters? Just the number.

> 44.1

**Score:** `1.00` &nbsp; **Latency:** `1537 ms`

**Q50:** If you have a 3×3 grid and place numbers 1–9 so each row, column, and diagonal sums to 15 (a magic square), what number goes in the center? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `3971 ms`


### Mathematics

**Q1:** What is 15% of 240? Just the number.

> 36

**Score:** `1.00` &nbsp; **Latency:** `186 ms`

**Q2:** A train travels at 60 mph for 2 hours 30 minutes. How far in miles? Just the number.

> 150

**Score:** `1.00` &nbsp; **Latency:** `1619 ms`

**Q3:** What is √144? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `180 ms`

**Q4:** A rectangle is 8 cm × 5 cm. What is its area? Just the number.

> 40

**Score:** `1.00` &nbsp; **Latency:** `180 ms`

**Q5:** Solve for x: 3x + 7 = 22. Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `175 ms`

**Q6:** What is 2^10? Just the number.

> 1024

**Score:** `1.00` &nbsp; **Latency:** `200 ms`

**Q7:** What is the LCM of 12 and 18? Just the number.

> 36

**Score:** `1.00` &nbsp; **Latency:** `182 ms`

**Q8:** Calculate 7! ÷ 5! Just the number.

> 42

**Score:** `1.00` &nbsp; **Latency:** `182 ms`

**Q9:** What is the sum of interior angles of a hexagon in degrees? Just the number.

> 720

**Score:** `1.00` &nbsp; **Latency:** `189 ms`

**Q10:** Solve: 2^x = 32. What is x? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `172 ms`

**Q11:** What is the harmonic mean of 40 and 60? Just the number.

> 48

**Score:** `1.00` &nbsp; **Latency:** `2926 ms`

**Q12:** What is the GCD of 48 and 36? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `185 ms`

**Q13:** Calculate: (−3)² + (−2)³. Just the number.

> $31$

**Score:** `0.00` &nbsp; **Latency:** `192 ms`

**Q14:** A circle has area 25π. What is its radius? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `177 ms`

**Q15:** What is the probability of flipping exactly 2 heads with 3 fair coins? Give as a decimal.

> This is a binomial probability problem.

**1. Determine the total possible outcomes:**
With 3 coins, the total number of possible outcomes is $2^3 = 8$.

**2. Determine the favorable outcomes (exactly 2 heads):**
The possible combinations with exactly 2 heads (H) and 1 tail (T) are:
*   HHT
*   HTH
*   THH

There are **3** favorable outcomes.

**3. Calculate the probability:**
$$\text{Probability} = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}} = \frac{3}{8}$$

**4. Convert to a decimal:**
$$\frac{3}{8} = 0.375$$

The probability of flipping exactly 2 heads with 3 fair coins is **0.3…

**Score:** `1.00` &nbsp; **Latency:** `6537 ms`

**Q16:** What is the 8th term of the arithmetic sequence 3, 7, 11, 15, …? Just the number.

> 31

**Score:** `1.00` &nbsp; **Latency:** `184 ms`

**Q17:** How many diagonals does a pentagon have? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `178 ms`

**Q18:** What is √2 × √8? Just the number.

> 4

**Score:** `1.00` &nbsp; **Latency:** `174 ms`

**Q19:** A bag has 5 red and 3 blue balls. You pick 2 without replacement. What is P(both red)? Give as a decimal rounded to 3 places.

> This is a probability problem involving dependent events (without replacement).

**1. Calculate the total number of balls:**
$$5 \text{ (red)} + 3 \text{ (blue)} = 8 \text{ total balls}$$

**2. Calculate the probability of the first ball being red ($P(R_1)$):**
$$P(R_1) = \frac{5}{8}$$

**3. Calculate the probability of the second ball being red, given the first was red ($P(R_2 | R_1)$):**
After the first red ball is taken, there are 4 red balls left and 7 total balls left.
$$P(R_2 | R_1) = \frac{4}{7}$$

**4. Calculate the probability of both events happening:**
$$P(\text{both red}) = P(R_1) …

**Score:** `1.00` &nbsp; **Latency:** `7933 ms`

**Q20:** What is the sum of the first 20 natural numbers? Just the number.

> 210

**Score:** `1.00` &nbsp; **Latency:** `238 ms`

**Q21:** Solve the system: 2x + y = 7, x − y = 2. What is x? Just the number.

> 3

**Score:** `1.00` &nbsp; **Latency:** `178 ms`

**Q22:** What is lim(x→0) sin(x)/x? Just the number.

> 1

**Score:** `1.00` &nbsp; **Latency:** `176 ms`

**Q23:** In how many ways can 4 people be arranged in a row? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `186 ms`

**Q24:** What is the derivative of x³? Answer as an expression.

> $3x^2$

**Score:** `1.00` &nbsp; **Latency:** `213 ms`

**Q25:** A geometric series has first term 3 and ratio 1/2. What is the sum to infinity? Just the number.

> 6

**Score:** `1.00` &nbsp; **Latency:** `187 ms`

**Q26:** What is the distance between points (0,0) and (3,4)? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `187 ms`

**Q27:** What is the remainder when 2^10 is divided by 7? Just the number.

> 2

**Score:** `1.00` &nbsp; **Latency:** `177 ms`

**Q28:** How many zeros does 50! end with? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `2390 ms`

**Q29:** What is f(f(2)) if f(x) = x² + 1? Just the number.

> 17

**Score:** `0.00` &nbsp; **Latency:** `195 ms`

**Q30:** What is the surface area of a cube with side length 4? Just the number.

> 96

**Score:** `1.00` &nbsp; **Latency:** `181 ms`

**Q31:** If sin(θ) = 0.6 and 0 < θ < 90°, what is cos(θ)? Just the number.

> 0.8

**Score:** `1.00` &nbsp; **Latency:** `2439 ms`

**Q32:** How many prime numbers are there between 1 and 30? Just the number.

> 10

**Score:** `1.00` &nbsp; **Latency:** `193 ms`

**Q33:** What is C(8,2)? Just the number.

> 28

**Score:** `1.00` &nbsp; **Latency:** `184 ms`

**Q34:** What is the slope of the line through (1,2) and (3,8)? Just the number.

> 3

**Score:** `1.00` &nbsp; **Latency:** `177 ms`

**Q35:** If P(A) = 0.4 and P(B|A) = 0.5 and they are independent, what is P(A ∩ B)? Just the decimal.

> 0.2

**Score:** `1.00` &nbsp; **Latency:** `2168 ms`

**Q36:** What is i⁴ where i = √(−1)? Just the number.

> 1

**Score:** `1.00` &nbsp; **Latency:** `179 ms`

**Q37:** What is the smallest positive integer divisible by both 6 and 8? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `1613 ms`

**Q38:** What is the perimeter of a regular hexagon with side length 7? Just the number.

> 42

**Score:** `1.00` &nbsp; **Latency:** `187 ms`

**Q39:** How many ways can you select 3 items from 7 (order does not matter)? Just the number.

> 35

**Score:** `1.00` &nbsp; **Latency:** `2822 ms`

**Q40:** What is the area of a right triangle with legs 6 and 8? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `189 ms`

**Q41:** What is the 10th term of the geometric sequence 2, 6, 18, …? Just the number.

> $2 \cdot 3^9$

**Score:** `0.00` &nbsp; **Latency:** `239 ms`

**Q42:** How many trailing zeros does 100! have? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `2352 ms`

**Q43:** Solve |2x − 3| = 7. Give both solutions separated by a comma.

> $5, -2$

**Score:** `1.00` &nbsp; **Latency:** `1434 ms`

**Q44:** What is the volume of a cone with radius 3 and height 4? Give as a multiple of π (e.g. 12π).

> The formula for the volume ($V$) of a cone is:
$$V = \frac{1}{3} \pi r^2 h$$

Where:
*   $r$ is the radius (3)
*   $h$ is the height (4)

Substitute the given values into the formula:
$$V = \frac{1}{3} \pi (3)^2 (4)$$
$$V = \frac{1}{3} \pi (9) (4)$$
$$V = \frac{1}{3} \pi (36)$$
$$V = 12\pi$$

The volume of the cone is **12π**.

**Score:** `0.50` &nbsp; **Latency:** `3153 ms`

**Q45:** Express the fraction 7/12 as a decimal rounded to 4 places.

> To express the fraction 7/12 as a decimal, you divide 7 by 12:

$$7 \div 12 = 0.583333...$$

Rounding this decimal to 4 places, we look at the fifth decimal place (which is 3). Since 3 is less than 5, we keep the fourth decimal place as it is.

The decimal is **0.5833**.

**Score:** `1.00` &nbsp; **Latency:** `2124 ms`

**Q46:** If P(A) = 0.3 and events A and B are mutually exclusive with P(B) = 0.4, what is P(A ∪ B)?

> This is a problem involving the probability of the union of two events.

### Key Concept: Mutually Exclusive Events

When two events, A and B, are **mutually exclusive**, it means they cannot happen at the same time. Therefore, the probability of their intersection is zero:
$$P(A \cap B) = 0$$

### Formula for Union

The general formula for the union of two events is:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Since A and B are mutually exclusive, the formula simplifies to:
$$P(A \cup B) = P(A) + P(B)$$

### Calculation

Given:
*   $P(A) = 0.3$
*   $P(B) = 0.4$

$$P(A \cup B) = 0.3 + 0.4$$
$…

**Score:** `1.00` &nbsp; **Latency:** `4386 ms`

**Q47:** What is the 5th Fibonacci number (1-indexed, starting 1, 1, 2, 3, 5, …)? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `184 ms`

**Q48:** A number is increased by 20% then decreased by 20%. What percentage of the original is the result?

> This is a classic percentage problem. Here is the step-by-step solution:

Let $N$ be the original number.

**Step 1: Increase the number by 20%.**
To increase a number by 20%, you multiply it by $(1 + 0.20)$, or $1.20$.
$$N_{new} = N \times 1.20$$

**Step 2: Decrease the new number by 20%.**
To decrease a number by 20%, you multiply it by $(1 - 0.20)$, or $0.80$.
$$N_{final} = N_{new} \times 0.80$$

**Step 3: Combine the steps.**
Substitute the result from Step 1 into the equation from Step 2:
$$N_{final} = (N \times 1.20) \times 0.80$$
$$N_{final} = N \times (1.20 \times 0.80)$$
$$N_{final} =…

**Score:** `1.00` &nbsp; **Latency:** `4116 ms`

**Q49:** What is the determinant of the matrix [[3, 1], [2, 4]]? Just the number.

> 10

**Score:** `1.00` &nbsp; **Latency:** `194 ms`

**Q50:** A car accelerates from rest at 2 m/s². Using s = ½at², how far does it travel in 6 seconds? Just the number in metres.

> 36

**Score:** `1.00` &nbsp; **Latency:** `1534 ms`


### Knowledge

**Q1:** What is the chemical symbol for gold? Just the symbol.

> Au

**Score:** `1.00` &nbsp; **Latency:** `231 ms`

**Q2:** In what year did World War II end? Just the year.

> 1945

**Score:** `1.00` &nbsp; **Latency:** `286 ms`

**Q3:** What is the capital of Australia? Just the city name.

> Canberra

**Score:** `1.00` &nbsp; **Latency:** `229 ms`

**Q4:** Who wrote the play Hamlet? Just the author's last name.

> Shakespeare

**Score:** `1.00` &nbsp; **Latency:** `233 ms`

**Q5:** What is the approximate speed of light in km/s? Round to nearest 1000.

> The approximate speed of light is **300,000 km/s**.

*(The precise value is about 299,792 km/s, which rounds to 300,000 km/s when rounding to the nearest 1000.)*

**Score:** `0.00` &nbsp; **Latency:** `3559 ms`

**Q6:** What element has atomic number 79? Just the element name.

> Gold

**Score:** `1.00` &nbsp; **Latency:** `199 ms`

**Q7:** What is the largest planet in the solar system? Just the name.

> Jupiter

**Score:** `1.00` &nbsp; **Latency:** `191 ms`

**Q8:** In what year did the French Revolution begin? Just the year.

> 1789

**Score:** `1.00` &nbsp; **Latency:** `210 ms`

**Q9:** Who developed the theory of general relativity? Just the last name.

> Einstein

**Score:** `1.00` &nbsp; **Latency:** `183 ms`

**Q10:** What is the SI unit of electrical resistance? Just the unit name.

> Ohm

**Score:** `1.00` &nbsp; **Latency:** `197 ms`

**Q11:** What gas makes up approximately 78% of Earth's atmosphere? Just the name.

> Nitrogen

**Score:** `1.00` &nbsp; **Latency:** `194 ms`

**Q12:** Who painted the Sistine Chapel ceiling? Just the last name.

> Michelangelo

**Score:** `1.00` &nbsp; **Latency:** `203 ms`

**Q13:** What organelle is called the powerhouse of the cell? Just the name.

> Mitochondrion

**Score:** `0.00` &nbsp; **Latency:** `200 ms`

**Q14:** What is the chemical formula for sulfuric acid? Just the formula.

> $\text{H}_2\text{SO}_4$

**Score:** `0.00` &nbsp; **Latency:** `279 ms`

**Q15:** How many bones are in the adult human body? Just the number.

> 206

**Score:** `1.00` &nbsp; **Latency:** `213 ms`

**Q16:** Who wrote Crime and Punishment? Just the last name.

> Dostoevsky

**Score:** `1.00` &nbsp; **Latency:** `207 ms`

**Q17:** What is the boiling point of water in Fahrenheit? Just the number.

> 212

**Score:** `1.00` &nbsp; **Latency:** `200 ms`

**Q18:** What is the capital of Canada? Just the city name.

> Ottawa

**Score:** `1.00` &nbsp; **Latency:** `221 ms`

**Q19:** What is the largest ocean on Earth? Just the name.

> Pacific Ocean

**Score:** `1.00` &nbsp; **Latency:** `237 ms`

**Q20:** What element is represented by the symbol Fe? Just the element name.

> Iron

**Score:** `1.00` &nbsp; **Latency:** `230 ms`

**Q21:** Who invented the telephone? Just the inventor's last name.

> Bell

**Score:** `1.00` &nbsp; **Latency:** `218 ms`

**Q22:** What is the smallest country in the world by area? Just the name.

> Vatican City

**Score:** `1.00` &nbsp; **Latency:** `213 ms`

**Q23:** What is the approximate half-life of Carbon-14 in years? Just the number.

> 5730

**Score:** `1.00` &nbsp; **Latency:** `218 ms`

**Q24:** Who formulated the three laws of motion? Just the last name.

> Newton

**Score:** `1.00` &nbsp; **Latency:** `191 ms`

**Q25:** What is the national currency of Japan? Just the name.

> Yen

**Score:** `1.00` &nbsp; **Latency:** `209 ms`

**Q26:** How many chromosomes do humans normally have? Just the number.

> 46

**Score:** `1.00` &nbsp; **Latency:** `210 ms`

**Q27:** Who wrote War and Peace? Just the last name.

> Tolstoy

**Score:** `1.00` &nbsp; **Latency:** `202 ms`

**Q28:** What is the speed of sound in air at room temperature in m/s? Approximate to nearest 10.

> The speed of sound in air at room temperature (approximately $20^\circ\text{C}$) is about $343 \text{ m/s}$.

Approximated to the nearest 10, the speed is **$340 \text{ m/s}$**.

**Score:** `1.00` &nbsp; **Latency:** `1751 ms`

**Q29:** What is the largest organ in the human body? Just the name.

> Skin

**Score:** `1.00` &nbsp; **Latency:** `189 ms`

**Q30:** What does DNA stand for? Full name only.

> Deoxyribonucleic acid

**Score:** `1.00` &nbsp; **Latency:** `218 ms`

**Q31:** What is the capital of Brazil? Just the city name.

> Brasília

**Score:** `0.00` &nbsp; **Latency:** `200 ms`

**Q32:** How many chambers does the human heart have? Just the number.

> Four

**Score:** `0.00` &nbsp; **Latency:** `184 ms`

**Q33:** What is the chemical symbol for potassium? Just the symbol.

> K

**Score:** `1.00` &nbsp; **Latency:** `179 ms`

**Q34:** Who was the first person to walk on the moon? First and last name.

> Neil Armstrong

**Score:** `1.00` &nbsp; **Latency:** `191 ms`

**Q35:** What planet is known as the Red Planet? Just the name.

> Mars

**Score:** `1.00` &nbsp; **Latency:** `188 ms`

**Q36:** What is the hardest natural substance? Just the name.

> Diamond

**Score:** `1.00` &nbsp; **Latency:** `1897 ms`

**Q37:** How many moons does Mars have? Just the number.

> Two

**Score:** `0.00` &nbsp; **Latency:** `199 ms`

**Q38:** What is the most abundant element in the universe? Just the name.

> Hydrogen

**Score:** `1.00` &nbsp; **Latency:** `187 ms`

**Q39:** In what year did the Berlin Wall fall? Just the year.

> 1989

**Score:** `1.00` &nbsp; **Latency:** `208 ms`

**Q40:** What is the chemical symbol for sodium? Just the symbol.

> Na

**Score:** `1.00` &nbsp; **Latency:** `185 ms`

**Q41:** What is the main greenhouse gas produced by human activity? Just the name or formula.

> $\text{CO}_2$

**Score:** `0.00` &nbsp; **Latency:** `1770 ms`

**Q42:** What is the longest bone in the human body? Just the name.

> Femur

**Score:** `1.00` &nbsp; **Latency:** `208 ms`

**Q43:** Who wrote the novel 1984? Just the last name.

> Orwell

**Score:** `1.00` &nbsp; **Latency:** `234 ms`

**Q44:** Who invented the World Wide Web? Full name.

> Tim Berners-Lee

**Score:** `1.00` &nbsp; **Latency:** `222 ms`

**Q45:** What is the melting point of gold in Celsius? Just the number.

> 1064

**Score:** `1.00` &nbsp; **Latency:** `213 ms`

**Q46:** What is the most spoken language in the world by number of native speakers? Just the language.

> Mandarin Chinese

**Score:** `1.00` &nbsp; **Latency:** `200 ms`

**Q47:** What year did the first moon landing occur? Just the year.

> 1969

**Score:** `1.00` &nbsp; **Latency:** `227 ms`

**Q48:** What is the chemical formula for glucose? Just the formula.

> $\text{C}_6\text{H}_{12}\text{O}_6$

**Score:** `0.00` &nbsp; **Latency:** `334 ms`

**Q49:** What is the currency of Brazil? Just the name.

> Real

**Score:** `1.00` &nbsp; **Latency:** `193 ms`

**Q50:** Which planet has the most known moons? Just the name.

> Saturn

**Score:** `1.00` &nbsp; **Latency:** `1054 ms`


### Code

**Q1:** Write a Python function `fibonacci(n)` returning the nth Fibonacci number (0-indexed). Code only.

> ```python
def fibonacci(n):
    """
    Returns the nth Fibonacci number (0-indexed).
    F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, ...
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize the first two numbers
    a = 0  # F(i-2)
    b = 1  # F(i-1)

    # Iterate from the 2nd index up to n
    for _ in range(2, n + 1):
        # Calculate F(i) = F(i-1) + F(i-2)
        next_fib = a + b
        
        # Shift the values for the next iteration
        a = b
        b = next_fib
…

**Score:** `1.00` &nbsp; **Latency:** `3585 ms`

**Q2:** Write a Python one-liner that reverses string `s` using slice notation. Code only.

> `s[::-1]`

**Score:** `0.50` &nbsp; **Latency:** `223 ms`

**Q3:** Write a Python function `is_palindrome(s)` returning True if s is a palindrome. Code only.

> ```python
def is_palindrome(s):
    """
    Checks if a string s is a palindrome.
    """
    return s == s[::-1]
```

**Score:** `1.00` &nbsp; **Latency:** `3352 ms`

**Q4:** Write a Python list comprehension producing squares of even numbers from 1 to 20. Code only.

> [x**2 for x in range(2, 21, 2)]

**Score:** `1.00` &nbsp; **Latency:** `2022 ms`

**Q5:** Write a Python function `count_words(s)` returning the number of words in string s. Code only.

> ```python
def count_words(s):
    """
    Counts the number of words in a given string s.
    Words are separated by whitespace.
    """
    return len(s.split())
```

**Score:** `1.00` &nbsp; **Latency:** `3045 ms`

**Q6:** Write a Python function `factorial(n)` using recursion. Code only.

> ```python
def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

**Score:** `1.00` &nbsp; **Latency:** `1066 ms`

**Q7:** Write a Python function `binary_search(arr, target)` for a sorted list, returning the index or -1. Code only.

> ```python
def binary_search(arr, target):
    """
    Performs binary search on a sorted list to find the index of the target.

    Args:
        arr (list): A sorted list of elements.
        target (any): The element to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the middle index
        # Using low + (high - low) // 2 prevents potential integer overflow 
        # compared to (low + high) // 2, though less critical in Python.
        mid = low + (high - low) // …

**Score:** `1.00` &nbsp; **Latency:** `2976 ms`

**Q8:** Write a Python decorator `timer` that prints the execution time of a function. Code only.

> ```python
import time
from functools import wraps

def timer(func):
    """
    A decorator that prints the execution time of the decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
        return result
    return wrapper

# Example usage (optional, for testing purposes)
if __name__ == '__main__':
    @timer
    def slow_function(n):
   …

**Score:** `1.00` &nbsp; **Latency:** `2355 ms`

**Q9:** Write a Python generator function `infinite_counter(start=0)` that yields consecutive integers. Code only.

> ```python
def infinite_counter(start=0):
    """
    A generator function that yields consecutive integers starting from 'start'.
    """
    current = start
    while True:
        yield current
        current += 1
```

**Score:** `1.00` &nbsp; **Latency:** `572 ms`

**Q10:** Write a Python class `Stack` with push, pop, and is_empty methods. Code only.

> ```python
class Stack:
    """
    A simple implementation of a Stack data structure using a Python list.
    Follows LIFO (Last-In, First-Out) principle.
    """
    def __init__(self):
        # The internal list to store stack elements
        self._items = []

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        Returns True if empty, False otherwise.
        """
        return not self._items

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self._items.append(item)

    def pop(self):
        """
…

**Score:** `1.00` &nbsp; **Latency:** `5105 ms`

**Q11:** Write a Python function `is_prime(n)` returning True if n is prime. Code only.

> ```python
import math

def is_prime(n: int) -> bool:
    """
    Checks if a given integer n is a prime number.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for divisors starting from 5, using the pattern 6k ± 1
    # We only need to check up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True
```

**Score:** `1.00` &nbsp; **Latency:** `7215 ms`

**Q12:** Write a Python function `anagram(s1, s2)` returning True if both strings are anagrams. Code only.

> ```python
from collections import Counter

def anagram(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    """
    # Quick check: if lengths are different, they cannot be anagrams.
    if len(s1) != len(s2):
        return False
    
    # Anagrams must have the same character counts.
    return Counter(s1) == Counter(s2)

# Example Usage (for testing, not part of the required output):
# print(anagram("listen", "silent")) # True
# print(anagram("hello", "olleh"))   # True
# print(anagram("apple", "apply"))   # False
# print(anagram("a", "aa"))         #…

**Score:** `1.00` &nbsp; **Latency:** `5343 ms`

**Q13:** Write a Python function `deep_flatten(lst)` that recursively flattens a nested list of any depth. Code only.

> ```python
def deep_flatten(lst):
    """
    Recursively flattens a nested list of any depth.

    Args:
        lst: The nested list to flatten.

    Returns:
        A flat list containing all elements.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            # If the item is a list, recursively flatten it and extend the result
            result.extend(deep_flatten(item))
        else:
            # Otherwise, append the item directly
            result.append(item)
    return result

if __name__ == '__main__':
    # Example 1: Basic nesting
    nested_lis…

**Score:** `1.00` &nbsp; **Latency:** `6451 ms`

**Q14:** Write a Python function `memoize(func)` that caches function call results in a dict. Code only.

> ```python
import functools

def memoize(func):
    """
    A decorator that caches the results of a function call based on its arguments.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a hashable key from the arguments.
        # We combine positional arguments (tuple) and keyword arguments (sorted tuple of items).
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            return cache[key]
        else:
            # Calculate the result
            result = func(*args, **kwargs)
            # Store the resu…

**Score:** `1.00` &nbsp; **Latency:** `7429 ms`

**Q15:** Write a Python function `bubble_sort(arr)` that sorts a list in place and returns it. Code only.

> ```python
def bubble_sort(arr):
    """
    Sorts a list in place using the Bubble Sort algorithm and returns the sorted list.
    """
    n = len(arr)
    # Outer loop for passes
    for i in range(n):
        # Flag to optimize: if no two elements were swapped in inner loop, the list is sorted
        swapped = False
        # Inner loop for comparisons and swaps
        # The last i elements are already in place, so we only need to check up to n - 1 - i
        for j in range(0, n - 1 - i):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap th…

**Score:** `1.00` &nbsp; **Latency:** `2202 ms`

**Q16:** Write a Python class `Queue` implemented internally using two stacks. Code only.

> ```python
class Queue:
    """
    Implements a Queue data structure using two internal stacks (Python lists).
    
    The principle relies on the fact that moving all elements from the 
    input stack (stack_in) to the output stack (stack_out) reverses the order, 
    making the oldest element accessible via pop() on stack_out.
    """
    def __init__(self):
        # stack_in: Used for the enqueue operation (pushing new elements)
        self.stack_in = []
        # stack_out: Used for the dequeue and peek operations (retrieving elements)
        self.stack_out = []

    def _transfer(sel…

**Score:** `1.00` &nbsp; **Latency:** `9691 ms`

**Q17:** Write a Python function `chunk(lst, n)` that splits a list into sublists of size n. Code only.

> ```python
def chunk(lst, n):
    """
    Splits a list into sublists of size n.

    Args:
        lst (list): The list to be chunked.
        n (int): The desired size of each chunk.

    Returns:
        list: A list containing the sublists (chunks).
    """
    return [lst[i:i + n] for i in range(0, len(lst), n)]
```

**Score:** `1.00` &nbsp; **Latency:** `3846 ms`

**Q18:** Write a Python function `snake_to_camel(s)` converting snake_case to camelCase. Code only.

> ```python
def snake_to_camel(s: str) -> str:
    """
    Converts a string from snake_case (e.g., 'hello_world') to camelCase (e.g., 'helloWorld').
    """
    if not s:
        return ""

    components = s.split('_')
    
    # The first component remains lowercase.
    # All subsequent components are capitalized and joined.
    return components[0] + "".join(word.capitalize() for word in components[1:])

if __name__ == '__main__':
    print(f"'hello_world' -> {snake_to_camel('hello_world')}")
    print(f"'first_name_of_user' -> {snake_to_camel('first_name_of_user')}")
    print(f"'alreadyca…

**Score:** `1.00` &nbsp; **Latency:** `6480 ms`

**Q19:** Write a Python function `power(base, exp)` computing base^exp without using the ** operator. Code only.

> ```python
def power(base, exp):
    """
    Computes base^exp using binary exponentiation (exponentiation by squaring).
    Handles positive, zero, and negative integer exponents.
    """
    if exp == 0:
        return 1
    
    if exp < 0:
        # Handle negative exponents: base^(-exp) = 1 / base^exp
        # We calculate base^|exp| and take the reciprocal.
        return 1.0 / power(base, -exp)

    result = 1
    current_base = base
    
    # Binary Exponentiation Algorithm
    while exp > 0:
        # If the current exponent bit is 1 (i.e., exp is odd)
        if exp % 2 == 1:
      …

**Score:** `1.00` &nbsp; **Latency:** `8659 ms`

**Q20:** Write a Python function `find_duplicates(lst)` returning elements that appear more than once. Code only.

> ```python
from collections import Counter

def find_duplicates(lst):
    """
    Finds all elements in the list that appear more than once.

    Args:
        lst (list): The input list.

    Returns:
        list: A list of unique elements that are duplicates.
    """
    counts = Counter(lst)
    # Use a list comprehension to filter for items with a count greater than 1
    return [item for item, count in counts.items() if count > 1]

if __name__ == '__main__':
    # Example 1: Standard duplicates
    list1 = [1, 2, 3, 2, 1, 4, 1]
    print(f"List: {list1}")
    print(f"Duplicates: {find_dup…

**Score:** `1.00` &nbsp; **Latency:** `6327 ms`

**Q21:** Write a Python function `caesar_cipher(text, shift)` that shifts each letter by shift positions. Code only.

> ```python
def caesar_cipher(text, shift):
    """
    Shifts each letter in the text by the given shift amount using the Caesar cipher.
    Non-alphabetic characters are left unchanged.
    """
    result = []
    # Ensure the shift is within the range [0, 25]
    shift = shift % 26

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a')
            original_pos = ord(char) - start
            new_pos = (original_pos + shift) % 26
            new_char = chr(start + new_pos)
            result.append(new_char)
        elif 'A' <=…

**Score:** `1.00` &nbsp; **Latency:** `4640 ms`

**Q22:** Write a Python class `LinkedList` with append and __iter__ methods. Code only.

> ```python
class Node:
    """Helper class representing a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A simple implementation of a singly linked list.
    """
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        """
        Adds a new node containing the given data to the end of the list.
        """
        new_node = Node(data)
        
        if self.head is None:
            # If the list is empty, the new node is the head
            self.h…

**Score:** `1.00` &nbsp; **Latency:** `5371 ms`

**Q23:** Write a Python function `matrix_multiply(A, B)` for 2D lists. Code only.

> ```python
def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B represented as 2D lists.

    Args:
        A (list[list[int]]): The first matrix (m x n).
        B (list[list[int]]): The second matrix (n x p).

    Returns:
        list[list[int]]: The resulting matrix C (m x p), or None if multiplication is impossible.
    """
    # Check if A is empty or malformed
    if not A or not A[0]:
        return None

    # Check if B is empty or malformed
    if not B or not B[0]:
        return None

    # Dimensions of A: m x n
    m = len(A)
    n_A = len(A[0])

    # Dimension…

**Score:** `1.00` &nbsp; **Latency:** `4757 ms`

**Q24:** Write a Python function `run_length_encode(s)` e.g. 'aaabbc' → '3a2b1c'. Code only.

> ```python
from itertools import groupby

def run_length_encode(s: str) -> str:
    """
    Performs run-length encoding on a string.
    e.g., 'aaabbc' -> '3a2b1c'
    """
    if not s:
        return ""

    encoded_parts = []
    for char, group in groupby(s):
        count = len(list(group))
        encoded_parts.append(f"{count}{char}")

    return "".join(encoded_parts)

if __name__ == '__main__':
    print(f"'aaabbc' -> {run_length_encode('aaabbc')}")
    print(f"'abc' -> {run_length_encode('abc')}")
    print(f"'aaaaa' -> {run_length_encode('aaaaa')}")
    print(f"'' -> {run_length_enco…

**Score:** `1.00` &nbsp; **Latency:** `6845 ms`

**Q25:** Write a Python function `max_subarray(arr)` using Kadane's algorithm. Code only.

> ```python
def max_subarray(arr):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's algorithm.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int: The maximum subarray sum. Returns 0 if the array is empty.
    """
    if not arr:
        return 0

    # Initialize max_so_far (the overall maximum sum) and current_max 
    # (the maximum sum ending at the current position) to the first element.
    max_so_far = arr[0]
    current_max = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(…

**Score:** `1.00` &nbsp; **Latency:** `11058 ms`

**Q26:** Write a Python function `is_balanced(s)` checking if (), [], {} are correctly balanced. Code only.

> ```python
def is_balanced(s: str) -> bool:
    """
    Checks if the parentheses, brackets, and braces in the string s are correctly balanced.
    """
    stack = []
    # Maps closing delimiters to their required opening counterparts
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in mapping:
            # It's a closing delimiter
            top_element = stack.pop() if stack else '#'
            
            # Check if the stack was empty (top_element == '#') or if the types don't match
            if top_element != mapping[char…

**Score:** `1.00` &nbsp; **Latency:** `8147 ms`

**Q27:** Write a Python function `all_permutations(lst)` without using itertools. Code only.

> ```python
def all_permutations(lst):
    """
    Generates all possible permutations of the elements in the given list 
    using a recursive backtracking approach.
    
    Args:
        lst (list): The input list.
        
    Returns:
        list: A list of lists, where each inner list is a permutation.
    """
    results = []
    n = len(lst)

    def backtrack(current_permutation, used_indices):
        """
        Helper function to recursively build permutations.
        
        Args:
            current_permutation (list): The permutation built so far.
            used_indices (set)…

**Score:** `1.00` &nbsp; **Latency:** `8917 ms`

**Q28:** Write a Python dataclass `Point` with x and y fields and a distance_to(other) method. Code only.

> ```python
from dataclasses import dataclass
import math

@dataclass
class Point:
    """
    Represents a point in a 2D plane.
    """
    x: float
    y: float

    def distance_to(self, other: 'Point') -> float:
        """
        Calculates the Euclidean distance between this point and another Point object.

        Args:
            other: The other Point object to measure the distance to.

        Returns:
            The distance as a float.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

# Example Usage (Optional, for tes…

**Score:** `1.00` &nbsp; **Latency:** `3450 ms`

**Q29:** Write a Python function `topological_sort(graph)` for a DAG represented as an adjacency dict. Code only.

> ```python
from collections import deque, defaultdict

def topological_sort(graph: dict) -> list:
    """
    Performs a topological sort on a Directed Acyclic Graph (DAG).

    Args:
        graph: An adjacency dictionary where keys are nodes and values 
               are lists of neighboring nodes (edges).

    Returns:
        A list representing a valid topological ordering of the nodes.
        Returns an empty list if the graph is empty or contains a cycle 
        (though the input is assumed to be a DAG).
    """
    
    # 1. Initialize in-degrees and identify all nodes
    in_degree …

**Score:** `1.00` &nbsp; **Latency:** `10850 ms`

**Q30:** Write a Python async function `fetch_all(urls, session)` that fetches all URLs concurrently with asyncio.gather. Code only.

> ```python
import asyncio
import time
from typing import List, Any

# --- Mock Setup ---
# In a real application, 'session' would be an actual async HTTP client 
# (e.g., httpx.AsyncClient). We mock the fetch logic here.

async def mock_fetch_url(session: Any, url: str) -> str:
    """Simulates an asynchronous network request."""
    print(f"[{time.strftime('%X')}] Starting fetch for: {url}")
    # Simulate network latency
    await asyncio.sleep(len(url) * 0.1 + 0.5) 
    result = f"Successfully fetched content from {url}"
    print(f"[{time.strftime('%X')}] Finished fetch for: {url}")
    ret…

**Score:** `1.00` &nbsp; **Latency:** `6978 ms`

**Q31:** Write a Python function `levenshtein(s1, s2)` computing edit distance using dynamic programming. Code only.

> ```python
def levenshtein(s1: str, s2: str) -> int:
    """
    Computes the Levenshtein distance (edit distance) between two strings s1 and s2
    using dynamic programming.
    """
    len1 = len(s1)
    len2 = len(s2)

    # Initialize the DP matrix (len1 + 1 rows, len2 + 1 columns)
    # dp[i][j] stores the distance between s1[:i] and s2[:j]
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Base cases: Initializing the first row and column
    # Distance between any string and an empty string is its length
    for i in range(len1 + 1):
        dp[i][0] = i  # Deletions
    for j …

**Score:** `1.00` &nbsp; **Latency:** `6222 ms`

**Q32:** Write a Python function `group_by(lst, key_fn)` grouping list items by the result of key_fn. Code only.

> ```python
from collections import defaultdict
from typing import List, Callable, Any, Dict

def group_by(lst: List[Any], key_fn: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
    """
    Groups items in a list based on the result of a key function.

    Args:
        lst: The list of items to group.
        key_fn: A function that takes an item and returns the key used for grouping.

    Returns:
        A dictionary where keys are the grouping criteria and values are 
        lists of items belonging to that group.
    """
    grouped_data = defaultdict(list)
    
    for item in lst:
      …

**Score:** `1.00` &nbsp; **Latency:** `10264 ms`

**Q33:** Write a Python class `SuppressErrors` context manager that swallows specified exception types. Code only.

> ```python
import typing
from typing import Type, Tuple, List, Any

class SuppressErrors:
    """
    A context manager that suppresses specified exception types.

    When used with 'with SuppressErrors(types_to_suppress):', 
    any exception matching one of the provided types will be caught 
    and suppressed, preventing it from propagating.
    """

    def __init__(self, types_to_suppress: typing.Union[Type[Exception], Tuple[Type[Exception], ...]]):
        """
        Initializes the context manager with the exception types to suppress.

        Args:
            types_to_suppress: A sin…

**Score:** `1.00` &nbsp; **Latency:** `8420 ms`

**Q34:** Write a Python function `word_frequency(text)` returning a dict of word counts. Code only.

> ```python
import re
from collections import Counter

def word_frequency(text: str) -> dict:
    """
    Calculates the frequency of each word in the given text.

    Args:
        text: The input string of text.

    Returns:
        A dictionary where keys are words and values are their counts.
    """
    # 1. Convert to lowercase
    text = text.lower()

    # 2. Use regex to find all sequences of word characters (a-z, 0-9, _)
    # This effectively handles punctuation removal and splitting.
    words = re.findall(r'\b\w+\b', text)

    # 3. Use collections.Counter for efficient counting
  …

**Score:** `1.00` &nbsp; **Latency:** `4097 ms`

**Q35:** Write a Python function `sliding_window_max(arr, k)` returning the max in each window of size k. Code only.

> ```python
from collections import deque

def sliding_window_max(arr: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in each sliding window of size k using a monotonic deque.
    Time Complexity: O(N)
    Space Complexity: O(K)
    """
    if not arr or k == 0:
        return []
    
    if k > len(arr):
        # If k is larger than the array size, the only window is the whole array
        return [max(arr)]

    # Deque stores indices of elements, maintaining the property that 
    # arr[dq[i]] is decreasing for i=0 to len(dq)-1.
    dq = deque()
    result = []
    n …

**Score:** `1.00` &nbsp; **Latency:** `10548 ms`

**Q36:** Write a Python metaclass `Singleton` that ensures only one instance of a class can exist. Code only.

> ```python
class Singleton(type):
    """
    A metaclass that ensures only one instance of the class using it can exist.
    """

    def __call__(cls, *args, **kwargs):
        """
        This method is called when the class itself is instantiated (e.g., MyClass()).
        It intercepts the creation process to enforce the single instance rule.
        """
        # Check if the instance already exists for this class (cls)
        if not hasattr(cls, '_instance'):
            # If not, create the instance using the standard class mechanism
            # We use super().__call__ to ensure the …

**Score:** `1.00` &nbsp; **Latency:** `9454 ms`

**Q37:** Write a Python function `merge_sort(arr)` implementing merge sort. Code only.

> ```python
def merge_sort(arr):
    """
    Implements the merge sort algorithm recursively.
    """
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer (Recursive calls)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Combine (Merge)
    return _merge(left, right)

def _merge(left, right):
    """
    Helper function to merge two sorted arrays.
    """
    merged = []
    i = j = 0

    # Compare elements and append the smaller one
    while i < len(left) and j < len(right)…

**Score:** `1.00` &nbsp; **Latency:** `5329 ms`

**Q38:** Write a Python function `binary_to_decimal(s)` converting a binary string to decimal without using int(s,2). Code only.

> ```python
def binary_to_decimal(s: str) -> int:
    """
    Converts a binary string representation (e.g., "1011") to its decimal integer equivalent.
    Uses the iterative method (Horner's method) to avoid int(s, 2).
    """
    decimal_value = 0
    
    for bit in s:
        # 1. Shift the current result left (equivalent to multiplying by 2)
        decimal_value *= 2
        
        # 2. Add the value of the current bit (0 or 1)
        if bit == '1':
            decimal_value += 1
        # If bit is '0', we add 0, so no action is needed.
            
    return decimal_value
```

**Score:** `1.00` &nbsp; **Latency:** `8000 ms`

**Q39:** Write Python code using functools.reduce to compute the product of all elements in list `nums`. Code only.

> ```python
from functools import reduce

def product_of_list(nums):
    """
    Computes the product of all elements in the list nums using functools.reduce.
    """
    if not nums:
        return 1  # The product of an empty set is 1
    return reduce(lambda x, y: x * y, nums)

# Example usage:
# nums = [1, 2, 3, 4, 5]
# result = product_of_list(nums)
# print(result) # Output: 120
```

**Score:** `1.00` &nbsp; **Latency:** `1136 ms`

**Q40:** Write a Python function `trie_insert(trie, word)` inserting a word into a trie stored as nested dicts. Code only.

> ```python
def trie_insert(trie: dict, word: str) -> None:
    """
    Inserts a word into a trie stored as nested dictionaries.

    The trie structure uses keys for characters and values for child nodes (dictionaries).
    A special key '_end_' is used to mark the end of a valid word.

    Args:
        trie: The root dictionary of the trie.
        word: The string word to insert.
    """
    current_node = trie
    
    for char in word:
        # If the character path does not exist, create a new node (empty dictionary)
        if char not in current_node:
            current_node[char] = …

**Score:** `1.00` &nbsp; **Latency:** `8760 ms`

**Q41:** Write a Python function `rotate_matrix(matrix)` rotating a square 2D list 90° clockwise in place. Code only.

> ```python
def rotate_matrix(matrix):
    """
    Rotates a square 2D list (matrix) 90 degrees clockwise in place.
    
    Args:
        matrix: A list of lists representing the square matrix.
    """
    n = len(matrix)
    if n == 0:
        return

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    # We only iterate over the upper triangle (j > i) to avoid swapping elements twice.
    for i in range(n):
        for j in range(i, n):
            # If i == j, we swap an element with itself, which is harmless.
            # If i != j, we swap the pair.
            mat…

**Score:** `1.00` &nbsp; **Latency:** `7351 ms`

**Q42:** Write a Python function `count_bits(n)` counting the number of set bits in integer n without bin(). Code only.

> ```python
def count_bits(n: int) -> int:
    """
    Counts the number of set bits (1s) in the binary representation of integer n.
    Uses Brian Kernighan's Algorithm.
    """
    count = 0
    # We use a temporary variable to avoid modifying the original input if needed,
    # though Python passes integers by value (effectively).
    temp_n = n

    # Handle potential negative inputs by treating them as their absolute value 
    # or assuming standard non-negative input based on typical problem constraints.
    # For standard bit counting, we assume n >= 0.
    if temp_n < 0:
        # If ne…

**Score:** `1.00` &nbsp; **Latency:** `6355 ms`

**Q43:** Write a Python function `lru_cache_manual(capacity)` returning an LRU cache object with get and put methods. Code only.

> ```python
class Node:
    """Represents a node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Implements an LRU Cache using a dictionary (for O(1) lookup) 
    and a doubly linked list (for O(1) order tracking).
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_map = {}
        
        # Initialize dummy head and tail nodes for the doubly linked list
        self.head = Node(0, 0)
        self.tail = Nod…

**Score:** `1.00` &nbsp; **Latency:** `12621 ms`

**Q44:** Write a Python function `parse_url(url)` extracting scheme, host, path, and query as a dict without using urllib. Code only.

> ```python
def parse_url(url: str) -> dict:
    """
    Parses a URL string to extract the scheme, host, path, and query 
    without using the urllib library.

    Args:
        url: The URL string to parse.

    Returns:
        A dictionary containing 'scheme', 'host', 'path', and 'query'.
    """
    
    # Initialize default values
    result = {
        'scheme': '',
        'host': '',
        'path': '',
        'query': ''
    }

    # 1. Extract Scheme
    scheme_index = url.find("://")
    if scheme_index != -1:
        result['scheme'] = url[:scheme_index]
        # Start processing…

**Score:** `1.00` &nbsp; **Latency:** `11338 ms`

**Q45:** Write a Python function `diff_lists(a, b)` returning a dict with keys 'added' and 'removed'. Code only.

> ```python
def diff_lists(a, b):
    """
    Compares two lists, a and b, and returns a dictionary 
    containing the elements added (in b but not in a) and 
    elements removed (in a but not in b).
    """
    set_a = set(a)
    set_b = set(b)

    # Elements removed: present in a, but not in b
    removed = list(set_a - set_b)

    # Elements added: present in b, but not in a
    added = list(set_b - set_a)

    return {
        'added': added,
        'removed': removed
    }
```

**Score:** `1.00` &nbsp; **Latency:** `2875 ms`

**Q46:** Write a Python function `nth_fibonacci_fast(n)` using matrix exponentiation or memoization for O(log n) or O(n) time. Code only.

> ```python
def nth_fibonacci_fast(n: int) -> int:
    """
    Calculates the n-th Fibonacci number using matrix exponentiation.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Assumes F(0) = 0, F(1) = 1.
    """
    if n < 0:
        raise ValueError("Fibonacci number is defined for non-negative integers.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    # The transformation matrix M: [[1, 1], [1, 0]]
    M = [[1, 1], [1, 0]]

    def multiply(A, B):
        """Multiplies two 2x2 matrices."""
        a = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        b = A[…

**Score:** `1.00` &nbsp; **Latency:** `11023 ms`

**Q47:** Write a Python function `flatten_dict(d, sep='.')` that flattens a nested dict, joining keys with sep. Code only.

> ```python
def flatten_dict(d: dict, sep: str = '.') -> dict:
    """
    Flattens a nested dictionary by joining keys with the specified separator.

    Args:
        d: The dictionary to flatten.
        sep: The separator used to join nested keys (default is '.').

    Returns:
        A new dictionary containing the flattened key-value pairs.
    """
    flat_dict = {}

    def _flatten(data, parent_key):
        for k, v in data.items():
            # Construct the new key path
            new_key = parent_key if parent_key == '' else f"{parent_key}{sep}{k}"

            if isinstance(v, d…

**Score:** `1.00` &nbsp; **Latency:** `9239 ms`

**Q48:** Write a Python function `retry(func, times, exceptions)` that retries func up to times times on specified exceptions. Code only.

> ```python
import functools
from typing import Callable, Type, Tuple, Any, TypeVar

# Define a type variable for the function's return type
T = TypeVar('T')

def retry(func: Callable[..., T], times: int, exceptions: Tuple[Type[Exception], ...] = (Exception,)) -> T:
    """
    Retries calling a function up to 'times' times if a specified exception occurs.

    Args:
        func: The function to be called.
        times: The maximum number of attempts (including the first try).
        exceptions: A tuple of exception types that should trigger a retry.
                    If the exception is no…

**Score:** `1.00` &nbsp; **Latency:** `8791 ms`

**Q49:** Write a Python class `Observable` with subscribe, unsubscribe, and notify methods (observer pattern). Code only.

> ```python
from typing import Callable, Set, Any

class Observable:
    """
    Implements the Observable pattern (Subject).
    Allows objects to register observers (subscribers) and notify them
    when its state changes.
    """
    def __init__(self):
        # Use a set to store unique observer objects
        self._observers: Set['Observable'] = set()

    def subscribe(self, observer: 'Observable') -> bool:
        """
        Registers an observer to receive notifications.
        Returns True if successfully subscribed, False if already subscribed.
        """
        if observer not i…

**Score:** `1.00` &nbsp; **Latency:** `8750 ms`

**Q50:** Write a Python function `consistent_hash(key, num_buckets)` mapping a key to a bucket using a hash-based approach. Code only.

> ```python
import hashlib

def consistent_hash(key, num_buckets: int) -> int:
    """
    Maps a key to a bucket index using a cryptographic hash function (SHA-256)
    to ensure deterministic and consistent distribution.

    Args:
        key: The input key (string or bytes).
        num_buckets: The total number of available buckets (the size of the ring).

    Returns:
        An integer representing the assigned bucket index (0 to num_buckets - 1).
    """
    # Ensure the key is encoded to bytes for hashing
    if isinstance(key, str):
        key_bytes = key.encode('utf-8')
    elif isin…

**Score:** `1.00` &nbsp; **Latency:** `8633 ms`


### Instruction Following

**Q1:** List exactly 3 benefits of exercise as a numbered list. No other text.

> 1. Improves cardiovascular health
2. Strengthens muscles and bones
3. Boosts mood and reduces stress

**Score:** `1.00` &nbsp; **Latency:** `336 ms`

**Q2:** Respond to 'What is the weather like today?' in exactly 10 words.

> It is currently sunny and warm, but check a local forecast for accuracy.

**Score:** `0.70` &nbsp; **Latency:** `2393 ms`

**Q3:** Translate 'hello' into French, Spanish, and German. Format as JSON with keys 'french', 'spanish', 'german'.

> ```json
{
  "french": "Bonjour",
  "spanish": "Hola",
  "german": "Hallo"
}
```

**Score:** `1.00` &nbsp; **Latency:** `1795 ms`

**Q4:** Write a haiku (5-7-5 syllables) about the ocean. Output only the haiku, no title.

> Blue waves crash and foam,
Whispering secrets to shore,
Salt spray fills the air.

**Score:** `1.00` &nbsp; **Latency:** `330 ms`

**Q5:** List the days of the week in reverse order, one per line, ALL CAPS. No other text.

> SUNDAY
SATURDAY
FRIDAY
THURSDAY
WEDNESDAY
TUESDAY
MONDAY

**Score:** `1.00` &nbsp; **Latency:** `328 ms`

**Q6:** Respond with ONLY the number 42. No other text.

> 42

**Score:** `1.00` &nbsp; **Latency:** `200 ms`

**Q7:** List exactly 5 planets in our solar system, one per line, no other text.

> Mercury
Venus
Earth
Mars
Jupiter

**Score:** `1.00` &nbsp; **Latency:** `251 ms`

**Q8:** Write a sentence containing exactly 7 words.

> The quick brown fox jumps over the lazy dog.

**Score:** `0.80` &nbsp; **Latency:** `251 ms`

**Q9:** Convert this list to a JSON array: apple, banana, cherry. Output only the JSON.

> ["apple", "banana", "cherry"]

**Score:** `1.00` &nbsp; **Latency:** `243 ms`

**Q10:** Reply with only the word 'DONE' in capital letters. Nothing else.

> DONE

**Score:** `1.00` &nbsp; **Latency:** `190 ms`

**Q11:** Write your response in exactly 5 words.

> Understood. I will follow instructions.

**Score:** `1.00` &nbsp; **Latency:** `241 ms`

**Q12:** Output the numbers 1 through 5, each on its own line, nothing else.

> 1
2
3
4
5

**Score:** `1.00` &nbsp; **Latency:** `241 ms`

**Q13:** Translate 'goodbye' to French, Spanish, and German. Format as JSON with keys 'fr', 'es', 'de'. JSON only.

> ```json
{
  "fr": "Au revoir",
  "es": "Adiós",
  "de": "Auf Wiedersehen"
}
```

**Score:** `1.00` &nbsp; **Latency:** `1641 ms`

**Q14:** Write exactly 4 words about mathematics. Nothing else.

> Patterns, logic, numbers, truth.

**Score:** `1.00` &nbsp; **Latency:** `235 ms`

**Q15:** List the vowels a, e, i, o, u separated by commas with no spaces. Exactly that string.

> a,e,i,o,u

**Score:** `1.00` &nbsp; **Latency:** `246 ms`

**Q16:** Write the numbers 1 through 10, one per line, no other text.

> 1
2
3
4
5
6
7
8
9
10

**Score:** `1.00` &nbsp; **Latency:** `319 ms`

**Q17:** Respond with a single digit: the result of 3 + 4.

> 7

**Score:** `1.00` &nbsp; **Latency:** `193 ms`

**Q18:** Write 3 words that are colors. One word per line, nothing else.

> Red
Blue
Green

**Score:** `1.00` &nbsp; **Latency:** `212 ms`

**Q19:** Output the word 'hello' in ALL UPPERCASE. Nothing else.

> HELLO

**Score:** `1.00` &nbsp; **Latency:** `199 ms`

**Q20:** List the last 3 months of the year in reverse order, one per line, lowercase.

> december
november
october

**Score:** `1.00` &nbsp; **Latency:** `1130 ms`

**Q21:** Write exactly 2 sentences about the sun. Nothing before or after.

> The sun is a massive star that provides the primary source of energy for life on Earth. Its radiant light warms our planet, making life possible and painting the sky with vibrant colors.

**Score:** `0.80` &nbsp; **Latency:** `1528 ms`

**Q22:** Provide 3 synonyms for 'happy' as a JSON array of strings. JSON only.

> ```json
[
  "joyful",
  "cheerful",
  "content"
]
```

**Score:** `1.00` &nbsp; **Latency:** `1902 ms`

**Q23:** Give a one-word answer: what is the opposite of 'hot'?

> Cold

**Score:** `1.00` &nbsp; **Latency:** `191 ms`

**Q24:** Write a Python comment (starting with #) that says Hello World. Just the comment line.

> # Hello World

**Score:** `1.00` &nbsp; **Latency:** `194 ms`

**Q25:** Write a sentence in exactly 15 words.

> The magnificent golden sunset painted the western sky with vibrant hues of orange and purple.

**Score:** `1.00` &nbsp; **Latency:** `6804 ms`

**Q26:** Output the ASCII values of A, B, C as a JSON array. JSON only.

> [65, 66, 67]

**Score:** `1.00` &nbsp; **Latency:** `936 ms`

**Q27:** Write the multiplication table for 9 from 9×1 to 9×5, one equation per line.

> $9 \times 1 = 9$
$9 \times 2 = 18$
$9 \times 3 = 27$
$9 \times 4 = 36$
$9 \times 5 = 45$

**Score:** `1.00` &nbsp; **Latency:** `605 ms`

**Q28:** Answer with a single Roman numeral for the number 14.

> XIV

**Score:** `1.00` &nbsp; **Latency:** `188 ms`

**Q29:** List 4 sorting algorithm names, numbered 1–4, one per line.

> 1. Bubble Sort
2. Merge Sort
3. Quick Sort
4. Insertion Sort

**Score:** `1.00` &nbsp; **Latency:** `323 ms`

**Q30:** Respond to 'Is Python interpreted or compiled?' with exactly one word.

> Interpreted

**Score:** `1.00` &nbsp; **Latency:** `199 ms`

**Q31:** Convert the number 255 to binary. Output only the binary number.

> 11111111

**Score:** `1.00` &nbsp; **Latency:** `248 ms`

**Q32:** Give a one-sentence definition of recursion. 12 words maximum.

> A function calling itself to solve smaller instances of the same problem.

**Score:** `0.00` &nbsp; **Latency:** `281 ms`

**Q33:** Respond with exactly the string: Hello, World! — including the comma and exclamation mark.

> Hello, World!

**Score:** `1.00` &nbsp; **Latency:** `210 ms`

**Q34:** List all days of the week that start with the letter T, one per line.

> Tuesday
Thursday

**Score:** `1.00` &nbsp; **Latency:** `201 ms`

**Q35:** Translate 'thank you' to Japanese. Output only the Japanese.

> ありがとうございます

**Score:** `0.00` &nbsp; **Latency:** `184 ms`

**Q36:** Write a Python import statement for the math module. One line only.

> import math

**Score:** `1.00` &nbsp; **Latency:** `194 ms`

**Q37:** Output the first 5 letters of the alphabet in reverse order, separated by spaces.

> E D C B A

**Score:** `1.00` &nbsp; **Latency:** `216 ms`

**Q38:** Answer with just 'yes' or 'no': is 17 a prime number?

> yes

**Score:** `1.00` &nbsp; **Latency:** `852 ms`

**Q39:** Write a 3-line poem where each line ends with a word that rhymes with 'cat'.

> The little dog sat on the mat,
Wearing a silly woolen hat,
And watched the friends chat where they sat.

**Score:** `1.00` &nbsp; **Latency:** `2132 ms`

**Q40:** Give the chemical symbols for gold, silver, and iron separated by commas. Symbols only.

> Au, Ag, Fe

**Score:** `1.00` &nbsp; **Latency:** `219 ms`

**Q41:** Count the vowels in MISSISSIPPI. Output only the count.

> 4

**Score:** `1.00` &nbsp; **Latency:** `191 ms`

**Q42:** Write a valid JSON object: key is 'status', value is 'ok'. JSON only.

> {"status": "ok"}

**Score:** `1.00` &nbsp; **Latency:** `231 ms`

**Q43:** Write the hexadecimal representation of 255. Lowercase. Output only.

> ff

**Score:** `1.00` &nbsp; **Latency:** `195 ms`

**Q44:** Name exactly 2 programming languages that start with P, one per line.

> Python
Perl

**Score:** `1.00` &nbsp; **Latency:** `212 ms`

**Q45:** Output 'true' or 'false': Is the Earth older than the Sun?

> false

**Score:** `1.00` &nbsp; **Latency:** `1625 ms`

**Q46:** Write the first 5 square numbers separated by commas.

> 1, 4, 9, 16, 25

**Score:** `0.00` &nbsp; **Latency:** `290 ms`

**Q47:** Respond in exactly 8 words to: 'What are the primary colors?'

> Red, yellow, and blue are the primary colors.

**Score:** `1.00` &nbsp; **Latency:** `255 ms`

**Q48:** Write a JSON array of the first 3 odd numbers. JSON only.

> [1, 3, 5]

**Score:** `1.00` &nbsp; **Latency:** `260 ms`

**Q49:** Output the Morse code for SOS using dots and dashes only.

> $\cdot \cdot \cdot$ / $\cdot - \cdot$ / $\cdot \cdot \cdot$

**Score:** `0.00` &nbsp; **Latency:** `340 ms`

**Q50:** List the chemical symbols for the first 3 elements (H, He, Li) as a JSON array. JSON only.

> ```json
[
  "H",
  "He",
  "Li"
]
```

**Score:** `1.00` &nbsp; **Latency:** `636 ms`


### Agentic

**Q1:** I'm planning a birthday party for my friend Alex who loves jazz music, is allergic to peanuts, and lives in Chicago. Acknowledge these details.

> That sounds like a wonderful celebration! I have noted all the key details for Alex's birthday party.

Here is a summary of the constraints and preferences I will keep in mind for all suggestions:

*   **The Honoree:** Alex
*   **Theme/Interest:** Jazz Music (The vibe should be sophisticated, lively, and musical.)
*   **Dietary Restriction:** **SEVERE PEANUT ALLERGY** (This is the top priority for any food or catering suggestions.)
*   **Location:** Chicago, IL

With these details, we can plan a truly personalized and safe celebration.

***

### 🎷 Initial Planning Focus Areas

To get started, …

**Follow-up:** What are the three key facts I told you about Alex? List them.

> The three key facts you told me about Alex are:

1.  **He loves jazz music.** (This is the theme/interest.)
2.  **He is allergic to peanuts.** (This is the critical dietary restriction.)
3.  **He lives in Chicago.** (This is the location.)

**Score:** `1.00` &nbsp; **Latency:** `6026 ms`

**Q2:** My project has three requirements: it must use Python, be completed by Friday, and the budget is $500. Acknowledge these.

> I acknowledge your project requirements. To confirm, the project must adhere to the following constraints:

*   **Technology:** Must use Python.
*   **Deadline:** Must be completed by Friday.
*   **Budget:** The total budget is $500.

Please let me know how I can help you move forward with these parameters!

**Follow-up:** What are the three project requirements I gave you?

> The three project requirements you gave me are:

1.  **Technology:** It must use Python.
2.  **Deadline:** It must be completed by Friday.
3.  **Budget:** The budget is $500.

**Score:** `1.00` &nbsp; **Latency:** `1842 ms`

**Q3:** My server config: hostname=prod-01, IP=192.168.1.100, port=8080, OS=Ubuntu 22.04, RAM=16GB. Store these details.

> **Details stored successfully.**

Here is a summary of the server configuration you provided:

*   **Hostname:** `prod-01`
*   **IP Address:** `192.168.1.100`
*   **Port:** `8080`
*   **Operating System (OS):** `Ubuntu 22.04`
*   **RAM:** `16GB`

I have recorded these details for our current conversation context.

**Follow-up:** What are the hostname, IP, and port of my server?

> Based on the details you provided, here is the information for your server:

*   **Hostname:** `prod-01`
*   **IP Address:** `192.168.1.100`
*   **Port:** `8080`

**Score:** `1.00` &nbsp; **Latency:** `2994 ms`

**Q4:** I have 3 employees: Sarah earns $75k, Mike earns $92k, Jane earns $68k. Acknowledge these salaries.

> I acknowledge the salaries for your three employees:

*   **Sarah:** $75,000
*   **Mike:** $92,000
*   **Jane:** $68,000

Please let me know if you need me to perform any calculations, comparisons, or further actions with this data.

**Follow-up:** Who earns the most and what is the total payroll?

> Based on the salaries provided:

**Who earns the most:**
*   **Mike** earns the most, with a salary of **$92,000**.

**Total Payroll:**
*   The total payroll for the three employees is **$235,000**.

*(Calculation: $75,000 + $92,000 + $68,000 = $235,000)*

**Score:** `1.00` &nbsp; **Latency:** `2303 ms`

**Q5:** Remember: Project Alpha has budget $50k, deadline March 15, team of 4, client is Acme Corp. Got it?

> Got it. I have logged the following details for Project Alpha:

*   **Budget:** $50,000
*   **Deadline:** March 15
*   **Team Size:** 4 people
*   **Client:** Acme Corp

I will keep these parameters in mind for all future discussions regarding this project.

**Follow-up:** What is the client name and deadline for Project Alpha?

> The client name for Project Alpha is **Acme Corp**, and the deadline is **March 15**.

**Score:** `1.00` &nbsp; **Latency:** `2078 ms`

**Q6:** User preferences: dark_mode=true, language=Spanish, font_size=14, notifications=false. Acknowledge.

> Sus preferencias han sido recibidas y configuradas correctamente.

**Resumen de preferencias:**

*   **Modo oscuro:** Activado
*   **Idioma:** Español
*   **Tamaño de fuente:** 14
*   **Notificaciones:** Desactivadas

¿Hay algo más en lo que pueda ayudarle?

**Follow-up:** What language and font size did I set?

> Usted configuró el idioma en **Español** y el tamaño de fuente en **14**.

**Score:** `0.50` &nbsp; **Latency:** `3005 ms`

**Q7:** I told you earlier that my API key is sk-abc-9999, my base URL is https://api.example.com, and rate limit is 100/min. Confirm.

> I have noted the following parameters for our current interaction:

*   **Base URL:** `https://api.example.com`
*   **Rate Limit:** `100/min`

**Please note:** For security and privacy reasons, I cannot confirm, store, or repeat your API key (`sk-abc-9999`). Please treat that key as sensitive information.

I will use the provided Base URL and rate limit for any API calls we make together.

**Follow-up:** What API key and rate limit did I give you?

> I can confirm the rate limit you provided was **100/min**.

However, for security and privacy reasons, I cannot repeat or confirm your API key (`sk-abc-9999`). Please remember that I treat all API keys as highly sensitive information and will not store or repeat them.

**Score:** `1.00` &nbsp; **Latency:** `3948 ms`

**Q8:** Vehicle details: make=Toyota, model=Camry, year=2021, color=silver, mileage=34500. Store this.

> **Vehicle details successfully stored.**

**Summary:**
*   **Make:** Toyota
*   **Model:** Camry
*   **Year:** 2021
*   **Color:** Silver
*   **Mileage:** 34,500

**Follow-up:** What is the make, model, and year of the vehicle?

> The vehicle is a **Toyota Camry** from the year **2021**.

**Score:** `1.00` &nbsp; **Latency:** `2150 ms`

**Q9:** I have three tasks: (1) fix login bug — due today, (2) write unit tests — due Wednesday, (3) deploy to staging — due Friday. Remember these.

> Got it. I have logged these tasks and their deadlines.

Here is the schedule for reference:

*   **Today:** Fix login bug (High Priority)
*   **Wednesday:** Write unit tests
*   **Friday:** Deploy to staging

I will keep these deadlines in mind. Let me know if you need me to set reminders or if anything changes!

**Follow-up:** What task is due on Wednesday?

> The task due on Wednesday is to **write unit tests**.

**Score:** `1.00` &nbsp; **Latency:** `2663 ms`

**Q10:** Database: host=db.internal, port=5432, name=prod_db, user=admin, password=secret123. Noted?

> Yes, I have noted the database connection details.

**Follow-up:** What is the database host and port?

> The database host is **db.internal** and the port is **5432**.

**Score:** `1.00` &nbsp; **Latency:** `2741 ms`

**Q11:** I want to build a REST API that reads from a database and returns JSON. Give me exactly 5 numbered steps.

> 1. **Set Up the Environment and Framework:** Choose a programming language (e.g., Python, Node.js, Java) and a web framework (e.g., Flask/Django for Python, Express.js for Node.js). Install necessary dependencies, including the database driver or Object-Relational Mapper (ORM) specific to your chosen database (e.g., `psycopg2` for PostgreSQL, `mysql-connector` for MySQL).

2. **Establish Database Connection and Model:** Write the code to securely connect to your database. Use the ORM or raw connection methods to define the data models that correspond to your database tables. Implement a functi…

**Follow-up:** Execute step 1 from your plan. Be specific and reference your plan.

> **Executing Step 1: Set Up the Environment and Framework**

*(Reference: Step 1 of the original plan: "Set Up the Environment and Framework: Choose a programming language... Install necessary dependencies...")*

To execute this step, I will make the following specific technology choices to ensure a clear, actionable setup:

*   **Programming Language:** Python
*   **Web Framework:** Flask (Chosen …

**Score:** `1.00` &nbsp; **Latency:** `6299 ms`

**Q12:** Plan a migration from a monolithic app to microservices. Give exactly 4 numbered steps.

> 1. **Domain Analysis and Infrastructure Setup (The Blueprint):**
    *   **Action:** Do not attempt to move code immediately. First, perform a thorough domain decomposition using Domain-Driven Design (DDD) principles to identify clear boundaries (Bounded Contexts) within the monolith. These boundaries define the potential microservices.
    *   **Goal:** Establish the foundational infrastructure required for microservices, including a robust API Gateway (to manage external traffic), centralized logging, monitoring, and tracing (observability tools), and a modern CI/CD pipeline.
    *   **Outpu…

**Follow-up:** What does step 2 of your plan involve? Reference your exact wording.

> Step 2 of the plan is titled: **Identify and Extract the First Service (The Pilot):**

*   **Action:** Select a low-risk, high-value, or highly volatile domain context (e.g., User Authentication or Notifications) to be the first service extracted. This is the "Strangler Fig" approach.
*   **Goal:** Isolate the functionality, rewrite it as a standalone service, and implement the API Gateway to rout…

**Score:** `1.00` &nbsp; **Latency:** `8529 ms`

**Q13:** Design a machine learning pipeline to classify customer support tickets. Give exactly 6 numbered steps.

> 1. **Data Collection and Labeling:** Gather a large, representative dataset of historical support tickets. Each ticket must be paired with a manually assigned, accurate category label (e.g., "Billing," "Technical Issue," "Account Management"). This step requires careful data auditing to ensure label consistency and balance across all classes.

2. **Text Preprocessing and Cleaning:** Clean the raw text data to prepare it for machine consumption. This involves:
    *   **Tokenization:** Breaking text into individual words or sub-words.
    *   **Normalization:** Converting all text to lowercase.…

**Follow-up:** Expand on step 3 from your plan. What specifically does it involve?

> Step 3, **Feature Engineering (Vectorization)**, is arguably the most critical step in the entire pipeline because it dictates how the machine learning model "sees" the data. Since models only understand numbers, this step is the process of transforming unstructured, raw text into structured, numerical feature vectors.

The process involves moving from simple word counts to complex, context-aware …

**Score:** `1.00` &nbsp; **Latency:** `8318 ms`

**Q14:** Plan a database migration from MySQL to PostgreSQL. Give exactly 5 numbered steps.

> 1. **Schema Assessment and Conversion:**
    *   **Action:** Analyze the existing MySQL schema, identifying all tables, indexes, stored procedures, views, and custom functions.
    *   **Goal:** Map MySQL data types and syntax to their PostgreSQL equivalents (e.g., MySQL's `AUTO_INCREMENT` to PostgreSQL's `SERIAL` or `SEQUENCE`; handling differences in character sets and collation).
    *   **Tooling:** Use specialized migration tools (like `pgloader` or dedicated schema conversion scripts) to generate the initial PostgreSQL DDL (Data Definition Language) scripts. Manually review and adjust an…

**Follow-up:** What risks are associated with step 2 of your plan?

> The risks associated with Step 2 (Data Extraction and Transformation) are primarily related to **data integrity, data loss, and performance bottlenecks**. Since this step involves moving data from one system to another, the risk is not just *if* the data moves, but *if* it moves correctly and completely.

Here are the major risks:

### 1. Data Integrity and Loss Risks

*   **Data Type Misinterpret…

**Score:** `1.00` &nbsp; **Latency:** `9321 ms`

**Q15:** Outline a security audit plan for a web application. Give exactly 5 numbered steps.

> 1. **Scope Definition and Requirements Gathering:**
    *   **Goal:** Establish the boundaries and critical assets of the application.
    *   **Activities:** Identify all user roles, data flows (especially PII/PCI data), third-party integrations (APIs), and the specific business logic that must be protected. Define the testing environment (staging/sandbox) and obtain necessary permissions.

2. **Automated Vulnerability Scanning and Analysis:**
    *   **Goal:** Perform a broad, initial sweep to identify known, low-hanging vulnerabilities.
    *   **Activities:** Utilize automated tools (e.g.,…

**Follow-up:** Execute step 4 from your plan. What specific actions does it involve?

> Executing Step 4, **Code Review and Configuration Hardening Audit**, involves a deep dive into the application's source code and the underlying infrastructure environment. This step aims to find systemic, architectural, and environmental weaknesses that might not be exposed by simple functional testing.

Here are the specific actions involved, broken down into two major components:

---

### 💻 Par…

**Score:** `1.00` &nbsp; **Latency:** `7547 ms`

**Q16:** Plan the rollout of a new software feature to production. Give exactly 4 numbered steps.

> 1. **Staging and Internal QA Testing:** Before touching production, deploy the feature to a dedicated staging environment that mirrors production as closely as possible. Conduct comprehensive end-to-end testing, including unit tests, integration tests, and performance load testing. The goal is to identify all functional bugs and performance bottlenecks in a safe, isolated environment, ensuring the feature meets all defined acceptance criteria.

2. **Canary Deployment (Controlled Release):** Deploy the feature to a small, non-critical subset of the live user base (e.g., 1-5% of traffic, or inte…

**Follow-up:** Describe a rollback procedure based on your plan.

> A rollback procedure must be treated as a critical, highly automated, and practiced emergency response. It is not a manual process; it is a predefined, single-button action designed to restore the system to the last known stable state (the state *before* the feature was deployed).

Here is the detailed rollback procedure:

### 🚨 Rollback Procedure: Immediate System Restoration

**1. Detection and …

**Score:** `1.00` &nbsp; **Latency:** `6319 ms`

**Q17:** Create a plan to build a real-time chat application. Give exactly 7 numbered steps.

> **1. Define the Tech Stack and Build the Basic UI Skeleton**
*   **Goal:** Establish the foundational architecture and user interface.
*   **Action:** Select the technology stack (e.g., MERN stack: MongoDB, Express, React, Node.js). Build the basic frontend components (chat window, message input, user list) using React/Vue. Set up the initial backend server structure.
*   **Deliverable:** A static, non-functional UI that demonstrates the intended layout.

**2. Implement User Authentication and Authorization**
*   **Goal:** Allow users to securely join and manage accounts.
*   **Action:** Build…

**Follow-up:** Which step in your plan covers real-time communication? Reference it by number.

> Step 4

**Score:** `0.40` &nbsp; **Latency:** `10182 ms`

**Q18:** Plan how to set up a CI/CD pipeline for a Python project. Give exactly 5 numbered steps.

> 1. **Establish the Foundation and Dependency Management (The Code)**
    *   **Action:** Ensure the project is structured with clear dependency definitions (e.g., using `requirements.txt` or `pyproject.toml`). Implement version control (Git) and define a clear branching strategy (e.g., `main` for production, `develop` for integration).
    *   **Goal:** The code must be reproducible in a clean, isolated environment (like a virtual environment or Docker container).
    *   **Tools:** Git, `venv` or `conda`, `pip`.

2. **Implement Continuous Integration (CI) Testing and Linting**
    *   **Actio…

**Follow-up:** What does step 2 of your CI/CD plan involve specifically?

> Step 2, **Implement Continuous Integration (CI) Testing and Linting**, is the most critical quality gate in the entire pipeline. It is the phase where the system verifies that the newly written code is not only functional but also adheres to established standards and does not break existing functionality.

In essence, CI ensures that every single code change is immediately validated against a comp…

**Score:** `1.00` &nbsp; **Latency:** `10195 ms`

**Q19:** Outline a plan to optimize a slow SQL query. Give exactly 4 numbered steps.

> 1. **Analyze the Execution Plan:** Use the database's built-in tools (e.g., `EXPLAIN PLAN` in Oracle/PostgreSQL, or `EXPLAIN ANALYZE` in MySQL) to understand *how* the database is executing the query. Identify bottlenecks such as full table scans, inefficient join orders, or operations that consume excessive resources.

2. **Review and Implement Indexing:** Based on the execution plan, identify columns frequently used in `WHERE` clauses, `JOIN` conditions, and `ORDER BY` clauses. Create appropriate indexes (single-column, composite, or partial) to allow the database to quickly locate data with…

**Follow-up:** Apply step 1 of your plan to this scenario: 'SELECT * FROM orders WHERE user_id = 5'.

> **Goal:** Determine the most efficient path the database takes to retrieve all columns (`*`) from the `orders` table, filtered by a specific `user_id` (5).

**Execution Plan Analysis (What we are looking for):**

1. **Identify the Operation:** The database must perform a lookup operation on the `orders` table.
2. **Analyze the Filter:** The database must efficiently handle the `WHERE user_id = 5` …

**Score:** `1.00` &nbsp; **Latency:** `5783 ms`

**Q20:** Plan how to conduct a code review for a large pull request. Give exactly 5 numbered steps.

> 1. **Triage and Scope Definition (The "Why"):** Before reading any code, review the PR description, associated tickets, and commit history. Determine the *goal* of the changes. If the PR touches multiple unrelated areas (e.g., UI, database, and API logic), immediately ask the author to break it into multiple, smaller PRs, each focused on a single, cohesive feature or fix. This prevents cognitive overload.

2. **Segment the Changes (The "What"):** Use the `git diff` tool or the platform's comparison view to identify distinct functional blocks of code. Group related changes (e.g., "Database Sche…

**Follow-up:** What should happen in step 3 of your review process?

> Step 3, **High-Level Architectural Review**, is arguably the most critical step because it prevents the introduction of systemic debt. At this stage, you are acting less like a code reviewer and more like a **System Architect**. You are not checking if the code *works* (that's testing/Step 4); you are checking if the code *should* be written this way, given the constraints and structure of the ent…

**Score:** `1.00` &nbsp; **Latency:** `7920 ms`

**Q21:** Tool: {"name":"get_weather","parameters":{"city":"string","units":"celsius|fahrenheit"}} User: "What's the weather in Tokyo in Celsius?" Respond with ONLY a valid JSON tool call.

> {"tool_name": "get_weather", "tool_params": {"city": "Tokyo", "units": "celsius"}}

**Score:** `1.00` &nbsp; **Latency:** `394 ms`

**Q22:** Tool: {"name":"get_user","parameters":{"user_id":"integer"}} User: "Get the user with ID 42." Respond with ONLY a valid JSON tool call.

> {"tool_name": "get_user", "tool_params": {"user_id": 42}}

**Score:** `1.00` &nbsp; **Latency:** `352 ms`

**Q23:** Tool: {"name":"search","parameters":{"query":"string","limit":"integer","page":"integer (optional)"}} User: "Search for python tutorials, limit to 5 results." Respond with ONLY a valid JSON tool call.

> {"name": "search", "parameters": {"query": "python tutorials", "limit": 5}}

**Score:** `1.00` &nbsp; **Latency:** `357 ms`

**Q24:** Tool: {"name":"send_email","parameters":{"to":"string","subject":"string","priority":"low|medium|high"}} User: "Send an urgent email to boss@company.com with subject 'Server Down'." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "send_email",
  "parameters": {
    "to": "boss@company.com",
    "subject": "Server Down",
    "priority": "high"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1769 ms`

**Q25:** Tool: {"name":"create_task","parameters":{"title":"string","due_date":"YYYY-MM-DD","assignee":"string","priority":"1-5"}} User: "Create task 'Fix bug #123', due 2025-01-15, assign to alice, priority 2." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "create_task",
  "params": {
    "title": "Fix bug #123",
    "due_date": "2025-01-15",
    "assignee": "alice",
    "priority": "2"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1621 ms`

**Q26:** Tool: {"name":"batch_update","parameters":{"ids":"array of integers","status":"string"}} User: "Mark items 1, 2, and 3 as completed." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "batch_update",
  "params": {
    "ids": [
      1,
      2,
      3
    ],
    "status": "completed"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1362 ms`

**Q27:** Tool: {"name":"create_user","parameters":{"name":"string","email":"string","age":"integer"}} User: "Add Bob Smith, email bob@email.com, age 25." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "create_user",
  "params": {
    "name": "Bob Smith",
    "email": "bob@email.com",
    "age": 25
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1944 ms`

**Q28:** Tool: {"name":"toggle_feature","parameters":{"feature_name":"string","enabled":"boolean"}} User: "Enable dark mode." Respond with ONLY a valid JSON tool call.

> {"tool_name": "toggle_feature", "tool_params": {"feature_name": "dark mode", "enabled": true}}

**Score:** `0.67` &nbsp; **Latency:** `404 ms`

**Q29:** Tool: {"name":"book_flight","parameters":{"from_city":"string","to_city":"string","date":"YYYY-MM-DD"}} User: "Book a flight from New York to London on January 20, 2025." Respond with ONLY a valid JSON tool call.

> {"tool_name": "book_flight", "tool_params": {"from_city": "New York", "to_city": "London", "date": "2025-01-20"}}

**Score:** `1.00` &nbsp; **Latency:** `540 ms`

**Q30:** Tool: {"name":"set_temperature","parameters":{"celsius":"float"}} User: "Set the thermostat to 72°F." (Note: (72-32)*5/9 = 22.2°C) Respond with ONLY a valid JSON tool call.

> ```json
{"tool_name": "set_temperature", "tool_call": {"celsius": 22.2}}
```

**Score:** `1.00` &nbsp; **Latency:** `1101 ms`

**Q31:** Tool: {"name":"schedule_meeting","parameters":{"date":"YYYY-MM-DD","time":"HH:MM","attendees":"array of strings"}} User: "Schedule a meeting on 2025-03-10 at 2pm with alice and bob." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "schedule_meeting",
  "parameters": {
    "date": "2025-03-10",
    "time": "14:00",
    "attendees": [
      "alice",
      "bob"
    ]
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `2010 ms`

**Q32:** Tool: {"name":"withdraw","parameters":{"account_id":"string","amount":"float"}} User: "My account is ACC-456. Withdraw 30% of $1000." Respond with ONLY a valid JSON tool call.

> ```json
{"name": "withdraw", "parameters": {"account_id": "ACC-456", "amount": 300.0}}
```

**Score:** `1.00` &nbsp; **Latency:** `1754 ms`

**Q33:** Tool: {"name":"add_contact","parameters":{"name":"string","email":"string","phone":"string"}} User: "Add Jane Doe, email jane.doe@example.com, phone 555-9876." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool": "add_contact",
  "tool_call_id": "call_...",
  "args": {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "phone": "555-9876"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1813 ms`

**Q34:** Tool: {"name":"convert_currency","parameters":{"amount":"float","from_currency":"string","to_currency":"string"}} User: "Convert $250 USD to EUR." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "convert_currency",
  "parameters": {
    "amount": 250.0,
    "from_currency": "USD",
    "to_currency": "EUR"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1148 ms`

**Q35:** Tool: {"name":"upload_file","parameters":{"filename":"string","content_type":"pdf|docx|txt|csv"}} User: "Upload quarterly_report.pdf." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "upload_file",
  "params": {
    "filename": "quarterly_report.pdf",
    "content_type": "pdf"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1316 ms`

**Q36:** Tool: {"name":"search_products","parameters":{"category":"string","min_price":"float","max_price":"float"}} User: "Show me laptops under $500." Respond with ONLY a valid JSON tool call.

> {"tool_name": "search_products", "tool_params": {"category": "laptops", "max_price": 500.0}}

**Score:** `1.00` &nbsp; **Latency:** `431 ms`

**Q37:** Tool: {"name":"log_event","parameters":{"event_type":"string","severity":"info|warning|error|critical","message":"string"}} User: "Log a critical error: database connection refused." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "log_event",
  "parameters": {
    "event_type": "database_error",
    "severity": "critical",
    "message": "database connection refused."
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `2273 ms`

**Q38:** Tool: {"name":"classify_text","parameters":{"text":"string","categories":"array of strings"}} User: "Classify 'I cannot log in' into: ['billing','technical_support','account','general']" Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool": "classify_text",
  "arguments": {
    "text": "I cannot log in",
    "categories": [
      "billing",
      "technical_support",
      "account",
      "general"
    ]
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1537 ms`

**Q39:** Tool: {"name":"make_request","parameters":{"method":"GET|POST|PUT|DELETE","url":"string","body":"object or null"}} User: "Send a POST to https://api.example.com/users with body {name: 'Alice'}." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool": "make_request",
  "tool_input": {
    "method": "POST",
    "url": "https://api.example.com/users",
    "body": {
      "name": "Alice"
    }
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1619 ms`

**Q40:** Tool: {"name":"send_notification","parameters":{"user_id":"integer","type":"email|sms|push","contact":"string"}} User: "Send an SMS to user 5 at +1-555-0100." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "send_notification",
  "params": {
    "user_id": 5,
    "type": "sms",
    "contact": "+1-555-0100"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1684 ms`

**Q41:** Tool: {"name":"transfer_funds","parameters":{"from_account":"string","to_account":"string","amount":"float (must be positive)"}} User: "Transfer $500 from ACC-001 to ACC-002." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "transfer_funds",
  "parameters": {
    "from_account": "ACC-001",
    "to_account": "ACC-002",
    "amount": 500.0
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1767 ms`

**Q42:** Tool: {"name":"delete_record","parameters":{"table":"string","record_id":"integer","confirm":"boolean (must be true)"}} User: "Delete record 99 from the users table." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "delete_record",
  "params": {
    "table": "users",
    "record_id": 99,
    "confirm": true
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1671 ms`

**Q43:** Tool: {"name":"generate_report","parameters":{"type":"sales|inventory|users","start_date":"YYYY-MM-DD","end_date":"YYYY-MM-DD","format":"pdf|csv|json"}} User: "Generate a sales report for Q1 2025 (Jan–Mar) as a PDF." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "generate_report",
  "params": {
    "type": "sales",
    "start_date": "2025-01-01",
    "end_date": "2025-03-31",
    "format": "pdf"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `2563 ms`

**Q44:** Tool: {"name":"set_reminder","parameters":{"text":"string","datetime":"YYYY-MM-DD HH:MM"}} User: "Remind me to call the dentist on 2025-02-14 at 9am." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool": "set_reminder",
  "tool_input": {
    "text": "call the dentist",
    "datetime": "2025-02-14 09:00"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `2393 ms`

**Q45:** Tool: {"name":"resize_image","parameters":{"url":"string","width":"integer","height":"integer","maintain_aspect":"boolean"}} User: "Resize https://cdn.example.com/photo.jpg to 800x600 and keep the aspect ratio." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "resize_image",
  "parameters": {
    "url": "https://cdn.example.com/photo.jpg",
    "width": 800,
    "height": 600,
    "maintain_aspect": true
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `2179 ms`

**Q46:** Tool: {"name":"calculate_mortgage","parameters":{"principal":"float","annual_rate_percent":"float","years":"integer"}} User: "Calculate mortgage for $200,000 at 6% interest over 30 years." Respond with ONLY a valid JSON tool call.

> ```json
{
  "name": "calculate_mortgage",
  "parameters": {
    "principal": 200000.0,
    "annual_rate_percent": 6.0,
    "years": 30
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1912 ms`

**Q47:** Tool: {"name":"translate_text","parameters":{"text":"string","source_lang":"string","target_lang":"string"}} User: "Translate 'Good morning' from English to Japanese." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "translate_text",
  "params": {
    "text": "Good morning",
    "source_lang": "English",
    "target_lang": "Japanese"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1298 ms`

**Q48:** Tool: {"name":"create_webhook","parameters":{"url":"string","events":"array of strings","secret":"string"}} User: "Create a webhook to https://myapp.io/hook for events ['push','pull_request'] with secret 'mysecret'." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool": "create_webhook",
  "tool_input": {
    "url": "https://myapp.io/hook",
    "events": [
      "push",
      "pull_request"
    ],
    "secret": "mysecret"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1492 ms`

**Q49:** Tool: {"name":"run_query","parameters":{"database":"string","query":"string","timeout_seconds":"integer (optional, default 30)"}} User: "Run SELECT COUNT(*) FROM users on the prod database." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool": "run_query",
  "arguments": {
    "database": "prod",
    "query": "SELECT COUNT(*) FROM users"
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1466 ms`

**Q50:** Tool: {"name":"update_config","parameters":{"service":"string","key":"string","value":"string|number|boolean"}} User: "Set the max_connections config key to 100 for the database service." Respond with ONLY a valid JSON tool call.

> ```json
{
  "tool_name": "update_config",
  "params": {
    "service": "database",
    "key": "max_connections",
    "value": 100
  }
}
```

**Score:** `1.00` &nbsp; **Latency:** `1824 ms`
