Alright Pradip, let’s turn Week 2 into something you can _actually understand + revise fast before exam_. I’ll keep it simple, structured, and exam-focused — like a smart friend explaining things before your test 😄

---

# 🧠 WEEK 2 NOTES — _Joy of Computing using Python_

---

# 1. 🐍 Introduction to Anaconda

### ✅ What is Anaconda?

- A **Python distribution** used for:
  - Data science
  - Easy package management

- Comes with:
  - Python
  - Libraries (NumPy, Pandas, etc.)
  - Tools like **Spyder**

### 🔑 Important Keyword:

👉 _Distribution_ = pre-installed tools + libraries

---

### ❓ Exam Questions

**MCQ:**

- Anaconda is mainly used for:
  - a) Gaming ❌
  - b) Data Science ✅

**Tricky:**

- Does Anaconda replace Python? ❌ (It includes Python)

---

# 2. ⚙️ Installation of Anaconda

### Steps:

1. Download from official site
2. Install (Next → Next → Install)
3. Open **Anaconda Navigator**

### ⚠️ Common Mistakes:

- Not adding to PATH (optional)
- Installing multiple Python versions (confusion)

---

### ❓ Exam Questions

- Which tool opens Spyder?
  - a) CMD ❌
  - b) Anaconda Navigator ✅

---

# 3. 🧪 Introduction to Spyder IDE

### ✅ What is Spyder?

- Python IDE (like Turbo C for Python 😄)
- Sections:
  - Editor
  - Console
  - Variable Explorer

---

### ❓ Exam Questions

**Output-based:**

```python
print("Hello")
```

👉 Output: `Hello`

---

# 4. 🖨️ Printing Statements

### ✅ Syntax:

```python
print("Hello World")
```

### Examples:

```python
print("Pradip")
print(10)
print("Sum =", 5+3)
```

### ⚠️ Mistakes:

- Missing quotes → error
- Using `Print` instead of `print`

---

### ❓ Exam Questions

**MCQ:**

- Correct syntax:
  - a) print Hello ❌
  - b) print("Hello") ✅

**Output:**

```python
print("5+3")
```

👉 Output: `5+3` (not 8)

---

# 5. 📦 Variables in Python

### ✅ Concept:

- Variable = container to store data

### Syntax:

```python
x = 10
name = "Pradip"
```

### Rules:

- No space: ❌ `my name`
- Can start with letter or `_`

---

### Example:

```python
a = 5
b = 3
print(a+b)
```

---

### ⚠️ Mistakes:

- Using keyword: `if = 5` ❌
- Case-sensitive: `A ≠ a`

---

### ❓ Exam Questions

**MCQ:**

- Valid variable?
  - a) 1a ❌
  - b) a1 ✅

---

# 6. ▶️ Sequence of Instructions

### ✅ Concept:

- Python executes **line by line (top to bottom)**

### Example:

```python
a = 5
b = 2
print(a+b)
```

👉 Output: `7`

---

### ❓ Tricky:

```python
a = 5
print(a)
a = 10
```

👉 Output: `5`

---

# 7. 👨‍💻 First Program

```python
print("Hello World")
```

👉 First step in programming

---

# 8. ⌨️ Taking Input

### ✅ Syntax:

```python
x = input("Enter number: ")
```

### Important:

👉 Input is **string by default**

---

### Convert:

```python
x = int(input("Enter number: "))
```

---

### Example:

```python
a = int(input())
b = int(input())
print(a+b)
```

---

### ⚠️ Mistakes:

- Forgetting `int()` → wrong output

---

### ❓ Exam Questions

**Output:**

```python
x = input()
print(x+2)
```

👉 ERROR (string + int)

---

# 9. 💸 Discount Calculation

### Example:

```python
price = int(input("Enter price: "))
discount = 10

final = price - (price * discount / 100)
print(final)
```

---

### ❓ Exam:

