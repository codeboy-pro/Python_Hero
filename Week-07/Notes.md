Alright Pradip — this is your **full power-packed Week 7 notes** 💥
Made exactly the way NPTEL exams test you: **simple + logic-heavy + assignment-focused**

---

# 📚 WEEK 7 – COMPLETE NOTES (EXAM READY)

---

# 🔥 SECTION 1: TUPLES (VERY IMPORTANT)

## ✅ What is a Tuple?

* A **tuple** is a collection of elements (like list)
* Written using `()`

```python
t = (1, 2, 3)
```

---

## ✅ Key Properties

* ✅ Ordered
* ✅ Immutable (cannot change)
* ✅ Allows duplicates

---

## ❗ Immutability (VERY IMPORTANT)

```python
t = (1, 2, 3)
t[0] = 10   # ❌ ERROR
```

👉 Error: `'tuple' object does not support item assignment`

### 🔥 Why?

* Tuple is stored in **fixed memory**
* Python prevents modification → safer & faster

---

## ✅ Indexing

```python
t = (10, 20, 30)
print(t[1])   # 20
```

---

## 🔁 Tuple vs List

| Feature | Tuple  | List   |
| ------- | ------ | ------ |
| Mutable | ❌ No  | ✅ Yes |
| Speed   | Faster | Slower |
| Syntax  | ()     | []     |

---

## ⚠️ Common Errors

```python
t = (1, 2, 3)
t.append(4)   # ❌ No append in tuple
```

---

## 🧠 EXAM QUESTIONS

### MCQ

* Tuple is:

  * a) Mutable ❌
  * b) Immutable ✅

### Output

```python
t = (1, 2, 3)
print(t[2])
```

👉 Output: `3`

---

# 🔥 SECTION 2: SETS

## ✅ What is a Set?

```python
s = {1, 2, 3}
```

---

## ✅ Properties

* ❌ Unordered
* ❌ No duplicates
* ✅ Mutable

---

## 🔥 Why duplicates disappear?

```python
s = {1, 2, 2, 3}
print(s)
```

👉 Output: `{1, 2, 3}`

👉 Because sets store **unique values only**

---

## 🔥 Why order changes?

```python
s = {10, 1, 5}
print(s)
```

👉 Output may be: `{1, 10, 5}` or any order

👉 Because **set uses hashing (no index)**

---

## ✅ Operations

```python
s.add(4)
s.remove(2)
```

---

## 🧠 EXAM QUESTIONS

### MCQ

* Set is:

  * a) Ordered ❌
  * b) Unordered ✅

---

### Output

```python
s = {1, 1, 2, 3}
print(len(s))
```

👉 Output: `3`

---

# 🔥 SECTION 3: DICTIONARY + LIST (VERY IMPORTANT)

## ✅ Dictionary Basics

```python
d = {"a": 1, "b": 2}
```

* Key → Value mapping

---

## 🔥 Dictionary with List

```python
d = {
    "Pradip": ["Python", "Math"],
    "Rahul": ["AI"]
}
```

---

## 🔥 Dictionary with Tuple

```python
d = {
    "A": (1, 2),
    "B": (3, 4)
}
```

---

## 📘 Assignment Logic: Student Mapping

```python
students = {
    "A": ["Python", "C"],
    "B": ["Java"]
}

print(students["A"])
```

👉 Output: `['Python', 'C']`

---

## 📘 Attendance Tracking

```python
attendance = {}

attendance["Mon"] = ["A", "B"]
attendance["Tue"] = ["A"]

print(attendance)
```

---

## ⚠️ Common Mistakes

```python
d = {1: "a", True: "b"}
print(d)
```

👉 Output: `{1: 'b'}`
👉 Because `1 == True`

---

## 🧠 EXAM QUESTIONS

### Output

```python
d = {"x": 1}
d["x"] = 5
print(d)
```

👉 Output: `{'x': 5}`

---

# 🔥 SECTION 4: FILE HANDLING (VERY IMPORTANT)

## ✅ Writing to File

```python
f = open("file.txt", "w")
f.write("Hello")
f.close()
```

