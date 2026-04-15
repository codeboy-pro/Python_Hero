Alright Pradip 😏 — this is exactly the kind of prep that can push you into **80–90% zone**.
I’ve designed these like a **real NPTEL paper**: tricky, logic-heavy, and based on patterns from assignments + PYQs.

---

# 🟢 EASY (1–10)

---

### **Q1. (Magic Square Formula)**

Magic constant for a 3×3 magic square is:

A. 10
B. 12
C. 15
D. 18

✅ **Answer:** C
💡 **Explanation:** ( M = n(n^2+1)/2 = 3(9+1)/2 = 15 )
🎯 **Why important:** Direct formula question — very common

---

### **Q2. (Magic Square Validity)**

Which is a valid magic square?

A.

```
1 2 3
4 5 6
7 8 9
```

B.

```
8 1 6
3 5 7
4 9 2
```

C.

```
2 7 6
9 5 1
4 3 8
```

D. Both B and C

✅ **Answer:** D
💡 Both are valid
🎯 Pattern recognition question

---

### **Q3. (Set Logic - Dobble)**

```python
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2)
```

A. {1,2}
B. {3}
C. {4,5}
D. Error

✅ **Answer:** B
💡 Intersection
🎯 Core Dobble logic

---

### **Q4. (Duplicate Detection)**

```python
lst = [1,2,3,2]
print(len(lst) == len(set(lst)))
```

A. True
B. False

✅ **Answer:** B
💡 Duplicate exists
🎯 Very common trick

---

### **Q5. (Birthday Paradox)**

Minimum people ≈ 50% probability?

A. 10
B. 15
C. 23
D. 50

✅ **Answer:** C
💡 Famous result
🎯 Direct MCQ

---

### **Q6. (String Logic)**

```python
print("a" in "apple")
```

A. True
B. False

✅ **Answer:** A
🎯 Basic but repeated

---

### **Q7. (Loop Output)**

```python
for i in range(3):
    print(i)
```

A. 1 2 3
B. 0 1 2
C. 0 1 2 3
D. 1 2

✅ **Answer:** B
🎯 Classic trap

---

### **Q8. (Random Function)**

```python
import random
print(random.randint(1,3))
```

A. Only 1
B. 1 or 2
C. 1,2,3
D. Error

✅ **Answer:** C
🎯 Inclusive range confusion

---

### **Q9. (Matrix Row Sum)**

```python
m = [[1,2],[3,4]]
print(sum(m[0]))
```

A. 3
B. 4
C. 5
D. Error

✅ **Answer:** A
🎯 Matrix basics

---

### **Q10. (Set Length)**

```python
print(len(set([1,1,2,2,3])))
```

A. 5
B. 3
C. 2
D. 4

✅ **Answer:** B
🎯 Duplicate removal logic

---

# 🟡 MEDIUM (11–20)

---

### **Q11. (Magic Square Check)**

Which condition is NOT required?

A. Row sum equal
B. Column sum equal
C. Diagonal sum equal
D. All numbers even

✅ **Answer:** D
🎯 Trick question

---

### **Q12. (Matrix Traversal)**

```python
m = [[1,2],[3,4]]
for row in m:
    for val in row:
        print(val, end=" ")
```

Output?

A. 1 2 3 4
B. 1 3 2 4
C. 2 1 4 3
D. Error

✅ **Answer:** A
🎯 Nested loops

---

### **Q13. (Diagonal Sum)**

```python
m = [[1,2,3],[4,5,6],[7,8,9]]
print(m[0][0] + m[1][1] + m[2][2])
```

A. 12
B. 15
C. 18
D. 20

✅ **Answer:** B
🎯 Magic square logic base

---

### **Q14. (Dobble MSQ ⚠️)**

Which guarantee one common element?

A. Use sets
B. Compare lists directly
C. Use intersection
D. Sort lists

✅ **Answer:** A, C
🎯 MSQ pattern

---

### **Q15. (Birthday Logic)**

Why probability increases fast?

A. More people
B. More comparisons
C. Less days
D. Randomness

✅ **Answer:** B
💡 n(n−1)/2 pairs
🎯 Conceptual

---

### **Q16. (Flag Variable)**

```python
found = False
for i in [1,2,3]:
    if i == 2:
        found = True
print(found)
```

A. True
B. False

✅ **Answer:** A
🎯 Game logic

---

