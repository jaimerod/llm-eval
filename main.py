#!/usr/bin/env python3
"""Automated LLM evaluation script using Ollama.

Usage:
    python main.py --model llama3.2
    python main.py --model mistral --output-dir results/
"""

import argparse
import ast
import json
import re
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import ollama
from tqdm import tqdm


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Question:
    category: str
    prompt: str
    expected: str
    score_fn: str
    follow_up: Optional[str] = None
    follow_up_expected: Optional[str] = None


@dataclass
class QuestionResult:
    question: Question
    response: str
    score: float
    latency_ms: float
    follow_up_response: Optional[str] = None


# ---------------------------------------------------------------------------
# Benchmark questions — 6 categories × 50 questions = 300 total
# ---------------------------------------------------------------------------

QUESTIONS: list[Question] = [
    # ── Reasoning (50) ─────────────────────────────────────────────────────
    Question(category="Reasoning", prompt="All cats are mammals. Some mammals are pets. Garfield is a cat. Is Garfield a mammal? Answer Yes or No.", expected="yes", score_fn="keyword"),
    # ── Reasoning continued ────────────────────────────────────────────────
    Question(category="Reasoning", prompt="If it takes 5 machines 5 minutes to make 5 widgets, how long for 100 machines to make 100 widgets? Answer with the number and unit only.", expected="5 minutes", score_fn="keyword"),
    Question(category="Reasoning", prompt="A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost in cents? Answer with just the number.", expected="5", score_fn="math"),
    Question(category="Reasoning", prompt="You have a 3-liter and a 5-liter bucket. How do you measure exactly 4 liters? Describe briefly.", expected="fill 5 empty 3", score_fn="keyword"),
    Question(category="Reasoning", prompt="Three boxes are labeled Apples, Oranges, and Mixed — all labels are wrong. You pick one fruit from the Mixed box and it's an apple. What is in each box? Answer concisely.", expected="apples and oranges", score_fn="keyword"),
    Question(category="Reasoning", prompt="A snail climbs 3 feet up a wall each day and slides 2 feet down each night. The wall is 10 feet tall. On which day does the snail reach the top? Just the number.", expected="8", score_fn="math"),
    Question(category="Reasoning", prompt="In a race you overtake the runner in 2nd place. What position are you now in? Answer with just the position.", expected="second 2nd", score_fn="keyword"),
    Question(category="Reasoning", prompt="How many months in a year have 28 days? Answer with just the number.", expected="12", score_fn="math"),
    Question(category="Reasoning", prompt="Mary's mother has four children: April, May, June, and one more. What is the fourth child's name?", expected="mary", score_fn="keyword"),
    Question(category="Reasoning", prompt="An electric train is traveling north. The wind is blowing east. Which direction does the smoke blow from the train?", expected="no smoke electric", score_fn="keyword"),
    Question(category="Reasoning", prompt="A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have? Just the number.", expected="9", score_fn="math"),
    Question(category="Reasoning", prompt="What comes next in the sequence: O, T, T, F, F, S, S, E, N, ? (Hint: think of number names)", expected="ten", score_fn="keyword"),
    Question(category="Reasoning", prompt="Two mothers and two daughters go fishing. Each catches exactly one fish, yet only 3 fish are caught total. How is this possible?", expected="grandmother mother daughter", score_fn="keyword"),
    Question(category="Reasoning", prompt="Rearrange the letters B, E, L, O, W to form a common English word.", expected="elbow", score_fn="keyword"),
    Question(category="Reasoning", prompt="A lily pad doubles in size every day and covers the entire pond in 48 days. How many days does it take to cover half the pond? Just the number.", expected="47", score_fn="math"),
    Question(category="Reasoning", prompt="You have two ropes. Each burns in exactly 60 minutes but not at a uniform rate. How do you measure exactly 45 minutes? Explain briefly.", expected="light both ends one", score_fn="keyword"),
    Question(category="Reasoning", prompt="A clock shows 3:15. What is the exact angle in degrees between the hour and minute hands? Just the number.", expected="7.5", score_fn="math"),
    Question(category="Reasoning", prompt="You have 12 identical-looking balls; one is heavier. Using a balance scale, what is the minimum number of weighings to guarantee finding the heavy ball?", expected="3 three", score_fn="keyword"),
    Question(category="Reasoning", prompt="If you drive to work at 30 mph, how fast must you drive back to average 60 mph for the round trip?", expected="impossible infinite never", score_fn="keyword"),
    Question(category="Reasoning", prompt="The Monty Hall problem: you pick door 1, the host opens door 3 revealing a goat. Should you switch to door 2? Answer Yes/No and give the win probability if you switch.", expected="yes 2/3 67", score_fn="keyword"),
    Question(category="Reasoning", prompt="If 2+3=10, 7+2=63, 6+5=66, 8+4=96, then 9+7=? Just the number.", expected="144", score_fn="math"),
    Question(category="Reasoning", prompt="How many squares are on a standard 8×8 chessboard? (Count all sizes, not just 1×1.) Just the number.", expected="204", score_fn="math"),
    Question(category="Reasoning", prompt="Is this argument valid? 'All dogs are animals. All cats are animals. Therefore all dogs are cats.' Answer Yes or No and identify the fallacy.", expected="no fallacy invalid", score_fn="keyword"),
    Question(category="Reasoning", prompt="Three friends pay $30 for a hotel room. Manager refunds $5; bellhop keeps $2 and returns $1 each. Each friend paid $9 = $27 total; plus $2 = $29. Where is the missing dollar?", expected="no missing false premise", score_fn="keyword"),
    Question(category="Reasoning", prompt="How many times does the digit 1 appear in all integers from 1 to 100? Just the number.", expected="21", score_fn="math"),
    Question(category="Reasoning", prompt="At what time between 3 and 4 o'clock are the hour and minute hands of a clock exactly coincident? Answer in minutes past 3, to 2 decimal places.", expected="16.36", score_fn="math"),
    Question(category="Reasoning", prompt="You have a 100-floor building and 2 eggs. You want to find the highest floor an egg survives from. What is the minimum worst-case number of drops needed?", expected="14", score_fn="math"),
    Question(category="Reasoning", prompt="A logician visits an island where everyone either always lies or always tells the truth. A native says: 'I am a liar.' Is the native a truth-teller, a liar, or is this impossible?", expected="impossible paradox neither", score_fn="keyword"),
    Question(category="Reasoning", prompt="What is the minimum number of moves to solve the Tower of Hanoi with 4 discs? Just the number.", expected="15", score_fn="math"),
    Question(category="Reasoning", prompt="A store reduces a price by 10% then reduces it by another 10%. Is the total reduction 20%? Answer Yes/No and give the actual percentage.", expected="no 19", score_fn="keyword"),
    Question(category="Reasoning", prompt="What is the maximum number of regions a plane can be divided into by 5 straight lines? Just the number.", expected="16", score_fn="math"),
    Question(category="Reasoning", prompt="If you write all numbers from 1 to 1000, how many times do you write the digit 0? Just the number.", expected="192", score_fn="math"),
    Question(category="Reasoning", prompt="Look-and-Say sequence: 1, 11, 21, 1211, 111221. What is the next term?", expected="312211", score_fn="keyword"),
    Question(category="Reasoning", prompt="Albert is taller than Bob. Carlos is shorter than Albert. David is taller than Carlos but shorter than Bob. Who is the second tallest? Just the name.", expected="bob", score_fn="keyword"),
    Question(category="Reasoning", prompt="What is 1/3 of 3/4 of 48? Just the number.", expected="12", score_fn="math"),
    Question(category="Reasoning", prompt="Two children share the same parents, were born at the same time, but are not twins. How?", expected="triplets triplet", score_fn="keyword"),
    Question(category="Reasoning", prompt="How many prime numbers are there between 1 and 20? Just the number.", expected="8", score_fn="math"),
    Question(category="Reasoning", prompt="Alice runs at 5 m/s and Bob at 3 m/s on a circular 400-meter track, both in the same direction. How many seconds until Alice laps Bob? Just the number.", expected="200", score_fn="math"),
    Question(category="Reasoning", prompt="If P(rain) = 0.3 on any day, what is P(no rain on two consecutive days)? Give as a decimal.", expected="0.49", score_fn="math"),
    Question(category="Reasoning", prompt="A doctor gives you 3 pills and says take one every 30 minutes. How many minutes until all pills are taken? Just the number.", expected="60", score_fn="math"),
    Question(category="Reasoning", prompt="What is wrong with this reasoning: 'I've flipped a coin 10 times and got heads every time, so tails is overdue.' Name the fallacy.", expected="gambler fallacy", score_fn="keyword"),
    Question(category="Reasoning", prompt="Four people cross a bridge at night with one torch: A=1 min, B=2 min, C=5 min, D=10 min. Max 2 per crossing. Minimum total time in minutes?", expected="17", score_fn="math"),
    Question(category="Reasoning", prompt="Complete the pattern: 2, 3, 5, 7, 11, 13, ? (What rule governs this sequence?)", expected="17", score_fn="math"),
    Question(category="Reasoning", prompt="You are in a room with two doors. One leads to freedom, one to a tiger. Two guards know which is which: one always lies, one always tells the truth. You can ask one guard one yes/no question. What do you ask?", expected="other guard door", score_fn="keyword"),
    Question(category="Reasoning", prompt="A number equals the sum of its proper divisors (divisors less than itself). What is the smallest such number greater than 1?", expected="6", score_fn="math"),
    Question(category="Reasoning", prompt="If all Wumps are Mooks and half of all Mooks are Wumps, what fraction of Mooks are Wumps? Answer as a fraction.", expected="1/2 half 50", score_fn="keyword"),
    Question(category="Reasoning", prompt="Which is larger: 2^(3^2) or (2^3)^2? State which and give both values.", expected="512 64", score_fn="keyword"),
    Question(category="Reasoning", prompt="A frog is at the bottom of a 10-foot well. Each day it climbs 3 feet; each night it falls 1 foot. On what day does it escape? Just the number.", expected="5", score_fn="math"),
    Question(category="Reasoning", prompt="You measure the height of a building by dropping a stone and timing its fall at 3 seconds. Using d = ½gt² and g = 9.8 m/s², how tall is the building in meters? Just the number.", expected="44.1", score_fn="math"),
    Question(category="Reasoning", prompt="If you have a 3×3 grid and place numbers 1–9 so each row, column, and diagonal sums to 15 (a magic square), what number goes in the center? Just the number.", expected="5", score_fn="math"),

    # ── Mathematics (50) ───────────────────────────────────────────────────
    Question(category="Mathematics", prompt="What is 15% of 240? Just the number.", expected="36", score_fn="math"),
    Question(category="Mathematics", prompt="A train travels at 60 mph for 2 hours 30 minutes. How far in miles? Just the number.", expected="150", score_fn="math"),
    Question(category="Mathematics", prompt="What is √144? Just the number.", expected="12", score_fn="math"),
    Question(category="Mathematics", prompt="A rectangle is 8 cm × 5 cm. What is its area? Just the number.", expected="40", score_fn="math"),
    Question(category="Mathematics", prompt="Solve for x: 3x + 7 = 22. Just the number.", expected="5", score_fn="math"),
    Question(category="Mathematics", prompt="What is 2^10? Just the number.", expected="1024", score_fn="math"),
    Question(category="Mathematics", prompt="What is the LCM of 12 and 18? Just the number.", expected="36", score_fn="math"),
    Question(category="Mathematics", prompt="Calculate 7! ÷ 5! Just the number.", expected="42", score_fn="math"),
    Question(category="Mathematics", prompt="What is the sum of interior angles of a hexagon in degrees? Just the number.", expected="720", score_fn="math"),
    Question(category="Mathematics", prompt="Solve: 2^x = 32. What is x? Just the number.", expected="5", score_fn="math"),
    Question(category="Mathematics", prompt="What is the harmonic mean of 40 and 60? Just the number.", expected="48", score_fn="math"),
    Question(category="Mathematics", prompt="What is the GCD of 48 and 36? Just the number.", expected="12", score_fn="math"),
    Question(category="Mathematics", prompt="Calculate: (−3)² + (−2)³. Just the number.", expected="1", score_fn="math"),
    Question(category="Mathematics", prompt="A circle has area 25π. What is its radius? Just the number.", expected="5", score_fn="math"),
    Question(category="Mathematics", prompt="What is the probability of flipping exactly 2 heads with 3 fair coins? Give as a decimal.", expected="0.375", score_fn="math"),
    Question(category="Mathematics", prompt="What is the 8th term of the arithmetic sequence 3, 7, 11, 15, …? Just the number.", expected="31", score_fn="math"),
    Question(category="Mathematics", prompt="How many diagonals does a pentagon have? Just the number.", expected="5", score_fn="math"),
    Question(category="Mathematics", prompt="What is √2 × √8? Just the number.", expected="4", score_fn="math"),
    Question(category="Mathematics", prompt="A bag has 5 red and 3 blue balls. You pick 2 without replacement. What is P(both red)? Give as a decimal rounded to 3 places.", expected="0.357", score_fn="math"),
    Question(category="Mathematics", prompt="What is the sum of the first 20 natural numbers? Just the number.", expected="210", score_fn="math"),
    Question(category="Mathematics", prompt="Solve the system: 2x + y = 7, x − y = 2. What is x? Just the number.", expected="3", score_fn="math"),
    Question(category="Mathematics", prompt="What is lim(x→0) sin(x)/x? Just the number.", expected="1", score_fn="math"),
    Question(category="Mathematics", prompt="In how many ways can 4 people be arranged in a row? Just the number.", expected="24", score_fn="math"),
    Question(category="Mathematics", prompt="What is the derivative of x³? Answer as an expression.", expected="3x", score_fn="keyword"),
    Question(category="Mathematics", prompt="A geometric series has first term 3 and ratio 1/2. What is the sum to infinity? Just the number.", expected="6", score_fn="math"),
    Question(category="Mathematics", prompt="What is the distance between points (0,0) and (3,4)? Just the number.", expected="5", score_fn="math"),
    Question(category="Mathematics", prompt="What is the remainder when 2^10 is divided by 7? Just the number.", expected="2", score_fn="math"),
    Question(category="Mathematics", prompt="How many zeros does 50! end with? Just the number.", expected="12", score_fn="math"),
    Question(category="Mathematics", prompt="What is f(f(2)) if f(x) = x² + 1? Just the number.", expected="26", score_fn="math"),
    Question(category="Mathematics", prompt="What is the surface area of a cube with side length 4? Just the number.", expected="96", score_fn="math"),
    Question(category="Mathematics", prompt="If sin(θ) = 0.6 and 0 < θ < 90°, what is cos(θ)? Just the number.", expected="0.8", score_fn="math"),
    Question(category="Mathematics", prompt="How many prime numbers are there between 1 and 30? Just the number.", expected="10", score_fn="math"),
    Question(category="Mathematics", prompt="What is C(8,2)? Just the number.", expected="28", score_fn="math"),
    Question(category="Mathematics", prompt="What is the slope of the line through (1,2) and (3,8)? Just the number.", expected="3", score_fn="math"),
    Question(category="Mathematics", prompt="If P(A) = 0.4 and P(B|A) = 0.5 and they are independent, what is P(A ∩ B)? Just the decimal.", expected="0.2", score_fn="math"),
    Question(category="Mathematics", prompt="What is i⁴ where i = √(−1)? Just the number.", expected="1", score_fn="math"),
    Question(category="Mathematics", prompt="What is the smallest positive integer divisible by both 6 and 8? Just the number.", expected="24", score_fn="math"),
    Question(category="Mathematics", prompt="What is the perimeter of a regular hexagon with side length 7? Just the number.", expected="42", score_fn="math"),
    Question(category="Mathematics", prompt="How many ways can you select 3 items from 7 (order does not matter)? Just the number.", expected="35", score_fn="math"),
    Question(category="Mathematics", prompt="What is the area of a right triangle with legs 6 and 8? Just the number.", expected="24", score_fn="math"),
    Question(category="Mathematics", prompt="What is the 10th term of the geometric sequence 2, 6, 18, …? Just the number.", expected="39366", score_fn="math"),
    Question(category="Mathematics", prompt="How many trailing zeros does 100! have? Just the number.", expected="24", score_fn="math"),
    Question(category="Mathematics", prompt="Solve |2x − 3| = 7. Give both solutions separated by a comma.", expected="5 -2", score_fn="keyword"),
    Question(category="Mathematics", prompt="What is the volume of a cone with radius 3 and height 4? Give as a multiple of π (e.g. 12π).", expected="12π 12pi", score_fn="keyword"),
    Question(category="Mathematics", prompt="Express the fraction 7/12 as a decimal rounded to 4 places.", expected="0.5833", score_fn="math"),
    Question(category="Mathematics", prompt="If P(A) = 0.3 and events A and B are mutually exclusive with P(B) = 0.4, what is P(A ∪ B)?", expected="0.7", score_fn="math"),
    Question(category="Mathematics", prompt="What is the 5th Fibonacci number (1-indexed, starting 1, 1, 2, 3, 5, …)? Just the number.", expected="5", score_fn="math"),
    Question(category="Mathematics", prompt="A number is increased by 20% then decreased by 20%. What percentage of the original is the result?", expected="96", score_fn="math"),
    Question(category="Mathematics", prompt="What is the determinant of the matrix [[3, 1], [2, 4]]? Just the number.", expected="10", score_fn="math"),
    Question(category="Mathematics", prompt="A car accelerates from rest at 2 m/s². Using s = ½at², how far does it travel in 6 seconds? Just the number in metres.", expected="36", score_fn="math"),

    # ── Knowledge (50) ─────────────────────────────────────────────────────
    Question(category="Knowledge", prompt="What is the chemical symbol for gold? Just the symbol.", expected="au", score_fn="keyword"),
    Question(category="Knowledge", prompt="In what year did World War II end? Just the year.", expected="1945", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the capital of Australia? Just the city name.", expected="canberra", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who wrote the play Hamlet? Just the author's last name.", expected="shakespeare", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the approximate speed of light in km/s? Round to nearest 1000.", expected="300000", score_fn="keyword"),
    Question(category="Knowledge", prompt="What element has atomic number 79? Just the element name.", expected="gold", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the largest planet in the solar system? Just the name.", expected="jupiter", score_fn="keyword"),
    Question(category="Knowledge", prompt="In what year did the French Revolution begin? Just the year.", expected="1789", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who developed the theory of general relativity? Just the last name.", expected="einstein", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the SI unit of electrical resistance? Just the unit name.", expected="ohm", score_fn="keyword"),
    Question(category="Knowledge", prompt="What gas makes up approximately 78% of Earth's atmosphere? Just the name.", expected="nitrogen", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who painted the Sistine Chapel ceiling? Just the last name.", expected="michelangelo", score_fn="keyword"),
    Question(category="Knowledge", prompt="What organelle is called the powerhouse of the cell? Just the name.", expected="mitochondria", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the chemical formula for sulfuric acid? Just the formula.", expected="H2SO4", score_fn="keyword"),
    Question(category="Knowledge", prompt="How many bones are in the adult human body? Just the number.", expected="206", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who wrote Crime and Punishment? Just the last name.", expected="dostoevsky", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the boiling point of water in Fahrenheit? Just the number.", expected="212", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the capital of Canada? Just the city name.", expected="ottawa", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the largest ocean on Earth? Just the name.", expected="pacific", score_fn="keyword"),
    Question(category="Knowledge", prompt="What element is represented by the symbol Fe? Just the element name.", expected="iron", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who invented the telephone? Just the inventor's last name.", expected="bell", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the smallest country in the world by area? Just the name.", expected="vatican", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the approximate half-life of Carbon-14 in years? Just the number.", expected="5730", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who formulated the three laws of motion? Just the last name.", expected="newton", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the national currency of Japan? Just the name.", expected="yen", score_fn="keyword"),
    Question(category="Knowledge", prompt="How many chromosomes do humans normally have? Just the number.", expected="46", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who wrote War and Peace? Just the last name.", expected="tolstoy", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the speed of sound in air at room temperature in m/s? Approximate to nearest 10.", expected="340 343", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the largest organ in the human body? Just the name.", expected="skin", score_fn="keyword"),
    Question(category="Knowledge", prompt="What does DNA stand for? Full name only.", expected="deoxyribonucleic", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the capital of Brazil? Just the city name.", expected="brasilia", score_fn="keyword"),
    Question(category="Knowledge", prompt="How many chambers does the human heart have? Just the number.", expected="4", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the chemical symbol for potassium? Just the symbol.", expected="k", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who was the first person to walk on the moon? First and last name.", expected="armstrong neil", score_fn="keyword"),
    Question(category="Knowledge", prompt="What planet is known as the Red Planet? Just the name.", expected="mars", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the hardest natural substance? Just the name.", expected="diamond", score_fn="keyword"),
    Question(category="Knowledge", prompt="How many moons does Mars have? Just the number.", expected="2", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the most abundant element in the universe? Just the name.", expected="hydrogen", score_fn="keyword"),
    Question(category="Knowledge", prompt="In what year did the Berlin Wall fall? Just the year.", expected="1989", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the chemical symbol for sodium? Just the symbol.", expected="na", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the main greenhouse gas produced by human activity? Just the name or formula.", expected="carbon dioxide co2", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the longest bone in the human body? Just the name.", expected="femur", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who wrote the novel 1984? Just the last name.", expected="orwell", score_fn="keyword"),
    Question(category="Knowledge", prompt="Who invented the World Wide Web? Full name.", expected="berners-lee tim", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the melting point of gold in Celsius? Just the number.", expected="1064", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the most spoken language in the world by number of native speakers? Just the language.", expected="mandarin chinese", score_fn="keyword"),
    Question(category="Knowledge", prompt="What year did the first moon landing occur? Just the year.", expected="1969", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the chemical formula for glucose? Just the formula.", expected="C6H12O6", score_fn="keyword"),
    Question(category="Knowledge", prompt="What is the currency of Brazil? Just the name.", expected="real", score_fn="keyword"),
    Question(category="Knowledge", prompt="Which planet has the most known moons? Just the name.", expected="saturn", score_fn="keyword"),

    # ── Code (50) ──────────────────────────────────────────────────────────
    Question(category="Code", prompt="Write a Python function `fibonacci(n)` returning the nth Fibonacci number (0-indexed). Code only.", expected="def fibonacci", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python one-liner that reverses string `s` using slice notation. Code only.", expected="[::-1]", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `is_palindrome(s)` returning True if s is a palindrome. Code only.", expected="def is_palindrome", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python list comprehension producing squares of even numbers from 1 to 20. Code only.", expected="for", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `count_words(s)` returning the number of words in string s. Code only.", expected="def count_words", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `factorial(n)` using recursion. Code only.", expected="def factorial", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `binary_search(arr, target)` for a sorted list, returning the index or -1. Code only.", expected="def binary_search", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python decorator `timer` that prints the execution time of a function. Code only.", expected="def timer", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python generator function `infinite_counter(start=0)` that yields consecutive integers. Code only.", expected="yield", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python class `Stack` with push, pop, and is_empty methods. Code only.", expected="class Stack", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `is_prime(n)` returning True if n is prime. Code only.", expected="def is_prime", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `anagram(s1, s2)` returning True if both strings are anagrams. Code only.", expected="def anagram", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `deep_flatten(lst)` that recursively flattens a nested list of any depth. Code only.", expected="def deep_flatten", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `memoize(func)` that caches function call results in a dict. Code only.", expected="def memoize", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `bubble_sort(arr)` that sorts a list in place and returns it. Code only.", expected="def bubble_sort", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python class `Queue` implemented internally using two stacks. Code only.", expected="class Queue", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `chunk(lst, n)` that splits a list into sublists of size n. Code only.", expected="def chunk", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `snake_to_camel(s)` converting snake_case to camelCase. Code only.", expected="def snake_to_camel", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `power(base, exp)` computing base^exp without using the ** operator. Code only.", expected="def power", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `find_duplicates(lst)` returning elements that appear more than once. Code only.", expected="def find_duplicates", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `caesar_cipher(text, shift)` that shifts each letter by shift positions. Code only.", expected="def caesar_cipher", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python class `LinkedList` with append and __iter__ methods. Code only.", expected="class LinkedList", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `matrix_multiply(A, B)` for 2D lists. Code only.", expected="def matrix_multiply", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `run_length_encode(s)` e.g. 'aaabbc' → '3a2b1c'. Code only.", expected="def run_length_encode", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `max_subarray(arr)` using Kadane's algorithm. Code only.", expected="def max_subarray", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `is_balanced(s)` checking if (), [], {} are correctly balanced. Code only.", expected="def is_balanced", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `all_permutations(lst)` without using itertools. Code only.", expected="def all_permutations", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python dataclass `Point` with x and y fields and a distance_to(other) method. Code only.", expected="dataclass", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `topological_sort(graph)` for a DAG represented as an adjacency dict. Code only.", expected="def topological_sort", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python async function `fetch_all(urls, session)` that fetches all URLs concurrently with asyncio.gather. Code only.", expected="async def", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `levenshtein(s1, s2)` computing edit distance using dynamic programming. Code only.", expected="def levenshtein", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `group_by(lst, key_fn)` grouping list items by the result of key_fn. Code only.", expected="def group_by", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python class `SuppressErrors` context manager that swallows specified exception types. Code only.", expected="class SuppressErrors", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `word_frequency(text)` returning a dict of word counts. Code only.", expected="def word_frequency", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `sliding_window_max(arr, k)` returning the max in each window of size k. Code only.", expected="def sliding_window_max", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python metaclass `Singleton` that ensures only one instance of a class can exist. Code only.", expected="class Singleton", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `merge_sort(arr)` implementing merge sort. Code only.", expected="def merge_sort", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `binary_to_decimal(s)` converting a binary string to decimal without using int(s,2). Code only.", expected="def binary_to_decimal", score_fn="syntax"),
    Question(category="Code", prompt="Write Python code using functools.reduce to compute the product of all elements in list `nums`. Code only.", expected="reduce", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `trie_insert(trie, word)` inserting a word into a trie stored as nested dicts. Code only.", expected="def trie_insert", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `rotate_matrix(matrix)` rotating a square 2D list 90° clockwise in place. Code only.", expected="def rotate_matrix", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `count_bits(n)` counting the number of set bits in integer n without bin(). Code only.", expected="def count_bits", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `lru_cache_manual(capacity)` returning an LRU cache object with get and put methods. Code only.", expected="capacity", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `parse_url(url)` extracting scheme, host, path, and query as a dict without using urllib. Code only.", expected="def parse_url", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `diff_lists(a, b)` returning a dict with keys 'added' and 'removed'. Code only.", expected="def diff_lists", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `nth_fibonacci_fast(n)` using matrix exponentiation or memoization for O(log n) or O(n) time. Code only.", expected="def nth_fibonacci_fast", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `flatten_dict(d, sep='.')` that flattens a nested dict, joining keys with sep. Code only.", expected="def flatten_dict", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `retry(func, times, exceptions)` that retries func up to times times on specified exceptions. Code only.", expected="def retry", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python class `Observable` with subscribe, unsubscribe, and notify methods (observer pattern). Code only.", expected="class Observable", score_fn="syntax"),
    Question(category="Code", prompt="Write a Python function `consistent_hash(key, num_buckets)` mapping a key to a bucket using a hash-based approach. Code only.", expected="def consistent_hash", score_fn="syntax"),

    # ── Instruction Following (50) ─────────────────────────────────────────
    Question(category="Instruction Following", prompt="List exactly 3 benefits of exercise as a numbered list. No other text.", expected="1.", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Respond to 'What is the weather like today?' in exactly 10 words.", expected="10_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Translate 'hello' into French, Spanish, and German. Format as JSON with keys 'french', 'spanish', 'german'.", expected='{"french"', score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a haiku (5-7-5 syllables) about the ocean. Output only the haiku, no title.", expected="haiku_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List the days of the week in reverse order, one per line, ALL CAPS. No other text.", expected="SUNDAY", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Respond with ONLY the number 42. No other text.", expected="42", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List exactly 5 planets in our solar system, one per line, no other text.", expected="5_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a sentence containing exactly 7 words.", expected="7_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Convert this list to a JSON array: apple, banana, cherry. Output only the JSON.", expected="json_array", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Reply with only the word 'DONE' in capital letters. Nothing else.", expected="DONE", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write your response in exactly 5 words.", expected="5_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Output the numbers 1 through 5, each on its own line, nothing else.", expected="5_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Translate 'goodbye' to French, Spanish, and German. Format as JSON with keys 'fr', 'es', 'de'. JSON only.", expected='{"fr"', score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write exactly 4 words about mathematics. Nothing else.", expected="4_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List the vowels a, e, i, o, u separated by commas with no spaces. Exactly that string.", expected="a,e,i,o,u", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write the numbers 1 through 10, one per line, no other text.", expected="10_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Respond with a single digit: the result of 3 + 4.", expected="7", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write 3 words that are colors. One word per line, nothing else.", expected="3_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Output the word 'hello' in ALL UPPERCASE. Nothing else.", expected="HELLO", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List the last 3 months of the year in reverse order, one per line, lowercase.", expected="december november october", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write exactly 2 sentences about the sun. Nothing before or after.", expected="2_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Provide 3 synonyms for 'happy' as a JSON array of strings. JSON only.", expected="json_array", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Give a one-word answer: what is the opposite of 'hot'?", expected="cold", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a Python comment (starting with #) that says Hello World. Just the comment line.", expected="# Hello", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a sentence in exactly 15 words.", expected="15_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Output the ASCII values of A, B, C as a JSON array. JSON only.", expected="json_array", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write the multiplication table for 9 from 9×1 to 9×5, one equation per line.", expected="5_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Answer with a single Roman numeral for the number 14.", expected="XIV", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List 4 sorting algorithm names, numbered 1–4, one per line.", expected="4_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Respond to 'Is Python interpreted or compiled?' with exactly one word.", expected="1_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Convert the number 255 to binary. Output only the binary number.", expected="11111111", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Give a one-sentence definition of recursion. 12 words maximum.", expected="recursion", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Respond with exactly the string: Hello, World! — including the comma and exclamation mark.", expected="Hello, World!", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List all days of the week that start with the letter T, one per line.", expected="2_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Translate 'thank you' to Japanese. Output only the Japanese.", expected="arigato arigatou", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a Python import statement for the math module. One line only.", expected="import math", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Output the first 5 letters of the alphabet in reverse order, separated by spaces.", expected="e d c b a", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Answer with just 'yes' or 'no': is 17 a prime number?", expected="yes", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a 3-line poem where each line ends with a word that rhymes with 'cat'.", expected="3_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Give the chemical symbols for gold, silver, and iron separated by commas. Symbols only.", expected="au ag fe", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Count the vowels in MISSISSIPPI. Output only the count.", expected="4", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a valid JSON object: key is 'status', value is 'ok'. JSON only.", expected='{"status"', score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write the hexadecimal representation of 255. Lowercase. Output only.", expected="ff", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Name exactly 2 programming languages that start with P, one per line.", expected="2_lines", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Output 'true' or 'false': Is the Earth older than the Sun?", expected="false", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write the first 5 square numbers separated by commas.", expected="1,4,9,16,25", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Respond in exactly 8 words to: 'What are the primary colors?'", expected="8_words", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Write a JSON array of the first 3 odd numbers. JSON only.", expected="json_array", score_fn="instruction"),
    Question(category="Instruction Following", prompt="Output the Morse code for SOS using dots and dashes only.", expected="... ---", score_fn="instruction"),
    Question(category="Instruction Following", prompt="List the chemical symbols for the first 3 elements (H, He, Li) as a JSON array. JSON only.", expected="json_array", score_fn="instruction"),

    # ── Agentic (50) ───────────────────────────────────────────────────────
    # Context retention (10)
    Question(category="Agentic", prompt="I'm planning a birthday party for my friend Alex who loves jazz music, is allergic to peanuts, and lives in Chicago. Acknowledge these details.", expected="jazz peanuts chicago", score_fn="agentic_context", follow_up="What are the three key facts I told you about Alex? List them.", follow_up_expected="jazz peanuts chicago"),
    Question(category="Agentic", prompt="My project has three requirements: it must use Python, be completed by Friday, and the budget is $500. Acknowledge these.", expected="python friday 500", score_fn="agentic_context", follow_up="What are the three project requirements I gave you?", follow_up_expected="python friday 500"),
    Question(category="Agentic", prompt="My server config: hostname=prod-01, IP=192.168.1.100, port=8080, OS=Ubuntu 22.04, RAM=16GB. Store these details.", expected="prod-01 192.168.1.100 8080", score_fn="agentic_context", follow_up="What are the hostname, IP, and port of my server?", follow_up_expected="prod-01 192.168.1.100 8080"),
    Question(category="Agentic", prompt="I have 3 employees: Sarah earns $75k, Mike earns $92k, Jane earns $68k. Acknowledge these salaries.", expected="sarah mike jane", score_fn="agentic_context", follow_up="Who earns the most and what is the total payroll?", follow_up_expected="mike 235"),
    Question(category="Agentic", prompt="Remember: Project Alpha has budget $50k, deadline March 15, team of 4, client is Acme Corp. Got it?", expected="alpha acme march", score_fn="agentic_context", follow_up="What is the client name and deadline for Project Alpha?", follow_up_expected="acme march"),
    Question(category="Agentic", prompt="User preferences: dark_mode=true, language=Spanish, font_size=14, notifications=false. Acknowledge.", expected="spanish 14", score_fn="agentic_context", follow_up="What language and font size did I set?", follow_up_expected="spanish 14"),
    Question(category="Agentic", prompt="I told you earlier that my API key is sk-abc-9999, my base URL is https://api.example.com, and rate limit is 100/min. Confirm.", expected="sk-abc-9999 example.com 100", score_fn="agentic_context", follow_up="What API key and rate limit did I give you?", follow_up_expected="sk-abc-9999 100"),
    Question(category="Agentic", prompt="Vehicle details: make=Toyota, model=Camry, year=2021, color=silver, mileage=34500. Store this.", expected="toyota camry 2021", score_fn="agentic_context", follow_up="What is the make, model, and year of the vehicle?", follow_up_expected="toyota camry 2021"),
    Question(category="Agentic", prompt="I have three tasks: (1) fix login bug — due today, (2) write unit tests — due Wednesday, (3) deploy to staging — due Friday. Remember these.", expected="login wednesday friday", score_fn="agentic_context", follow_up="What task is due on Wednesday?", follow_up_expected="unit tests wednesday"),
    Question(category="Agentic", prompt="Database: host=db.internal, port=5432, name=prod_db, user=admin, password=secret123. Noted?", expected="db.internal 5432 prod_db", score_fn="agentic_context", follow_up="What is the database host and port?", follow_up_expected="db.internal 5432"),
    # Task decomposition (10)
    Question(category="Agentic", prompt="I want to build a REST API that reads from a database and returns JSON. Give me exactly 5 numbered steps.", expected="1. 2. 3. 4. 5.", score_fn="agentic_decompose", follow_up="Execute step 1 from your plan. Be specific and reference your plan.", follow_up_expected="step 1"),
    Question(category="Agentic", prompt="Plan a migration from a monolithic app to microservices. Give exactly 4 numbered steps.", expected="1. 2. 3. 4.", score_fn="agentic_decompose", follow_up="What does step 2 of your plan involve? Reference your exact wording.", follow_up_expected="step 2"),
    Question(category="Agentic", prompt="Design a machine learning pipeline to classify customer support tickets. Give exactly 6 numbered steps.", expected="1. 2. 3. 4. 5. 6.", score_fn="agentic_decompose", follow_up="Expand on step 3 from your plan. What specifically does it involve?", follow_up_expected="step 3"),
    Question(category="Agentic", prompt="Plan a database migration from MySQL to PostgreSQL. Give exactly 5 numbered steps.", expected="1. 2. 3. 4. 5.", score_fn="agentic_decompose", follow_up="What risks are associated with step 2 of your plan?", follow_up_expected="step 2"),
    Question(category="Agentic", prompt="Outline a security audit plan for a web application. Give exactly 5 numbered steps.", expected="1. 2. 3. 4. 5.", score_fn="agentic_decompose", follow_up="Execute step 4 from your plan. What specific actions does it involve?", follow_up_expected="step 4"),
    Question(category="Agentic", prompt="Plan the rollout of a new software feature to production. Give exactly 4 numbered steps.", expected="1. 2. 3. 4.", score_fn="agentic_decompose", follow_up="Describe a rollback procedure based on your plan.", follow_up_expected="step"),
    Question(category="Agentic", prompt="Create a plan to build a real-time chat application. Give exactly 7 numbered steps.", expected="1. 2. 3. 4. 5. 6. 7.", score_fn="agentic_decompose", follow_up="Which step in your plan covers real-time communication? Reference it by number.", follow_up_expected="step"),
    Question(category="Agentic", prompt="Plan how to set up a CI/CD pipeline for a Python project. Give exactly 5 numbered steps.", expected="1. 2. 3. 4. 5.", score_fn="agentic_decompose", follow_up="What does step 2 of your CI/CD plan involve specifically?", follow_up_expected="step 2"),
    Question(category="Agentic", prompt="Outline a plan to optimize a slow SQL query. Give exactly 4 numbered steps.", expected="1. 2. 3. 4.", score_fn="agentic_decompose", follow_up="Apply step 1 of your plan to this scenario: 'SELECT * FROM orders WHERE user_id = 5'.", follow_up_expected="step 1"),
    Question(category="Agentic", prompt="Plan how to conduct a code review for a large pull request. Give exactly 5 numbered steps.", expected="1. 2. 3. 4. 5.", score_fn="agentic_decompose", follow_up="What should happen in step 3 of your review process?", follow_up_expected="step 3"),
    # Tool use (30) — single turn
    Question(category="Agentic", prompt='Tool: {"name":"get_weather","parameters":{"city":"string","units":"celsius|fahrenheit"}}\nUser: "What\'s the weather in Tokyo in Celsius?"\nRespond with ONLY a valid JSON tool call.', expected="get_weather tokyo celsius", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"get_user","parameters":{"user_id":"integer"}}\nUser: "Get the user with ID 42."\nRespond with ONLY a valid JSON tool call.', expected="get_user 42", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"search","parameters":{"query":"string","limit":"integer","page":"integer (optional)"}}\nUser: "Search for python tutorials, limit to 5 results."\nRespond with ONLY a valid JSON tool call.', expected="search python 5", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"send_email","parameters":{"to":"string","subject":"string","priority":"low|medium|high"}}\nUser: "Send an urgent email to boss@company.com with subject \'Server Down\'."\nRespond with ONLY a valid JSON tool call.', expected="send_email boss@company.com high", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"create_task","parameters":{"title":"string","due_date":"YYYY-MM-DD","assignee":"string","priority":"1-5"}}\nUser: "Create task \'Fix bug #123\', due 2025-01-15, assign to alice, priority 2."\nRespond with ONLY a valid JSON tool call.', expected="create_task 2025-01-15 alice 2", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"batch_update","parameters":{"ids":"array of integers","status":"string"}}\nUser: "Mark items 1, 2, and 3 as completed."\nRespond with ONLY a valid JSON tool call.', expected="batch_update completed", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"create_user","parameters":{"name":"string","email":"string","age":"integer"}}\nUser: "Add Bob Smith, email bob@email.com, age 25."\nRespond with ONLY a valid JSON tool call.', expected="create_user bob@email.com 25", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"toggle_feature","parameters":{"feature_name":"string","enabled":"boolean"}}\nUser: "Enable dark mode."\nRespond with ONLY a valid JSON tool call.', expected="toggle_feature dark_mode true", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"book_flight","parameters":{"from_city":"string","to_city":"string","date":"YYYY-MM-DD"}}\nUser: "Book a flight from New York to London on January 20, 2025."\nRespond with ONLY a valid JSON tool call.', expected="book_flight new york london 2025-01-20", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"set_temperature","parameters":{"celsius":"float"}}\nUser: "Set the thermostat to 72°F." (Note: (72-32)*5/9 = 22.2°C)\nRespond with ONLY a valid JSON tool call.', expected="set_temperature 22", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"schedule_meeting","parameters":{"date":"YYYY-MM-DD","time":"HH:MM","attendees":"array of strings"}}\nUser: "Schedule a meeting on 2025-03-10 at 2pm with alice and bob."\nRespond with ONLY a valid JSON tool call.', expected="schedule_meeting 2025-03-10 14:00 alice bob", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"withdraw","parameters":{"account_id":"string","amount":"float"}}\nUser: "My account is ACC-456. Withdraw 30% of $1000."\nRespond with ONLY a valid JSON tool call.', expected="withdraw ACC-456 300", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"add_contact","parameters":{"name":"string","email":"string","phone":"string"}}\nUser: "Add Jane Doe, email jane.doe@example.com, phone 555-9876."\nRespond with ONLY a valid JSON tool call.', expected="add_contact jane.doe@example.com 555-9876", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"convert_currency","parameters":{"amount":"float","from_currency":"string","to_currency":"string"}}\nUser: "Convert $250 USD to EUR."\nRespond with ONLY a valid JSON tool call.', expected="convert_currency 250 USD EUR", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"upload_file","parameters":{"filename":"string","content_type":"pdf|docx|txt|csv"}}\nUser: "Upload quarterly_report.pdf."\nRespond with ONLY a valid JSON tool call.', expected="upload_file quarterly_report.pdf pdf", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"search_products","parameters":{"category":"string","min_price":"float","max_price":"float"}}\nUser: "Show me laptops under $500."\nRespond with ONLY a valid JSON tool call.', expected="search_products laptop 500", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"log_event","parameters":{"event_type":"string","severity":"info|warning|error|critical","message":"string"}}\nUser: "Log a critical error: database connection refused."\nRespond with ONLY a valid JSON tool call.', expected="log_event critical database", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"classify_text","parameters":{"text":"string","categories":"array of strings"}}\nUser: "Classify \'I cannot log in\' into: [\'billing\',\'technical_support\',\'account\',\'general\']"\nRespond with ONLY a valid JSON tool call.', expected="classify_text account", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"make_request","parameters":{"method":"GET|POST|PUT|DELETE","url":"string","body":"object or null"}}\nUser: "Send a POST to https://api.example.com/users with body {name: \'Alice\'}."\nRespond with ONLY a valid JSON tool call.', expected="make_request POST https://api.example.com/users alice", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"send_notification","parameters":{"user_id":"integer","type":"email|sms|push","contact":"string"}}\nUser: "Send an SMS to user 5 at +1-555-0100."\nRespond with ONLY a valid JSON tool call.', expected="send_notification 5 sms +1-555-0100", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"transfer_funds","parameters":{"from_account":"string","to_account":"string","amount":"float (must be positive)"}}\nUser: "Transfer $500 from ACC-001 to ACC-002."\nRespond with ONLY a valid JSON tool call.', expected="transfer_funds ACC-001 ACC-002 500", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"delete_record","parameters":{"table":"string","record_id":"integer","confirm":"boolean (must be true)"}}\nUser: "Delete record 99 from the users table."\nRespond with ONLY a valid JSON tool call.', expected="delete_record users 99 true", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"generate_report","parameters":{"type":"sales|inventory|users","start_date":"YYYY-MM-DD","end_date":"YYYY-MM-DD","format":"pdf|csv|json"}}\nUser: "Generate a sales report for Q1 2025 (Jan–Mar) as a PDF."\nRespond with ONLY a valid JSON tool call.', expected="generate_report sales 2025-01-01 2025-03-31 pdf", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"set_reminder","parameters":{"text":"string","datetime":"YYYY-MM-DD HH:MM"}}\nUser: "Remind me to call the dentist on 2025-02-14 at 9am."\nRespond with ONLY a valid JSON tool call.', expected="set_reminder dentist 2025-02-14 09:00", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"resize_image","parameters":{"url":"string","width":"integer","height":"integer","maintain_aspect":"boolean"}}\nUser: "Resize https://cdn.example.com/photo.jpg to 800x600 and keep the aspect ratio."\nRespond with ONLY a valid JSON tool call.', expected="resize_image cdn.example.com 800 600 true", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"calculate_mortgage","parameters":{"principal":"float","annual_rate_percent":"float","years":"integer"}}\nUser: "Calculate mortgage for $200,000 at 6% interest over 30 years."\nRespond with ONLY a valid JSON tool call.', expected="calculate_mortgage 200000 6 30", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"translate_text","parameters":{"text":"string","source_lang":"string","target_lang":"string"}}\nUser: "Translate \'Good morning\' from English to Japanese."\nRespond with ONLY a valid JSON tool call.', expected="translate_text good morning english japanese", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"create_webhook","parameters":{"url":"string","events":"array of strings","secret":"string"}}\nUser: "Create a webhook to https://myapp.io/hook for events [\'push\',\'pull_request\'] with secret \'mysecret\'."\nRespond with ONLY a valid JSON tool call.', expected="create_webhook myapp.io push pull_request mysecret", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"run_query","parameters":{"database":"string","query":"string","timeout_seconds":"integer (optional, default 30)"}}\nUser: "Run SELECT COUNT(*) FROM users on the prod database."\nRespond with ONLY a valid JSON tool call.', expected="run_query prod SELECT COUNT users", score_fn="agentic_tool"),
    Question(category="Agentic", prompt='Tool: {"name":"update_config","parameters":{"service":"string","key":"string","value":"string|number|boolean"}}\nUser: "Set the max_connections config key to 100 for the database service."\nRespond with ONLY a valid JSON tool call.', expected="update_config database max_connections 100", score_fn="agentic_tool"),
]


