Alright Pradip — this is exactly what an NPTEL setter would prepare 🔥
These are **high-probability, assignment-style, trap-heavy questions** for Week 7.

I’ve carefully balanced:

* ✅ Concepts
* ✅ Output traps
* ✅ Logic
* ✅ PYQ patterns

---

# 🟢 EASY LEVEL (1–10)

---

## Q1. (Tuple Immutability)

```python
t = (1, 2, 3)
t[1] = 5
```

**What happens?**

A. (1,5,3)
B. Error
C. (1,2,3,5)
D. None

✅ **Answer:** B

💡 **Explanation:** Tuples are immutable → cannot modify
🎯 **Why important:** Most common MCQ trap

---

## Q2. (Set Duplicate Removal)

```python
s = {1, 2, 2, 3}
print(len(s))
```

A. 4
B. 3
C. 2
D. Error

✅ **Answer:** B

💡 Duplicates removed automatically
🎯 Very common output question

---

## Q3. (Dictionary Overwrite)

```python
d = {"a":1}
d["a"] = 5
print(d["a"])
```

A. 1
B. 5
C. Error
D. None

✅ **Answer:** B

💡 Key gets overwritten
🎯 Assignment-style pattern

---

## Q4. (File readlines)

```python
f = open("a.txt","w")
f.write("Hi\nHello")
f.close()

f = open("a.txt","r")
print(len(f.readlines()))
```

A. 1
B. 2
C. 8
D. Error

✅ **Answer:** B

💡 Two lines stored
🎯 Frequently asked

---

## Q5. (Tuple Indexing)

```python
t = (10,20,30)
print(t[-1])
```

A. 10
B. 20
C. 30
D. Error

✅ **Answer:** C

💡 Negative indexing
🎯 Basic but important

---

## Q6. (Set Order)

```python
s = {5,1,3}
print(s)
```

A. {5,1,3}
B. Sorted order
C. Random order
D. Error

✅ **Answer:** C

💡 Unordered
🎯 Classic trap

---

## Q7. (Dictionary Key Type)

```python
d = {1:"a", True:"b"}
print(d)
```

A. {1:"a",True:"b"}
B. {1:"b"}
C. Error
D. {True:"a"}

✅ **Answer:** B

💡 1 == True
🎯 HIGHLY repeated

---

## Q8. (File Write Behavior)

```python
f = open("a.txt","w")
f.write("Hello")
f.write("World")
f.close()
```

Content?

A. Hello World
B. HelloWorld
C. World
D. Error

✅ **Answer:** B

💡 No space automatically
🎯 Common mistake

---

## Q9. (GPS Basic Move)

Start (0,0), moves = "UR"

Final?

A. (1,1)
B. (0,2)
C. (2,0)
D. (1,0)

✅ **Answer:** A

💡 U→y+1, R→x+1
🎯 Core logic

---

## Q10. (Tuple Length)

```python
t = (1,)
print(len(t))
```

A. 0
B. 1
C. Error
D. 2

✅ **Answer:** B

💡 Single element tuple
🎯 Very tricky

---

# 🟡 MEDIUM LEVEL (11–20)

---

## Q11. (Set Add)

```python
s = {1,2}
s.add(2)
print(s)
```

A. {1,2,2}
B. {1,2}
C. Error
D. None

✅ B

💡 No duplicates
🎯 Basic logic reinforcement

---

## Q12. (List in Dict)

```python
d = {"A":[1,2]}
d["A"].append(3)
print(d)
```

A. {"A":[1,2]}
B. {"A":[1,2,3]}
C. Error
D. None

✅ B

💡 Mutable inside dict
🎯 Important concept

---

## Q13. (File Append Trap)

```python
f = open("a.txt","w")
f.write("Hi")
f.close()

f = open("a.txt","a")
f.write("Hello")
f.close()
```

Content?

A. Hi
B. Hello
C. HiHello
D. Error

✅ C

💡 Append adds
🎯 Very important

---

## Q14. (Tuple Inside List)

```python
l = [(1,2),(3,4)]
l[0] = (5,6)
print(l)
```

A. Error
B. [(5,6),(3,4)]
C. [(1,2),(3,4)]
D. None

✅ B

💡 List mutable
🎯 Concept clarity

---

## Q15. (Set Remove)

```python
s = {1,2,3}
s.remove(4)
```

A. No change
B. Error
C. Removes 1
D. None

✅ B

💡 remove() error if absent
🎯 Trick question

---

## Q16. (Spiral Start)

Matrix:

```
1 2
3 4
```

Output?

A. 1 2 4 3
B. 1 3 4 2
C. 2 1 3 4
D. 1 4 2 3

✅ A

💡 Spiral logic
🎯 Important logic

---

## Q17. (GPS Path)

Moves: "UUDDLR"

