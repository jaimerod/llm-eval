# LLM Evaluation Report: `qwen3-coder:30b`

**Date:** 2026-05-07  
**Overall Score:** 92.1 / 100

---

## Summary

| Category | Score | Questions |
|----------|------:|----------:|
| Reasoning | 82.7 | 50 |
| Mathematics | 93.0 | 50 |
| Knowledge | 88.3 | 50 |
| Code | 100.0 | 50 |
| Instruction Following | 93.0 | 50 |
| Agentic | 95.5 | 50 |

## Performance Metrics

| Metric | Value |
|--------|------:|
| Average latency | 17510 ms |
| Estimated tokens / sec | 14.2 |
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

Since all cats are mammals and Garfield is a cat, Garfield must be a mammal.

**Score:** `1.00` &nbsp; **Latency:** `969 ms`

**Q2:** If it takes 5 machines 5 minutes to make 5 widgets, how long for 100 machines to make 100 widgets? Answer with the number and unit only.

> 5 minutes

**Score:** `1.00` &nbsp; **Latency:** `405 ms`

**Q3:** A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost in cents? Answer with just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `373 ms`

**Q4:** You have a 3-liter and a 5-liter bucket. How do you measure exactly 4 liters? Describe briefly.

> Fill the 5-liter bucket, then pour from it into the 3-liter bucket until the 3-liter bucket is full. This leaves exactly 2 liters in the 5-liter bucket. Empty the 3-liter bucket, then pour the 2 liters from the 5-liter bucket into the 3-liter bucket. Finally, fill the 5-liter bucket again and pour from it into the 3-liter bucket (which already has 2 liters) until it's full. This leaves exactly 4 liters in the 5-liter bucket.

**Score:** `1.00` &nbsp; **Latency:** `3337 ms`

**Q5:** Three boxes are labeled Apples, Oranges, and Mixed — all labels are wrong. You pick one fruit from the Mixed box and it's an apple. What is in each box? Answer concisely.

> Since all labels are wrong and the Mixed box actually contains apples, the Mixed box must contain apples.