# ---------------------------------------------------------------------------
# Scoring functions
# ---------------------------------------------------------------------------

def score_keyword(response: str, expected: str) -> float:
    resp_lower = response.lower()
    keywords = [kw.strip().lower() for kw in expected.split() if kw.strip()]
    if not keywords:
        return 0.0
    return sum(1 for kw in keywords if kw in resp_lower) / len(keywords)


def score_math(response: str, expected: str) -> float:
    numbers = re.findall(r"-?\d+\.?\d*", response.replace(",", ""))
    if not numbers:
        return 0.0
    target = float(expected.replace(",", ""))
    return 1.0 if any(abs(float(n) - target) < 0.01 for n in numbers) else 0.0


def score_syntax(response: str, expected: str) -> float:
    code_match = re.search(r"```(?:python)?\n?(.*?)```", response, re.DOTALL)
    code = code_match.group(1).strip() if code_match else response.strip()

    valid_syntax = False
    try:
        ast.parse(code)
        valid_syntax = True
    except SyntaxError:
        pass

    has_expected = expected.lower() in code.lower()
    return (0.5 if valid_syntax else 0.0) + (0.5 if has_expected else 0.0)


def score_instruction(response: str, expected: str) -> float:
    # Generic: "N_words" (e.g. "10_words", "7_words")
    if re.fullmatch(r"\d+_words", expected):
        n = int(expected.split("_")[0])
        count = len(response.strip().split())
        return 1.0 if count == n else max(0.0, 1.0 - abs(count - n) * 0.1)

    # Generic: "N_lines" (e.g. "5_lines", "3_lines")
    if re.fullmatch(r"\d+_lines", expected):
        n = int(expected.split("_")[0])
        lines = [ln for ln in response.strip().splitlines() if ln.strip()]
        return 1.0 if len(lines) == n else max(0.0, 1.0 - abs(len(lines) - n) * 0.2)

    # Backwards-compat alias
    if expected == "haiku_lines":
        lines = [ln for ln in response.strip().splitlines() if ln.strip()]
        return 1.0 if len(lines) == 3 else max(0.0, 1.0 - abs(len(lines) - 3) * 0.25)

    # JSON array
    if expected == "json_array":
        arr_match = re.search(r"\[.*\]", response, re.DOTALL)
        if arr_match:
            try:
                obj = json.loads(arr_match.group())
                return 1.0 if isinstance(obj, list) else 0.5
            except json.JSONDecodeError:
                pass
        return 0.3 if "[" in response else 0.0

    # JSON object
    if expected.startswith("{"):
        json_match = re.search(r"\{.*\}", response, re.DOTALL)
        if json_match:
            try:
                json.loads(json_match.group())
                return 1.0
            except json.JSONDecodeError:
                pass
        key = expected.strip('{"').split('"')[0]
        return 0.5 if key.lower() in response.lower() else 0.0

    return score_keyword(response, expected)