---

## ✅ Reading File

```python
f = open("file.txt", "r")
print(f.read())
```

---

## ✅ readlines()

```python
f.readlines()
```

👉 Returns list of lines

---

## 🔥 Memory vs File

| Memory             | File      |
| ------------------ | --------- |
| Temporary          | Permanent |
| Lost after program | Stored    |

---

## ❗ Important Concept

👉 After writing → data stored in file
👉 Not lost like variables

---

## 🧠 EXAM QUESTIONS

### MCQ

* `readlines()` returns:

  * a) String ❌
  * b) List ✅

---

# 🔥 SECTION 5: LOGIC PROBLEMS

---

## 🐍 Snakes & Ladders Logic

### Steps:

1. Start at 0
2. Roll dice (1–6)
3. Add to position
4. If ladder → go up
5. If snake → go down

```python
pos += dice

if pos in ladder:
    pos = ladder[pos]
```

---

## 🌀 Spiral Traversal

### Matrix Example:

```
1 2 3
4 5 6
7 8 9
```

👉 Output:
`1 2 3 6 9 8 7 4 5`

### Logic:

* Top row
* Right column
* Bottom row
* Left column

---

## 📍 GPS Tracking

### Concept:

* Start at (0,0)
* Move using directions

```python
x, y = 0, 0

if move == "U":
    y += 1
```

---

## 🧠 EXAM QUESTIONS

### Output

```python
x, y = 0, 0
moves = "UURD"

# Final position?
```

👉 Answer: `(1,1)`

---

# 💀 COMMON MISTAKES

* ❌ Modifying tuple
* ❌ Assuming set is ordered
* ❌ Confusing dict vs list
* ❌ Forgetting file close

---

# 🧪 PRACTICE SECTION

## 🔹 Data Structure (10)

1. Tuple vs list
2. Set duplicate behavior
3. Dict key uniqueness
4. Tuple indexing
5. Set add/remove
6. Dict update
7. Nested dict
8. List inside dict
9. Tuple inside dict
10. Key overwrite logic

---

## 🔹 Output (10)

1.

```python
print((1,2)+(3,))
```

2.

```python
print({1,2,2})
```

3.

```python
d={True:1,1:2}
print(d)
```

... (continue similar pattern)

---

## 🔹 File Handling (5)

1. Difference `r` vs `w`
2. Output of `readlines()`
3. Write then read
4. File overwrite
5. Append mode

---

## 🔹 Logic (5)

1. Snake ladder move
2. Spiral print
3. GPS final position
4. Matrix boundary
5. Path tracking

---

# 📌 FINAL SECTION

---

## 🎯 TOP 20 IMPORTANT QUESTIONS

1. Why tuple immutable?
2. Set vs list
3. Dict key uniqueness
4. readlines() output
5. Snake ladder logic
6. Spiral traversal steps
7. GPS movement
8. Tuple indexing
9. Dict overwrite
10. Set duplicate removal
11. File write effect
12. Memory vs file
13. Nested dict
14. List vs tuple speed
15. Set unordered reason
16. Key collision (True vs 1)
17. Spiral dry run
18. Position tracking
19. Dict with list
20. Output tracing

---

## 🔁 MOST REPEATED PATTERNS

* Output prediction
* Dictionary overwriting
* Set uniqueness
* Tuple immutability
* File read/write behavior

---

## ⚡ LAST MINUTE CHEAT SHEET

* Tuple → immutable
* Set → no duplicates + unordered
* Dict → key unique
* File → permanent storage
* Spiral → boundary traversal
* Snake ladder → condition jump
* GPS → coordinate update

---

# 🎯 FINAL RESULT

After this, you should be able to:

✅ Solve assignment easily
✅ Crack output questions
✅ Handle logic problems
✅ Score **80–90% easily**

---

If you want next level prep 🔥
I can give you:

* 💯 **Top 30 expected MCQs (exact exam level)**
* 🧠 **Hard tricky questions**
* ⚔️ **Full mock test (like NPTEL)**

Just tell me 👍
