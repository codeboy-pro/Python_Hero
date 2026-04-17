Alright Pradip — this is exactly the kind of prep that **boosts your score fast**. I’ve designed these like an **actual NPTEL exam setter**: assignment-style, trap-based, and output-heavy 🔥

---

# 🚀 TOP 30 HIGH-PROBABILITY QUESTIONS (WEEK 12)

---

# 🟢 EASY (1–10)

---

## **Q1 (MCQ – PageRank Basic)**

If a page has 4 outgoing links and rank = 1, how much rank does each link receive?

A. 1
B. 0.5
C. 0.25
D. 4

✅ **Answer:** C
🧠 **Explanation:** Each gets (1/4 = 0.25)
🎯 **Why important:** Basic formula — always tested

---

## **Q2 (MCQ – Graph Logic)**

Which determines PageRank of a node?

A. Outgoing links
B. Incoming links
C. Total nodes
D. Self loops

✅ **Answer:** B
🧠 Incoming links give rank
🎯 Very common PYQ

---

## **Q3 (MCQ – Collatz Rule)**

If n = 7, next value is:

A. 3
B. 21
C. 22
D. 14

✅ **Answer:** C
🧠 3×7+1 = 22
🎯 Basic Collatz check

---

## **Q4 (Output – Collatz)**

```python
n = 4
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    print(n)
```

A. 2 1
B. 2 4 1
C. 2 1 0
D. 1

✅ **Answer:** A
🧠 4→2→1
🎯 Output tracing

---

## **Q5 (MCQ – Graph)**

A node with no incoming links will have:

A. Highest rank
B. Zero contribution
C. Infinite rank
D. Same rank

✅ **Answer:** B
🎯 Trap question

---

## **Q6 (MCQ – Iteration)**

Initial PageRank values are:

A. 0
B. 1
C. Random
D. Infinite

✅ **Answer:** B
🎯 Always assumed = 1

---

## **Q7 (Output)**

```python
n = 3
print(3*n+1)
```

A. 9
B. 10
C. 8
D. 7

✅ B
🎯 Basic Collatz logic

---

## **Q8 (MCQ)**

PageRank is calculated:

A. Once
B. Iteratively
C. Randomly
D. Recursively

✅ B
🎯 Core concept

---

## **Q9 (MCQ)**

A → B means:

A. B gives rank to A
B. A gives rank to B
C. Both
D. None

✅ B
🎯 Direction trap

---

## **Q10 (Output)**

```python
n = 6
print(n//2)
```

A. 2
B. 3
C. 4
D. 5

✅ B
🎯 Even case

---

# 🟡 MEDIUM (11–20)

---

## **Q11 (PageRank – 1 Iteration)**

Graph: A → B, C

Initial ranks: 1

Rank of B after 1 iteration?

A. 1
B. 0.5
C. 2
D. 0

✅ B
🧠 A splits into 2
🎯 Assignment style

---

## **Q12 (PageRank)**

Graph: A → B, B → C

Rank of C?

A. 1
B. 0.5
C. From B
D. 0

✅ C
🎯 Flow concept

---

## **Q13 (MSQ – Graph)** ⚠️

Correct statements:

A. Incoming links increase rank
B. Outgoing links divide rank
C. Rank depends on nodes count
D. Iteration required

✅ A, B, D
🎯 MSQ common

---

## **Q14 (Output – Collatz steps)**

n = 3 → steps?

A. 5
B. 6
C. 7
D. 8

✅ C
🧠 Sequence length
🎯 Very common

---

## **Q15 (Iteration Table)**

After 2 iterations rank changes:

A. Same
B. Random
C. Depends on graph
D. Always decreases

✅ C
🎯 Concept check

---

## **Q16 (Output)**

```python
n=5
count=0
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    count+=1
print(count)
```

A. 4
B. 5
C. 6
D. 7

✅ B
🎯 Classic

---

## **Q17 (Graph)**

Outdegree of node A with 3 edges:

A. 1
B. 2
C. 3
D. 0

✅ C
🎯 Basic

---

## **Q18 (PageRank)**

If no outgoing links:

A. Rank lost
B. Rank stays
C. Infinite
D. Zero

✅ A
🎯 Trick

---

## **Q19 (MSQ)** ⚠️

Convergence means:

A. Values stabilize
B. Values oscillate
C. Stop changing
D. Become zero

✅ A, C
🎯 Important

---

## **Q20 (Output)**

```python
n=2
print(3*n+1)
```

A. 7
B. 5
C. 6
D. 4

✅ A

---

# 🔴 HARD (21–30) 🔥🔥🔥

---

## **Q21 (PageRank Iteration)**

Graph:
A → B, C
B → C
C → A

Initial: 1

Rank of C after 1 iteration?

A. 1
B. 1.5
C. 2
D. 0.5

✅ B
🧠 A gives 0.5 + B gives 1
🎯 VERY IMPORTANT

---

## **Q22 (2 Iterations)**

Same graph — rank of A after 2 iterations?

A. 1
B. 1.5
C. 0.5
D. 2

✅ B
🎯 Iteration trap

---

## **Q23 (MSQ)** ⚠️

Which affect PageRank?

A. Incoming links
B. Outgoing links
C. Iterations
D. Node color

✅ A, B, C

---

## **Q24 (Output)**

```python
n=7
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
print(n)
```

A. 7
B. 1
C. 0
D. Infinite

✅ B

---

## **Q25 (Logic)**

Which node gets highest rank?

Graph:
A → B
C → B

A. A
B. B
C. C
D. Equal

✅ B
🎯 Multiple incoming

---

## **Q26 (Trap)**

Updating ranks using current iteration gives:

A. Correct
B. Wrong
C. Same
D. Faster

✅ B
🎯 BIG mistake

---

## **Q27 (Output)**

```python
n=1
while n!=1:
    n=3*n+1
print(n)
```

A. Infinite
B. 1
C. Error
D. 0

✅ B
🎯 Loop skip

---

## **Q28 (Collatz Max Value)**

Which grows fastest?

A. 2
B. 3
C. 4
D. 8

✅ B
🎯 Odd expands

---

## **Q29 (Iteration Stability)**

After many iterations:

A. Random
B. Stable
C. Infinite
D. Zero

✅ B

---

## **Q30 (Complex Output)**

n = 6 → max value reached?

A. 6
B. 8
C. 10
D. 16

✅ D
🧠 Sequence peak
🎯 Advanced

---

# 📌 FINAL SECTION

---

## 🔥 TOP 7 MOST REPEATED TYPES

1. PageRank 1 iteration
2. PageRank 2 iteration
3. Highest rank node
4. Collatz steps count
5. Collatz sequence output
6. MSQ on graph logic
7. Output tracing loops

---

## 💀 COMMON MISTAKES

### PageRank:

❌ Forget dividing by outgoing
❌ Using updated values in same iteration
❌ Ignoring incoming links

### Collatz:

❌ Wrong odd formula
❌ Missing step count
❌ Infinite loop confusion

---

## ⚡ LAST MINUTE STRATEGY

👉 Do THIS:

* Solve 2 PageRank problems
* Practice 5 Collatz outputs
* Revise formulas

👉 Focus on:

* Iteration tables
* Output tracing

---

# 🎯 FINAL PUSH

If you master:

✅ PageRank iterations
✅ Output tracing
✅ Collatz logic

👉 **80–90% is absolutely achievable**

---

If you want next level:
🔥 I can give you **“exact exam-level mock test (same difficulty as NPTEL)”**
or
🔥 **Full assignment solution breakdown step-by-step**

Just say 👍