Final?

A. (0,0)
B. (1,1)
C. (2,0)
D. (-1,0)

✅ A

💡 Balanced moves
🎯 Logical thinking

---

## Q18. (Dictionary Length)

```python
d = {"a":1,"b":2,"a":3}
print(len(d))
```

A. 3
B. 2
C. 1
D. Error

✅ B

💡 Duplicate keys overwrite
🎯 Classic

---

## Q19. (File Read After Write Without Close)

```python
f = open("a.txt","w")
f.write("Hi")

f = open("a.txt","r")
print(f.read())
```

A. Hi
B. Empty
C. Error
D. None

✅ B

💡 Not flushed/closed
🎯 VERY tricky

---

## Q20. (Snake Ladder Jump)

Position = 3, dice = 2, ladder at 5→10

Final?

A. 5
B. 10
C. 3
D. 7

✅ B

💡 Jump after move
🎯 Core logic

---

# 🔴 HARD LEVEL (21–30)

---

## Q21. (Tuple + List Trap)

```python
t = (1,[2,3])
t[1][0] = 5
print(t)
```

A. Error
B. (1,[5,3])
C. (1,[2,3])
D. None

✅ B

💡 Inner list mutable
🎯 VERY IMPORTANT

---

## Q22. (Set + List Conversion)

```python
s = set([1,2,2,3])
print(list(s))
```

A. [1,2,3]
B. Sorted list
C. Random order
D. Error

✅ C

💡 Order not guaranteed
🎯 Trap

---

## Q23. (Dict Nested)

```python
d = {"A":{"x":1}}
d["A"]["x"] = 5
print(d)
```

A. {"A":{"x":1}}
B. {"A":{"x":5}}
C. Error
D. None

✅ B

💡 Nested mutable
🎯 Important

---

## Q24. (File Overwrite Trap)

```python
f = open("a.txt","w")
f.write("Hello")
f.close()

f = open("a.txt","w")
f.write("Hi")
f.close()
```

Content?

A. HelloHi
B. Hi
C. Hello
D. Error

✅ B

💡 w mode overwrites
🎯 Must know

---

## Q25. (Spiral 3x3)

Output?

```
1 2 3
4 5 6
7 8 9
```

A. 1 2 3 6 9 8 7 4 5
B. 1 4 7 8 9
C. 3 2 1 4
D. None

✅ A

💡 Full spiral
🎯 High weight

---

## Q26. (GPS Complex)

Moves: "URDLUR"

Final?

A. (1,1)
B. (0,0)
C. (2,2)
D. (1,0)

✅ A

💡 Trace carefully
🎯 Exam-level

---

## Q27. (Set Intersection Logic)

```python
a={1,2,3}
b={2,3,4}
print(a & b)
```

A. {1,2,3,4}
B. {2,3}
C. {}
D. Error

✅ B

💡 Intersection
🎯 Common

---

## Q28. (Dict Key Error)

```python
d={"a":1}
print(d["b"])
```

A. None
B. Error
C. 0
D. ""

✅ B

💡 KeyError
🎯 Important

---

## Q29. (File + readlines trap)

File content:

```
Hi
Hello
```

```python
f=open("a.txt")
print(f.readlines()[0])
```

A. Hi
B. Hi\n
C. Hello
D. Error

✅ B

💡 newline included
🎯 VERY IMPORTANT

---

## Q30. (Snake Back Jump)

Position 10, snake at 10→3

Final?

A. 10
B. 3
C. 7
D. Error

✅ B

💡 Snake logic
🎯 Core

---

# 📊 FINAL SECTION

---

## 🔥 TOP 7 MOST REPEATED TYPES

1. Tuple immutability traps
2. Set duplicate removal
3. Dictionary overwrite
4. File modes (w vs a)
5. readlines() output
6. Spiral traversal order
7. GPS coordinate logic

---

## 💀 COMMON MISTAKES

* Modifying tuple ❌
* Assuming set order ❌
* Forgetting file close ❌
* Ignoring newline in file ❌
* Confusing dict key overwrite ❌

---

## ⚡ LAST MINUTE STRATEGY

👉 Revise:

* Tuple vs list
* Set properties
* Dict overwrite cases
* File modes

👉 Practice:

* Output questions (MOST IMPORTANT 🔥)
* Spiral dry run
* GPS tracing

👉 Trick:

* Always trace step-by-step
* Watch for hidden traps (True vs 1, newline, overwrite)

---

# 🎯 FINAL WORD

If you can solve these 30 comfortably →
💥 You’re already in **80–90% zone**

---

If you want next level 🔥
I can give you:

* 💣 **Most expected 15 EXACT exam questions**
* 🧪 **Full mock test (with timer)**
* 🧠 **Only tricky PYQ patterns**

Just say 👍