def score_agentic_context(follow_up_response: str, follow_up_expected: str) -> float:
    keywords = [kw.strip().lower() for kw in follow_up_expected.split() if kw.strip()]
    resp_lower = follow_up_response.lower()
    hits = sum(1 for kw in keywords if kw in resp_lower)
    base = hits / len(keywords) if keywords else 0.0
    if len(follow_up_response.split()) < 5:
        base *= 0.5
    return base


def score_agentic_decompose(first_response: str, follow_up_response: str) -> float:
    steps = len(re.findall(r"^\s*\d+[\.\)]\s+", first_response, re.MULTILINE))
    plan_score = min(steps / 4, 1.0)
    reference_words = ["step", "first", "second", "1", "plan", "above"]
    ref_score = 1.0 if any(w in follow_up_response.lower() for w in reference_words) else 0.0
    return plan_score * 0.6 + ref_score * 0.4


def score_agentic_tool(response: str, expected: str) -> float:
    """Score a tool-call response. `expected` is space-separated keywords that must
    appear in the JSON payload (case-insensitive). Partial credit for partial matches."""
    json_match = re.search(r"\{.*\}", response, re.DOTALL)
    required = [kw.strip().lower() for kw in expected.split() if kw.strip()]
    if not required:
        return 0.0
    if not json_match:
        # Partial credit from raw response text
        resp_lower = response.lower()
        hits = sum(1 for kw in required if kw in resp_lower)
        return (hits / len(required)) * 0.3
    try:
        obj = json.loads(json_match.group())
        payload = json.dumps(obj).lower()
        hits = sum(1 for kw in required if kw in payload)
        return hits / len(required)
    except json.JSONDecodeError:
        resp_lower = response.lower()
        hits = sum(1 for kw in required if kw in resp_lower)
        return (hits / len(required)) * 0.5


