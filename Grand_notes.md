# 🎯 GRAND MASTER NOTES — _The Joy of Computing Using Python_ (Weeks 1–12)

## NPTEL Exam Preparation Guide

---

## 📖 TABLE OF CONTENTS

1. **Week-wise Sections** (Complete breakdown of all 12 weeks)
2. **Core Topics Merged View** (Important concepts across the course)
3. **Output Solving Strategy** (How to predict outputs fast)
4. **Formula + Logic Cheatsheet** (Quick reference)
5. **Assignment Insights** (Patterns that repeat in exams)
6. **Final Revision Sheet** (Ultra-quick 1-page notes)

---

---

# ⏱️ PART 1: WEEK-WISE COMPLETE BREAKDOWN

---

## 🔷 WEEK 1: INTRODUCTION TO PROGRAMMING

### 📌 Concepts

- **Programming**: Writing instructions for a computer to solve problems
- **Algorithm**: Step-by-step method to solve a problem
- **Key Process**: Input → Processing → Output
- **Debugging**: Finding and fixing errors
- **Scratch**: Visual block-based programming language (beginner-friendly)
- **Loops**: Repeating instructions multiple times

### 💻 Code + Examples

```python
# Basic concepts (Scratch/Python idea)
# Input: Take data
name = input("Enter name: ")

# Processing
message = f"Hello {name}"

# Output
print(message)

# Loop example
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### 🔥 NPTEL Exam Tricks

- **Never modify code without thinking**: Algorithm first, coding second
- **Order matters**: Steps must be in sequence
- **Test small cases**: Don't jump to complex problems
- **Trace by hand**: Before running code

### ⚠️ Common Mistakes

- ❌ Confusing algorithm with program
- ❌ Thinking computer can understand vague instructions
- ❌ Writing code without planning
- ❌ Missing debugging step

### 🎯 Important Patterns

- Problem → Algorithm → Code → Test → Debug
- Loop basics: `for i in range(n)`
- Selection: `if-else` structure

---

## 🔷 WEEK 2: PYTHON BASICS (Variables, Input, Output, Conditions, Loops)

### 📌 Concepts

- **Variables**: Containers to store data (e.g., `x = 10`)
- **Data types**: `int`, `float`, `string`
- **Input**: `input()` returns **string by default**
- **Print**: Display output to console
- **Indentation**: Python uses indentation instead of `{}`
- **if-else**: Decision making
- **Loops**: `for` and `while`

### 💻 Code + Examples

```python
# Variables
a = 5
b = 3.5
name = "Pradip"

# Input (convert to int)
x = int(input("Enter: "))

# Print
print(f"Sum = {a + b}")

# If-else
if x > 5:
    print("Greater")
else:
    print("Lesser")

# For loop
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# While loop
i = 1
while i <= 3:
    print(i)
    i += 1

# Sum of N
n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)
```

### 🔥 NPTEL Exam Tricks

- `print(5+3)` → 8 but `print("5+3")` → "5+3" (strings don't compute)
- `input()` is **always string** → use `int()` for numbers
- Indentation errors stop code immediately
- Loop variable changes don't affect iteration: `for i in range(5): i=10` still prints 0,1,2,3,4

### ⚠️ Common Mistakes

- ❌ Forgetting `int()` conversion on input
- ❌ Using `Print` instead of `print`
- ❌ Missing colon `:` after `if`, `for`, `while`
- ❌ Wrong indentation

### 🎯 Important Patterns

- Discount calculation: `final = price - (price * discount / 100)`
- Multiplication table: Loop from 1 to 10, print `n * i`
- Sum pattern: Initialize sum=0, add in loop

---

## 🔷 WEEK 3: LISTS & SLICING

### 📌 Concepts

- **List**: Ordered collection (mutable, allows duplicates)
- **Indexing**: `a[0]` (0-indexed), `a[-1]` (last element)
- **Slicing**: `a[start:end:step]` (end is **excluded**)
- **List operations**: `append()`, `remove()`, `pop()`
- **Loop through list**: `for item in list`
- **List concatenation**: `a + b`
- **List repetition**: `a * 2`

### 💻 Code + Examples

```python
# List basics
a = [1, 2, 3, 4, 5]

# Indexing
print(a[0])    # 1
print(a[-1])   # 5
print(a[-2])   # 4

# Slicing (end is excluded)
print(a[1:4])   # [2, 3, 4]
print(a[:3])    # [1, 2, 3]
print(a[::2])   # [1, 3, 5]  (step=2)
print(a[::-1])  # [5, 4, 3, 2, 1]  (reverse)

# Operations
a.append(6)     # [1, 2, 3, 4, 5, 6]
a.remove(2)     # [1, 3, 4, 5, 6]  (removes first occurrence)
a.pop()         # removes last element
a.pop(1)        # removes index 1

# Nested loops
for i in [1,2]:
    for j in [3,4]:
        print(i, j)  # 1 3, 1 4, 2 3, 2 4

# FizzBuzz (Important pattern)
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### 🔥 NPTEL Exam Tricks

- **Slicing**: Remember `a[1:4]` gives indices 1,2,3 (NOT 4)
- **Negative slicing**: `a[-3:-1]` same as `a[len(a)-3:len(a)-1]`
- **Iteration**: Loop ignores manual variable changes (e.g., `for i in range(5): i=10` still does 0,1,2,3,4)
- **remove() vs pop()**: remove() takes VALUE, pop() takes INDEX
- **Order matters in FizzBuzz**: Check 3&&5 **before** 3 or 5 alone

