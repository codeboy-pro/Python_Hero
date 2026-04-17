Alright Pradip — this is **exactly the kind of set that mirrors real NPTEL papers** 🔥
I’ve mixed assignment-style + PYQ patterns + traps. Do these seriously and you’ll feel the jump.

---

# 🎯 TOP 30 MOST IMPORTANT QUESTIONS — WEEK 10

---

# 🟢 EASY (1–10)

---

## **Q1 (FLAMES basic)**

Names: `"ram"` and `"sita"`
After removing common characters, what is the count?

A. 3
B. 4
C. 5
D. 6

✅ **Answer:** C
💡 **Explanation:**
Common = `a` → remaining = `rm` (2) + `sit` (3) = 5
🔥 **Why important:** First step of FLAMES (very common)

---

## **Q2 (String slicing)**

```python
print("python"[1:4])
```

A. pyt
B. yth
C. tho
D. ytho

✅ **Answer:** B
💡 Slice from index 1 to 3 → `yth`
🔥 Common output question

---

## **Q3 (RLE basic)**

Compress `"AAAABB"`

A. A3B2
B. A4B2
C. A4B1
D. A3B3

✅ **Answer:** B
💡 A=4, B=2
🔥 Direct assignment pattern

---

## **Q4 (String count)**

```python
"banana".count("a")
```

A. 2
B. 3
C. 4
D. 1

✅ **Answer:** B
💡 3 occurrences
🔥 Very frequent MCQ

---

## **Q5 (FLAMES letters)**

What does “M” stand for?

A. Mate
B. Marriage
C. Memory
D. Magic

✅ **Answer:** B
🔥 Easy scoring

---

## **Q6 (Reverse string)**

```python
print("abc"[::-1])
```

A. abc
B. cba
C. bac
D. error

✅ **Answer:** B
🔥 Classic PYQ

---

## **Q7 (RLE edge)**

Compress `"ABC"`

A. ABC
B. A1B1C1
C. A3
D. Error

✅ **Answer:** B
🔥 Important edge case

---

## **Q8 (Remove char)**

```python
"hello".replace("l","")
```

A. heo
B. helo
C. hlo
D. heloo

✅ **Answer:** A
🔥 String manipulation core

---

## **Q9 (FLAMES count)**

If count = 1, which letter is removed first?

A. F
B. L
C. A
D. S

✅ **Answer:** A
💡 Start from F → remove F
🔥 Trap question

---

## **Q10 (Loop traversal)**

```python
s="ab"
for i in s:
    print(i,end="")
```

Output?

A. ab
B. a b
C. error
D. ba

✅ **Answer:** A

---

# 🟡 MEDIUM (11–20)

---

## **Q11 (FLAMES elimination)**

Count = 3
FLAMES → which removed first?

A. A
B. M
C. L
D. E

✅ **Answer:** A
💡 F(1), L(2), A(3) → remove A
🔥 Core logic

---

## **Q12 (RLE tricky)**

Compress `"AABBA"`

A. A2B2A1
B. A3B2
C. A2B3
D. ABBA

✅ **Answer:** A
🔥 Group-based logic

---

## **Q13 (String index)**

```python
s="abcd"
print(s[-2])
```

A. c
B. d
C. b
D. error

✅ **Answer:** A

---

## **Q14 (FLAMES edge)**

Names: `"abc"` and `"abc"`
Remaining count?

A. 0
B. 3
C. 6
D. 1

✅ **Answer:** A
🔥 Important edge case

---

## **Q15 (Frequency)**

```python
s="aabbcc"
len(set(s))
```

A. 6
B. 3
C. 2
D. 1

✅ **Answer:** B

---

## **Q16 (RLE decode)**

Decode `"A3B2"`

A. AAABB
B. AABBB
C. ABB
D. error

✅ **Answer:** A

---

## **Q17 (Pattern count)**

Groups in `"aaabbcaaa"`

A. 2
B. 3
C. 4
D. 5

✅ **Answer:** C
💡 aaa | bb | c | aaa