def compute_score(question: Question, response: str, follow_up_response: Optional[str]) -> float:
    fn = question.score_fn
    if fn == "keyword":
        return score_keyword(response, question.expected)
    if fn == "math":
        return score_math(response, question.expected)
    if fn == "syntax":
        return score_syntax(response, question.expected)
    if fn == "instruction":
        return score_instruction(response, question.expected)
    if fn == "agentic_context":
        return score_agentic_context(follow_up_response or "", question.follow_up_expected or "")
    if fn == "agentic_decompose":
        return score_agentic_decompose(response, follow_up_response or "")
    if fn == "agentic_tool":
        return score_agentic_tool(response, question.expected)
    return 0.0


# ---------------------------------------------------------------------------
# Ollama interaction
# ---------------------------------------------------------------------------

def run_question(model: str, question: Question) -> QuestionResult:
    messages: list[dict] = [{"role": "user", "content": question.prompt}]

    start = time.perf_counter()
    resp = ollama.chat(model=model, messages=messages, options={"temperature": 0})
    latency_ms = (time.perf_counter() - start) * 1000
    response_text: str = resp["message"]["content"]

    follow_up_response: Optional[str] = None
    if question.follow_up:
        messages.append({"role": "assistant", "content": response_text})
        messages.append({"role": "user", "content": question.follow_up})
        fu_resp = ollama.chat(model=model, messages=messages, options={"temperature": 0})
        follow_up_response = fu_resp["message"]["content"]

    score = compute_score(question, response_text, follow_up_response)
    return QuestionResult(
        question=question,
        response=response_text,
        score=score,
        latency_ms=latency_ms,
        follow_up_response=follow_up_response,
    )


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------