- What is 10% of 100?
  👉 10

---

# 10. 🤔 Motivation for if Condition

👉 Decision making

Example:

```python
if marks > 50:
    print("Pass")

```

---

# 11. 🔢 Numbers Reminder

Types:

- int → 5
- float → 5.5

---

### ❓ Tricky:

```python
print(5/2)
```

👉 2.5

```python
print(5//2) #floor value
```

👉 2

---

# 12. 🔀 If Condition

### Syntax:

```python
if condition:
    statement
```

### Example:

```python
x = 10
if x > 5:
    print("Greater")
```

---

### if-else:

```python
if x > 5:
    print("Big")
else:
    print("Small")
```

---

### ⚠️ Mistakes:

- Missing colon `:`
- Wrong indentation

---

### ❓ Exam Questions

**Output:**

```python
x = 5
if x > 10:
    print("Hi")
else:
    print("Bye")
```

👉 Bye

---

# 13. 📏 Syntax & Indentation

### VERY IMPORTANT ⚠️

- Python uses indentation instead of `{}`

```python
if True:
    print("Yes")
```

---

### ❓ Mistake:

```python
if True:
print("Hi")
```

👉 ERROR

---

# 14. 🔁 Introduction to Loops

👉 Repeat tasks

---

# 15. 🔄 For Loop

### Syntax:

```python
for i in range(n):
    print(i)
```

---

### Example:

```python
for i in range(5):
    print(i)
```

👉 0 1 2 3 4

---

# 16. ➕ Sum using Loop

```python
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i

print(sum)
```

---

# 17. 📊 Multiplication Table

```python
n = int(input())

for i in range(1, 11):
    print(n * i)
```

---

# 18. 🔄 While Loop

### Syntax:

```python
while condition:
    statement
```

---

### Example:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

### ⚠️ Mistakes:

- Infinite loop

---

# 🧪 PRACTICE SECTION

## 🔹 10 Basic Questions

1. Print your name
2. Add two numbers
3. Take input and print square
4. Check even/odd
5. Find max of two numbers
6. Print 1–10
7. Sum of first n numbers
8. Multiplication table
9. Input string and print
10. Simple discount

---

## 🔹 10 Output Questions

1.

```python
print(2+3*2)
```

👉 8

2.

```python
print("2+3")
```

👉 2+3

3.

```python
x=5
if x<3:
 print("A")
else:
 print("B")
```

👉 B

(Continue similarly… practice more)

---

## 🔹 5 Logic Problems

1. Check prime
2. Reverse number
3. Factorial
4. Sum of digits
5. Largest of 3 numbers

---

# ⭐ TOP 15 MOST IMPORTANT QUESTIONS

1. Difference between `input()` and `int(input())`
2. Output prediction
3. If-else logic
4. Loop sum
5. Multiplication table
6. Indentation error
7. Variable naming rules
8. Range function behavior
9. While loop condition
10. Integer division vs float
11. Discount calculation
12. Infinite loop case
13. Sequence execution
14. Print formatting
15. Type conversion

---

# ⚠️ COMMON ERRORS

- ❌ Missing colon `:`
- ❌ Wrong indentation
- ❌ Not converting input
- ❌ Infinite loop
- ❌ Using `=` instead of `==`

---

# 📝 1-PAGE QUICK REVISION

👉 print → output
👉 input → always string
👉 int() → conversion
👉 if → decision
👉 for → fixed loop
👉 while → condition loop
👉 indentation = must
👉 range(n) → 0 to n-1
👉 // → integer division
👉 % → remainder

---

💬 **Final Advice (friend-to-friend):**
Week 2 is _super scoring_ if you master **input + if + loops + output prediction**. Most students lose marks in silly syntax mistakes — don’t be that guy 😄

---

If you want, I can next give:
👉 **Top 30 expected MCQs from Week 2**
👉 OR a **1-hour revision plan before exam**
