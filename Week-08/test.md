Alright Pradip — this is exactly how NPTEL sets papers: **pattern-based + tricky logic + output traps**.
I’ve designed these **Top 30 questions** to mirror **assignment + PYQ style** so you’re basically practicing the *actual exam*.

---

# 🔥 TOP 30 MOST EXPECTED QUESTIONS – WEEK 8

---

# 🟢 EASY (1–10)

---

## Q1 (MCQ – Lottery Basics)

What does `random.randint(1,10)` return?

A. 1 to 9
B. 0 to 10
C. 1 to 10
D. Only integers except 10

✅ **Answer:** C
💡 **Explanation:** Includes both endpoints
🎯 **Why important:** Very common trap

---

## Q2 (MCQ – Probability)

Probability of winning lottery (1–10 range)?

A. 1/5
B. 1/10
C. 1/9
D. 1/100

✅ B
💡 One correct number out of 10
🎯 Core concept

---

## Q3 (Output)

```python
print((1,2)+(3,))
```

A. (1,2,3)
B. Error
C. (3,1,2)
D. (1,2,(3,))

✅ A
💡 Tuple concatenation
🎯 Repeated PYQ

---

## Q4 (MCQ – Tuple)

Which is a valid tuple?

A. (1)
B. (1,)
C. [1]
D. {1}

✅ B
💡 Comma required
🎯 Classic trap

---

## Q5 (MCQ – Anagram)

Which are anagrams?

A. "rat", "tar"
B. "rat", "car"
C. "rat", "artt"
D. "rat", "rat "

✅ A
💡 Same characters
🎯 Basic concept

---

## Q6 (MCQ – Sentiment)

If positive > negative → result?

A. Neutral
B. Negative
C. Positive
D. Error

✅ C
🎯 Basic scoring logic

---

## Q7 (Output)

```python
print(type((1)))
```

A. tuple
B. int
C. list
D. error

✅ B
🎯 Very common mistake

---

## Q8 (MCQ – Tuple Property)

Tuple is:

A. Mutable
B. Immutable
C. Unordered
D. Dynamic

✅ B
🎯 Core concept

---

## Q9 (MCQ – Simulation)

Why simulate many trials?

A. Faster code
B. More randomness
C. Better approximation
D. Less memory

✅ C
🎯 Important theory

---

## Q10 (Output)

```python
import random
print(random.randint(1,1))
```

A. 0
B. 1
C. Random
D. Error

✅ B
🎯 Trick question

---

# 🟡 MEDIUM (11–20)

---

## Q11 (Logic – Lottery)

Why does player lose money long-term?

A. Winning amount small
B. Losing probability higher
C. Random error
D. Code bug

✅ B
💡 9/10 loss vs 1/10 win
🎯 Core exam logic

---

## Q12 (Output)

```python
t = (1,2,3)
t[1] = 5
```

A. Works
B. Error
C. (1,5,3)
D. None

✅ B
🎯 Immutability

---

## Q13 (MSQ – Anagram Methods)

Ways to check anagram:

A. Sorting
B. Counting
C. Reverse
D. Length check

✅ A, B
🎯 Multi-select pattern

---

## Q14 (Output)

```python
print(sorted("bca"))
```

A. bca
B. abc
C. ['a','b','c']
D. ('a','b','c')

✅ C
🎯 Output format matters

---

## Q15 (Logic – Isomorphic)

Why two dictionaries used?

A. Speed
B. Memory
C. Ensure one-to-one mapping
D. Reduce code

✅ C
🎯 Most asked concept

---

## Q16 (Output)

```python
d = {}
d['a'] = 1
d['a'] = 2
print(d)
```

A. {'a':1}
B. {'a':2}
C. Error
D. None

✅ B
🎯 Key overwrite

---

## Q17 (Logic – Simulation)

Short-term result of lottery:

A. Always loss
B. Always profit
C. Random
D. Fixed

✅ C
🎯 Important concept

---

## Q18 (Output)

```python
print(len((1,)))
```

A. 0
B. 1
C. Error
D. 2

✅ B
🎯 Tuple understanding

---

## Q19 (MCQ – Sentiment)

Split string used for:

A. Sorting
B. Tokenizing words
C. Counting chars
D. Loop control

✅ B

---

## Q20 (Output)

```python
print("abc" == "cba")
```

A. True
B. False

✅ B
🎯 Anagram trap

---

# 🔴 HARD (21–30)

---

## Q21 (Lottery Code)

```python
bet = 100
account = 1000

for i in range(10):
    account -= bet

print(account)
```

Final balance?

A. 0
B. 100
C. -100
D. 900

✅ A
💡 1000 - 1000
🎯 Basic tracing

---

## Q22 (Probability Trap)

Winning chance decreases to 1/20 → result?

A. Profit increases
B. Loss increases
C. No change
D. Equal

✅ B
🎯 Important reasoning

---

## Q23 (Isomorphic – Output)

```python
s="foo"
t="bar"
```

Result?

A. True
B. False

✅ B
🎯 Mapping conflict

---

## Q24 (Isomorphic Edge Case)

```python
s="ab"
t="aa"
```

A. True
B. False

✅ B
💡 Many-to-one mapping invalid

---

## Q25 (Output)

```python
from collections import Counter
print(Counter("aab") == Counter("aba"))
```

A. True
B. False

✅ A
🎯 Frequency logic

---

## Q26 (Lottery Reasoning)

Graph of account vs days:

A. Increasing
B. Decreasing
C. Constant
D. Random spikes but downward

✅ D
🎯 Real exam concept

---

## Q27 (MSQ – Tuple)

True about tuples:

A. Ordered
B. Mutable
C. Allows duplicates
D. Faster than list

✅ A, C, D

---

## Q28 (Output)

```python
print(("a","b")*2)
```

A. ('a','b','a','b')
B. ('a','b')
C. Error
D. ['a','b','a','b']

✅ A
🎯 Tuple repetition

---

## Q29 (Sentiment Logic)

If score = 0:

A. Positive
B. Negative
C. Neutral
D. Error

✅ C

---

## Q30 (Advanced Logic – Lottery)

Why expected value may be ~0 but still loss?

A. Code issue
B. Random fluctuation
C. Frequent small losses dominate
D. Win impossible

✅ C
🎯 Deep concept (VERY IMPORTANT)

---

# 📌 TOP 7 MOST REPEATED QUESTION TYPES

1. Output of tuple operations
2. `random.randint` behavior
3. Lottery profit/loss reasoning
4. Isomorphic mapping logic
5. Anagram detection
6. Dictionary overwrite behavior
7. Simulation vs probability

---

# 💀 COMMON MISTAKES

❌ Thinking random = equal outcomes
❌ Using one dictionary in mapping
❌ Forgetting `(1,)` tuple
❌ Confusing sorted output type
❌ Ignoring edge cases in strings

---

# ⚡ LAST MINUTE REVISION STRATEGY

👉 1. Focus MOST on:

* Lottery logic (VERY IMPORTANT 🔥)
* Isomorphic strings
* Output questions

👉 2. Practice:

* 15 output questions
* 5 simulation problems

👉 3. Revise formulas:

* Probability = favorable / total
* Expected value logic

👉 4. Remember traps:

* Tuple comma
* Dict overwrite
* Two maps needed

---

# 🎯 FINAL WORD

If you master:

* **Lottery reasoning**
* **String mapping**
* **Output prediction**

👉 You are **100% ready for 80–90% score**

---

If you want next level prep:
👉 I can give you **“Exact Assignment Questions with Step-by-Step Solutions”** or
👉 **“Full Mock Test (30 questions, timed like real NPTEL exam)”**
