Alright Pradip 😎 — this is your **EXAM-HIT LIST 🔥**.
These are crafted *exactly like NPTEL style*: tricky, output-heavy, and assignment-inspired.

---

# 🎯 TOP 30 MOST EXPECTED QUESTIONS (WEEK 3)

---

# 🟢 EASY (1–10)

---

### **Q1. (MCQ)**

```python
a = [10, 20, 30]
print(a[-1])
```

A. 10
B. 20
C. 30
D. Error

✅ **Answer:** C
🧠 **Explanation:** `-1` → last element
🎯 **Why Important:** Negative indexing = very common

---

### **Q2. (MCQ)**

```python
a = [1,2,3]
a.append(4)
print(a)
```

A. [1,2,3]
B. [1,2,3,4]
C. Error
D. None

✅ B
🧠 append adds at end
🎯 Basic list operation

---

### **Q3. (MCQ)**

```python
a = [1,2,3]
a.pop()
print(a)
```

A. [1,2]
B. [2,3]
C. [1,2,3]
D. Error

✅ A
🧠 pop removes last
🎯 Very repeated

---

### **Q4. (MCQ)**

```python
a = [1,2,3]
print(len(a))
```

A. 2
B. 3
C. 1
D. Error

✅ B
🎯 Basic but appears often

---

### **Q5. (MCQ)**

```python
print([1,2] * 2)
```

A. [2,4]
B. [1,2,1,2]
C. Error
D. [1,2,2]

✅ B
🎯 Trick: not multiplication

---

### **Q6. (MCQ)**

```python
a = [1,2,3]
print(a[1:3])
```

A. [2,3]
B. [1,2]
C. [2]
D. Error

✅ A
🎯 Slicing basics

---

### **Q7. (MCQ)**

```python
for i in range(3):
    print(i)
```

A. 1 2 3
B. 0 1 2
C. 0 1 2 3
D. Error

✅ B
🎯 range confusion

---

### **Q8. (MCQ)**

```python
a = [1,2,3]
a.remove(2)
print(a)
```

A. [1,3]
B. [2,3]
C. Error
D. [1,2]

✅ A
🎯 remove vs pop

---

### **Q9. (MCQ)**

```python
print(5 % 2)
```

A. 2
B. 1
C. 0
D. Error

✅ B
🎯 FizzBuzz base

---

### **Q10. (MCQ)**

```python
a = [1,2,3]
print(a[::-1])
```

A. [3,2,1]
B. [1,2,3]
C. Error
D. [2,1]

✅ A
🎯 Reverse slicing 🔥

---

# 🟡 MEDIUM (11–20)

---

### **Q11. (Output)**

```python
a = [1,2,3,4]
print(a[-3:-1])
```

A. [2,3]
B. [1,2]
C. [3,4]
D. Error

✅ A
🎯 Negative slicing trap

---

### **Q12. (Output)**


```python
a = [1,2,3]
a.append([4,5])
print(len(a))
```

A. 4
B. 5
C. 3
D. Error

✅ A
🧠 Nested list added as ONE element
🎯 VERY IMPORTANT 🔥

---

### **Q13. (Output)**

```python
a = [1,2,3]
print(a[::2])
```

A. [1,3]
B. [2]
C. [1,2]
D. Error

✅ A
🎯 Step slicing

---

### **Q14. (Output)**

```python
for i in range(2):
    for j in range(2):
        print(i+j)
```

A. 0 1 1 2
B. 1 2 3
C. 0 1 2
D. Error

✅ A
🎯 Nested loop output

---

### **Q15. (MCQ)**

Which removes element at index 1?

A. remove(1)
B. pop(1)
C. delete(1)
D. append(1)

✅ B
🎯 Classic confusion

---

### **Q16. (Output)**

```python
a = [1,2,2,3]
a.remove(2)
print(a)
```

A. [1,3]
B. [1,2,3]
C. [1,2,2]
D. Error

✅ B
🎯 Only first removed

---

### **Q17. (Output)**

```python
a = [1,2,3]
print(a + [4])
```

A. [1,2,3,4]
B. Error
C. [4,1,2,3]
D. [1,2,3]

✅ A
🎯 List concat

---