### ⚠️ Common Mistakes

- ❌ `a[5]` on list of 4 elements → IndexError
- ❌ Confusing `remove(value)` and `pop(index)`
- ❌ `pop()` removes last, not first
- ❌ Wrong FizzBuzz order
- ❌ Slicing end index is excluded (common mistake)

### 🎯 Important Patterns

- **Output prediction**: Master slicing, list operations
- **Nested loops**: Output multiplication of iterations
- **FizzBuzz logic**: Check combined condition first

---

## 🔷 WEEK 4: LOGIC & PROBLEM-SOLVING

### 📌 Concepts

- **Problem-solving approach**: Understand → Design → Code
- **Magic Square**: Sum of rows = columns = diagonals = `n(n²+1)/2`
- **Dobble Game**: Use **sets** to find common element
- **Birthday Paradox**: With 23 people, ~50% chance of shared birthday
- **String matching**: Pattern recognition and comparison
- **Trial-and-error**: Valid problem-solving method

### 💻 Code + Examples

```python
# Magic Square sum formula
n = 3
magic_sum = n * (n*n + 1) // 2  # 15

# Common elements (Dobble)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
common = set1 & set2  # {3}

# Birthday paradox simulation
import random
count = sum(1 for trial in range(1000)
           if len(set(random.randint(1,365)
           for _ in range(23))) < 23) / 1000
print(f"Probability: {count}")  # ~0.5

# String matching
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))  # True
```

### 🔥 NPTEL Exam Tricks

- **Magic Sum formula**: `n(n²+1)/2` — memorize this!
- **Dobble logic**: Use set **intersection** (&) to find common
- **Birthday paradox**: Always use **complement** (probability of NO match)
- **Set is faster** than list for uniqueness check

### ⚠️ Common Mistakes

- ❌ Forgetting diagonal check in magic square
- ❌ Using list instead of set (slower)
- ❌ Direct probability instead of complement for birthday paradox
- ❌ Case sensitivity in string matching

### 🎯 Important Patterns

- Set operations: `&` (intersection), `|` (union), `-` (difference)
- Probability thinking: Use complement
- Trial-and-error: Valid for optimization

---

## 🔷 WEEK 5: DICTIONARIES, SORTING, SEARCHING

### 📌 Concepts

- **Dictionary**: Key → Value mapping (unique keys)
- **Dictionary methods**: `.keys()`, `.values()`, `.items()`, `.get()`
- **Sorting**: `.sort()` (modifies list) vs `sorted()` (returns new list)
- **Linear search**: Check one by one
- **Binary search**: Only on sorted arrays (if-else to halve search space)
- **Monty Hall Problem**: Always switch! (2/3 probability)
- **Rock-Paper-Scissors**: Game logic with conditions

### 💻 Code + Examples

```python
# Dictionary
d = {"name": "Pradip", "age": 20}
print(d["name"])    # Pradip
print(d.get("name")) # Pradip (safer)
for key in d:
    print(key, d[key])

# Sorting
arr = [3, 1, 2]
arr.sort()          # [1, 2, 3] (modifies)
new = sorted(arr)   # [1, 2, 3] (returns new)

# Linear search
def linear_search(arr, x):
    for i in arr:
        if i == x:
            return True
    return False

# Monty Hall probability
# Always switch → 2/3 chance to win
# Stay → 1/3 chance to win

# Rock-Paper-Scissors
def rps(p1, p2):
    if p1 == p2:
        return "Draw"
    elif (p1 == "rock" and p2 == "scissors"):
        return "P1 wins"
    elif (p1 == "scissors" and p2 == "paper"):
        return "P1 wins"
    elif (p1 == "paper" and p2 == "rock"):
        return "P1 wins"
    else:
        return "P2 wins"
```

### 🔥 NPTEL Exam Tricks

- **Dictionary access**: Use `.get(key)` to avoid KeyError
- **Sort vs sorted**: Know the difference for output questions
- **Binary search**: Only works on sorted data
- **Monty Hall**: ALWAYS switch (2/3 vs 1/3)
- **Dictionary loop**: `for k in d` iterates over keys

### ⚠️ Common Mistakes

- ❌ Accessing missing dictionary key (use `.get()`)
- ❌ Assuming binary search on unsorted array
- ❌ Thinking Monty Hall = 50-50
- ❌ Wrong RPS logic (all cases needed)

### 🎯 Important Patterns

- Dictionary iteration and key checking
- Sorting decision: sort vs sorted
- Probability with Monty Hall concept

---

## 🔷 WEEK 6: RECURSION, TIC-TAC-TOE, CIPHER

### 📌 Concepts

- **Recursion**: Function calling itself with smaller problem
- **Base condition**: Must stop recursion (else infinite loop)
- **In-place reversal**: Swap elements from start and end, shrink inward
- **Tic-tac-toe logic**: Check rows, columns, diagonals for winner
- **Substitution cipher**: Map characters (encrypt/decrypt)

### 💻 Code + Examples