The box labeled "Mixed" actually contains apples.
The box labeled "Apples" must contain oranges (since it can't contain apples or mixed).
The box labeled "Oranges" must contain the mixed fruits (since it can't contain oranges or apples).

So:
- Box labeled "Mixed" = Apples
- Box labeled "Apples" = Oranges  
- Box labeled "Oranges" = Mixed

**Score:** `1.00` &nbsp; **Latency:** `3421 ms`

**Q6:** A snail climbs 3 feet up a wall each day and slides 2 feet down each night. The wall is 10 feet tall. On which day does the snail reach the top? Just the number.

> 8

**Score:** `1.00` &nbsp; **Latency:** `363 ms`

**Q7:** In a race you overtake the runner in 2nd place. What position are you now in? Answer with just the position.

> 2nd place

**Score:** `0.50` &nbsp; **Latency:** `379 ms`

**Q8:** How many months in a year have 28 days? Answer with just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `242 ms`

**Q9:** Mary's mother has four children: April, May, June, and one more. What is the fourth child's name?

> The fourth child's name is Mary.

The question states "Mary's mother has four children" and then lists April, May, June, and "one more." Since we're told at the beginning that this is Mary's mother, Mary herself must be the fourth child.

**Score:** `1.00` &nbsp; **Latency:** `1691 ms`

**Q10:** An electric train is traveling north. The wind is blowing east. Which direction does the smoke blow from the train?

> This is a trick question! An electric train doesn't produce smoke.

Electric trains are powered by electricity from overhead lines or batteries, so they don't have engines that burn fuel and produce smoke. Therefore, there would be no smoke to be blown by the wind in any direction.

If this were a steam train instead, then the smoke would be blown westward (opposite to the wind direction) as the train moves north and the wind blows east. But since it's specifically an electric train, no smoke is produced at all.

**Score:** `1.00` &nbsp; **Latency:** `3295 ms`

**Q11:** A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have? Just the number.

> 9

**Score:** `1.00` &nbsp; **Latency:** `230 ms`

**Q12:** What comes next in the sequence: O, T, T, F, F, S, S, E, N, ? (Hint: think of number names)

> Looking at this sequence, I need to think about the names of numbers and how they start:

O - One
T - Two  
T - Three
F - Four
F - Five
S - Six
S - Seven
E - Eight
N - Nine

So the pattern is the first letter of each number name in order:
- One (O)
- Two (T)
- Three (T)
- Four (F)
- Five (F)
- Six (S)
- Seven (S)
- Eight (E)
- Nine (N)
- Ten (T)

The next letter would be **T** for "Ten."

The sequence continues: O, T, T, F, F, S, S, E, N, T

**Score:** `1.00` &nbsp; **Latency:** `4719 ms`

**Q13:** Two mothers and two daughters go fishing. Each catches exactly one fish, yet only 3 fish are caught total. How is this possible?

> This is a classic riddle! The solution is that the group consists of only 3 people total, not 4.

The three people are:
- A grandmother (who is also a mother)
- A mother (who is also a daughter)  
- A daughter (who is also a granddaughter)

So we have:
- 2 mothers: the grandmother and the mother
- 2 daughters: the mother and the daughter

But there are only 3 people total, so only 3 fish are caught.

The key is realizing that one person (the mother) fills two roles in the family relationship - she is both a mother to her daughter and a daughter to her mother.

**Score:** `1.00` &nbsp; **Latency:** `4337 ms`

**Q14:** Rearrange the letters B, E, L, O, W to form a common English word.

> The letters B, E, L, O, W can be arranged to form the word **"WELBO"** - but that's not a common English word.

Let me try again: The letters B, E, L, O, W can form **"BLOWE"** - but that's also not a standard English word.

Actually, rearranging B, E, L, O, W, the common English word is **"WELBO"** - no, let me reconsider this more carefully.

The letters B, E, L, O, W can form the word **"BLOW"** - but that uses only 4 letters, and we have 5 letters.

Wait - the letters B, E, L, O, W can form the word **"WELBO"** - no, that's not right.

Looking at this again, the letters B, E, L, O, W can f…

**Score:** `0.00` &nbsp; **Latency:** `4568640 ms`

**Q15:** A lily pad doubles in size every day and covers the entire pond in 48 days. How many days does it take to cover half the pond? Just the number.

> 47

**Score:** `1.00` &nbsp; **Latency:** `473 ms`

**Q16:** You have two ropes. Each burns in exactly 60 minutes but not at a uniform rate. How do you measure exactly 45 minutes? Explain briefly.

> Light both ends of the first rope AND one end of the second rope simultaneously.

When the first rope burns out completely (after 30 minutes), light the other end of the second rope. The second rope will then burn out in 15 more minutes, giving you exactly 45 minutes total.

The key insight is that lighting both ends of the first rope makes it burn twice as fast, so it burns out in 30 minutes regardless of its non-uniform burning rate.

**Score:** `1.00` &nbsp; **Latency:** `3532 ms`

**Q17:** A clock shows 3:15. What is the exact angle in degrees between the hour and minute hands? Just the number.

> 12.5

**Score:** `0.00` &nbsp; **Latency:** `452 ms`

**Q18:** You have 12 identical-looking balls; one is heavier. Using a balance scale, what is the minimum number of weighings to guarantee finding the heavy ball?

> I need to find the minimum number of weighings to guarantee identifying the one heavier ball among 12 identical-looking balls using a balance scale.

Let me think about this systematically using the concept of information theory and divide-and-conquer strategy.

Each weighing on a balance scale can give me one of three results:
- Left side heavier
- Right side heavier  
- Both sides equal

So each weighing gives me log₂(3) ≈ 1.58 bits of information.

With n weighings, I can distinguish between 3ⁿ different outcomes.

I need to distinguish between 12 possible cases (any one of the 12 balls cou…

**Score:** `1.00` &nbsp; **Latency:** `17254 ms`

**Q19:** If you drive to work at 30 mph, how fast must you drive back to average 60 mph for the round trip?

> This is a classic puzzle! Let me work through it step by step.

Let's say the distance to work is $d$ miles.

**Going to work:**
- Speed: 30 mph
- Time: $\frac{d}{30}$ hours

**Coming back:**
- Speed: $v$ mph (what we're looking for)
- Time: $\frac{d}{v}$ hours

**For the round trip:**
- Total distance: $2d$ miles
- Total time: $\frac{d}{30} + \frac{d}{v}$ hours
- Average speed: 60 mph

Using the average speed formula:
$$\text{Average speed} = \frac{\text{Total distance}}{\text{Total time}}$$

$$60 = \frac{2d}{\frac{d}{30} + \frac{d}{v}}$$

Simplifying:
$$60 = \frac{2d}{d(\frac{1}{30} + \frac{…

**Score:** `0.67` &nbsp; **Latency:** `14870 ms`

**Q20:** The Monty Hall problem: you pick door 1, the host opens door 3 revealing a goat. Should you switch to door 2? Answer Yes/No and give the win probability if you switch.

> Yes

If you switch to door 2, your win probability is 2/3.

Here's why: Initially, there's a 1/3 chance the prize is behind door 1 (your original choice) and a 2/3 chance it's behind one of doors 2 or 3. When the host opens door 3 to reveal a goat, they're not changing the initial probabilities - the prize is still twice as likely to be behind door 2 than door 1. So switching gives you a 2/3 chance of winning.

**Score:** `0.67` &nbsp; **Latency:** `4060 ms`

**Q21:** If 2+3=10, 7+2=63, 6+5=66, 8+4=96, then 9+7=? Just the number.

> 96

**Score:** `0.00` &nbsp; **Latency:** `370 ms`

**Q22:** How many squares are on a standard 8×8 chessboard? (Count all sizes, not just 1×1.) Just the number.

> 204

**Score:** `1.00` &nbsp; **Latency:** `408 ms`

**Q23:** Is this argument valid? 'All dogs are animals. All cats are animals. Therefore all dogs are cats.' Answer Yes or No and identify the fallacy.

> No

The fallacy is "Affirming the consequent" or more specifically a "False dichotomy" / "Equivocation" fallacy. 

The argument incorrectly assumes that because dogs and cats share a common property (being animals), they must be the same thing. This ignores the fact that multiple different categories can belong to the same broader category. Just because all dogs are animals and all cats are animals, it doesn't follow that all dogs are cats.

**Score:** `0.67` &nbsp; **Latency:** `3383 ms`

**Q24:** Three friends pay $30 for a hotel room. Manager refunds $5; bellhop keeps $2 and returns $1 each. Each friend paid $9 = $27 total; plus $2 = $29. Where is the missing dollar?

> This is a classic puzzle that tricks people with misleading arithmetic!

The error is in the final calculation. Here's what actually happened:

**What the friends paid:**
- Each friend originally paid $10
- Each friend got $1 back
- Each friend effectively paid $9
- Total paid by friends: $9 × 3 = $27

**Where that $27 went:**
- $25 went to the hotel (the actual room cost)
- $2 went to the bellhop (tip/keep)
- $27 = $25 (hotel) + $2 (bellhop) ✓

**The mistake in the puzzle:**
The puzzle incorrectly adds the bellhop's $2 to the $27 the friends paid, but the bellhop's $2 is **part of** the $27 -…

**Score:** `0.50` &nbsp; **Latency:** `10452 ms`

**Q25:** How many times does the digit 1 appear in all integers from 1 to 100? Just the number.

> 21

**Score:** `1.00` &nbsp; **Latency:** `265 ms`

**Q26:** At what time between 3 and 4 o'clock are the hour and minute hands of a clock exactly coincident? Answer in minutes past 3, to 2 decimal places.

> I need to find the time between 3 and 4 o'clock when the hour and minute hands coincide.

Let me set up the problem by defining the speeds of the hands:
- The minute hand moves at 6° per minute (360°/60 minutes)
- The hour hand moves at 0.5° per minute (360°/12 hours = 30°/hour = 0.5°/minute)

At 3:00, the hour hand is at 90° (3 × 30°) and the minute hand is at 0°.

Let t be the number of minutes after 3:00.

After t minutes:
- The minute hand will be at 6t degrees
- The hour hand will be at 90 + 0.5t degrees

The hands coincide when their positions are equal:
6t = 90 + 0.5t

Solving for t:
6t…

**Score:** `1.00` &nbsp; **Latency:** `12815 ms`

**Q27:** You have a 100-floor building and 2 eggs. You want to find the highest floor an egg survives from. What is the minimum worst-case number of drops needed?

> I need to find the minimum worst-case number of drops to determine the highest floor an egg can survive from in a 100-floor building with 2 eggs.

Let me think about this systematically.

Let's say the minimum worst-case number of drops is `k`. I need to find the smallest `k` such that I can guarantee finding the answer in at most `k` drops.

The key insight is that with 2 eggs, I can use a strategy where:
- First egg: I drop it from floors at strategic intervals
- Second egg: I test each floor sequentially between my drops

Let me work backwards. If I have `k` drops available, what's the maxi…

**Score:** `1.00` &nbsp; **Latency:** `29881 ms`

**Q28:** A logician visits an island where everyone either always lies or always tells the truth. A native says: 'I am a liar.' Is the native a truth-teller, a liar, or is this impossible?

> This is a classic logical paradox! Let me analyze this step by step.

Let's consider what happens if the native is a truth-teller:
- If the native is a truth-teller, then everything they say is true
- So the statement "I am a liar" would be true
- But if they are telling the truth, they cannot be a liar
- This creates a contradiction

Now let's consider what happens if the native is a liar:
- If the native is a liar, then everything they say is false
- So the statement "I am a liar" would be false
- For the statement "I am a liar" to be false, the native must actually be a truth-teller
- But w…

**Score:** `0.67` &nbsp; **Latency:** `10064 ms`

**Q29:** What is the minimum number of moves to solve the Tower of Hanoi with 4 discs? Just the number.

> 15

**Score:** `1.00` &nbsp; **Latency:** `261 ms`

**Q30:** A store reduces a price by 10% then reduces it by another 10%. Is the total reduction 20%? Answer Yes/No and give the actual percentage.

> No

Let's say the original price is $100.

After the first 10% reduction: $100 - 10% = $100 - $10 = $90

After the second 10% reduction: $90 - 10% = $90 - $9 = $81

The final price is $81, which represents a reduction of $19 from the original $100.

The actual percentage reduction is: ($19/$100) × 100% = 19%

The total reduction is 19%, not 20%.

**Score:** `1.00` &nbsp; **Latency:** `4738 ms`

**Q31:** What is the maximum number of regions a plane can be divided into by 5 straight lines? Just the number.

> 31

**Score:** `0.00` &nbsp; **Latency:** `267 ms`

**Q32:** If you write all numbers from 1 to 1000, how many times do you write the digit 0? Just the number.

> 300

**Score:** `0.00` &nbsp; **Latency:** `403 ms`

**Q33:** Look-and-Say sequence: 1, 11, 21, 1211, 111221. What is the next term?

> I need to find the next term in the Look-and-Say sequence by analyzing the pattern.

Let me examine each term and see how it's generated:

1. Start with: 1
2. Next term: 11 (one 1)
3. Next term: 21 (two 1s)
4. Next term: 1211 (one 2, one 1)
5. Next term: 111221 (one 1, one 2, two 1s)

Wait, let me be more careful about the last term:
- 111221 means: one 1, one 2, two 1s
- That's: 11 12 21 = 111221

Actually, let me trace this properly:
- 1 → "one 1" → 11
- 11 → "two 1s" → 21  
- 21 → "one 2, one 1" → 1211
- 1211 → "one 1, one 2, two 1s" → 111221

Now for the next term:
111221 → "three 1s, two …

**Score:** `1.00` &nbsp; **Latency:** `11304 ms`

**Q34:** Albert is taller than Bob. Carlos is shorter than Albert. David is taller than Carlos but shorter than Bob. Who is the second tallest? Just the name.

> Bob

**Score:** `1.00` &nbsp; **Latency:** `340 ms`

**Q35:** What is 1/3 of 3/4 of 48? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `263 ms`

**Q36:** Two children share the same parents, were born at the same time, but are not twins. How?

> They are triplets (or part of a larger multiple birth like quadruplets, quintuplets, etc.).

While the riddle states "two children share the same parents, were born at the same time, but are not twins," it doesn't explicitly rule out other types of multiple births. Triplets are three children born at the same time to the same parents, so any two of them would be correct - they share the same parents, were born at the same time, and are not twins (since there are three total, not two).

This is a classic riddle that plays on the common assumption that "two children sharing the same parents and …

**Score:** `1.00` &nbsp; **Latency:** `5325 ms`

**Q37:** How many prime numbers are there between 1 and 20? Just the number.

> 8

**Score:** `1.00` &nbsp; **Latency:** `216 ms`

**Q38:** Alice runs at 5 m/s and Bob at 3 m/s on a circular 400-meter track, both in the same direction. How many seconds until Alice laps Bob? Just the number.

> To find when Alice laps Bob, I need to determine when Alice has gained a full lap (400 meters) on Bob.

Since they're running in the same direction, I need to find the relative speed at which Alice is gaining on Bob.

Alice's speed: 5 m/s
Bob's speed: 3 m/s
Relative speed of Alice with respect to Bob: 5 - 3 = 2 m/s

Alice needs to gain 400 meters on Bob to complete one full lap.
Time = Distance ÷ Relative speed
Time = 400 ÷ 2 = 200 seconds

200

**Score:** `1.00` &nbsp; **Latency:** `4670 ms`

**Q39:** If P(rain) = 0.3 on any day, what is P(no rain on two consecutive days)? Give as a decimal.

> I need to find the probability of no rain on two consecutive days.

Given information:
- P(rain) = 0.3 on any day
- Therefore, P(no rain) = 1 - 0.3 = 0.7 on any day

Since the weather on consecutive days are independent events, I can multiply the probabilities:

P(no rain on day 1 AND no rain on day 2) = P(no rain on day 1) × P(no rain on day 2)

P(no rain on two consecutive days) = 0.7 × 0.7 = 0.49

0.49

**Score:** `1.00` &nbsp; **Latency:** `4620 ms`

**Q40:** A doctor gives you 3 pills and says take one every 30 minutes. How many minutes until all pills are taken? Just the number.

> 60

**Score:** `1.00` &nbsp; **Latency:** `376 ms`

**Q41:** What is wrong with this reasoning: 'I've flipped a coin 10 times and got heads every time, so tails is overdue.' Name the fallacy.

> This reasoning commits the **Gambler's Fallacy** (also known as the Monte Carlo Fallacy).

The fallacy occurs when someone believes that past random events affect the probabilities of future independent events. In this case, the person incorrectly thinks that because they've gotten heads 10 times in a row, tails "must" come up soon to "balance out" the results.

**Why this is wrong:**
- Each coin flip is an independent event
- The probability of getting heads or tails remains 50/50 for each individual flip
- The coin has no memory of previous flips
- The law of large numbers doesn't work the w…

**Score:** `1.00` &nbsp; **Latency:** `8290 ms`

**Q42:** Four people cross a bridge at night with one torch: A=1 min, B=2 min, C=5 min, D=10 min. Max 2 per crossing. Minimum total time in minutes?

> I need to find the minimum time for four people with different crossing times to cross a bridge with one torch.

Let me denote the people by their crossing times:
- A: 1 minute
- B: 2 minutes  
- C: 5 minutes
- D: 10 minutes

Constraints:
- Maximum 2 people per crossing
- Must have the torch to cross
- Need to get everyone across

Let me think about the optimal strategy:

The key insight is that the slowest people (C and D) should cross together to minimize the number of times the torch needs to be carried back.

Here's my approach:
1. First crossing: A and B go together (time = 2 minutes)
2. …

**Score:** `1.00` &nbsp; **Latency:** `17852 ms`

**Q43:** Complete the pattern: 2, 3, 5, 7, 11, 13, ? (What rule governs this sequence?)

> This sequence is the **prime numbers** in ascending order.

The pattern is: **2, 3, 5, 7, 11, 13, 17**

The rule governing this sequence is that each number is a **prime number** - a natural number greater than 1 that has no positive divisors other than 1 and itself.

Looking at the sequence:
- 2 (prime)
- 3 (prime)
- 5 (prime)
- 7 (prime)
- 11 (prime)
- 13 (prime)
- 17 (prime)

The next number in the sequence is **17**.

This is one of the most fundamental and well-known sequences in mathematics, as prime numbers are the building blocks of all natural numbers through prime factorization.

**Score:** `1.00` &nbsp; **Latency:** `5742 ms`

**Q44:** You are in a room with two doors. One leads to freedom, one to a tiger. Two guards know which is which: one always lies, one always tells the truth. You can ask one guard one yes/no question. What do you ask?

> I ask either guard: "If I were to ask the other guard which door leads to freedom, what would they point to?"

Then I choose the opposite door from whichever one they indicate.

Here's why this works:

Let's say Door A leads to freedom and Door B leads to the tiger.

If I ask the truth-teller:
- They know the liar would point to Door B (the tiger)
- So they truthfully tell me the liar would point to Door B

If I ask the liar:
- They know the truth-teller would point to Door A (freedom)
- But since they lie, they lie about this and point to Door B (the tiger)

In both cases, the guard I ask wil…

**Score:** `1.00` &nbsp; **Latency:** `6791 ms`

**Q45:** A number equals the sum of its proper divisors (divisors less than itself). What is the smallest such number greater than 1?

> I need to find the smallest perfect number greater than 1.

A perfect number equals the sum of its proper divisors (divisors less than itself).

Let me check small numbers systematically:

For n = 2:
- Proper divisors: 1
- Sum of proper divisors: 1
- 1 ≠ 2, so 2 is not perfect

For n = 3:
- Proper divisors: 1
- Sum of proper divisors: 1
- 1 ≠ 3, so 3 is not perfect

For n = 4:
- Proper divisors: 1, 2
- Sum of proper divisors: 1 + 2 = 3
- 3 ≠ 4, so 4 is not perfect

For n = 5:
- Proper divisors: 1
- Sum of proper divisors: 1
- 1 ≠ 5, so 5 is not perfect

For n = 6:
- Proper divisors: 1, 2, 3
- …

**Score:** `1.00` &nbsp; **Latency:** `11341 ms`

**Q46:** If all Wumps are Mooks and half of all Mooks are Wumps, what fraction of Mooks are Wumps? Answer as a fraction.

> I need to analyze the relationship between Wumps and Mooks based on the given information.

Given information:
- All Wumps are Mooks
- Half of all Mooks are Wumps

Let me define variables:
- Let W = number of Wumps
- Let M = number of Mooks

From the first statement: "All Wumps are Mooks"
This means every Wump is also a Mook, so W ≤ M.

From the second statement: "Half of all Mooks are Wumps"
This means W = (1/2) × M

So: W = M/2

The fraction of Mooks that are Wumps = W/M = (M/2)/M = 1/2

Therefore, 1/2 of Mooks are Wumps.

The answer is 1/2.

**Score:** `0.67` &nbsp; **Latency:** `5874 ms`

**Q47:** Which is larger: 2^(3^2) or (2^3)^2? State which and give both values.

> I need to calculate both expressions to compare them.

First, let me calculate 2^(3^2):
- 3^2 = 9
- 2^(3^2) = 2^9 = 512

Next, let me calculate (2^3)^2:
- 2^3 = 8
- (2^3)^2 = 8^2 = 64

Comparing the results:
- 2^(3^2) = 512
- (2^3)^2 = 64

Therefore, 2^(3^2) is larger.

**Answer: 2^(3^2) is larger**
- 2^(3^2) = 512
- (2^3)^2 = 64

**Score:** `1.00` &nbsp; **Latency:** `5701 ms`

**Q48:** A frog is at the bottom of a 10-foot well. Each day it climbs 3 feet; each night it falls 1 foot. On what day does it escape? Just the number.

> 7

**Score:** `0.00` &nbsp; **Latency:** `355 ms`

**Q49:** You measure the height of a building by dropping a stone and timing its fall at 3 seconds. Using d = ½gt² and g = 9.8 m/s², how tall is the building in meters? Just the number.

> 44.1

**Score:** `1.00` &nbsp; **Latency:** `477 ms`

**Q50:** If you have a 3×3 grid and place numbers 1–9 so each row, column, and diagonal sums to 15 (a magic square), what number goes in the center? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `375 ms`


### Mathematics

**Q1:** What is 15% of 240? Just the number.

> 36

**Score:** `1.00` &nbsp; **Latency:** `242 ms`

**Q2:** A train travels at 60 mph for 2 hours 30 minutes. How far in miles? Just the number.

> 150

**Score:** `1.00` &nbsp; **Latency:** `290 ms`

**Q3:** What is √144? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `229 ms`

**Q4:** A rectangle is 8 cm × 5 cm. What is its area? Just the number.

> 40

**Score:** `1.00` &nbsp; **Latency:** `247 ms`

**Q5:** Solve for x: 3x + 7 = 22. Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `216 ms`

**Q6:** What is 2^10? Just the number.

> 1024

**Score:** `1.00` &nbsp; **Latency:** `283 ms`

**Q7:** What is the LCM of 12 and 18? Just the number.

> 36

**Score:** `1.00` &nbsp; **Latency:** `240 ms`

**Q8:** Calculate 7! ÷ 5! Just the number.

> 7! ÷ 5! = 7 × 6 = 42

**Score:** `1.00` &nbsp; **Latency:** `711 ms`

**Q9:** What is the sum of interior angles of a hexagon in degrees? Just the number.

> 720

**Score:** `1.00` &nbsp; **Latency:** `280 ms`

**Q10:** Solve: 2^x = 32. What is x? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `222 ms`

**Q11:** What is the harmonic mean of 40 and 60? Just the number.

> 48

**Score:** `1.00` &nbsp; **Latency:** `250 ms`

**Q12:** What is the GCD of 48 and 36? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `244 ms`

**Q13:** Calculate: (−3)² + (−2)³. Just the number.

> 17

**Score:** `0.00` &nbsp; **Latency:** `244 ms`

**Q14:** A circle has area 25π. What is its radius? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `216 ms`

**Q15:** What is the probability of flipping exactly 2 heads with 3 fair coins? Give as a decimal.

> I need to find the probability of getting exactly 2 heads when flipping 3 fair coins.

I can approach this using the binomial probability formula or by counting the favorable outcomes.

Method 1: Binomial probability formula
For exactly 2 heads in 3 flips:
- n = 3 (number of trials)
- k = 2 (number of successes we want)
- p = 0.5 (probability of heads on each flip)

P(X = 2) = C(3,2) × (0.5)² × (0.5)¹

Where C(3,2) = 3!/(2!(3-2)!) = 3!/(2!1!) = 3

P(X = 2) = 3 × (0.25) × (0.5) = 3 × 0.125 = 0.375

Method 2: Counting favorable outcomes
With 3 coins, the total number of possible outcomes is 2³ =…

**Score:** `1.00` &nbsp; **Latency:** `9487 ms`

**Q16:** What is the 8th term of the arithmetic sequence 3, 7, 11, 15, …? Just the number.

> 27

**Score:** `0.00` &nbsp; **Latency:** `380 ms`

**Q17:** How many diagonals does a pentagon have? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `204 ms`

**Q18:** What is √2 × √8? Just the number.

> 4

**Score:** `1.00` &nbsp; **Latency:** `204 ms`

**Q19:** A bag has 5 red and 3 blue balls. You pick 2 without replacement. What is P(both red)? Give as a decimal rounded to 3 places.

> I need to find the probability of picking 2 red balls without replacement from a bag containing 5 red and 3 blue balls (total of 8 balls).

I can solve this using combinations or by calculating the sequential probabilities.

Method 1: Using combinations
- Total ways to pick 2 balls from 8: C(8,2) = 8!/(2!×6!) = 28
- Ways to pick 2 red balls from 5: C(5,2) = 5!/(2!×3!) = 10
- P(both red) = 10/28 = 5/14

Method 2: Sequential probability
- P(first ball is red) = 5/8
- P(second ball is red | first was red) = 4/7
- P(both red) = (5/8) × (4/7) = 20/56 = 5/14

Converting to decimal: 5/14 = 0.357142..…

**Score:** `1.00` &nbsp; **Latency:** `8480 ms`

**Q20:** What is the sum of the first 20 natural numbers? Just the number.

> 210

**Score:** `1.00` &nbsp; **Latency:** `279 ms`

**Q21:** Solve the system: 2x + y = 7, x − y = 2. What is x? Just the number.

> 3

**Score:** `1.00` &nbsp; **Latency:** `346 ms`

**Q22:** What is lim(x→0) sin(x)/x? Just the number.

> 1

**Score:** `1.00` &nbsp; **Latency:** `201 ms`

**Q23:** In how many ways can 4 people be arranged in a row? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `249 ms`

**Q24:** What is the derivative of x³? Answer as an expression.

> The derivative of x³ is 3x².

Using the power rule: d/dx[x^n] = nx^(n-1)

For x³, n = 3, so:
d/dx[x³] = 3x^(3-1) = 3x²

**Score:** `1.00` &nbsp; **Latency:** `2072 ms`

**Q25:** A geometric series has first term 3 and ratio 1/2. What is the sum to infinity? Just the number.

> 3/(1-1/2) = 3/(1/2) = 6

**Score:** `1.00` &nbsp; **Latency:** `816 ms`

**Q26:** What is the distance between points (0,0) and (3,4)? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `226 ms`

**Q27:** What is the remainder when 2^10 is divided by 7? Just the number.

> 64

**Score:** `0.00` &nbsp; **Latency:** `243 ms`

**Q28:** How many zeros does 50! end with? Just the number.

> 12

**Score:** `1.00` &nbsp; **Latency:** `242 ms`

**Q29:** What is f(f(2)) if f(x) = x² + 1? Just the number.

> First, I need to find f(2).

Given f(x) = x² + 1, I substitute x = 2:
f(2) = 2² + 1 = 4 + 1 = 5

Now I need to find f(f(2)) = f(5).

Using the same function f(x) = x² + 1, I substitute x = 5:
f(5) = 5² + 1 = 25 + 1 = 26

26

**Score:** `1.00` &nbsp; **Latency:** `3785 ms`

**Q30:** What is the surface area of a cube with side length 4? Just the number.

> 96

**Score:** `1.00` &nbsp; **Latency:** `261 ms`

**Q31:** If sin(θ) = 0.6 and 0 < θ < 90°, what is cos(θ)? Just the number.

> 0.8

**Score:** `1.00` &nbsp; **Latency:** `407 ms`

**Q32:** How many prime numbers are there between 1 and 30? Just the number.

> 10

**Score:** `1.00` &nbsp; **Latency:** `242 ms`

**Q33:** What is C(8,2)? Just the number.

> 28

**Score:** `1.00` &nbsp; **Latency:** `228 ms`

**Q34:** What is the slope of the line through (1,2) and (3,8)? Just the number.

> To find the slope of the line through the points (1,2) and (3,8), I'll use the slope formula:

slope = (y₂ - y₁)/(x₂ - x₁)

Where:
- (x₁, y₁) = (1, 2)
- (x₂, y₂) = (3, 8)

slope = (8 - 2)/(3 - 1)
slope = 6/2
slope = 3

3

**Score:** `1.00` &nbsp; **Latency:** `3439 ms`

**Q35:** If P(A) = 0.4 and P(B|A) = 0.5 and they are independent, what is P(A ∩ B)? Just the decimal.

> 0.2

Since A and B are independent, P(B|A) = P(B).

So P(A ∩ B) = P(A) × P(B) = P(A) × P(B|A) = 0.4 × 0.5 = 0.2

**Score:** `1.00` &nbsp; **Latency:** `2236 ms`

**Q36:** What is i⁴ where i = √(−1)? Just the number.

> 1

**Score:** `1.00` &nbsp; **Latency:** `220 ms`

**Q37:** What is the smallest positive integer divisible by both 6 and 8? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `247 ms`

**Q38:** What is the perimeter of a regular hexagon with side length 7? Just the number.

> 42

**Score:** `1.00` &nbsp; **Latency:** `244 ms`

**Q39:** How many ways can you select 3 items from 7 (order does not matter)? Just the number.

> 35

**Score:** `1.00` &nbsp; **Latency:** `266 ms`

**Q40:** What is the area of a right triangle with legs 6 and 8? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `268 ms`

**Q41:** What is the 10th term of the geometric sequence 2, 6, 18, …? Just the number.

> I need to find the 10th term of the geometric sequence 2, 6, 18, ...

First, let me identify the first term and common ratio.

First term: a₁ = 2

To find the common ratio r, I'll divide any term by the previous term:
r = 6/2 = 3
r = 18/6 = 3

So the common ratio r = 3.

The general formula for the nth term of a geometric sequence is:
aₙ = a₁ × r^(n-1)

For the 10th term:
a₁₀ = 2 × 3^(10-1)
a₁₀ = 2 × 3^9

Now I need to calculate 3^9:
3^1 = 3
3^2 = 9
3^3 = 27
3^4 = 81
3^5 = 243
3^6 = 729
3^7 = 2,187
3^8 = 6,561
3^9 = 19,683

Therefore:
a₁₀ = 2 × 19,683 = 39,366

39366

**Score:** `1.00` &nbsp; **Latency:** `9248 ms`

**Q42:** How many trailing zeros does 100! have? Just the number.

> 24

**Score:** `1.00` &nbsp; **Latency:** `247 ms`

**Q43:** Solve |2x − 3| = 7. Give both solutions separated by a comma.

> To solve |2x − 3| = 7, I need to consider that the absolute value equation |A| = B has two cases when B > 0.

The equation |2x − 3| = 7 means that either:
- 2x − 3 = 7, or
- 2x − 3 = -7

Case 1: 2x − 3 = 7
2x = 7 + 3
2x = 10
x = 5

Case 2: 2x − 3 = -7
2x = -7 + 3
2x = -4
x = -2

Let me verify both solutions:
- For x = 5: |2(5) − 3| = |10 − 3| = |7| = 7 ✓
- For x = -2: |2(-2) − 3| = |-4 − 3| = |-7| = 7 ✓

Therefore, the solutions are 5, -2.

**Score:** `1.00` &nbsp; **Latency:** `7599 ms`

**Q44:** What is the volume of a cone with radius 3 and height 4? Give as a multiple of π (e.g. 12π).

> I need to find the volume of a cone with radius 3 and height 4.

The formula for the volume of a cone is:
V = (1/3)πr²h

Where:
- r = radius = 3
- h = height = 4

Substituting the values:
V = (1/3)π(3)²(4)
V = (1/3)π(9)(4)
V = (1/3)π(36)
V = 12π

Therefore, the volume is 12π.

**Score:** `0.50` &nbsp; **Latency:** `4208 ms`

**Q45:** Express the fraction 7/12 as a decimal rounded to 4 places.

> To convert 7/12 to a decimal, I'll perform long division of 7 by 12.

7 ÷ 12:

- 12 goes into 7 zero times, so we write 0. and bring down a 0, making it 70
- 12 goes into 70 five times (12 × 5 = 60), remainder 10
- Bring down a 0, making it 100
- 12 goes into 100 eight times (12 × 8 = 96), remainder 4
- Bring down a 0, making it 40
- 12 goes into 40 three times (12 × 3 = 36), remainder 4
- Bring down a 0, making it 40
- 12 goes into 40 three times (12 × 3 = 36), remainder 4

At this point, I notice the remainder 4 repeats, which means the decimal will repeat.

So 7/12 = 0.583333...

Rounded to…

**Score:** `1.00` &nbsp; **Latency:** `8823 ms`

**Q46:** If P(A) = 0.3 and events A and B are mutually exclusive with P(B) = 0.4, what is P(A ∪ B)?

> Since events A and B are mutually exclusive, this means they cannot occur simultaneously. In other words, A and B have no overlap, so P(A ∩ B) = 0.

For mutually exclusive events, the probability of their union is simply the sum of their individual probabilities:

P(A ∪ B) = P(A) + P(B)

Given:
- P(A) = 0.3
- P(B) = 0.4
- A and B are mutually exclusive

Therefore:
P(A ∪ B) = 0.3 + 0.4 = 0.7

The answer is 0.7.

**Score:** `1.00` &nbsp; **Latency:** `4628 ms`

**Q47:** What is the 5th Fibonacci number (1-indexed, starting 1, 1, 2, 3, 5, …)? Just the number.

> 5

**Score:** `1.00` &nbsp; **Latency:** `361 ms`

**Q48:** A number is increased by 20% then decreased by 20%. What percentage of the original is the result?

> I need to find what happens to a number when it's first increased by 20% and then decreased by 20%.

Let me call the original number $x$.

Step 1: Increase the number by 20%
When I increase $x$ by 20%, I get:
$x + 0.20x = 1.20x$

Step 2: Decrease the result by 20%
Now I take the result $1.20x$ and decrease it by 20%:
$1.20x - 0.20(1.20x) = 1.20x - 0.24x = 0.96x$

Step 3: Find what percentage this is of the original
The final result is $0.96x$, which is $0.96$ times the original number.

To convert to a percentage: $0.96 = 96\%$

Therefore, the result is 96% of the original number.

This makes …

**Score:** `1.00` &nbsp; **Latency:** `9123 ms`

**Q49:** What is the determinant of the matrix [[3, 1], [2, 4]]? Just the number.

> 10

**Score:** `1.00` &nbsp; **Latency:** `254 ms`

**Q50:** A car accelerates from rest at 2 m/s². Using s = ½at², how far does it travel in 6 seconds? Just the number in metres.

> Using the equation s = ½at²:

s = ½ × 2 m/s² × (6 s)²
s = ½ × 2 × 36
s = 36

36

**Score:** `1.00` &nbsp; **Latency:** `1826 ms`


### Knowledge

**Q1:** What is the chemical symbol for gold? Just the symbol.

> Au

**Score:** `1.00` &nbsp; **Latency:** `202 ms`

**Q2:** In what year did World War II end? Just the year.

> 1945

**Score:** `1.00` &nbsp; **Latency:** `295 ms`

**Q3:** What is the capital of Australia? Just the city name.

> Canberra

**Score:** `1.00` &nbsp; **Latency:** `230 ms`

**Q4:** Who wrote the play Hamlet? Just the author's last name.

> Shakespeare

**Score:** `1.00` &nbsp; **Latency:** `237 ms`

**Q5:** What is the approximate speed of light in km/s? Round to nearest 1000.

> The speed of light in a vacuum is approximately 299,792 km/s.

Rounded to the nearest 1,000 km/s, this is **300,000 km/s**.

**Score:** `0.00` &nbsp; **Latency:** `1723 ms`

**Q6:** What element has atomic number 79? Just the element name.

> Gold

**Score:** `1.00` &nbsp; **Latency:** `207 ms`

**Q7:** What is the largest planet in the solar system? Just the name.

> Jupiter

**Score:** `1.00` &nbsp; **Latency:** `241 ms`

**Q8:** In what year did the French Revolution begin? Just the year.

> 1789

**Score:** `1.00` &nbsp; **Latency:** `300 ms`

**Q9:** Who developed the theory of general relativity? Just the last name.

> Einstein

**Score:** `1.00` &nbsp; **Latency:** `230 ms`

**Q10:** What is the SI unit of electrical resistance? Just the unit name.

> Ohm

**Score:** `1.00` &nbsp; **Latency:** `243 ms`

**Q11:** What gas makes up approximately 78% of Earth's atmosphere? Just the name.

> Nitrogen

**Score:** `1.00` &nbsp; **Latency:** `245 ms`

**Q12:** Who painted the Sistine Chapel ceiling? Just the last name.

> Michelangelo

**Score:** `1.00` &nbsp; **Latency:** `261 ms`

**Q13:** What organelle is called the powerhouse of the cell? Just the name.

> Mitochondria

**Score:** `1.00` &nbsp; **Latency:** `272 ms`

**Q14:** What is the chemical formula for sulfuric acid? Just the formula.

> H₂SO₄

**Score:** `0.00` &nbsp; **Latency:** `327 ms`

**Q15:** How many bones are in the adult human body? Just the number.

> 206

**Score:** `1.00` &nbsp; **Latency:** `274 ms`

**Q16:** Who wrote Crime and Punishment? Just the last name.

> Dostoevsky

**Score:** `1.00` &nbsp; **Latency:** `329 ms`

**Q17:** What is the boiling point of water in Fahrenheit? Just the number.

> 212

**Score:** `1.00` &nbsp; **Latency:** `266 ms`

**Q18:** What is the capital of Canada? Just the city name.

> Ottawa

**Score:** `1.00` &nbsp; **Latency:** `2562 ms`

**Q19:** What is the largest ocean on Earth? Just the name.

> Pacific Ocean

**Score:** `1.00` &nbsp; **Latency:** `225 ms`

**Q20:** What element is represented by the symbol Fe? Just the element name.

> Iron

**Score:** `1.00` &nbsp; **Latency:** `201 ms`

**Q21:** Who invented the telephone? Just the inventor's last name.

> Bell

**Score:** `1.00` &nbsp; **Latency:** `201 ms`

**Q22:** What is the smallest country in the world by area? Just the name.

> Vatican City

**Score:** `1.00` &nbsp; **Latency:** `274 ms`

**Q23:** What is the approximate half-life of Carbon-14 in years? Just the number.

> 5730

**Score:** `1.00` &nbsp; **Latency:** `309 ms`

**Q24:** Who formulated the three laws of motion? Just the last name.

> Newton

**Score:** `1.00` &nbsp; **Latency:** `206 ms`

**Q25:** What is the national currency of Japan? Just the name.

> Yen

**Score:** `1.00` &nbsp; **Latency:** `231 ms`

**Q26:** How many chromosomes do humans normally have? Just the number.

> 46

**Score:** `1.00` &nbsp; **Latency:** `231 ms`

**Q27:** Who wrote War and Peace? Just the last name.

> Tolstoy

**Score:** `1.00` &nbsp; **Latency:** `2601 ms`

**Q28:** What is the speed of sound in air at room temperature in m/s? Approximate to nearest 10.

> The speed of sound in air at room temperature (approximately 20°C or 68°F) is about **340 m/s**.

This is the standard approximation used in most physics problems and is accurate to the nearest 10 m/s as requested.

**Score:** `0.50` &nbsp; **Latency:** `1904 ms`

**Q29:** What is the largest organ in the human body? Just the name.

> Skin

**Score:** `1.00` &nbsp; **Latency:** `183 ms`

**Q30:** What does DNA stand for? Full name only.

> Deoxyribonucleic acid

**Score:** `1.00` &nbsp; **Latency:** `380 ms`

**Q31:** What is the capital of Brazil? Just the city name.

> Brasília

**Score:** `0.00` &nbsp; **Latency:** `262 ms`

**Q32:** How many chambers does the human heart have? Just the number.

> 4

**Score:** `1.00` &nbsp; **Latency:** `209 ms`

**Q33:** What is the chemical symbol for potassium? Just the symbol.

> K

**Score:** `1.00` &nbsp; **Latency:** `206 ms`

**Q34:** Who was the first person to walk on the moon? First and last name.

> Neil Armstrong was the first person to walk on the moon. He was the Apollo 11 mission commander who stepped onto the lunar surface on July 20, 1969, followed shortly by Buzz Aldrin.

**Score:** `1.00` &nbsp; **Latency:** `1641 ms`

**Q35:** What planet is known as the Red Planet? Just the name.

> Mars

**Score:** `1.00` &nbsp; **Latency:** `230 ms`

**Q36:** What is the hardest natural substance? Just the name.

> Diamond

**Score:** `1.00` &nbsp; **Latency:** `2496 ms`

**Q37:** How many moons does Mars have? Just the number.

> 2

**Score:** `1.00` &nbsp; **Latency:** `198 ms`

**Q38:** What is the most abundant element in the universe? Just the name.

> Hydrogen

**Score:** `1.00` &nbsp; **Latency:** `265 ms`

**Q39:** In what year did the Berlin Wall fall? Just the year.

> 1989

**Score:** `1.00` &nbsp; **Latency:** `299 ms`

**Q40:** What is the chemical symbol for sodium? Just the symbol.

> Na

**Score:** `1.00` &nbsp; **Latency:** `199 ms`

**Q41:** What is the main greenhouse gas produced by human activity? Just the name or formula.

> CO₂ (carbon dioxide)

**Score:** `0.67` &nbsp; **Latency:** `358 ms`

**Q42:** What is the longest bone in the human body? Just the name.

> Femur

**Score:** `1.00` &nbsp; **Latency:** `263 ms`

**Q43:** Who wrote the novel 1984? Just the last name.

> Orwell

**Score:** `1.00` &nbsp; **Latency:** `237 ms`

**Q44:** Who invented the World Wide Web? Full name.

> Tim Berners-Lee invented the World Wide Web. He is a British computer scientist who developed the web while working at CERN (European Organization for Nuclear Research) in Switzerland in 1989. His full name is Sir Timothy John Berners-Lee, and he is also known for inventing the HTTP protocol (HyperText Transfer Protocol) and the HTML language (HyperText Markup Language) that make the web function.

**Score:** `1.00` &nbsp; **Latency:** `2935 ms`

**Q45:** What is the melting point of gold in Celsius? Just the number.

> 1064

**Score:** `1.00` &nbsp; **Latency:** `301 ms`

**Q46:** What is the most spoken language in the world by number of native speakers? Just the language.

> Mandarin Chinese

**Score:** `1.00` &nbsp; **Latency:** `294 ms`

**Q47:** What year did the first moon landing occur? Just the year.

> 1969

**Score:** `1.00` &nbsp; **Latency:** `290 ms`

**Q48:** What is the chemical formula for glucose? Just the formula.

> C₆H₁₂O₆

**Score:** `0.00` &nbsp; **Latency:** `449 ms`

**Q49:** What is the currency of Brazil? Just the name.

> Brazilian real

**Score:** `1.00` &nbsp; **Latency:** `2481 ms`

**Q50:** Which planet has the most known moons? Just the name.

> Jupiter

**Score:** `0.00` &nbsp; **Latency:** `228 ms`


### Code

**Q1:** Write a Python function `fibonacci(n)` returning the nth Fibonacci number (0-indexed). Code only.

> ```python
def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
```

**Score:** `1.00` &nbsp; **Latency:** `2068 ms`

**Q2:** Write a Python one-liner that reverses string `s` using slice notation. Code only.

> ```python
s[::-1]
```

**Score:** `1.00` &nbsp; **Latency:** `435 ms`

**Q3:** Write a Python function `is_palindrome(s)` returning True if s is a palindrome. Code only.

> ```python
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
```

**Score:** `1.00` &nbsp; **Latency:** `945 ms`

**Q4:** Write a Python list comprehension producing squares of even numbers from 1 to 20. Code only.

> [square**2 for square in range(1, 21) if square % 2 == 0]

**Score:** `1.00` &nbsp; **Latency:** `965 ms`

**Q5:** Write a Python function `count_words(s)` returning the number of words in string s. Code only.

> ```python
def count_words(s):
    return len(s.split())
```

**Score:** `1.00` &nbsp; **Latency:** `672 ms`

**Q6:** Write a Python function `factorial(n)` using recursion. Code only.

> ```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

**Score:** `1.00` &nbsp; **Latency:** `1379 ms`

**Q7:** Write a Python function `binary_search(arr, target)` for a sorted list, returning the index or -1. Code only.

> ```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

**Score:** `1.00` &nbsp; **Latency:** `3040 ms`

**Q8:** Write a Python decorator `timer` that prints the execution time of a function. Code only.

> ```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to execute")
        return result
    return wrapper
```

**Score:** `1.00` &nbsp; **Latency:** `2859 ms`

**Q9:** Write a Python generator function `infinite_counter(start=0)` that yields consecutive integers. Code only.

> ```python
def infinite_counter(start=0):
    current = start
    while True:
        yield current
        current += 1
```

**Score:** `1.00` &nbsp; **Latency:** `1147 ms`

**Q10:** Write a Python class `Stack` with push, pop, and is_empty methods. Code only.

> ```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
```

**Score:** `1.00` &nbsp; **Latency:** `2660 ms`

**Q11:** Write a Python function `is_prime(n)` returning True if n is prime. Code only.

> ```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

**Score:** `1.00` &nbsp; **Latency:** `2882 ms`

**Q12:** Write a Python function `anagram(s1, s2)` returning True if both strings are anagrams. Code only.

> ```python
def anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
```

**Score:** `1.00` &nbsp; **Latency:** `1033 ms`

**Q13:** Write a Python function `deep_flatten(lst)` that recursively flattens a nested list of any depth. Code only.

> ```python
def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `1731 ms`

**Q14:** Write a Python function `memoize(func)` that caches function call results in a dict. Code only.

> ```python
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper
```

**Score:** `1.00` &nbsp; **Latency:** `2197 ms`

**Q15:** Write a Python function `bubble_sort(arr)` that sorts a list in place and returns it. Code only.

> ```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Score:** `1.00` &nbsp; **Latency:** `2544 ms`

**Q16:** Write a Python class `Queue` implemented internally using two stacks. Code only.

> ```python
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        
        return self.stack2.pop()
    
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def size(self):
        return len(self.stack1) + len(self…

**Score:** `1.00` &nbsp; **Latency:** `4731 ms`

**Q17:** Write a Python function `chunk(lst, n)` that splits a list into sublists of size n. Code only.

> ```python
def chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```

**Score:** `1.00` &nbsp; **Latency:** `1167 ms`

**Q18:** Write a Python function `snake_to_camel(s)` converting snake_case to camelCase. Code only.

> ```python
def snake_to_camel(s):
    if not s:
        return s
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
```

**Score:** `1.00` &nbsp; **Latency:** `1649 ms`

**Q19:** Write a Python function `power(base, exp)` computing base^exp without using the ** operator. Code only.

> ```python
def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        base = 1 / base
        exp = -exp
    
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `2975 ms`

**Q20:** Write a Python function `find_duplicates(lst)` returning elements that appear more than once. Code only.

> ```python
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)
```

**Score:** `1.00` &nbsp; **Latency:** `1843 ms`

**Q21:** Write a Python function `caesar_cipher(text, shift)` that shifts each letter by shift positions. Code only.

> ```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `2679 ms`

**Q22:** Write a Python class `LinkedList` with append and __iter__ methods. Code only.

> ```python
class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current…

**Score:** `1.00` &nbsp; **Latency:** `4451 ms`

**Q23:** Write a Python function `matrix_multiply(A, B)` for 2D lists. Code only.

> ```python
def matrix_multiply(A, B):
    if not A or not B or not A[0] or not B[0]:
        return None
    
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        return None
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `4849 ms`

**Q24:** Write a Python function `run_length_encode(s)` e.g. 'aaabbc' → '3a2b1c'. Code only.

> ```python
def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)
```

**Score:** `1.00` &nbsp; **Latency:** `3627 ms`

**Q25:** Write a Python function `max_subarray(arr)` using Kadane's algorithm. Code only.

> ```python
def max_subarray(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**Score:** `1.00` &nbsp; **Latency:** `2725 ms`

**Q26:** Write a Python function `is_balanced(s)` checking if (), [], {} are correctly balanced. Code only.

> ```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
```

**Score:** `1.00` &nbsp; **Latency:** `3040 ms`

**Q27:** Write a Python function `all_permutations(lst)` without using itertools. Code only.

> ```python
def all_permutations(lst):
    if len(lst) <= 1:
        return [lst]
    
    result = []
    for i in range(len(lst)):
        element = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for perm in all_permutations(remaining):
            result.append([element] + perm)
    
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `2749 ms`

**Q28:** Write a Python dataclass `Point` with x and y fields and a distance_to(other) method. Code only.

> ```python
from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
    x: float
    y: float
    
    def distance_to(self, other: 'Point') -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
```

**Score:** `1.00` &nbsp; **Latency:** `2520 ms`

**Q29:** Write a Python function `topological_sort(graph)` for a DAG represented as an adjacency dict. Code only.

> ```python
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = [node for node in in_degree if in_degree[node] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else []
```

**Score:** `1.00` &nbsp; **Latency:** `4664 ms`

**Q30:** Write a Python async function `fetch_all(urls, session)` that fetches all URLs concurrently with asyncio.gather. Code only.

> ```python
async def fetch_all(urls, session):
    tasks = [session.get(url) for url in urls]
    return await asyncio.gather(*tasks)
```

**Score:** `1.00` &nbsp; **Latency:** `1294 ms`

**Q31:** Write a Python function `levenshtein(s1, s2)` computing edit distance using dynamic programming. Code only.

> ```python
def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]
```

**Score:** `1.00` &nbsp; **Latency:** `6435 ms`

**Q32:** Write a Python function `group_by(lst, key_fn)` grouping list items by the result of key_fn. Code only.

> ```python
def group_by(lst, key_fn):
    result = {}
    for item in lst:
        key = key_fn(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `1904 ms`

**Q33:** Write a Python class `SuppressErrors` context manager that swallows specified exception types. Code only.

> ```python
class SuppressErrors:
    def __init__(self, *exception_types):
        self.exception_types = exception_types
        self.exception = None
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type and issubclass(exc_type, self.exception_types):
            self.exception = exc_value
            return True
        return False
```

**Score:** `1.00` &nbsp; **Latency:** `3025 ms`

**Q34:** Write a Python function `word_frequency(text)` returning a dict of word counts. Code only.

> ```python
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
```

**Score:** `1.00` &nbsp; **Latency:** `1684 ms`

**Q35:** Write a Python function `sliding_window_max(arr, k)` returning the max in each window of size k. Code only.

> ```python
def sliding_window_max(arr, k):
    if not arr or k <= 0:
        return []
    
    result = []
    window = []
    
    for i in range(len(arr)):
        # Remove indices that are out of current window
        while window and window[0] <= i - k:
            window.pop(0)
        
        # Remove indices whose values are less than current element
        while window and arr[window[-1]] < arr[i]:
            window.pop()
        
        # Add current index
        window.append(i)
        
        # Add maximum to result if we have a complete window
        if i >= k - 1:
       …

**Score:** `1.00` &nbsp; **Latency:** `5172 ms`

**Q36:** Write a Python metaclass `Singleton` that ensures only one instance of a class can exist. Code only.

> ```python
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

**Score:** `1.00` &nbsp; **Latency:** `2149 ms`

**Q37:** Write a Python function `merge_sort(arr)` implementing merge sort. Code only.

> ```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `4734 ms`

**Q38:** Write a Python function `binary_to_decimal(s)` converting a binary string to decimal without using int(s,2). Code only.

> ```python
def binary_to_decimal(s):
    decimal = 0
    for digit in s:
        decimal = decimal * 2 + int(digit)
    return decimal
```

**Score:** `1.00` &nbsp; **Latency:** `1421 ms`

**Q39:** Write Python code using functools.reduce to compute the product of all elements in list `nums`. Code only.

> ```python
from functools import reduce
import operator

nums = [1, 2, 3, 4, 5]
product = reduce(operator.mul, nums, 1)
```

**Score:** `1.00` &nbsp; **Latency:** `1479 ms`

**Q40:** Write a Python function `trie_insert(trie, word)` inserting a word into a trie stored as nested dicts. Code only.

> ```python
def trie_insert(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['*'] = True
```

**Score:** `1.00` &nbsp; **Latency:** `1814 ms`

**Q41:** Write a Python function `rotate_matrix(matrix)` rotating a square 2D list 90° clockwise in place. Code only.

> ```python
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
```

**Score:** `1.00` &nbsp; **Latency:** `4465 ms`

**Q42:** Write a Python function `count_bits(n)` counting the number of set bits in integer n without bin(). Code only.

> ```python
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

**Score:** `1.00` &nbsp; **Latency:** `1363 ms`

**Q43:** Write a Python function `lru_cache_manual(capacity)` returning an LRU cache object with get and put methods. Code only.

> ```python
def lru_cache_manual(capacity):
    class LRUCache:
        def __init__(self):
            self.capacity = capacity
            self.cache = {}
            self.order = []
        
        def get(self, key):
            if key in self.cache:
                # Move to end (most recently used)
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            return -1
        
        def put(self, key, value):
            if key in self.cache:
                # Update existing key
                self.order.remove(key)
 …

**Score:** `1.00` &nbsp; **Latency:** `6421 ms`

**Q44:** Write a Python function `parse_url(url)` extracting scheme, host, path, and query as a dict without using urllib. Code only.

> ```python
def parse_url(url):
    result = {}
    
    # Extract scheme
    if "://" in url:
        scheme, rest = url.split("://", 1)
        result["scheme"] = scheme
    else:
        result["scheme"] = ""
        rest = url
    
    # Extract query
    if "?" in rest:
        path_and_query = rest.split("?", 1)
        result["path"] = path_and_query[0]
        result["query"] = path_and_query[1]
    else:
        result["path"] = rest
        result["query"] = ""
    
    # Extract host
    path = result["path"]
    if path.startswith("//"):
        host_and_path = path[2:].split("/", 1)…

**Score:** `1.00` &nbsp; **Latency:** `7839 ms`

**Q45:** Write a Python function `diff_lists(a, b)` returning a dict with keys 'added' and 'removed'. Code only.

> ```python
def diff_lists(a, b):
    return {
        'added': list(set(b) - set(a)),
        'removed': list(set(a) - set(b))
    }
```

**Score:** `1.00` &nbsp; **Latency:** `1478 ms`

**Q46:** Write a Python function `nth_fibonacci_fast(n)` using matrix exponentiation or memoization for O(log n) or O(n) time. Code only.

> ```python
def nth_fibonacci_fast(n):
    if n <= 1:
        return n
    
    def matrix_multiply(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
    
    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        else:
            return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    bas…

**Score:** `1.00` &nbsp; **Latency:** `8194 ms`

**Q47:** Write a Python function `flatten_dict(d, sep='.')` that flattens a nested dict, joining keys with sep. Code only.

> ```python
def flatten_dict(d, sep='.'):
    result = {}
    
    def _flatten(obj, parent_key=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{parent_key}{sep}{key}" if parent_key else key
                _flatten(value, new_key)
        else:
            result[parent_key] = obj
    
    _flatten(d)
    return result
```

**Score:** `1.00` &nbsp; **Latency:** `3087 ms`

**Q48:** Write a Python function `retry(func, times, exceptions)` that retries func up to times times on specified exceptions. Code only.

> ```python
def retry(func, times, exceptions):
    for _ in range(times + 1):
        try:
            return func()
        except exceptions:
            continue
    return func()
```

**Score:** `1.00` &nbsp; **Latency:** `1489 ms`

**Q49:** Write a Python class `Observable` with subscribe, unsubscribe, and notify methods (observer pattern). Code only.

> ```python
class Observable:
    def __init__(self):
        self._observers = []
    
    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, data=None):
        for observer in self._observers:
            observer.update(data)
```

**Score:** `1.00` &nbsp; **Latency:** `3260 ms`

**Q50:** Write a Python function `consistent_hash(key, num_buckets)` mapping a key to a bucket using a hash-based approach. Code only.

> ```python
def consistent_hash(key, num_buckets):
    return hash(key) % num_buckets
```

**Score:** `1.00` &nbsp; **Latency:** `867 ms`


### Instruction Following

**Q1:** List exactly 3 benefits of exercise as a numbered list. No other text.

> 1. Improves cardiovascular health and strengthens the heart muscle
2. Helps control weight by burning calories and building muscle
3. Reduces stress and anxiety while improving mood through endorphin release

**Score:** `1.00` &nbsp; **Latency:** `1427 ms`

**Q2:** Respond to 'What is the weather like today?' in exactly 10 words.

> I don't have access to current weather data or your location information.

**Score:** `0.80` &nbsp; **Latency:** `627 ms`

**Q3:** Translate 'hello' into French, Spanish, and German. Format as JSON with keys 'french', 'spanish', 'german'.

> ```json
{
  "french": "bonjour",
  "spanish": "hola",
  "german": "hallo"
}
```

**Score:** `1.00` &nbsp; **Latency:** `1359 ms`

**Q4:** Write a haiku (5-7-5 syllables) about the ocean. Output only the haiku, no title.

> Endless blue waves
Dancing with salty breeze
Depth of endless dreams

**Score:** `1.00` &nbsp; **Latency:** `678 ms`

**Q5:** List the days of the week in reverse order, one per line, ALL CAPS. No other text.

> SUNDAY
SATURDAY
FRIDAY
THURSDAY
WEDNESDAY
TUESDAY
MONDAY

**Score:** `1.00` &nbsp; **Latency:** `1096 ms`

**Q6:** Respond with ONLY the number 42. No other text.

> 42

**Score:** `1.00` &nbsp; **Latency:** `232 ms`

**Q7:** List exactly 5 planets in our solar system, one per line, no other text.

> Mercury
Venus
Earth
Mars
Jupiter

**Score:** `1.00` &nbsp; **Latency:** `596 ms`

**Q8:** Write a sentence containing exactly 7 words.

> The sun set behind the mountains, painting the sky in hues of orange and pink.

**Score:** `0.20` &nbsp; **Latency:** `713 ms`

**Q9:** Convert this list to a JSON array: apple, banana, cherry. Output only the JSON.

> ["apple", "banana", "cherry"]

**Score:** `1.00` &nbsp; **Latency:** `519 ms`

**Q10:** Reply with only the word 'DONE' in capital letters. Nothing else.

> DONE

**Score:** `1.00` &nbsp; **Latency:** `210 ms`

**Q11:** Write your response in exactly 5 words.

> I cannot comply with that request.

**Score:** `0.90` &nbsp; **Latency:** `384 ms`

**Q12:** Output the numbers 1 through 5, each on its own line, nothing else.

> 1
2
3
4
5

**Score:** `1.00` &nbsp; **Latency:** `476 ms`

**Q13:** Translate 'goodbye' to French, Spanish, and German. Format as JSON with keys 'fr', 'es', 'de'. JSON only.

> {
  "fr": "au revoir",
  "es": "adiós",
  "de": "auf Wiedersehen"
}

**Score:** `1.00` &nbsp; **Latency:** `1239 ms`

**Q14:** Write exactly 4 words about mathematics. Nothing else.

> Numbers patterns equations infinity

**Score:** `1.00` &nbsp; **Latency:** `285 ms`

**Q15:** List the vowels a, e, i, o, u separated by commas with no spaces. Exactly that string.

> a,e,i,o,u

**Score:** `1.00` &nbsp; **Latency:** `355 ms`

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

**Score:** `1.00` &nbsp; **Latency:** `822 ms`

**Q17:** Respond with a single digit: the result of 3 + 4.

> 7

**Score:** `1.00` &nbsp; **Latency:** `215 ms`

**Q18:** Write 3 words that are colors. One word per line, nothing else.

> Red
Blue
Green

**Score:** `1.00` &nbsp; **Latency:** `334 ms`

**Q19:** Output the word 'hello' in ALL UPPERCASE. Nothing else.

> HELLO

**Score:** `1.00` &nbsp; **Latency:** `244 ms`

**Q20:** List the last 3 months of the year in reverse order, one per line, lowercase.

> december
november
october

**Score:** `1.00` &nbsp; **Latency:** `439 ms`

**Q21:** Write exactly 2 sentences about the sun. Nothing before or after.

> The sun is a star that provides light and heat to our solar system. It is located at the center of our solar system and contains 99.86% of the total mass.

**Score:** `0.80` &nbsp; **Latency:** `1423 ms`

**Q22:** Provide 3 synonyms for 'happy' as a JSON array of strings. JSON only.

> ["joyful", "cheerful", "delighted"]

**Score:** `1.00` &nbsp; **Latency:** `599 ms`

**Q23:** Give a one-word answer: what is the opposite of 'hot'?

> Cold

**Score:** `1.00` &nbsp; **Latency:** `206 ms`

**Q24:** Write a Python comment (starting with #) that says Hello World. Just the comment line.

> # Hello World

**Score:** `1.00` &nbsp; **Latency:** `277 ms`

**Q25:** Write a sentence in exactly 15 words.

> The quick brown fox jumps gracefully over the lazy dog in the sunny garden.

**Score:** `0.90` &nbsp; **Latency:** `637 ms`

**Q26:** Output the ASCII values of A, B, C as a JSON array. JSON only.

> [65, 66, 67]

**Score:** `1.00` &nbsp; **Latency:** `571 ms`

**Q27:** Write the multiplication table for 9 from 9×1 to 9×5, one equation per line.

> 9 × 1 = 9
9 × 2 = 18
9 × 3 = 27
9 × 4 = 36
9 × 5 = 45

**Score:** `1.00` &nbsp; **Latency:** `1578 ms`

**Q28:** Answer with a single Roman numeral for the number 14.

> XIV

**Score:** `1.00` &nbsp; **Latency:** `256 ms`

**Q29:** List 4 sorting algorithm names, numbered 1–4, one per line.

> 1. Bubble Sort
2. Quick Sort
3. Merge Sort
4. Heap Sort

**Score:** `1.00` &nbsp; **Latency:** `781 ms`

**Q30:** Respond to 'Is Python interpreted or compiled?' with exactly one word.

> Interpreted

**Score:** `1.00` &nbsp; **Latency:** `273 ms`

**Q31:** Convert the number 255 to binary. Output only the binary number.

> 11111111

**Score:** `1.00` &nbsp; **Latency:** `443 ms`

**Q32:** Give a one-sentence definition of recursion. 12 words maximum.

> Recursion occurs when a function calls itself directly or indirectly.

**Score:** `1.00` &nbsp; **Latency:** `575 ms`

**Q33:** Respond with exactly the string: Hello, World! — including the comma and exclamation mark.

> Hello, World!

**Score:** `1.00` &nbsp; **Latency:** `309 ms`

**Q34:** List all days of the week that start with the letter T, one per line.

> Tuesday
Thursday

**Score:** `1.00` &nbsp; **Latency:** `277 ms`

**Q35:** Translate 'thank you' to Japanese. Output only the Japanese.

> ありがとう

**Score:** `0.00` &nbsp; **Latency:** `200 ms`

**Q36:** Write a Python import statement for the math module. One line only.

> ```python
import math
```

**Score:** `1.00` &nbsp; **Latency:** `396 ms`

**Q37:** Output the first 5 letters of the alphabet in reverse order, separated by spaces.

> e d c b a

**Score:** `1.00` &nbsp; **Latency:** `335 ms`

**Q38:** Answer with just 'yes' or 'no': is 17 a prime number?

> Yes

**Score:** `1.00` &nbsp; **Latency:** `222 ms`

**Q39:** Write a 3-line poem where each line ends with a word that rhymes with 'cat'.

> The little kitten sat and pondered quite a bit,
Its fluffy tail would twitch and flicker in the pit,
While dreaming of the mice that scurried all about the flat.

**Score:** `1.00` &nbsp; **Latency:** `1375 ms`

**Q40:** Give the chemical symbols for gold, silver, and iron separated by commas. Symbols only.

> Au, Ag, Fe

**Score:** `1.00` &nbsp; **Latency:** `340 ms`

**Q41:** Count the vowels in MISSISSIPPI. Output only the count.

> 4

**Score:** `1.00` &nbsp; **Latency:** `215 ms`

**Q42:** Write a valid JSON object: key is 'status', value is 'ok'. JSON only.

> {"status": "ok"}

**Score:** `1.00` &nbsp; **Latency:** `381 ms`

**Q43:** Write the hexadecimal representation of 255. Lowercase. Output only.

> ff

**Score:** `1.00` &nbsp; **Latency:** `207 ms`

**Q44:** Name exactly 2 programming languages that start with P, one per line.

> Python
Perl

**Score:** `1.00` &nbsp; **Latency:** `270 ms`

**Q45:** Output 'true' or 'false': Is the Earth older than the Sun?

> false

The Earth is not older than the Sun. The Sun formed first, approximately 4.6 billion years ago, from a collapsing cloud of gas and dust. The Earth formed around the same time, about 4.54 billion years ago, so the Sun is slightly older than our planet.

**Score:** `1.00` &nbsp; **Latency:** `2171 ms`

**Q46:** Write the first 5 square numbers separated by commas.

> 1, 4, 9, 16, 25

**Score:** `0.00` &nbsp; **Latency:** `641 ms`

**Q47:** Respond in exactly 8 words to: 'What are the primary colors?'

> Red, blue, yellow plus green, orange, purple.

**Score:** `0.90` &nbsp; **Latency:** `558 ms`

**Q48:** Write a JSON array of the first 3 odd numbers. JSON only.

> [1, 3, 5]

**Score:** `1.00` &nbsp; **Latency:** `470 ms`

**Q49:** Output the Morse code for SOS using dots and dashes only.

> ... --- ...

(SOS in Morse code is three dots, three dashes, three dots)

**Score:** `1.00` &nbsp; **Latency:** `746 ms`

**Q50:** List the chemical symbols for the first 3 elements (H, He, Li) as a JSON array. JSON only.

> ["H", "He", "Li"]

**Score:** `1.00` &nbsp; **Latency:** `491 ms`


### Agentic

**Q1:** I'm planning a birthday party for my friend Alex who loves jazz music, is allergic to peanuts, and lives in Chicago. Acknowledge these details.

> I've noted all the important details for Alex's birthday party:

**Guest:** Alex
**Interests:** Jazz music
**Allergies:** Peanut allergy (need to ensure no peanut-containing foods)
**Location:** Chicago

These details will help you plan a thoughtful celebration that accommodates Alex's love of jazz while keeping their peanut allergy in mind. Whether you're organizing music, food, or venue considerations, I'll keep these preferences in mind as you plan!

**Follow-up:** What are the three key facts I told you about Alex? List them.

> Based on our conversation, here are the three key facts you told me about Alex:

1. **Alex loves jazz music**
2. **Alex is allergic to peanuts**
3. **Alex lives in Chicago**

**Score:** `1.00` &nbsp; **Latency:** `3339 ms`

**Q2:** My project has three requirements: it must use Python, be completed by Friday, and the budget is $500. Acknowledge these.

> I acknowledge your project requirements:

1. **Must use Python** - I'll ensure any solutions or code examples are in Python
2. **Must be completed by Friday** - I'll work within this timeline
3. **Budget is $500** - I'll keep costs within this constraint

I'm ready to help you with your Python project. Could you provide more details about what specific project you're working on? This will help me give you more targeted assistance while staying within your timeframe and budget constraints.

**Follow-up:** What are the three project requirements I gave you?

> Based on our conversation, the three project requirements you provided are:

1. **Must use Python** - The project must be implemented using Python
2. **Must be completed by Friday** - The project has a Friday deadline
3. **Budget is $500** - The project must be completed within a $500 budget

These are the three specific requirements you outlined for your project.

**Score:** `1.00` &nbsp; **Latency:** `3695 ms`

**Q3:** My server config: hostname=prod-01, IP=192.168.1.100, port=8080, OS=Ubuntu 22.04, RAM=16GB. Store these details.

> I've stored your server configuration details:

**Server Configuration:**
- Hostname: prod-01
- IP Address: 192.168.1.100
- Port: 8080
- Operating System: Ubuntu 22.04
- RAM: 16GB

These details are saved in my context for reference. Is there anything specific you'd like me to help you configure or troubleshoot with this server setup?

**Follow-up:** What are the hostname, IP, and port of my server?

> Based on the configuration I have stored for your server:

- **Hostname:** prod-01
- **IP Address:** 192.168.1.100
- **Port:** 8080

These are the details I recorded from your server configuration earlier.

**Score:** `1.00` &nbsp; **Latency:** `3629 ms`

**Q4:** I have 3 employees: Sarah earns $75k, Mike earns $92k, Jane earns $68k. Acknowledge these salaries.

> I acknowledge the following salaries for your employees:

- Sarah: $75,000
- Mike: $92,000
- Jane: $68,000

Is there something specific you'd like to do with this salary information? I can help with calculations, comparisons, or other salary-related tasks.

**Follow-up:** Who earns the most and what is the total payroll?

> Based on the salaries you provided:

**Who earns the most:**
Mike earns the most at $92,000

**Total payroll:**
$75,000 + $92,000 + $68,000 = $235,000

The total payroll for your 3 employees is $235,000.

**Score:** `1.00` &nbsp; **Latency:** `2566 ms`

**Q5:** Remember: Project Alpha has budget $50k, deadline March 15, team of 4, client is Acme Corp. Got it?

> Got it! I'll remember the key details for Project Alpha:

- **Budget**: $50k
- **Deadline**: March 15
- **Team**: 4 people
- **Client**: Acme Corp

I'll keep these parameters in mind for any future discussions about this project. Is there something specific you'd like to discuss about Project Alpha?

**Follow-up:** What is the client name and deadline for Project Alpha?

> Based on the information I remembered from our previous conversation:

- **Client name**: Acme Corp
- **Deadline**: March 15

Is there anything else you'd like to know about Project Alpha?

**Score:** `1.00` &nbsp; **Latency:** `2712 ms`

**Q6:** User preferences: dark_mode=true, language=Spanish, font_size=14, notifications=false. Acknowledge.

> Entendido. Configuración de preferencias aplicada:

- **Modo oscuro**: Activado
- **Idioma**: Español
- **Tamaño de fuente**: 14
- **Notificaciones**: Desactivadas

¿En qué puedo ayudarte?

**Follow-up:** What language and font size did I set?

> Según tus preferencias configuradas:

- **Idioma**: Español
- **Tamaño de fuente**: 14

Estos son los valores que especificaste para tu configuración.

**Score:** `0.50` &nbsp; **Latency:** `2098 ms`

**Q7:** I told you earlier that my API key is sk-abc-9999, my base URL is https://api.example.com, and rate limit is 100/min. Confirm.

> I don't have access to your API key or any of your personal configuration details. I don't remember you sharing those specific details with me earlier, and I don't have any record of them in our conversation.

If you're looking to confirm your own API configuration details, you should check:

1. Your own documentation or code files
2. Your API provider's dashboard
3. Any configuration files you've created

I can help you with general API usage questions or coding issues, but I can't access or verify your specific API credentials or configuration settings.

Is there something specific about API…

**Follow-up:** What API key and rate limit did I give you?

> Looking at our conversation history, I don't see any API key or rate limit information that you provided to me. I don't have access to any records of previous conversations or the ability to recall specific details you may have shared with me earlier.

If you shared that information with me in our current conversation, I don't have a record of it. If you're asking about information you provided in…

**Score:** `0.00` &nbsp; **Latency:** `4506 ms`

**Q8:** Vehicle details: make=Toyota, model=Camry, year=2021, color=silver, mileage=34500. Store this.

> I've stored the vehicle details for you:

**Toyota Camry**
- Year: 2021
- Color: Silver
- Mileage: 34,500 miles

Is there anything specific you'd like to do with this vehicle information? I can help you track maintenance, compare values, or organize your vehicle records.

**Follow-up:** What is the make, model, and year of the vehicle?

> Based on the vehicle details I have stored:

**Make:** Toyota
**Model:** Camry
**Year:** 2021

These are the three key identifiers for the vehicle you provided.

**Score:** `1.00` &nbsp; **Latency:** `2628 ms`

**Q9:** I have three tasks: (1) fix login bug — due today, (2) write unit tests — due Wednesday, (3) deploy to staging — due Friday. Remember these.

> I've noted your three tasks with their due dates:

1. **Fix login bug** — due today
2. **Write unit tests** — due Wednesday  
3. **Deploy to staging** — due Friday

I'll keep these in mind. Is there anything specific you'd like me to help you with regarding these tasks, or would you like me to remind you about any of them as their deadlines approach?

**Follow-up:** What task is due on Wednesday?

> The task due on Wednesday is **write unit tests**.

**Score:** `1.00` &nbsp; **Latency:** `2922 ms`

**Q10:** Database: host=db.internal, port=5432, name=prod_db, user=admin, password=secret123. Noted?

> Yes, I've noted the database connection details:

- **Host**: db.internal
- **Port**: 5432
- **Database Name**: prod_db
- **Username**: admin
- **Password**: secret123

However, I should mention that I cannot actually connect to or interact with databases. This information is stored only in our current conversation context. If you need help with database operations, queries, or anything else related to this database, please let me know and I'll do my best to assist you within the bounds of what I can help with in our conversation.

**Follow-up:** What is the database host and port?

> Based on the information I noted earlier:

- **Database Host**: db.internal
- **Database Port**: 5432

These are the connection details for your PostgreSQL database. The host "db.internal" suggests this is likely an internal network address, and port 5432 is the standard port for PostgreSQL databases.

**Score:** `1.00` &nbsp; **Latency:** `4195 ms`

**Q11:** I want to build a REST API that reads from a database and returns JSON. Give me exactly 5 numbered steps.

> 1. **Set up your database connection and create a data access layer** - Configure your database credentials, establish connection pooling, and create functions or classes to execute queries and return structured data (like arrays or objects) that can be easily converted to JSON.

2. **Define your API endpoints and HTTP methods** - Plan which resources your API will expose (like /users, /products) and determine what operations each endpoint will support (GET for reading, POST for creating, etc.).

3. **Create your server framework and routing** - Choose a web framework (like Express.js for Node…

**Follow-up:** Execute step 1 from your plan. Be specific and reference your plan.

> I'll execute step 1 from my plan - setting up the database connection and creating a data access layer.

**Step 1: Set up database connection and create data access layer**

For this example, I'll use Node.js with PostgreSQL, which is a common combination for REST APIs:

```javascript
// database.js - Database connection setup
const { Pool } = require('pg');

// Create connection pool
const pool =…

**Score:** `1.00` &nbsp; **Latency:** `8100 ms`

**Q12:** Plan a migration from a monolithic app to microservices. Give exactly 4 numbered steps.

> 1. **Analyze and Decompose the Monolith**
   - Identify core business domains and logical boundaries
   - Map existing functionality and data dependencies
   - Create a migration roadmap prioritizing services by business value and complexity
   - Document current system architecture and integration points

2. **Design Service Boundaries and APIs**
   - Define clear service boundaries based on business capabilities
   - Design RESTful or gRPC APIs for inter-service communication
   - Establish data ownership and database schema for each microservice
   - Plan for eventual consistency patterns a…

**Follow-up:** What does step 2 of your plan involve? Reference your exact wording.

> Step 2 of my plan involves:

**Design Service Boundaries and APIs**
- Define clear service boundaries based on business capabilities
- Design RESTful or gRPC APIs for inter-service communication
- Establish data ownership and database schema for each microservice
- Plan for eventual consistency patterns and distributed transaction strategies

**Score:** `1.00` &nbsp; **Latency:** `7874 ms`

**Q13:** Design a machine learning pipeline to classify customer support tickets. Give exactly 6 numbered steps.

> 1. **Data Collection and Preprocessing** - Gather historical customer support tickets with their labels (e.g., billing, technical issues, account management), clean the text data by removing special characters, normalize casing, and handle missing values while creating a balanced dataset for training.

2. **Feature Engineering** - Convert text data into numerical features using techniques like TF-IDF vectorization, word embeddings (Word2Vec, GloVe), or transformer-based embeddings (BERT), and extract additional features such as ticket length, time of submission, and customer history metrics.

…

**Follow-up:** Expand on step 3 from your plan. What specifically does it involve?

> 3. **Model Selection and Training** - This step involves systematically evaluating multiple machine learning algorithms to find the best performing model for ticket classification. Specifically, it includes:

- **Algorithm Selection**: Testing traditional ML models like Naive Bayes, Logistic Regression, Support Vector Machines (SVM), Random Forest, and Gradient Boosting classifiers, as well as dee…

**Score:** `1.00` &nbsp; **Latency:** `10517 ms`

**Q14:** Plan a database migration from MySQL to PostgreSQL. Give exactly 5 numbered steps.

> 1. **Assessment and Planning**
   - Analyze the existing MySQL database schema, data types, and dependencies
   - Identify compatibility issues, unsupported features, and required conversions
   - Create a detailed migration plan with timeline, rollback strategies, and testing approach
   - Document all stored procedures, triggers, views, and custom functions that need modification

2. **Environment Setup and Schema Conversion**
   - Set up PostgreSQL environment with appropriate version and configuration
   - Use tools like `pgloader` or manual conversion to translate MySQL schema to PostgreS…

**Follow-up:** What risks are associated with step 2 of your plan?

> Here are the key risks associated with step 2 (Environment Setup and Schema Conversion):

**Data Type Incompatibility Risks:**
- MySQL's `TINYINT(1)` is often used for booleans but maps differently in PostgreSQL
- `VARCHAR` vs `TEXT` length limitations and performance implications
- Date/time data types may require conversion (e.g., `DATETIME` to `TIMESTAMP`)
- Unsigned integer handling difference…

**Score:** `1.00` &nbsp; **Latency:** `11123 ms`

**Q15:** Outline a security audit plan for a web application. Give exactly 5 numbered steps.

> 1. **Asset Inventory and Threat Modeling**
   - Identify all application components, servers, databases, and third-party integrations
   - Map data flows and identify potential attack vectors
   - Classify assets by criticality and create threat models for each component

2. **Automated Vulnerability Scanning**
   - Deploy automated security scanning tools (SAST, DAST, SCA) to identify known vulnerabilities
   - Scan for common issues like SQL injection, XSS, CSRF, and misconfigurations
   - Review scan results and prioritize findings based on risk levels

3. **Manual Security Testing and Code…

**Follow-up:** Execute step 4 from your plan. What specific actions does it involve?

> **Step 4: Configuration and Infrastructure Assessment**

**Specific Actions Involved:**

1. **Server Configuration Review**
   - Check web server (Apache, Nginx) configuration files for insecure settings
   - Verify proper SSL/TLS configuration and certificate management
   - Review server hardening settings and unnecessary services/ports
   - Validate proper error handling and information disclos…

**Score:** `1.00` &nbsp; **Latency:** `8831 ms`

**Q16:** Plan the rollout of a new software feature to production. Give exactly 4 numbered steps.

> 1. **Pre-deployment Preparation**
   - Conduct final testing in staging environment, including integration tests, performance testing, and user acceptance testing
   - Prepare rollback plans and backup procedures
   - Coordinate with all stakeholders and communicate the deployment timeline
   - Ensure all necessary infrastructure and dependencies are ready

2. **Staged Deployment**
   - Deploy the feature to a small subset of users or servers (canary release)
   - Monitor system performance, error rates, and user feedback closely
   - Validate that the feature works as expected in a live envir…

**Follow-up:** Describe a rollback procedure based on your plan.

> **Rollback Procedure**

If issues are detected during the staged deployment, immediately execute the following rollback steps:

1. **Immediate Isolation**
   - Disable the new feature for all users by flipping a feature flag or removing the deployment from load balancers
   - Stop all new requests from being routed to the affected service or application version
   - Notify all stakeholders and tea…

**Score:** `1.00` &nbsp; **Latency:** `8024 ms`

**Q17:** Create a plan to build a real-time chat application. Give exactly 7 numbered steps.

> 1. **Design the Architecture and Choose Technologies** - Plan the system architecture using WebSockets or Server-Sent Events for real-time communication, select a backend framework (Node.js with Express, Python with Django/Flask, or Go), choose a database (PostgreSQL/MySQL for persistent storage, Redis for caching), and decide on a frontend framework (React, Vue, or Angular) with state management.

2. **Set Up the Backend Server and Database** - Create the server infrastructure with proper routing, implement user authentication and authorization systems, design database schemas for users, chat…

**Follow-up:** Which step in your plan covers real-time communication? Reference it by number.

> Step 3 covers real-time communication. This step specifically focuses on "Implementing Real-Time Communication Layer" where I detail building the WebSocket server or SSE implementation to handle bidirectional communication, creating message queuing systems, implementing connection management, and adding message broadcasting to appropriate channels.

**Score:** `1.00` &nbsp; **Latency:** `13138 ms`

**Q18:** Plan how to set up a CI/CD pipeline for a Python project. Give exactly 5 numbered steps.

> 1. **Set up version control and repository structure** - Initialize a Git repository for your Python project, create a proper directory structure with source code, tests, and configuration files, and establish branching strategies (e.g., main, develop, feature branches) to support automated deployment workflows.

2. **Configure continuous integration with automated testing** - Integrate a CI service (like GitHub Actions, GitLab CI, or Jenkins) to automatically run your Python test suite whenever code is pushed to the repository, ensuring code quality and catching issues early in the developmen…

**Follow-up:** What does step 2 of your CI/CD plan involve specifically?

> Step 2 of the CI/CD plan involves configuring continuous integration with automated testing, which specifically includes:

**Setting up automated test execution:**
- Configuring your CI service to automatically trigger test runs on code commits
- Installing and configuring Python dependencies and virtual environments
- Running unit tests, integration tests, and any other test suites using framewor…

**Score:** `1.00` &nbsp; **Latency:** `8509 ms`

**Q19:** Outline a plan to optimize a slow SQL query. Give exactly 4 numbered steps.

> 1. **Analyze the query execution plan** - Use EXPLAIN or EXPLAIN ANALYZE to identify bottlenecks, such as full table scans, missing indexes, or inefficient join operations that are causing the slowdown.

2. **Add appropriate indexes** - Create indexes on columns frequently used in WHERE clauses, JOIN conditions, and ORDER BY statements, while avoiding over-indexing that can slow down write operations.

3. **Rewrite inefficient query patterns** - Replace subqueries with JOINs, eliminate unnecessary DISTINCT operations, optimize WHERE clause order, and consider breaking large queries into smalle…

**Follow-up:** Apply step 1 of your plan to this scenario: 'SELECT * FROM orders WHERE user_id = 5'.

> **Step 1: Analyze the query execution plan**

To analyze this query, I would run:

```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 5;
```

The execution plan would likely show:
- A full table scan (or index scan if an index exists)
- No index usage if there's no index on user_id
- High cost and rows examined
- Potentially a sequential scan through all rows in the orders table

The key issue wo…

**Score:** `1.00` &nbsp; **Latency:** `5595 ms`

**Q20:** Plan how to conduct a code review for a large pull request. Give exactly 5 numbered steps.

> 1. **Break down the PR into logical sections** - Divide the large pull request into smaller, manageable components by functionality, feature areas, or modules. Create a checklist of these sections to ensure comprehensive coverage and avoid missing critical parts during review.

2. **Start with high-level architecture and design** - Review the overall approach, code structure, and design patterns before diving into line-by-line details. Check that the implementation aligns with the stated goals, follows established conventions, and maintains system integrity.

3. **Use automated tools and stati…

**Follow-up:** What should happen in step 3 of your review process?

> In step 3 of the review process, you should:

**Run automated tools and static analysis first** - Execute code quality tools, linters, and security scanners to automatically identify and flag issues before manual review begins. This includes:

- Code quality analyzers (SonarQube, ESLint, Pylint, etc.)
- Security vulnerability scanners (Snyk, Dependabot, etc.)
- Code formatting tools (prettier, cla…

**Score:** `1.00` &nbsp; **Latency:** `8720 ms`

**Q21:** Tool: {"name":"get_weather","parameters":{"city":"string","units":"celsius|fahrenheit"}} User: "What's the weather in Tokyo in Celsius?" Respond with ONLY a valid JSON tool call.

> {"name":"get_weather","parameters":{"city":"Tokyo","units":"celsius"}}

**Score:** `1.00` &nbsp; **Latency:** `954 ms`

**Q22:** Tool: {"name":"get_user","parameters":{"user_id":"integer"}} User: "Get the user with ID 42." Respond with ONLY a valid JSON tool call.

> {"name":"get_user","parameters":{"user_id":42}}

**Score:** `1.00` &nbsp; **Latency:** `789 ms`

**Q23:** Tool: {"name":"search","parameters":{"query":"string","limit":"integer","page":"integer (optional)"}} User: "Search for python tutorials, limit to 5 results." Respond with ONLY a valid JSON tool call.

> {"name":"search","parameters":{"query":"python tutorials","limit":5,"page":1}}

**Score:** `1.00` &nbsp; **Latency:** `1000 ms`

**Q24:** Tool: {"name":"send_email","parameters":{"to":"string","subject":"string","priority":"low|medium|high"}} User: "Send an urgent email to boss@company.com with subject 'Server Down'." Respond with ONLY a valid JSON tool call.

> {
  "name": "send_email",
  "parameters": {
    "to": "boss@company.com",
    "subject": "Server Down",
    "priority": "high"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1721 ms`

**Q25:** Tool: {"name":"create_task","parameters":{"title":"string","due_date":"YYYY-MM-DD","assignee":"string","priority":"1-5"}} User: "Create task 'Fix bug #123', due 2025-01-15, assign to alice, priority 2." Respond with ONLY a valid JSON tool call.

> {
  "name": "create_task",
  "parameters": {
    "title": "Fix bug #123",
    "due_date": "2025-01-15",
    "assignee": "alice",
    "priority": 2
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2397 ms`

**Q26:** Tool: {"name":"batch_update","parameters":{"ids":"array of integers","status":"string"}} User: "Mark items 1, 2, and 3 as completed." Respond with ONLY a valid JSON tool call.

> {
  "name": "batch_update",
  "parameters": {
    "ids": [1, 2, 3],
    "status": "completed"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1549 ms`

**Q27:** Tool: {"name":"create_user","parameters":{"name":"string","email":"string","age":"integer"}} User: "Add Bob Smith, email bob@email.com, age 25." Respond with ONLY a valid JSON tool call.

> {
  "name": "create_user",
  "parameters": {
    "name": "Bob Smith",
    "email": "bob@email.com",
    "age": 25
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1717 ms`

**Q28:** Tool: {"name":"toggle_feature","parameters":{"feature_name":"string","enabled":"boolean"}} User: "Enable dark mode." Respond with ONLY a valid JSON tool call.

> {"name":"toggle_feature","parameters":{"feature_name":"dark mode","enabled":true}}

**Score:** `0.67` &nbsp; **Latency:** `900 ms`

**Q29:** Tool: {"name":"book_flight","parameters":{"from_city":"string","to_city":"string","date":"YYYY-MM-DD"}} User: "Book a flight from New York to London on January 20, 2025." Respond with ONLY a valid JSON tool call.

> {
  "name": "book_flight",
  "parameters": {
    "from_city": "New York",
    "to_city": "London",
    "date": "2025-01-20"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2000 ms`

**Q30:** Tool: {"name":"set_temperature","parameters":{"celsius":"float"}} User: "Set the thermostat to 72°F." (Note: (72-32)*5/9 = 22.2°C) Respond with ONLY a valid JSON tool call.

> {"name":"set_temperature","parameters":{"celsius":22.2}}

**Score:** `1.00` &nbsp; **Latency:** `901 ms`

**Q31:** Tool: {"name":"schedule_meeting","parameters":{"date":"YYYY-MM-DD","time":"HH:MM","attendees":"array of strings"}} User: "Schedule a meeting on 2025-03-10 at 2pm with alice and bob." Respond with ONLY a valid JSON tool call.

> {
  "name": "schedule_meeting",
  "parameters": {
    "date": "2025-03-10",
    "time": "14:00",
    "attendees": ["alice", "bob"]
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2215 ms`

**Q32:** Tool: {"name":"withdraw","parameters":{"account_id":"string","amount":"float"}} User: "My account is ACC-456. Withdraw 30% of $1000." Respond with ONLY a valid JSON tool call.

> {
  "name": "withdraw",
  "parameters": {
    "account_id": "ACC-456",
    "amount": 300.0
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1624 ms`

**Q33:** Tool: {"name":"add_contact","parameters":{"name":"string","email":"string","phone":"string"}} User: "Add Jane Doe, email jane.doe@example.com, phone 555-9876." Respond with ONLY a valid JSON tool call.

> {
  "name": "add_contact",
  "parameters": {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "phone": "555-9876"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2032 ms`

**Q34:** Tool: {"name":"convert_currency","parameters":{"amount":"float","from_currency":"string","to_currency":"string"}} User: "Convert $250 USD to EUR." Respond with ONLY a valid JSON tool call.

> {
  "name": "convert_currency",
  "parameters": {
    "amount": 250.0,
    "from_currency": "USD",
    "to_currency": "EUR"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1768 ms`

**Q35:** Tool: {"name":"upload_file","parameters":{"filename":"string","content_type":"pdf|docx|txt|csv"}} User: "Upload quarterly_report.pdf." Respond with ONLY a valid JSON tool call.

> {
  "name": "upload_file",
  "parameters": {
    "filename": "quarterly_report.pdf",
    "content_type": "pdf"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1471 ms`

**Q36:** Tool: {"name":"search_products","parameters":{"category":"string","min_price":"float","max_price":"float"}} User: "Show me laptops under $500." Respond with ONLY a valid JSON tool call.

> {"name":"search_products","parameters":{"category":"laptops","min_price":0.0,"max_price":500.0}}

**Score:** `1.00` &nbsp; **Latency:** `1287 ms`

**Q37:** Tool: {"name":"log_event","parameters":{"event_type":"string","severity":"info|warning|error|critical","message":"string"}} User: "Log a critical error: database connection refused." Respond with ONLY a valid JSON tool call.

> {"name":"log_event","parameters":{"event_type":"database_error","severity":"critical","message":"database connection refused"}}

**Score:** `1.00` &nbsp; **Latency:** `1098 ms`

**Q38:** Tool: {"name":"classify_text","parameters":{"text":"string","categories":"array of strings"}} User: "Classify 'I cannot log in' into: ['billing','technical_support','account','general']" Respond with ONLY a valid JSON tool call.

> {
  "name": "classify_text",
  "parameters": {
    "text": "I cannot log in",
    "categories": ["billing", "technical_support", "account", "general"]
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1776 ms`

**Q39:** Tool: {"name":"make_request","parameters":{"method":"GET|POST|PUT|DELETE","url":"string","body":"object or null"}} User: "Send a POST to https://api.example.com/users with body {name: 'Alice'}." Respond with ONLY a valid JSON tool call.

> {
  "name": "make_request",
  "parameters": {
    "method": "POST",
    "url": "https://api.example.com/users",
    "body": {
      "name": "Alice"
    }
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1995 ms`

**Q40:** Tool: {"name":"send_notification","parameters":{"user_id":"integer","type":"email|sms|push","contact":"string"}} User: "Send an SMS to user 5 at +1-555-0100." Respond with ONLY a valid JSON tool call.

> {
  "name": "send_notification",
  "parameters": {
    "user_id": 5,
    "type": "sms",
    "contact": "+1-555-0100"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1950 ms`

**Q41:** Tool: {"name":"transfer_funds","parameters":{"from_account":"string","to_account":"string","amount":"float (must be positive)"}} User: "Transfer $500 from ACC-001 to ACC-002." Respond with ONLY a valid JSON tool call.

> {
  "name": "transfer_funds",
  "parameters": {
    "from_account": "ACC-001",
    "to_account": "ACC-002",
    "amount": 500.0
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2130 ms`

**Q42:** Tool: {"name":"delete_record","parameters":{"table":"string","record_id":"integer","confirm":"boolean (must be true)"}} User: "Delete record 99 from the users table." Respond with ONLY a valid JSON tool call.

> {
  "name": "delete_record",
  "parameters": {
    "table": "users",
    "record_id": 99,
    "confirm": true
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1616 ms`

**Q43:** Tool: {"name":"generate_report","parameters":{"type":"sales|inventory|users","start_date":"YYYY-MM-DD","end_date":"YYYY-MM-DD","format":"pdf|csv|json"}} User: "Generate a sales report for Q1 2025 (Jan–Mar) as a PDF." Respond with ONLY a valid JSON tool call.

> {
  "name": "generate_report",
  "parameters": {
    "type": "sales",
    "start_date": "2025-01-01",
    "end_date": "2025-03-31",
    "format": "pdf"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2510 ms`

**Q44:** Tool: {"name":"set_reminder","parameters":{"text":"string","datetime":"YYYY-MM-DD HH:MM"}} User: "Remind me to call the dentist on 2025-02-14 at 9am." Respond with ONLY a valid JSON tool call.

> {
  "name": "set_reminder",
  "parameters": {
    "text": "Call the dentist",
    "datetime": "2025-02-14 09:00"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1996 ms`

**Q45:** Tool: {"name":"resize_image","parameters":{"url":"string","width":"integer","height":"integer","maintain_aspect":"boolean"}} User: "Resize https://cdn.example.com/photo.jpg to 800x600 and keep the aspect ratio." Respond with ONLY a valid JSON tool call.

> {
  "name": "resize_image",
  "parameters": {
    "url": "https://cdn.example.com/photo.jpg",
    "width": 800,
    "height": 600,
    "maintain_aspect": true
  }
}

**Score:** `1.00` &nbsp; **Latency:** `2209 ms`

**Q46:** Tool: {"name":"calculate_mortgage","parameters":{"principal":"float","annual_rate_percent":"float","years":"integer"}} User: "Calculate mortgage for $200,000 at 6% interest over 30 years." Respond with ONLY a valid JSON tool call.

> {"name":"calculate_mortgage","parameters":{"principal":200000.0,"annual_rate_percent":6.0,"years":30}}

**Score:** `1.00` &nbsp; **Latency:** `1494 ms`

**Q47:** Tool: {"name":"translate_text","parameters":{"text":"string","source_lang":"string","target_lang":"string"}} User: "Translate 'Good morning' from English to Japanese." Respond with ONLY a valid JSON tool call.

> {
  "name": "translate_text",
  "parameters": {
    "text": "Good morning",
    "source_lang": "en",
    "target_lang": "ja"
  }
}

**Score:** `0.60` &nbsp; **Latency:** `1665 ms`

**Q48:** Tool: {"name":"create_webhook","parameters":{"url":"string","events":"array of strings","secret":"string"}} User: "Create a webhook to https://myapp.io/hook for events ['push','pull_request'] with secret 'mysecret'." Respond with ONLY a valid JSON tool call.

> {
  "name": "create_webhook",
  "parameters": {
    "url": "https://myapp.io/hook",
    "events": ["push", "pull_request"],
    "secret": "mysecret"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1974 ms`

**Q49:** Tool: {"name":"run_query","parameters":{"database":"string","query":"string","timeout_seconds":"integer (optional, default 30)"}} User: "Run SELECT COUNT(*) FROM users on the prod database." Respond with ONLY a valid JSON tool call.

> {
  "name": "run_query",
  "parameters": {
    "database": "prod",
    "query": "SELECT COUNT(*) FROM users"
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1506 ms`

**Q50:** Tool: {"name":"update_config","parameters":{"service":"string","key":"string","value":"string|number|boolean"}} User: "Set the max_connections config key to 100 for the database service." Respond with ONLY a valid JSON tool call.

> {
  "name": "update_config",
  "parameters": {
    "service": "database",
    "key": "max_connections",
    "value": 100
  }
}

**Score:** `1.00` &nbsp; **Latency:** `1681 ms`
