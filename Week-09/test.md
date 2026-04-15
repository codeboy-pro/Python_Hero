Alright Pradip — this is **exactly how NPTEL sets papers** 🔥
I’ve designed these 30 questions to match:

* Assignment patterns ✅
* PYQ trends ✅
* Tricky output-based logic ✅

If you master these, **80–90% is very realistic**.

---

# 🟢 EASY LEVEL (1–10)

---

## **Q1. (MCQ – NLP)**

What does tokenization do?

A. Removes punctuation
B. Splits text into words
C. Converts to lowercase
D. Removes stopwords

✅ **Answer:** B
💡 **Explanation:** Tokenization = splitting text into tokens (words).
🎯 **Exam Insight:** Basic but always asked.

---

## **Q2. (MCQ – Output)**

```python
text = "Hello World"
print(text.lower())
```

A. HELLO WORLD
B. hello world
C. Hello world
D. Error

✅ **Answer:** B
💡 Converts all characters to lowercase
🎯 Common warm-up question

---

## **Q3. (MCQ – isalpha)**

What does `"abc123".isalpha()` return?

A. True
B. False
C. Error
D. None

✅ **Answer:** B
💡 Contains digits → not purely alphabetic
🎯 VERY COMMON trap

---

## **Q4. (MCQ – Stopwords)**

Why are stopwords removed?

A. Increase data size
B. Improve grammar
C. Remove meaningless words
D. Convert to lowercase

✅ **Answer:** C
🎯 Direct theory → often appears

---

## **Q5. (MCQ – Sentiment)**

Polarity range is:

A. 0 to 1
B. -1 to 1
C. 1 to 10
D. -10 to 10

✅ **Answer:** B
🎯 Very direct

---

## **Q6. (MCQ – Graph)**

In a graph:

A. Nodes = connections
B. Edges = users
C. Nodes = users
D. None

✅ **Answer:** C
🎯 Basic but important

---

## **Q7. (MCQ – Shortest Path)**

Shortest path means:

A. Longest path
B. Minimum steps between nodes
C. Number of nodes
D. Degree of node

✅ **Answer:** B

---

## **Q8. (MCQ – Six Degrees)**

Average path length is approximately:

A. 2
B. 4
C. 6
D. 10

✅ **Answer:** C

---

## **Q9. (MCQ – Monte Carlo)**

Monte Carlo method uses:

A. Sorting
B. Recursion
C. Random sampling
D. Graphs

✅ **Answer:** C

---

## **Q10. (Output)**

```python
words = ["hello", "world"]
print([len(w) for w in words])
```

A. [5, 5]
B. [10]
C. [5]
D. Error

✅ **Answer:** A
🎯 Important for stylometry

---

# 🟡 MEDIUM LEVEL (11–20)

---

## **Q11. (Output – Filtering)**

```python
words = ["Hi!", "Python", "123"]
print([w for w in words if w.isalpha()])
```

A. ['Hi!', 'Python']
B. ['Python']
C. ['Hi!']
D. []

✅ **Answer:** B
💡 "Hi!" removed due to `!`
🎯 VERY IMPORTANT pattern

---

## **Q12. (MSQ – NLP)**

Which are preprocessing steps?

A. Lowercase
B. Tokenization
C. Sorting
D. Stopword removal

✅ **Answer:** A, B, D

---

## **Q13. (Output)**

```python
text = "The cat and the dog"
words = text.lower().split()
print(words)
```

A. ['The', 'cat', 'and']
B. ['the', 'cat', 'and', 'the', 'dog']
C. ['cat', 'dog']
D. Error

✅ **Answer:** B

---

## **Q14. (Logic – Stopwords)**

If stopwords are NOT removed, what happens?

A. Better accuracy
B. Noise increases
C. No change
D. Faster execution

✅ **Answer:** B

---

## **Q15. (Output – Edge Case)**

```python
print("hello!".isalpha())
```

A. True
B. False
C. Error
D. None

✅ **Answer:** B

---

## **Q16. (Graph – Code)**

```python
import networkx as nx
G = nx.Graph()
G.add_edge("A", "B")
```

Number of nodes?

A. 1
B. 2
C. 0
D. Error

✅ **Answer:** B

---

## **Q17. (Shortest Path Logic)**

Why use `u != v`?

A. Faster code
B. Avoid self-loop
C. Remove edges
D. Increase nodes

✅ **Answer:** B

---

## **Q18. (MSQ – Sentiment)**

Which are true?

A. Polarity can be negative
B. 0 means neutral
C. Always positive
D. Range is -1 to 1

✅ **Answer:** A, B, D

---

## **Q19. (Output – Length)**