```python
# Recursion: Reverse list in-place
def reverse_list(lst, start, end):
    if start >= end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start+1, end-1)

a = [1, 2, 3, 4]
reverse_list(a, 0, len(a)-1)
print(a)  # [4, 3, 2, 1]

# Recursion: Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Tic-tac-toe winner check
def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Substitution cipher
mapping = {'a': 'd', 'b': 'e', 'c': 'f'}
def encrypt(text, mapping):
    return ''.join(mapping.get(ch, ch) for ch in text)
```

### 🔥 NPTEL Exam Tricks

- **Recursion output prediction**: Trace calls on paper
- **Base condition placement**: Usually `if start >= end` for two-pointer problems
- **Tic-tac-toe**: Check all 8 conditions (3 rows + 3 cols + 2 diagonals)
- **Stack depth**: Recursion uses O(n) space

### ⚠️ Common Mistakes

- ❌ Missing base condition → infinite recursion
- ❌ Wrong base condition (`>` vs `>=`)
- ❌ Forgetting to update indices
- ❌ Incomplete win check in tic-tac-toe

### 🎯 Important Patterns

- Recursion: Break problem, add base case, return result
- In-place swap: `a[i], a[j] = a[j], a[i]`
- Game logic: Check all winning conditions

---

## 🔷 WEEK 7: TUPLES, SETS, DICTIONARIES (ADVANCED), FILE HANDLING

### 📌 Concepts

- **Tuple**: Immutable collection (faster, safer for fixed data)
- **Set**: Unordered, unique values only (no duplicates)
- **Dictionary with complex values**: Dict of lists, dict of tuples
- **File operations**: `open()`, `read()`, `write()`, `readlines()`, `close()`

### 💻 Code + Examples

```python
# Tuple (immutable)
t = (1, 2, 3)
print(t[1])      # 2
# t[0] = 10      # ❌ ERROR

# Set (unique, unordered)
s = {1, 2, 2, 3}
print(s)         # {1, 2, 3}  (duplicates removed)
print(len(s))    # 3

# Dict with list values
students = {
    "A": ["Python", "C"],
    "B": ["Java"]
}
print(students["A"][0])  # Python

# File handling
# Writing
f = open("file.txt", "w")
f.write("Hello\n")
f.write("World")
f.close()

# Reading
f = open("file.txt", "r")
content = f.read()  # entire file as string
f.close()

# Readlines
f = open("file.txt", "r")
lines = f.readlines()  # list of lines
f.close()

# Snakes & Ladders logic
pos = 0
board = {3: 10, 5: 8}  # ladder/snake mapping
for dice_roll in [1, 2, 1]:
    pos += dice_roll
    if pos in board:
        pos = board[pos]
print(pos)
```

### 🔥 NPTEL Exam Tricks

- **Tuple vs List**: Use tuple when data shouldn't change
- **Set automatically removes duplicates**: `{1,1,1}` → `{1}`
- **Set is unordered**: Don't rely on order
- **File must close**: Use `f.close()` after operations
- **readlines() returns list**: Not string

### ⚠️ Common Mistakes