def aggregate_results(results: list[QuestionResult]) -> dict:
    by_cat: dict[str, list[QuestionResult]] = {}
    for r in results:
        by_cat.setdefault(r.question.category, []).append(r)

    cat_scores = {cat: float(np.mean([r.score for r in rs])) * 100 for cat, rs in by_cat.items()}
    overall = float(np.mean(list(cat_scores.values())))
    latencies = [r.latency_ms for r in results]
    total_words = sum(len(r.response.split()) for r in results)
    total_seconds = sum(latencies) / 1000
    tokens_per_sec = (total_words * 1.3 / total_seconds) if total_seconds > 0 else 0.0

    return {
        "category_scores": cat_scores,
        "overall": overall,
        "latencies": latencies,
        "avg_latency_ms": float(np.mean(latencies)),
        "tokens_per_second": tokens_per_sec,
        "total_questions": len(results),
    }


# ---------------------------------------------------------------------------
# Visualizations
# ---------------------------------------------------------------------------

_PALETTE = {"good": "#4CAF50", "fair": "#FFC107", "poor": "#F44336", "blue": "#2196F3"}


def _bar_color(score: float) -> str:
    if score >= 70:
        return _PALETTE["good"]
    if score >= 40:
        return _PALETTE["fair"]
    return _PALETTE["poor"]