### **Q18. (Logic)**

FizzBuzz prints:

A. Only multiples of 3
B. Only multiples of 5
C. Multiples of both 3 and 5
D. All numbers

✅ C
🎯 Concept check

---

### **Q19. (Output)**

```python
for i in range(3):
    i = 10
    print(i)
```

A. 0 1 2
B. 10 10 10
C. Error
D. Infinite loop

✅ B
🎯 Loop variable overwritten inside

---

### **Q20. (Logic)**

Permutation of 3 letters:

A. 3
B. 6
C. 9
D. 1

✅ B
🎯 n! concept

---

# 🔴 HARD (21–30) 🔥🔥🔥

---

### **Q21. (Output)**

```python
a = [1,2,3,4,5]
print(a[1:5:2])
```

A. [2,4]
B. [1,3,5]
C. [2,3,4]
D. Error

✅ A
🎯 Step slicing mastery

---

### **Q22. (Output)**

```python
a = [1,2,3]
b = a
b.append(4)
print(a)
```

A. [1,2,3]
B. [1,2,3,4]
C. Error
D. None

✅ B
🎯 Reference concept 🔥

---

### **Q23. (Output)**

```python
a = [1,2,3]
print(a.pop(1))
```

A. 1
B. 2
C. 3
D. Error

✅ B
🎯 pop returns value

---

### **Q24. (Output)**

```python
a = [1,2,3,4]
print(a[-1:-4:-1])
```

A. [4,3,2]
B. [1,2,3]
C. [4,3]
D. Error

✅ A
🎯 Reverse slicing tricky 🔥

---

### **Q25. (Output)**

```python
a = [1,2]
for i in a:
    a.append(i)
    if len(a) > 4:
        break
print(a)
```

A. [1,2,1,2,1]
B. Infinite
C. [1,2,1,2]
D. Error

✅ A
🎯 Modifying list while iterating

---

### **Q26. (Logic)**

Second smallest in `[5,2,8,2,1]`:

A. 1
B. 2
C. 5
D. 8

✅ B
🎯 Assignment-type 🔥

---

### **Q27. (Output)**

```python
a = [1,2,3]
print(a * 0)
```

A. []
B. [0]
C. Error
D. [1,2,3]

✅ A
🎯 Edge case

---

### **Q28. (Output)**

```python
a = [1,2,3]
print(a[::-2])
```

A. [3,1]
B. [1,3]
C. [2]
D. Error

✅ A
🎯 Advanced slicing

---

### **Q29. (Logic)**

Crowd computing works best when:

A. All guesses same
B. Average of guesses taken
C. Only largest taken
D. Only smallest taken

✅ B
🎯 Conceptual

---

### **Q30. (Output)**

```python
count = 0
for i in range(3):
    for j in range(3):
        count += 1
print(count)
```

A. 3
B. 6
C. 9
D. 12

✅ C
🎯 Nested loop counting 🔥🔥

---

# 📊 FINAL SECTION

---

## 🔥 TOP 7 REPEATED QUESTION TYPES

1. List slicing outputs
2. append vs remove vs pop
3. Nested loop output
4. FizzBuzz logic
5. Negative indexing
6. List reference behavior
7. Step slicing (`[::-1]`, `[::2]`)

---

## ❌ COMMON MISTAKES

* Confusing `remove()` vs `pop()`
* Wrong slicing end index
* Ignoring loop iterations count
* Wrong FizzBuzz condition order
* Thinking `*` multiplies elements
* Not understanding references (`b = a`)

---

## ⚡ LAST MINUTE STRATEGY

👉 Do this before exam:

✅ Solve **15 output questions**
✅ Revise **all slicing patterns**
✅ Practice **2 nested loop problems**
✅ Remember:

* `a[::-1]` → reverse
* `pop()` vs `remove()`
* FizzBuzz order matters

---

# 🎯 FINAL TRUTH

If you master:

* **Slicing 🔥**
* **Nested loops 🔥**
* **List operations 🔥**

👉 You will easily hit **80–90%**.

---

If you want next level 🚀
I can give:
👉 “Most Expected 15 EXACT Assignment-Type Questions (with solutions)”
👉 OR rapid mock test (timed)

Just say 👍
