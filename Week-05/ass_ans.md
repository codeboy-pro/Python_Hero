Nice — you uploaded the **actual Week 5 assignment** 👍
I’ll now explain the **solutions clearly (step-by-step + logic + exam tricks)**.

---

# 🧠 WEEK 5 ASSIGNMENT SOLUTIONS (EXPLAINED)

(From your PDF: )

---

# 🔥 Q1. Nested Dictionary Access

### Code:

```python
students = {
 102: {"name":"Riya","marks":[88,92,79]}
}

print(students[102]["marks"][0])
```

## ✅ Answer: **88**

## 💡 Explanation:

* `students[102]` → gets Riya
* `"marks"` → `[88,92,79]`
* `[0]` → first element

👉 **Index starts from 0**

---

# 🔥 Q2. List inside Dictionary

### Code:

```python
student["marks"] = [70,75,80]
student["marks"].append(85)
print(len(student["marks"]))
```

## ✅ Answer: **4**

## 💡 Explanation:

* Initially → 3 elements
* After append → 4 elements

---

# 🔥 Q3. Reference Concept (VERY IMPORTANT 🔥)

### Code:

```python
data = {"nums":[1,2,3]}
ref = data["nums"]

ref.append(4)
print(data["nums"])
```

## ✅ Answer: **[1,2,3,4]**

## 💡 Explanation:

👉 `ref` and `data["nums"]` point to **same list**

⚠️ Modification affects original

---

# 🔥 Q4. Slice vs Original

### Code:

```python
student["marks"] = [10,20,30,40]
subset = student["marks"][1:2]
subset.append(99)

print(student["marks"])
```

## ✅ Answer: **[10,20,30,40]**

## 💡 Explanation:

👉 Slicing creates **new list (copy)**
👉 So original is unchanged

---

# 🔥 Q5. Function Reassignment Trap

### Code:

```python
def update(d):
    d = {"x":100}

data = {"x":10}
update(data)
print(data["x"])
```

## ✅ Answer: **10**

## 💡 Explanation:

👉 `d = {...}` creates new local object
👉 Original dictionary NOT changed

⚠️ Only mutation changes original

---

# 🔥 Q6. Modifying Dict During Iteration

### Code:

```python
for k in data.keys():
    data["c"] = 3
```

## ✅ Answer: **Runtime Error**

## 💡 Explanation:

👉 Cannot change dictionary size while iterating

---

# 🔥 Q7. Fair Comparison (Average)

Students:

* Ayaan → [70,80,90] → avg = 80
* Riya → [85,90] → avg = 87.5
* Kabir → [60,65,70,75] → avg = 67.5

## ✅ Answer: **Riya**

## 💡 Explanation:

👉 Fair comparison = **average**, not sum

---

# 🔥 Q8. Highest Test (Column-wise)

Marks:

```
Test1: 50,60,70 → avg=60  
Test2: 60,70,80 → avg=70  
Test3: 70,80,90 → avg=80
```

## ✅ Answer: **Test 3**

---

# 🔥 Q9. Pass vs Fail

Condition: pass ≥ 60

Marks:

* 45 ❌
* 75 ✅
* 65 ✅
* 55 ❌
* 85 ✅

👉 Pass = 3, Fail = 2

## ✅ Answer: **Pass section**

---

# 🔥 Q10. Cumulative Trend

Data:

```
[10,20] → [30] → [40,50]
```

👉 Values increasing

## ✅ Answer: **Increasing trend**

---

# 🔥 Q11. Linear Search Iterations

Given:

* List size = 10
* Target at index 6

## ✅ Answer: **7**

## 💡 Explanation:

👉 Checks from index 0 → 6
👉 Total = 7 checks

---

# 🔥 Q12. Why Binary Search Faster?

## ✅ Answer:

**Loop runs fewer times due to index jumps**

## 💡 Explanation:

👉 Each step removes half

---

# 🔥 Q13. Missing Element Case

## ✅ Answer:

**Linear search will check all elements**

---

# 🔥 Q14. Binary Search Growth

## ✅ Answer:

**Slowly rising curve**

## 💡 Explanation:

👉 log(n) growth

---

# 🔥 Q15. Binary Search on Unsorted

## ✅ Answer:

**Element may not be found even if present**

---

# 🧠 MOST IMPORTANT CONCEPTS FROM ASSIGNMENT

---

## 🔥 1. Reference vs Copy (VERY IMPORTANT)

* Direct assignment → same object
* Slice → new object

---

## 🔥 2. Mutation vs Reassignment

* Mutation → affects original
* Reassignment → does NOT

---

## 🔥 3. Dictionary Iteration Rule

❌ Don’t modify during loop

---

## 🔥 4. Average vs Sum

👉 Always use **average for fairness**

---

## 🔥 5. Linear vs Binary Search

| Feature    | Linear   | Binary      |
| ---------- | -------- | ----------- |
| Works on   | Any list | Sorted only |
| Speed      | Slow     | Fast        |
| Iterations | n        | log n       |

---

# ⚠️ COMMON TRAPS FROM THIS ASSIGNMENT

1. Reference confusion
2. Slice vs original
3. Reassignment vs mutation
4. Binary search on unsorted
5. Iteration count (off-by-one error)

---

# 🎯 FINAL ADVICE (VERY IMPORTANT)

This assignment shows:
👉 NPTEL LOVES:

* Output-based questions
* Reference/memory logic
* Search iteration counting
* Dictionary structure

---

If you want next level 🔥
I can:
👉 Solve **Programming Assignments 1–3**
👉 OR give **exact same pattern mock test (100% exam-like)**