### **Q17. (String Replace Logic)**

```python
word = "hello"
print(word.replace("l","_"))
```

A. he__o
B. hel_o
C. hello
D. error

✅ **Answer:** A
🎯 Guess game logic

---

### **Q18. (Random Choice)**

```python
import random
print(random.choice([1,2,3]))
```

A. Always 1
B. 1,2,3 randomly
C. Error
D. None

✅ **Answer:** B

---

### **Q19. (Matrix Column Sum)**

```python
m = [[1,2],[3,4]]
print(m[0][1] + m[1][1])
```

A. 3
B. 5
C. 6
D. 7

✅ **Answer:** C

---

### **Q20. (Set Trick)**

```python
print({1,2,3} == {3,2,1})
```

A. True
B. False

✅ **Answer:** A
🎯 Order doesn’t matter

---

# 🔴 HARD (21–30)

---

### **Q21. (Magic Square Trap 🔥)**

```python
m = [[2,7,6],[9,5,1],[4,3,8]]
print(sum(m[0]) == sum(m[1]) == sum(m[2]))
```

A. True
B. False

✅ **Answer:** A
💡 Only row check
🎯 Missing diagonal trap

---

### **Q22. (Complete Check Logic)**

Which ensures full magic square?

A. Only rows
B. Rows + columns
C. Rows + columns + diagonals
D. Only diagonals

✅ **Answer:** C

---

### **Q23. (Birthday Simulation)**

```python
import random
lst = [random.randint(1,365) for _ in range(30)]
print(len(lst) != len(set(lst)))
```

What does True mean?

A. All unique
B. Duplicate exists
C. Error
D. Sorted

✅ **Answer:** B
🎯 Key simulation question

---

### **Q24. (Nested Loop Count)**

```python
count = 0
for i in range(3):
    for j in range(2):
        count += 1
print(count)
```

A. 3
B. 5
C. 6
D. 9

✅ **Answer:** C

---

### **Q25. (Matrix Index Trap)**

```python
m = [[1,2,3],[4,5,6]]
print(m[1][2])
```

A. 5
B. 6
C. 3
D. Error

✅ **Answer:** B

---

### **Q26. (Guess Game Logic 🔥)**

Which is correct approach?

A. Compare full string
B. Compare char by char
C. Use loop
D. Use flag

✅ **Answer:** B, C, D
🎯 MSQ tricky

---

### **Q27. (Set Intersection Trap)**

```python
print(len({1,2,3} & {4,5,6}))
```

A. 0
B. 1
C. 3
D. Error

✅ **Answer:** A

---

### **Q28. (Probability Trap)**

Probability that all birthdays are different:

A. Multiply probabilities
B. Add probabilities
C. Ignore order
D. Always 0

✅ **Answer:** A
🎯 Complement logic

---

### **Q29. (Loop Break Logic)**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

A. 0 1 2
B. 0 1 2 3
C. 1 2 3
D. 0 1

✅ **Answer:** A

---

### **Q30. (Assignment-style Logic 🔥🔥)**

Which code checks duplicate efficiently?

A.

```python
for i in lst:
    if lst.count(i) > 1:
        return True
```

B.

```python
len(lst) != len(set(lst))
```

C.

```python
sort(lst)
```

D.

```python
lst == set(lst)
```

✅ **Answer:** B
🎯 Most repeated pattern

---

# 🔁 TOP 7 REPEATED QUESTION TYPES

1. Magic square validation 🔥
2. Set intersection (Dobble) 🔥
3. Birthday paradox logic 🔥
4. Nested loop output
5. Matrix indexing
6. String pattern matching
7. Duplicate detection

---

# ❌ COMMON MISTAKES

* Forgetting diagonals (Magic Square 🚨)
* Using list instead of set
* Misunderstanding probability
* Off-by-one errors in loops
* Ignoring break/flag logic

---

# 🚀 LAST MINUTE STRATEGY

👉 Focus 2 hours:

### 1️⃣ Magic Square (30 min)

* Formula + checks

### 2️⃣ Sets + Dobble (20 min)

* Intersection logic

### 3️⃣ Birthday Paradox (30 min)

* Concept + simulation

### 4️⃣ Output Questions (40 min)

* Practice loops + matrix

---

💬 If you want next level prep:
I can take a **FULL MOCK TEST (like real NPTEL)** with timer + analysis 😈
























