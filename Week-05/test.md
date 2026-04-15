Alright Pradip 😎 — this is **exactly what NPTEL loves to ask**.
I’ve designed these **Top 30 questions** to feel like *assignment + PYQ + tricky twists*.

---

# 🧠 TOP 30 MOST EXPECTED QUESTIONS — WEEK 5

---

# 🟢 EASY (1–10)

---

### **Q1. (Dictionary Basics)**

```python
d = {"a":1, "b":2, "a":3}
print(d["a"])
```

A. 1
B. 2
C. 3
D. Error

✅ **Answer:** C
💡 **Explanation:** Duplicate key → last value kept
🎯 **Why important:** VERY common trap

---

### **Q2.**

Which is a valid dictionary key?

A. List
B. String
C. Dictionary
D. Set

✅ **Answer:** B
💡 Keys must be immutable
🎯 Basic concept

---

### **Q3.**

```python
d = {"x":10}
print(d.get("y"))
```

A. Error
B. None
C. 0
D. "y"

✅ **Answer:** B
💡 `.get()` avoids error
🎯 VERY IMPORTANT

---

### **Q4.**

Binary search works on:

A. Any list
B. Sorted list
C. Unsorted list
D. Dictionary

✅ **Answer:** B
🎯 Classic MCQ

---

### **Q5.**

Monty Hall best strategy?

A. Stay
B. Switch
C. Random
D. None

✅ **Answer:** B
🎯 Repeated PYQ

---

### **Q6.**

```python
arr = [3,1,2]
arr.sort()
print(arr)
```

A. [3,1,2]
B. [1,2,3]
C. None
D. Error

✅ **Answer:** B
🎯 Sorting basic

---

### **Q7.**

Linear search checks:

A. Half elements
B. One by one
C. Random
D. Sorted only

✅ **Answer:** B

---

### **Q8.**

```python
d = {}
d["a"] = 5
print(len(d))
```

A. 0
B. 1
C. Error
D. None

✅ **Answer:** B

---

### **Q9.**

Rock vs Scissors winner?

A. Rock
B. Scissors
C. Draw
D. None

✅ **Answer:** A

---

### **Q10.**

```python
d = {"a":1,"b":2}
d.clear()
print(d)
```

A. {}
B. None
C. Error
D. {"a":1}

✅ **Answer:** A

---

# 🟡 MEDIUM (11–20)

---

### **Q11.**

```python
d = {"a":1,"b":2}
d["b"] = 5
print(d)
```

A. {"a":1,"b":2}
B. {"a":1,"b":5}
C. Error
D. None

✅ B
💡 Value updated

---

### **Q12.**

```python
d = {"a":1,"b":2}
print("a" in d)
```

A. True
B. False
C. Error
D. None

✅ A
🎯 Key check

---

### **Q13. (Bubble Sort Pass)**

Array: `[3,2,1]` after 1st pass?

A. [3,2,1]
B. [2,1,3]
C. [1,2,3]
D. [2,3,1]

✅ B
💡 Largest moves to end

---

### **Q14.**

```python
d = {"a":1}
d.pop("a")
print(d)
```

A. {"a":1}
B. {}
C. Error
D. None

✅ B

---

### **Q15.**

Binary search middle index formula?

A. (l+r)//2
B. l+r
C. l*r
D. l-r

✅ A

---

### **Q16.**

Monty Hall probability after switching?

A. 1/2
B. 1/3
C. 2/3
D. 3/2

✅ C

---

### **Q17.**

```python
arr = [5,4,3]
print(sorted(arr))
print(arr)
```

A. [3,4,5] and [5,4,3]
B. [3,4,5] and [3,4,5]
C. Error
D. None

✅ A
🎯 sorted vs sort

---

### **Q18.**

Rock vs Paper?

A. Rock
B. Paper
C. Draw
D. None

✅ B

---

### **Q19.**

```python
d = {"x":1}
print(d["y"])
```

A. None
B. Error
C. 0
D. "y"

✅ B

---

### **Q20.**

Number of comparisons in linear search (worst case)?

A. 1
B. n
C. log n
D. n/2

✅ B

---

# 🔴 HARD (21–30) 🔥🔥🔥

---

### **Q21. (Tricky Dictionary)**

```python
d = {1:"a", True:"b"}
print(d)
```

A. {1:"a", True:"b" }
B. {1:"b"}
C. Error
D. {}

✅ B
💡 True == 1

🎯 VERY IMPORTANT TRAP

---

### **Q22. (Bubble Sort Steps)**

Array: `[4,3,2,1]` after 2 passes?

A. [3,2,1,4]
B. [2,1,3,4]
C. [1,2,3,4]
D. [3,1,2,4]

✅ B

---

### **Q23. (MSQ ⚠️ Binary Search Conditions)**

Which are required?

A. Sorted list
B. Random access
C. Unique elements
D. Divide into halves

✅ A, B, D

---

### **Q24.**

```python
d = {"a":1,"b":2}
for k,v in d.items():
    print(v)
```

Output?

A. a b
B. 1 2
C. a 1
D. Error

✅ B

---

### **Q25. (Monty Hall Logic)**

Why switching works?

A. Random chance
B. Host gives info
C. Equal probability
D. No logic

✅ B

---

### **Q26. (RPS Logic Trap)**

If both choose same?

A. Player1 wins
B. Player2 wins
C. Draw

D. Error

✅ C

---

### **Q27. (Search Trap)**

Binary search on unsorted list:

A. Works
B. Gives correct result
C. Wrong result
D. Error always

✅ C

---

### **Q28. (Dictionary Loop Output)**

```python
d = {"a":1,"b":2}
for i in d:
    print(i)
```

A. 1 2
B. a b
C. (a,1)
D. Error

✅ B

---

### **Q29. (Bubble Sort Swaps)**

Max swaps in worst case (n elements)?

A. n
B. n²
C. n(n-1)/2
D. log n

✅ C

---

### **Q30. (Mixed Logic)**

```python
arr = [2,1]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
```

A. [2,1]
B. [1,2]
C. Error
D. None

✅ B

🎯 Bubble sort core logic

---

# 🔁 TOP 7 MOST REPEATED QUESTION TYPES

1. Dictionary duplicate key behavior 🔥
2. `.get()` vs direct access
3. Bubble sort pass output 🔥🔥
4. sorted() vs sort()
5. Binary search condition trap
6. Monty Hall probability
7. Loop output on dictionary

---

# ⚠️ MOST COMMON MISTAKES

### Dictionaries

* Thinking duplicate keys allowed ❌
* Using list as key ❌
* Confusing `.get()` vs `[]`

---

### Sorting

* Forgetting passes
* Not tracking swaps
* Confusing sorted vs sort

---

### Logic

* Monty Hall = 50% ❌
* Missing RPS conditions

---

# ⚡ LAST MINUTE REVISION STRATEGY

⏱️ **1–2 Hours Plan**

### Step 1 (30 min)

* Revise dictionary methods
* Practice 5 output questions

### Step 2 (40 min)

* Practice bubble sort step tracing
* Solve 5 sorting questions

### Step 3 (20 min)

* Monty Hall concept
* RPS logic

### Step 4 (10 min)

* Revise formulas & traps

---

# 🎯 FINAL TALK (IMPORTANT)

If you:

* Master **dictionary outputs**
* Practice **bubble sort steps**
* Remember **binary search conditions**
* Lock **Monty Hall logic**

👉 You’re easily in **80–90% range** 💯

---

If you want next level 🔥
I can give:
👉 **Full mock test (same as NPTEL interface)**
👉 OR **Top 50 ultra-tricky questions (rank booster)**
