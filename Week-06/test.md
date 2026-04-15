Got it, Pradip — I carefully went through your Week 6 assignment PDF  (especially recursion + Tic Tac Toe logic), and I’ve built **TOP 30 HIGH-PROBABILITY QUESTIONS** exactly like NPTEL pattern 🔥

These are **very close to assignment style + PYQ patterns** — if you master these, **80–90% is realistic**.

---

# 🔥 TOP 30 MOST IMPORTANT QUESTIONS (WEEK 6)

---

# 🟢 EASY (1–10)

---

## 1. (MCQ – Recursion)

When does recursion stop in reverse function?

A. start == end
B. start > end
C. end == 0
D. swap == 0

✅ **Answer:** B
💡 **Explanation:** Base condition → `start > end` 
🎯 **Why:** Direct PYQ

---

## 2. (MCQ)

What does reverseArray return?

A. None
B. New list
C. Modified list
D. Last swapped value

✅ C
💡 Returns same list (in-place)
🎯 Very common trap

---

## 3. (MCQ)

What happens for odd-length list?

A. Middle removed
B. Crash
C. Middle unchanged
D. Swapped twice

✅ C 
🎯 Classic concept

---

## 4. (MCQ)

Output: reverseArray([])

A. Error
B. None
C. []
D. [0]

✅ C
🎯 Edge case

---

## 5. (MCQ)

Role of `swap` variable?

A. Controls recursion
B. Stores temp value
C. Counts depth
D. Stores result

✅ B
🎯 Important for logic clarity

---

## 6. (MCQ – Tic Tac Toe)

Initial board state?

A. Filled with X
B. Filled with O
C. Empty
D. Random

✅ C 

---

## 7. (MCQ)

Invalid input → what happens?

A. Game stops
B. Crash
C. Ask again
D. Skip turn

✅ C 

---

## 8. (MCQ)

Turn increases when?

A. Invalid input
B. Display
C. Valid move
D. Game end

✅ C 

---

## 9. (MCQ)

Game stops when?

A. 9 turns
B. Winner found
C. Invalid move
D. Always

✅ B 

---

## 10. (MCQ – Cipher)

Substitution cipher does:

A. Sorting
B. Mapping characters
C. Deleting chars
D. Encrypt numbers

✅ B

---

# 🟡 MEDIUM (11–20)

---

## 11. (OUTPUT – Recursion)

```python
def f(n):
    if n==0: return
    print(n)
    f(n-1)

f(4)
```

A. 1 2 3 4
B. 4 3 2 1
C. 4 3 2
D. Error

✅ B

---

## 12. (OUTPUT)

```python
def f(n):
    if n==0: return
    f(n-1)
    print(n)

f(3)
```

✅ Output: `1 2 3`
🎯 Stack concept

---

## 13. (MCQ)

Space complexity of recursion?

A. O(1)
B. O(n)
C. O(log n)
D. O(n²)

✅ B 

---

## 14. (MCQ)

For n=6, swaps?

A. 6
B. 4
C. 3
D. 2

✅ C 

---

## 15. (MCQ)

If return removed in recursion?

A. Works fine
B. Only first swap
C. Error
D. Infinite

✅ B 

---

## 16. (MSQ – Tic Tac Toe)

Valid win conditions:

A. Row
B. Column
C. Diagonal
D. Random

✅ A, B, C

---

## 17. (MCQ)

Draw happens when:

A. Winner found
B. Board full + no winner
C. Invalid move
D. After 5 turns

✅ B 

---

## 18. (OUTPUT – Recursion)

```python
def f(i,j):
    if i>=j: return
    print(i,j)
    f(i+1,j-1)

f(0,3)
```

✅ Output:

```
0 3
1 2
```

---

## 19. (MCQ – Logic)

Why no extra list used?

A. Faster
B. Memory constraint
C. Easy
D. Required

✅ B 

---

## 20. (MCQ – Cipher)

If mapping not unique?

A. Works fine
B. Error
C. Wrong decryption
D. Faster

✅ C

---

# 🔴 HARD (21–30)

---

## 21. (OUTPUT – Recursion 🔥)

```python
def f(lst,s,e):
    if s>=e: return
    lst[s],lst[e]=lst[e],lst[s]
    f(lst,s+1,e-1)

a=[1,2,3,4,5]
f(a,0,4)
print(a)
```

A. [5,4,3,2,1]
B. [5,2,3,4,1]
C. [1,2,3,4,5]
D. Error

✅ A

---

## 22. (MCQ)

Recursive calls count for n elements?

A. n
B. n/2
C. log n
D. n²

✅ B

---

## 23. (MSQ)

Which cause infinite recursion?

A. No base
B. Wrong update
C. Wrong swap
D. Missing return

✅ A, B

---

## 24. (OUTPUT 🔥)

```python
def f(n):
    if n==0: return 0
    return n + f(n-1)

print(f(3))
```

✅ 6

---

## 25. (Tic Tac Toe Logic 🔥)

If player enters occupied cell:

A. Overwrite
B. Skip
C. Ask again
D. Game ends

✅ C

---

## 26. (MCQ)

Turn switching logic:

A. Always X
B. X↔O
C. Random
D. Fixed

✅ B

---

## 27. (OUTPUT – Game Logic)

If winner detected mid-game:

A. Continue
B. Reset
C. Stop immediately
D. Skip turn

✅ C 

---

## 28. (MCQ)

Which is NOT win?

A. Same row
B. Same column
C. Mixed row
D. Diagonal

✅ C

---

## 29. (OUTPUT – Cipher)

Mapping: A→D, B→E
Text: AB

Output?

A. DE
B. AB
C. ED
D. Error

✅ A

---

## 30. (LOGIC 🔥)

Why recursion used instead of loop?

A. Faster
B. Memory heavy
C. Training + concept
D. Required

✅ C 

---

# 📌 FINAL SECTION

---

## 🔁 Top 7 Repeated Question Types

1. Base condition (`start > end`)
2. Output of recursion
3. Number of recursive calls
4. Swap logic tracing
5. Tic Tac Toe win/draw
6. Invalid input handling
7. Space complexity

---

## 💀 Most Common Mistakes

* Missing base condition
* Using `start == end` wrongly
* Forgetting return
* Wrong index update
* Allowing invalid moves
* Not stopping after win

---

## ⚡ Last Minute Strategy

👉 1 hour before exam:

1. Revise:

   * recursion dry run
   * swap logic
   * base condition

2. Practice:

   * 5 output questions
   * 2 Tic Tac Toe traces

3. Remember:

   * `start >= end`
   * swaps = n/2
   * stack = O(n)

---

# 🎯 FINAL TALK (IMPORTANT)

If you:
✔ Can trace recursion line-by-line
✔ Understand Tic Tac Toe flow
✔ Avoid common mistakes

👉 You’re easily in **80–90% zone**

---

If you want next level:
🔥 I can give you **full mock test (same difficulty as NPTEL)**
🔥 Or **super tricky recursion set (hard questions)**