- ❌ Trying to modify tuple
- ❌ Assuming set is ordered
- ❌ Using True/1 as different keys (they're equal!)
- ❌ Forgetting `f.close()`
- ❌ Confusing `read()` and `readlines()`

### 🎯 Important Patterns

- Tuple: Use for immutable data
- Set: Use for uniqueness checks
- Dictionary: Key-value pairs for mapping
- File: Write, close, then read

---

## 🔷 WEEK 8: PROBABILITY, STRINGS, SIMULATION

### 📌 Concepts

- **Lottery simulation**: Random events, probability analysis
- **Probability**: Win chance = 1/n, lose chance = (n-1)/n
- **String isomorphic**: Two strings with consistent mapping
- **Anagrams**: Same characters, different order
- **Sentiment analysis**: Count positive/negative words
- **Image processing basics**: Pixels as (R,G,B) tuples

### 💻 Code + Examples

```python
# Lottery simulation
import random
account = 1000
for day in range(30):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    if x == y:
        account += 900
    else:
        account -= 100
print(account)

# Isomorphic strings
def isomorphic(s, t):
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        if s[i] in s_map and s_map[s[i]] != t[i]:
            return False
        if t[i] in t_map and t_map[t[i]] != s[i]:
            return False
        s_map[s[i]] = t[i]
        t_map[t[i]] = s[i]
    return True

# Anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Sentiment (simple)
pos = ["good", "happy"]
neg = ["bad", "sad"]
score = 0
for word in text.split():
    if word in pos: score += 1
    elif word in neg: score -= 1
print("Positive" if score > 0 else "Negative")
```

### 🔥 NPTEL Exam Tricks

- **Lottery:** Expected loss due to probability (9 losses vs 1 win)
- **Isomorphic:** Need TWO dictionaries (no two-to-one mapping)
- **Anagrams:** Use `sorted()` for comparison
- **Sentiment:** Use full text, not individual tokens
- **Random.randint(a,b):** Includes both a and b

### ⚠️ Common Mistakes

- ❌ Using single dictionary for isomorphic check
- ❌ Forgetting case sensitivity in anagrams
- ❌ Token-level sentiment (ignores context)
- ❌ Wrong probability calculation

### 🎯 Important Patterns

- Simulation for probability understanding
- Dictionary mapping for pattern matching
- `sorted()` for comparison of collections

---

## 🔷 WEEK 9: TEXT PROCESSING, NLP, GRAPHS

### 📌 Concepts

- **Text preprocessing**: Lowercase, tokenize, remove stopwords/punctuation
- **Word analysis**: Length distribution, frequency
- **Sentiment analysis**: Use TextBlob for polarity (-1 to +1)
- **Graph basics**: Nodes (entities) + Edges (connections)
- **Shortest path**: Minimum steps between two nodes (NetworkX)
- **Six degrees of separation**: Any two people ~6 steps apart

### 💻 Code + Examples

```python
# Text preprocessing
text = "Liberty liberty the Constitution"
words = text.lower().split()
words = [w for w in words if w.isalpha()]
stopwords = ["the", "is", "and"]
words = [w for w in words if w not in stopwords]
print(words)  # ['liberty', 'liberty', 'constitution']

# Word length analysis
lengths = [len(word) for word in words]

# Sentiment using TextBlob
from textblob import TextBlob
blob = TextBlob(text)
polarity = blob.sentiment.polarity  # -1 to +1

# Graph with NetworkX
import networkx as nx
G = nx.read_edgelist("file.txt")
print(len(G.nodes()))  # number of nodes

# Shortest path
path_length = nx.shortest_path_length(G, u, v)

# Monte Carlo (estimate area)
# Random points in square, count inside circle
import random
points_inside = 0
for _ in range(1000):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if x*x + y*y <= 1:
        points_inside += 1
area = (points_inside / 1000) * 4
```

### 🔥 NPTEL Exam Tricks

- **`.isalpha()`**: Returns True only for pure letters (no numbers/punctuation)
- **Stopwords**: Remove high-frequency, low-meaning words
- **TextBlob**: Full text needed for accurate sentiment (not tokens)
- **Graph shortest path**: Only between different nodes (u ≠ v)
- **Six degrees**: Exponential growth of connections

### ⚠️ Common Mistakes

- ❌ Forgetting `.isalpha()` removes "hello!"
- ❌ Not removing stopwords → skewed frequency
- ❌ Token-level sentiment instead of full text
- ❌ Shortest path to same node

### 🎯 Important Patterns

- Text cleaning pipeline: lowercase → tokenize → filter → remove stopwords
- Graph analysis: nodes, edges, shortest path
- Monte Carlo: Random sampling for approximation

---

## 🔷 WEEK 10: FLAMES, COMPRESSION

### 📌 Concepts

- **FLAMES**: Relationship prediction using name matching
  - Remove common characters between names
  - Count remaining letters
  - Eliminate cyclically from FLAMES: F(1), L(2), A(3), M(4), E(5), S(6)
  - Last remaining = result
- **Data compression**: Run-length encoding (RLE)
- **String manipulation**: Pattern recognition, grouping

### 💻 Code + Examples

```python
# FLAMES game
def flames(name1, name2):
    # Remove common characters
    for ch in name1:
        if ch in name2:
            name1 = name1.replace(ch, '', 1)
            name2 = name2.replace(ch, '', 1)

    count = len(name1) + len(name2)

    # Elimination
    flames_list = ['F', 'L', 'A', 'M', 'E', 'S']
    idx = 0
    while len(flames_list) > 1:
        idx = (idx + count - 1) % len(flames_list)
        flames_list.pop(idx)

    return flames_list[0]

# Run-length encoding
def encode(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

# Decode
def decode(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i].isalpha():
            count = int(s[i+1])
            result += s[i] * count
            i += 2
        else:
            i += 1
    return result

# Example
encode("AAABB")  # "A3B2"
decode("A3B2")   # "AAABB"
```

### 🔥 NPTEL Exam Tricks

- **FLAMES elimination**: Count from current position, move in circle
- **Circular logic**: Use `(idx + count - 1) % len(list)`
- **Compression**: Always check last character after loop
- **Encoding output**: Character + count (e.g., "A3B2")

### ⚠️ Common Mistakes

- ❌ Wrong elimination direction in FLAMES
- ❌ Forgetting last character in compression
- ❌ Off-by-one in circular counting
- ❌ Incorrect loop restart position

### 🎯 Important Patterns

- FLAMES: Circular elimination (modulo arithmetic)
- Compression: Group consecutive characters
- String traversal: One-pass algorithm

---

## 🔷 WEEK 11: CALENDAR LOGIC

### 📌 Concepts

- **Day of week**: 0=Sun, 1=Mon, ..., 6=Sat
- **Day shift per year**: Normal year +1, Leap year +2
- **Leap year rules**:
  - If `year % 400 == 0` → Leap
  - Else if `year % 100 == 0` → Not leap
  - Else if `year % 4 == 0` → Leap
  - Else → Not leap
- **Calendar formula**: `(base_day + year_shift + month_shift + date) % 7`

### 💻 Code + Examples

```python
# Leap year check
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# Days in month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Find day of week
def day_of_date(year, month, date):
    # Base: 1 Jan 2000 = Saturday (6)
    base_day = 6

    # Count years from 2000
    leap_count = sum(1 for y in range(2000, year) if is_leap(y))
    normal_count = (year - 2000) - leap_count
    year_shift = (normal_count + leap_count * 2) % 7

    # Days till this month
    month_shift = sum(days_in_month[:month-1])
    if month > 2 and is_leap(year):
        month_shift += 1  # Feb has 29 days in leap year

    # Final calculation
    total = (base_day + year_shift + month_shift + date) % 7
    return ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][total]

# Day after N days
new_day = (current_day + n) % 7
```

### 🔥 NPTEL Exam Tricks

- **Always use % 7**: Prevents overflow
- **Leap year century rule**: 2000 is leap, 1900 is NOT
- **Month days by memory**: 31-day months are 1,3,5,7,8,10,12
- **Feb handling**: 28 normally, 29 in leap years

### ⚠️ Common Mistakes

- ❌ Forgetting leap year adds +2 (not +1)
- ❌ Wrong century rule (1900 is NOT leap)
- ❌ Not using % 7
- ❌ Off-by-one in month calculation

### 🎯 Important Patterns

- Calendar math: Always modulo 7
- Leap year: Remember 1900 ≠ leap, 2000 = leap
- Date arithmetic: Add days, take mod 7

---

## 🔷 WEEK 12: PAGERANK, COLLATZ

### 📌 Concepts

- **PageRank**: Google's algorithm to rank web pages
  - Rank depends on incoming links
  - Higher quality links → higher rank
  - Formula: PR(A) = Σ(PR(B) / OutDegree(B))
- **Iterative process**: Update ranks repeatedly until convergence
- **Outgoing links**: Divide rank equally among them
- **Collatz conjecture**: If n even → n/2, if odd → 3n+1, repeat until 1

### 💻 Code + Examples

```python
# PageRank calculation
# Initial: all pages rank = 1
# Iteration: PR(A) = sum of (rank/outgoing) from all sources

# Example:
# A → B, C (2 outgoing)
# B → C (1 outgoing)
# C → A (1 outgoing)

# Iteration 1:
# A receives from C: 1/1 = 1
# B receives from A: 1/2 = 0.5
# C receives from A: 1/2 + from B: 1 = 1.5

# Key point: Use previous iteration values
# Create table:
# | Iter | A | B | C |
# |------|---|---|---|
# | 0 | 1 | 1 | 1 |
# | 1 | 1 | 0.5 | 1.5 |
# | 2 | 1.5 | 0.5 | 1 |

# Collatz sequence
def collatz(n):
    steps = 0
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        steps += 1
        sequence.append(n)
    return steps, sequence

# Example
steps, seq = collatz(6)
# steps = 8, seq = [6, 3, 10, 5, 16, 8, 4, 2, 1]
```

### 🔥 NPTEL Exam Tricks

- **PageRank**: Divide rank by OUTGOING links, not incoming
- **Incoming links matter**: They contribute to your rank
- **Iteration table**: Always fill with previous values (don't update in-place)
- **Collatz convergence**: Always stops at 1 (assumed)
- **Count iterations**: Loop until n==1, count steps

### ⚠️ Common Mistakes

- ❌ Using current iteration values instead of previous
- ❌ Dividing by incoming instead of outgoing links
- ❌ Forgetting node with no outgoing links
- ❌ Collatz: Wrong odd formula (should be 3n+1)
- ❌ Off-by-one in step counting

### 🎯 Important Patterns

- PageRank: Iteration table with two rows (current vs previous)
- Graph analysis: Track incoming and outgoing
- Collatz: Simple simulation with loop counting

---

---

# 🌟 PART 2: CORE TOPICS MERGED VIEW

## 🎯 FUNDAMENTAL CONCEPTS

### 💡 Data Types

```
int       → 5, -10, 0
float     → 3.5, -2.1, 0.0
string    → "hello", 'world'
bool      → True, False
list      → [1,2,3], ["a","b"]
tuple     → (1,2,3), ("x", "y")
dict      → {"key": "value"}
set       → {1,2,3} (unique only)
```

### 🔄 Control Flow

```
if condition:
    do something
elif other_condition:
    do other
else:
    do default

for i in range(n):
    repeat n times

while condition:
    repeat while true

# Use break to exit, continue to skip
```

### 📚 Collections

| Type  | Mutable | Ordered | Unique  | Use Case                     |
| ----- | ------- | ------- | ------- | ---------------------------- |
| List  | ✅      | ✅      | ❌      | Ordered data, modifications  |
| Tuple | ❌      | ✅      | ❌      | Fixed data, function returns |
| Set   | ✅      | ❌      | ✅      | Uniqueness, fast lookup      |
| Dict  | ✅      | ✅      | ✅ keys | Key-value mapping            |

### 🔍 Key Operations

- **List**: `append()`, `remove()`, `pop()`, slicing
- **Tuple**: indexing only (immutable)
- **Set**: `add()`, `remove()`, `&` (intersection), `|` (union)
- **Dict**: `keys()`, `values()`, `items()`, `.get()`

---

## 🎮 ALGORITHMS & LOGIC

### ✍️ Loops (Core Pattern)

```python
# Count-based loop
for i in range(n):
    # Do n times

# Collection loop
for item in collection:
    # Process each

# While loop (condition-based)
while condition:
    # Repeat

# Nested loops (cartesian product)
for i in range(n):
    for j in range(m):
        # n × m iterations
```

### 🔀 Nested Structures

```python
# Nested loops output
for i in range(2):           # i: 0, 1
    for j in range(2):       # j: 0, 1
        print(i, j)          # 4 outputs total

# Nested lists
matrix = [[1,2], [3,4]]
matrix[0][1]  # 2

# Nested dictionaries
d = {"A": {"x": 1}}
d["A"]["x"]  # 1
```

### 📋 Sorting & Searching

```python
# Sorting
arr.sort()           # O(n log n), modifies
sorted(arr)          # O(n log n), new list

# Linear search
for item in arr:     # O(n)
    if item == target: found

# Binary search (only sorted)
left, right = 0, len(arr)-1
while left <= right:  # O(log n)
    mid = (left + right) // 2
```

### 🧮 String Algorithms

```python
# Reverse
s[::-1]

# Remove characters
s.replace("a", "")

# Filter
[ch for ch in s if ch.isalpha()]

# Frequency count
from collections import Counter
Counter(s)
```

### 📊 Mathematical Concepts

| Concept          | Formula                | Example                    |
| ---------------- | ---------------------- | -------------------------- |
| **Factorial**    | n! = n×(n-1)×...×1     | 5! = 120                   |
| **Sum of N**     | Σ = n(n+1)/2           | Sum of 1-100 = 5050        |
| **Magic Square** | Sum = n(n²+1)/2        | n=3 → sum=15               |
| **Permutations** | n!                     | 3 letters → 6 permutations |
| **Probability**  | P(A) = favorable/total | Coin: 1/2                  |
| **Complement**   | P(A') = 1 - P(A)       | P(NOT heads) = 1/2         |

---

---

# ⚡ PART 3: OUTPUT SOLVING STRATEGY (QUICK HACKS)

## 🚀 Fast Prediction Techniques

### 1️⃣ **Loop Tracing** (Most Common)

```python
for i in range(3):
    print(i+1)
# Output: 1, 2, 3

for i in range(2):
    for j in range(2):
        print(i*j)
# Output: 0, 0, 0, 1
```

**Hack**: Write loop variable values on paper, fill in order

### 2️⃣ **List Slicing** (High Probability)

```python
a = [1,2,3,4,5]
print(a[1:4])    # [2,3,4]      (1 to 3, 4 excluded)
print(a[::2])    # [1,3,5]      (every 2nd)
print(a[::-1])   # [5,4,3,2,1]  (reverse)
```

**Hack**: Remember `end is excluded`, count on fingers

### 3️⃣ **String Operations** (Common)

```python
"hello".isalpha()        # True
"hello123".isalpha()     # False
"hello!".isalpha()       # False
"Hello".lower()          # "hello"
"hello".upper()          # "HELLO"
```

**Hack**: `.isalpha()` removes numbers AND punctuation

### 4️⃣ **Dictionary/Set Operations** (Moderate)

```python
d = {True: "a", 1: "b"}
print(d)              # {True: 'b'}  (True == 1)

s = {1,1,1,2,3}
print(len(s))         # 3 (duplicates removed)
```

**Hack**: Duplicate keys overwrite, `True == 1`

### 5️⃣ **Condition Tracing** (Important)

```python
if x > 5:
    print("A")
elif x > 2:
    print("B")
else:
    print("C")

# For x=3: prints "B"
# For x=6: prints "A"
# For x=1: prints "C"
```

**Hack**: Follow if-elif-else in order, FIRST match wins

### 6️⃣ **Recursion Output** (Tricky)

```python
def f(n):
    if n == 0: return
    print(n)
    f(n-1)

f(3)  # Output: 3, 2, 1
```

**Hack**: Trace calls on paper, follow stack order

### 7️⃣ **Modulo Operations** (Calendar, FLAMES)

```python
print(15 % 7)         # 1
print((0 + 365) % 7)  # 1 (day shifts by 1)
print((6 + 10) % 7)   # 2
```

**Hack**: `a % b` gives remainder, wraps around

### 8️⃣ **Type Conversions** (Gotchas)

```python
int("10")     # 10 (string to int)
str(10)       # "10" (int to string)
int("10.5")   # ERROR (can't convert float-string directly)
int(float("10.5"))  # 10 (via float first)
```

**Hack**: Know conversion rules, errors are common

---

## 📊 Output Prediction Checklist

1. Read code **line by line**
2. Track **variable changes**
3. Follow **control flow** (if-else, loops)
4. Watch for **edge cases** (empty list, None, etc.)
5. Remember **order of operations** (multiplication before addition)

---

---

# 💾 PART 4: FORMULA + LOGIC CHEATSHEET

## 🧮 Mathematical Formulas

### Arithmetic

```
Sum of 1 to N:        S = N(N+1)/2
Sum of AP:            S = (first + last) × count / 2
Average:              avg = sum / count
```

### Geometry (Calendar)

```
Day after N days:       (day + N) % 7
Year shift:             (normal_years + 2×leap_years) % 7
```

### Magic Square

```
Magic Sum:            M = N(N² + 1) / 2
Example (3×3):        M = 3(9+1)/2 = 15
```

### Probability

```
P(event) = favorable outcomes / total outcomes
P(A AND B) = P(A) × P(B)
P(A OR B) = P(A) + P(B) - P(A AND B)
P(NOT A) = 1 - P(A)

Birthday Paradox:     With 23 people, ~50% chance 2 share birthday
                      (Use complement: 1 - P(all different))
```

### Collatz

```
If n even:  n = n / 2
If n odd:   n = 3n + 1
Continue until n = 1
```

### PageRank

```
PR(A) = Σ (PR(B) / OutDegree(B))
        for all B linking to A
```

### Leap Year

```
if year % 400 == 0:     LEAP
elif year % 100 == 0:   NOT LEAP
elif year % 4 == 0:     LEAP
else:                   NOT LEAP
```

---

## 🔑 Key Logic Patterns

### Pattern 1: Remove Duplicates

```python
# Using set
unique = set(lst)

# Using list comprehension
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
```

### Pattern 2: Frequency Count

```python
from collections import Counter
freq = Counter(lst)

# Or manually
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
```

### Pattern 3: Find Common Elements

```python
# Using set intersection
common = set1 & set2

# Or loop
common = []
for item in set1:
    if item in set2:
        common.append(item)
```

### Pattern 4: Circular Indexing (FLAMES)

```python
current_idx = (current_idx + count - 1) % len(list)
```

### Pattern 5: Two-Pointer Swapping (Reverse)

```python
left, right = 0, len(lst) - 1
while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
```

### Pattern 6: String Mapping Check (Isomorphic)

```python
s_map = {}
t_map = {}
for i in range(len(s)):
    if s[i] not in s_map:
        s_map[s[i]] = t[i]
    elif s_map[s[i]] != t[i]:
        return False
    # Similar for t_map
```

### Pattern 7: Simulation (Lottery, Collatz)

```python
for iteration in range(trials):
    # Simulate one trial
    # Track results
# Analyze aggregate results
```

---

---

# 🎯 PART 5: ASSIGNMENT INSIGHTS (HIGH-PROBABILITY QUESTIONS)

## 📍 Most Repeated Question Types

### **Type 1: Output Prediction** (35-40% of exam)

- **Loops with variable tracking**: "What will this print?"
- **List slicing**: Common slicing combinations
- **Dictionary operations**: Key access, iteration
- **Nested loops**: Cartesian product outputs
- **Recursion traces**: Step-by-step call tracking

**To Practice**: Go through all Notes.md files, find output questions marked with 👉

### **Type 2: Logic Filling** (25-30% of exam)

- **Complete the code**: Missing lines, conditions, loops
- **Bug fixing**: Identify and correct errors
- **Algorithm implementation**: Write for given problem
- **Pattern continuation**: FizzBuzz, compression, encryption

**Pattern**: If question shows partial code, complete logically

### **Type 3: Concept MCQs** (20-25% of exam)

- **Why questions**: "Why use set instead of list?"
- **Which is correct**: "Which loop is valid?"
- **Purpose**: "What does this function do?"
- **Edge cases**: "What happens when N=0?"

**To Master**: Review common mistakes section of each week

### **Type 4: Complex Problems** (10-15% of exam)

- **Multi-step logic**: FLAMES, PageRank, Calendar
- **Data processing**: Text cleaning, compression
- **Game logic**: Tic-tac-toe, RPS
- **Mathematical puzzles**: Birthday paradox, magic square

**Strategy**: Break into steps, solve each part

---

## 🔥 Assignment Patterns (Week-wise PYQs)

### Week 1-2: Basics

- Print and input
- Simple loops
- Basic conditions
- Discount calculations

### Week 3-4: Collections & Logic

- List slicing
- FizzBuzz
- Set operations
- Magic square basics

### Week 5: Sorting & Dictionaries

- Sort vs sorted
- Dictionary iteration
- Binary search idea
- Monty Hall probability

### Week 6: Recursion & Games

- Reverse in-place
- Tic-tac-toe winner check
- Cipher mapping

### Week 7: Advanced Collections

- Tuple immutability
- Set uniqueness
- File I/O operations
- Snakes & ladders

### Week 8: Strings & Simulation

- Isomorphic strings
- Anagrams
- Sentiment analysis
- Lottery simulation

### Week 9: NLP & Graphs

- Text preprocessing
- `.isalpha()` usage
- Graph shortest path
- Word frequency

### Week 10: FLAMES & Compression

- **FLAMES elimination** (HIGH PROBABILITY!)
- Run-length encoding
- String grouping

### Week 11: Calendar

- **Day of week calculation** (HIGH PROBABILITY!)
- Leap year checks
- Date arithmetic

### Week 12: PageRank & Collatz

- **PageRank iteration** (HIGH PROBABILITY!)
- **Collatz sequence** (HIGH PROBABILITY!)
- Graph analysis

---

## 🔴 RED-FLAG Questions (Most Common in Exams)

1. **FLAMES elimination** → Practice circular counting
2. **PageRank iteration** → Use table format
3. **Collatz steps** → Count iterations carefully
4. **List slicing** → Remember end is excluded
5. **FizzBuzz order** → Check 3&&5 first
6. **Dictionary key collision** → True == 1
7. **Recursion base case** → Missing returns infinite loop
8. **Monty Hall** → ALWAYS switch (2/3)
9. **Leap year century rule** → 1900 ≠ leap, 2000 = leap
10. **`.isalpha()`** → Removes numbers AND punctuation

---

---

# 📄 PART 6: FINAL REVISION SHEET (1-2 Pages)

## ⏱️ ULTRA-QUICK REVISION (Study 10 minutes before exam)

### 🟦 WEEK 1-3: FUNDAMENTALS

```
Variable:       x = 5
Input:          int(input("msg"))
Loop:           for i in range(n):  print(i)
List:           [1,2,3]
Indexing:       a[0], a[-1]
Slicing:        a[1:4:2]   (start:end:step, end excluded)
Append/Pop:     a.append(x), a.pop()
```

### 🟦 WEEK 4-5: LOGIC & COLLECTIONS

```
Set:            {1,2,3}  (unique only)
Dict:           {"key": value}
Sorting:        arr.sort() / sorted(arr)
Magic Sum:      n(n²+1)/2
Monty Hall:     SWITCH = 2/3, STAY = 1/3
```

### 🟦 WEEK 6-7: RECURSION & STRUCTURES

```
Recursion:      Base case REQUIRED!
Swap:           a[i],a[j] = a[j],a[i]
Tuple:          (1,2,3) IMMUTABLE
Tic-tac-toe:    Check 3 rows + 3 cols + 2 diags
File:           open(), read(), write(), close()
```

### 🟦 WEEK 8-9: STRINGS & NLP

```
String:         .lower(), .isalpha(), .split()
Sentiment:      TextBlob(-1 to +1) on FULL text
Graph node:     Entity
Graph edge:     Connection
Shortest path:  Min steps between nodes
```

### 🟦 WEEK 10-11: FLAMES & CALENDAR

```
FLAMES:         Remove common → count → eliminate circularly
                Use: (idx + count - 1) % len
RLE:            A4B2C1 (group+count)
Day shift:      Normal +1, Leap +2
Leap year:      If %400: yes. If %100: no. If %4: yes. Else: no.
```

### 🟦 WEEK 12: PAGERANK & COLLATZ

```
PageRank:       PR(A) = Σ(PR(B)/OutDegree(B))
                Divide by OUTGOING, get from INCOMING
Collatz:        Even: n/2, Odd: 3n+1, repeat till 1
Iteration:      Always use PREVIOUS values (not current)
```

---

### 🔴 CRITICAL TRAPS

```
❌ Slicing end is EXCLUDED
❌ remove() = value, pop() = index
❌ .isalpha() removes numbers AND punctuation
❌ FizzBuzz: Check 3&&5 FIRST
❌ Monty Hall: 2/3 not 50-50
❌ True == 1 in dictionaries
❌ Set is UNORDERED
❌ Leap: 1900 NO, 2000 YES
❌ PageRank: Divide by OUTGOING links
❌ FLAMES: Circular counting from next position
```

---

### ✅ QUICK REFERENCE

| Type       | Example                     | Output  |
| ---------- | --------------------------- | ------- |
| Slice      | [1,2,3,4,5][1:4]            | [2,3,4] |
| Step slice | [1,2,3,4,5][::2]            | [1,3,5] |
| Reverse    | [1,2,3][::-1]               | [3,2,1] |
| Remove dup | {1,1,2,3}                   | {1,2,3} |
| Loop       | for i in range(3): print(i) | 0 1 2   |
| Set &      | {1,2}&{2,3}                 | {2}     |

---

## 🎯 EXAM STRATEGY

### ⏰ Time Management (3-hour exam)

- First 30 min: Do all MCQs (50% of score)
- Next 90 min: Output + logic questions
- Last 30 min: Review + difficult problems

### 🧠 Question Approach

1. Read completely before answering
2. Mark easy ones, come back to hard
3. For output questions: trace on paper
4. For logic: break into smaller parts
5. Double-check calculations (modulo, counts)

### 🎓 Scoring Tips

- **Easy points**: Output prediction (high accuracy if traced)
- **Medium points**: Logic filling (test with simple examples)
- **Hard points**: Complex multi-step problems (read twice)
- **Watch for**: Off-by-one errors, wrong operators, missing steps

---

## 💪 FINAL CONFIDENCE BOOSTS

✅ **You know**: All 12 weeks covered
✅ **You practiced**: Loop tracing multiple times
✅ **You remember**: FLAMES, PageRank, Calendar
✅ **You avoided**: Common mistakes (slicing, leap year, etc.)
✅ **You're ready**: To score 80-90% 🚀

---

### 🎓 IF YOU WANT TO SCORE 80-90%

Focus on these:

- [ ] Master loop tracing (35% of questions)
- [ ] Perfect your slicing (10% of questions)
- [ ] Lock in FLAMES, PageRank, Calendar logic (15% of questions)
- [ ] Know all common mistakes (20% safety net)
- [ ] Practice output prediction (20% practice)

**One week of focused revision = 80-90% guaranteed!**

---

---

# 🏆 FINAL WORDS

**Dear Student**,

This document contains **everything you need** to ace the NPTEL "Joy of Computing Using Python" exam. The key is:

1. **Read week-wise sections** → Understand concepts
2. **Practice output questions** → Build intuition
3. **Master 10 red-flag topics** → Secure bonus points
4. **Avoid common mistakes** → Easy marks
5. **Solve assignment patterns** → Predict exam questions

**Remember**: This course teaches **problem-solving**, not just syntax. Focus on **logic** and **how things work**, not memorization.

**Your target**: 80-90% ✅
**Your path**: Follow this document + practice problems + avoid traps

**You've got this! 💪🔥**

---

_Last updated: April 2026_
_Created for: Maximum exam readiness_
_Target audience: NPTEL Joy of Computing students_