---

## **Q18 (String build)**

```python
s="abc"
res=""
for i in s:
    res = i + res
print(res)
```

A. abc
B. cba
C. bac
D. error

✅ **Answer:** B

---

## **Q19 (FLAMES round logic)**

After removing one letter, where do we start next count?

A. Beginning
B. Removed position next
C. Random
D. End

✅ **Answer:** B
🔥 VERY IMPORTANT

---

## **Q20 (RLE last char bug)**

Which is common mistake?

A. Forget first char
B. Forget last group
C. Counting wrong
D. All

✅ **Answer:** D

---

# 🔴 HARD (21–30) 🔥🔥🔥

---

## **Q21 (FULL FLAMES)**

Names: `"ak"` and `"bk"`

Step result?

A. F
B. L
C. A
D. M

✅ **Answer:** L

💡 Remove common `k` → a,b → count=2
Eliminate → L survives

🔥 Full simulation type

---

## **Q22 (FLAMES tricky)**

Count = 4
First removed?

A. M
B. E
C. S
D. A

✅ **Answer:** A
💡 F(1),L(2),A(3),M(4)

---

## **Q23 (RLE tricky)**

Compress `"AAABBAAC"`

A. A3B2A2C1
B. A5B2C1
C. A3B2C1
D. A2B2A3C1

✅ **Answer:** A

---

## **Q24 (String trap)**

```python
s="aaa"
print(s.replace("a","b",2))
```

A. bbb
B. bba
C. baa
D. aaa

✅ **Answer:** B

---

## **Q25 (FLAMES multi-step)**

Count = 5
Remaining letters after removing E?

A. F L A M S
B. L A M S
C. F A M S
D. F L M S

✅ **Answer:** A

---

## **Q26 (Pattern logic)**

Longest sequence in `"aaabbccccd"`

A. 2
B. 3
C. 4
D. 5

✅ **Answer:** C

---

## **Q27 (MSQ ⚠️ RLE)**

Which are true?

A. RLE works on consecutive chars
B. Order matters
C. Can skip groups
D. Needs sorting

✅ **Answer:** A, B

---

## **Q28 (MSQ ⚠️ FLAMES)**

Which are correct?

A. Remove common chars
B. Count total
C. Use circular logic
D. Sort strings

✅ **Answer:** A, B, C

---

## **Q29 (Output tricky)**

```python
s="aab"
res=""
count=1

for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        res+=s[i-1]+str(count)
        count=1

print(res)
```

Output?

A. A2B1
B. a2
C. a2b1
D. error

✅ **Answer:** B
💡 Last char missing
🔥 VERY IMPORTANT BUG

---

## **Q30 (Ultimate FLAMES)**

Names: `"aabb"` and `"ab"`

Final count?

A. 1
B. 2
C. 3
D. 4

✅ **Answer:** B
💡 remove 2 matches → left = ab → 2

---

# 📌 FINAL SECTION

---

## 🔁 TOP 7 MOST REPEATED QUESTION TYPES

1. FLAMES full simulation 🔥
2. Remove common characters
3. RLE encoding
4. Missing last character bug
5. String slicing output
6. Pattern grouping
7. Circular elimination logic

---

## 💀 COMMON MISTAKES

### FLAMES:

* Wrong starting index
* Incorrect removal position
* Not wrapping circularly

### COMPRESSION:

* Missing last group 🔥
* Wrong grouping
* Mixing separated chars

---

## ⚡ LAST MINUTE REVISION STRATEGY

👉 Do this before exam:

1. Practice **3 FLAMES full problems**
2. Solve **5 RLE encoding**
3. Do **10 output-based questions**
4. Revise:

   * slicing
   * replace
   * count

---

# 🎯 FINAL BOOST

Pradip, if you can:

* Solve Q21, Q23, Q29 confidently
  👉 You are **exam-ready 💀🔥**

---

If you want next:
👉 I can give you **1 full mock test (real NPTEL style)**
👉 or **step-by-step solutions of these 30**

Just tell me 👍