def generate_charts(agg: dict, out_dir: Path) -> None:
    chart_dir = out_dir / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)

    cats = list(agg["category_scores"].keys())
    vals = list(agg["category_scores"].values())

    # 1 — Horizontal bar chart
    fig, ax = plt.subplots(figsize=(9, 5))
    colors = [_bar_color(v) for v in vals]
    bars = ax.barh(cats, vals, color=colors, edgecolor="white", height=0.55)
    ax.set_xlim(0, 110)
    ax.set_xlabel("Score (0 – 100)", fontsize=11)
    ax.set_title("Evaluation Scores by Category", fontsize=13, fontweight="bold")
    ax.axvline(agg["overall"], color="#555", linestyle="--", linewidth=1.2)
    ax.text(agg["overall"] + 0.5, len(cats) - 0.5, f"avg {agg['overall']:.1f}", fontsize=8, color="#555")
    for bar, v in zip(bars, vals):
        ax.text(v + 1, bar.get_y() + bar.get_height() / 2, f"{v:.1f}", va="center", fontsize=9)
    patches = [
        mpatches.Patch(color=_PALETTE["good"], label="≥ 70  Good"),
        mpatches.Patch(color=_PALETTE["fair"], label="40–69  Fair"),
        mpatches.Patch(color=_PALETTE["poor"], label="< 40  Poor"),
    ]
    ax.legend(handles=patches, loc="lower right", fontsize=8)
    plt.tight_layout()
    fig.savefig(chart_dir / "category_scores.png", dpi=130)
    plt.close(fig)

    # 2 — Radar / spider chart
    n = len(cats)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    radar_vals = [v / 100 for v in vals] + [vals[0] / 100]
    angles_closed = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True})
    ax.plot(angles_closed, radar_vals, "o-", linewidth=2, color=_PALETTE["blue"])
    ax.fill(angles_closed, radar_vals, alpha=0.2, color=_PALETTE["blue"])
    ax.set_thetagrids(np.degrees(angles), cats, fontsize=10)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["25", "50", "75", "100"], fontsize=8)
    ax.set_title("Capability Radar", pad=20, fontsize=13, fontweight="bold")
    plt.tight_layout()
    fig.savefig(chart_dir / "radar_chart.png", dpi=130)
    plt.close(fig)

    # 3 — Latency distribution (box + jitter)
    latencies = agg["latencies"]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.boxplot(
        latencies, vert=True, patch_artist=True,
        boxprops={"facecolor": "#BBDEFB"},
        medianprops={"color": "#1565C0", "linewidth": 2},
        whiskerprops={"color": "#555"},
        capprops={"color": "#555"},
    )
    rng = np.random.default_rng(42)
    jitter = rng.uniform(-0.12, 0.12, len(latencies))
    ax.scatter(1 + jitter, latencies, alpha=0.65, color=_PALETTE["blue"], s=35, zorder=3)
    ax.set_xticks([1])
    ax.set_xticklabels(["All Questions"])
    ax.set_ylabel("Latency (ms)", fontsize=11)
    ax.set_title("Response Latency Distribution", fontsize=13, fontweight="bold")
    plt.tight_layout()
    fig.savefig(chart_dir / "latency_distribution.png", dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

def write_report(model: str, results: list[QuestionResult], agg: dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / "report.md"

    lines: list[str] = [
        f"# LLM Evaluation Report: `{model}`",
        "",
        f"**Date:** {date.today().isoformat()}  ",
        f"**Overall Score:** {agg['overall']:.1f} / 100",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Category | Score | Questions |",
        "|----------|------:|----------:|",
    ]
    for cat, score in agg["category_scores"].items():
        n = sum(1 for r in results if r.question.category == cat)
        lines.append(f"| {cat} | {score:.1f} | {n} |")

    lines += [
        "",
        "## Performance Metrics",
        "",
        "| Metric | Value |",
        "|--------|------:|",
        f"| Average latency | {agg['avg_latency_ms']:.0f} ms |",
        f"| Estimated tokens / sec | {agg['tokens_per_second']:.1f} |",
        f"| Total questions | {agg['total_questions']} |",
        "",
        "---",
        "",
        "## Visualizations",
        "",
        "![Category Scores](charts/category_scores.png)",
        "",
        "![Capability Radar](charts/radar_chart.png)",
        "",
        "![Latency Distribution](charts/latency_distribution.png)",
        "",
        "---",
        "",
        "## Detailed Results",
    ]

    by_cat: dict[str, list[QuestionResult]] = {}
    for r in results:
        by_cat.setdefault(r.question.category, []).append(r)

    for cat, cat_results in by_cat.items():
        lines += ["", f"### {cat}", ""]
        for i, r in enumerate(cat_results, 1):
            prompt_preview = r.question.prompt.replace("\n", " ")
            resp_preview = r.response[:600] + ("…" if len(r.response) > 600 else "")
            lines += [
                f"**Q{i}:** {prompt_preview}",
                "",
                f"> {resp_preview}",
                "",
            ]
            if r.follow_up_response:
                fu_preview = r.follow_up_response[:400] + ("…" if len(r.follow_up_response) > 400 else "")
                lines += [
                    f"**Follow-up:** {r.question.follow_up}",
                    "",
                    f"> {fu_preview}",
                    "",
                ]
            lines.append(f"**Score:** `{r.score:.2f}` &nbsp; **Latency:** `{r.latency_ms:.0f} ms`")
            lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ---------------------------------------------------------------------------
# README.md index
# ---------------------------------------------------------------------------

_INDEX_PATH = Path(__file__).parent / "README.md"

_TABLE_HEADER = (
    "| Model | Score | Tokens/sec | Date | Report |\n"
    "|-------|------:|-----------:|------|--------|\n"
)


def update_main_index(model: str, overall_score: float, tokens_per_sec: float, report_path: Path) -> None:
    rel = report_path.resolve().relative_to(Path(__file__).resolve().parent)
    new_row = f"| `{model}` | {overall_score:.1f} / 100 | {tokens_per_sec:.1f} | {date.today().isoformat()} | [Report]({rel}) |"

    if _INDEX_PATH.exists():
        content = _INDEX_PATH.read_text(encoding="utf-8")
        pattern = re.compile(rf"^\| `{re.escape(model)}` \|.*$", re.MULTILINE)
        if pattern.search(content):
            content = pattern.sub(new_row, content)
        else:
            content = content.rstrip("\n") + "\n" + new_row + "\n"
        _INDEX_PATH.write_text(content, encoding="utf-8")
    else:
        _INDEX_PATH.write_text(
            "# LLM Evaluation Index\n\n"
            + _TABLE_HEADER
            + new_row + "\n",
            encoding="utf-8",
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate an Ollama LLM model across 6 capability categories.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--model", default=None, help="Ollama model name, e.g. llama3.2")
    parser.add_argument("--output-dir", default="evaluations", help="Root output directory")
    args = parser.parse_args()

    model: str = args.model
    if not model:
        try:
            available = [m["name"] for m in ollama.list()["models"]]
        except Exception:
            available = []

        if available:
            print("\nAvailable models:")
            for i, name in enumerate(available, 1):
                print(f"  {i}. {name}")
            print()

        model = input("Model name to evaluate: ").strip()
        if not model:
            print("No model specified. Exiting.")
            raise SystemExit(1)
    out_root = Path(args.output_dir) / model.replace(":", "_")

    print(f"\nModel      : {model}")
    print(f"Output     : {out_root}")
    print(f"Questions  : {len(QUESTIONS)}\n")

    print("Warming up model (loading into memory)...", end=" ", flush=True)
    try:
        ollama.chat(model=model, messages=[{"role": "user", "content": "Hello!"}], options={"temperature": 0})
        print("ready.\n")
    except Exception as exc:
        print(f"warning: warmup failed ({exc})\n")

    results: list[QuestionResult] = []
    for q in tqdm(QUESTIONS, desc="Benchmarking", unit="q"):
        try:
            result = run_question(model, q)
        except Exception as exc:
            tqdm.write(f"  [ERROR] {q.category} — {exc}")
            result = QuestionResult(question=q, response=f"ERROR: {exc}", score=0.0, latency_ms=0.0)
        results.append(result)
        tqdm.write(f"  [{q.category:<22}] score={result.score:.2f}  latency={result.latency_ms:6.0f} ms")

    agg = aggregate_results(results)

    print(f"\n{'─' * 42}")
    print(f"  Overall Score : {agg['overall']:.1f} / 100")
    print(f"{'─' * 42}")
    for cat, score in agg["category_scores"].items():
        bar = "█" * int(score / 5)
        print(f"  {cat:<24} {score:5.1f}  {bar}")
    print(f"{'─' * 42}\n")

    generate_charts(agg, out_root)
    report_path = write_report(model, results, agg, out_root)
    update_main_index(model, agg["overall"], agg["tokens_per_second"], report_path)

    print(f"Report : {report_path}")
    print(f"Charts : {out_root / 'charts'}")
    print(f"Index  : {_INDEX_PATH}\n")


if __name__ == "__main__":
    main()