```python
words = ["a", "ab", "abc"]
print(sum(len(w) for w in words))
```

A. 3
B. 6
C. 5
D. 4

✅ **Answer:** B

---

## **Q20. (Graph Logic)**

If A connected to B, B to C → shortest path A to C:

A. 1
B. 2
C. 3
D. 0

✅ **Answer:** B

---

# 🔴 HARD LEVEL (21–30)

---

## **Q21. (Output – Combined NLP 🔥)**

```python
text = "Hello! This is AI 2025"
words = text.lower().split()
print([w for w in words if w.isalpha()])
```

A. ['hello', 'this', 'is', 'ai']
B. ['this', 'is', 'ai']
C. ['hello!', 'ai']
D. ['hello']

✅ **Answer:** B
💡 "hello!" removed, "2025" removed
🎯 VERY HIGH PROBABILITY

---

## **Q22. (MSQ – Graph)**

Which are true?

A. Graph can be directed
B. Nodes represent entities
C. Edges represent relations
D. Graph must be cyclic

✅ **Answer:** A, B, C

---

## **Q23. (Output – Trick)**

```python
words = ["Hello", "world!"]
print([w.lower() for w in words if w.isalpha()])
```

A. ['hello', 'world']
B. ['hello']
C. ['world']
D. []

✅ **Answer:** B

---

## **Q24. (Logic – Stylometry)**

Why word length used?

A. Faster code
B. Represents writing style
C. Reduces memory
D. None

✅ **Answer:** B

---

## **Q25. (Output – Graph)**

```python
G.add_edge("A", "B")
G.add_edge("B", "C")
print(nx.shortest_path_length(G, "A", "C"))
```

A. 1
B. 2
C. 3
D. 0

✅ **Answer:** B

---

## **Q26. (Monte Carlo Logic)**

Accuracy increases when:

A. Fewer points
B. More random points
C. Less computation
D. Fixed points

✅ **Answer:** B

---

## **Q27. (Output – Stopwords Logic 🔥)**

```python
stop = ["the"]
words = ["the", "cat", "the", "dog"]
print([w for w in words if w not in stop])
```

A. ['cat', 'dog']
B. ['the']
C. ['cat']
D. []

✅ **Answer:** A

---

## **Q28. (Shortest Path Trap 🔥)**

Shortest path from A to A:

A. 1
B. 0
C. Infinite
D. Error

✅ **Answer:** B

---

## **Q29. (Six Degrees Logic)**

Why small-world property exists?

A. Linear growth
B. Exponential connections
C. Random graphs
D. Cycles

✅ **Answer:** B

---

Nice — this is exactly what a smart exam setter would do 😄🔥
Let’s **fix the question properly** so it becomes valid and still tests the same concept.

---

# ✅ **Modified Q30 (Corrected Version)**

## **Q30. (Hard Output 🔥🔥🔥)**

```python
text = "AI is the future!"
words = text.lower().split()
filtered = [w for w in words if w.isalpha() and w != "the"]
print(filtered)
```

### Options:

A. `['ai', 'is']`
B. `['ai', 'future']`
C. `['ai', 'is', 'future']`
D. `['future']`

---

## ✅ **Correct Answer: A**

---

## 🧠 Explanation (Exam-level)

* `'ai'` → valid ✔
* `'is'` → valid ✔
* `'the'` → removed ❌
* `'future!'` → removed ❌ (fails `.isalpha()`)

👉 Final:

```python
['ai', 'is']
```

---


---

# 📌 TOP 7 MOST REPEATED QUESTION TYPES

1. `.isalpha()` filtering 🔥
2. Stopword removal output
3. List comprehension outputs
4. Graph shortest path
5. Word length calculation
6. Sentiment polarity
7. Edge case strings ("hello!", "123")

---

# 💀 COMMON MISTAKES

❌ Forgetting punctuation removal
❌ Assuming `"hello!"` is valid word
❌ Not removing stopwords
❌ Confusing nodes vs edges
❌ Wrong shortest path logic
❌ Using tokens for sentiment

---

# ⚡ LAST MINUTE REVISION STRATEGY

👉 1 hour plan:

**30 min:**

* Practice output questions 🔥
* `.isalpha()` + filtering

**20 min:**

* Graph + shortest path

**10 min:**

* Sentiment + Monte Carlo

---

# 🎯 FINAL ADVICE

If exam is tricky:

👉 Focus on:

* Output prediction (MOST IMPORTANT)
* Filtering logic
* Graph reasoning

---

If you want next level prep, I can:
🔥 Solve your **actual Week 9 assignment line-by-line (with tricks)**
🔥 OR give **Top 10 MOST LIKELY questions (almost guaranteed)**
