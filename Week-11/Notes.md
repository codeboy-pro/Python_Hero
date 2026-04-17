Alright Pradip, this is *one of the most scoring weeks* if you get the logic clean 🔥
I’ll make this **super exam-focused + step-by-step**, exactly how NPTEL questions come.

---

# 🧠 WEEK 11 NOTES — JOY OF COMPUTING (EXAM READY)

---

# 🔥 SECTION 1: CALENDAR LOGIC (MOST IMPORTANT 🔥🔥🔥)

## 🧩 1. Day Mapping (VERY IMPORTANT)

| Number | Day       |
| ------ | --------- |
| 0      | Sunday    |
| 1      | Monday    |
| 2      | Tuesday   |
| 3      | Wednesday |
| 4      | Thursday  |
| 5      | Friday    |
| 6      | Saturday  |

👉 **Golden Rule:**
Always use →

```
(day + shift) % 7
```

---

## 🧩 2. Core Idea: How Day Changes

👉 Every normal year shifts **+1 day**
👉 Every leap year shifts **+2 days**

Example:

* 2023 → Sunday
* 2024 (leap) → Tuesday (+2)

---

## 🧩 3. Step-by-Step: Find Day of Any Date 🔥

👉 Suppose: Find day of **15 Aug 2025**

### ✅ STEP 1: Take base date

Usually: **1 Jan 2000 → Saturday (6)**

---

### ✅ STEP 2: Count years difference

From 2000 → 2025:

* Total years = 25
* Leap years = 2000, 2004, 2008, 2012, 2016, 2020, 2024 → 7

👉 Total shift:

```
= Normal years + 2×(leap years)
= (25 - 7) + (2×7)
= 18 + 14 = 32
```

---

### ✅ STEP 3: Take mod 7

```
32 % 7 = 4
```

👉 New year day shift = +4

---

### ✅ STEP 4: Add month + date

Month days till July:

| Month | Days  |
| ----- | ----- |
| Jan   | 31    |
| Feb   | 28/29 |
| Mar   | 31    |
| Apr   | 30    |
| May   | 31    |
| Jun   | 30    |
| Jul   | 31    |

👉 Total till July = 212
Add date: 15 → **227**

```
227 % 7 = 3
```

---

### ✅ STEP 5: Final Answer

```
Final = Base + Year shift + Month shift
= 6 + 4 + 3 = 13
13 % 7 = 6 → Saturday
```

---

## ⚡ Shortcut Trick (Exam Hack)

👉 Instead of full sum:

* Only track mod 7
* Reduce every step mod 7

---

## 🎯 EXAM QUESTIONS

### 🔹 MCQ

* If 1 Jan 2023 is Sunday, what is 1 Jan 2024?

🧠 Given:

👉 1 Jan 2023 = Sunday

⚡ Step 1: Check next year (2024)

👉 2024 is a leap year

⚡ Step 2: Apply shift rule
Normal year → +1
Leap year → +2

👉 So shift = +2

⚡ Step 3: Add shift

Sunday (0) + 2 = 2

👉 2 = Tuesday

✅ FINAL ANSWER: Tuesday

---

## 💀 Common Mistakes

* Forgetting leap year extra day
* Not using mod 7
* Wrong base day

---

# 🔥 SECTION 2: LEAP YEAR LOGIC

## 🧩 Rules (VERY IMPORTANT)

```
if year % 400 == 0 → Leap
elif year % 100 == 0 → Not Leap
elif year % 4 == 0 → Leap
else → Not Leap
```

---

## 🧪 Examples

| Year | Result     |
| ---- | ---------- |
| 2000 | Leap ✅     |
| 1900 | Not Leap ❌ |
| 2024 | Leap ✅     |
| 2023 | Not Leap ❌ |

---

## 🎯 EXAM QUESTIONS

### 🔹 Output-based

```python
year = 1900
print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
```

👉 Output: False

---

## 💀 Mistakes

* Thinking every /4 is leap
* Ignoring century rule

---

# 🔥 SECTION 3: DATE CALCULATIONS

---

## 🧩 1. Add Days

👉 Formula:

```
new_day = (current_day + n) % 7
```

---

## 🧩 2. Next Day

```
(day + 1) % 7
```

---

## 🧩 3. Month Transition

👉 Important:

| Month              | Days  |
| ------------------ | ----- |
| Feb                | 28/29 |
| Apr, Jun, Sep, Nov | 30    |
| Rest               | 31    |

---

## 🎯 EXAM QUESTIONS

### 🔹 Output 🔥

```python
day = 5
day = (day + 10) % 7
print(day)
```

👉 1 → Monday

---

### 🔹 Logic

* What is day after 100 days?

---

## 💀 Mistakes

* Not handling February
* Off-by-one error

---

# 🔥 SECTION 4: CALENDAR PATTERNS

---

## 🧩 Repetition Logic

👉 Calendar repeats every:

* 28 years (normal cycle)
* Because:

```
7 (days) × 4 (leap cycle)
```

---

## 🧩 Key Insight

* Same date same day after 28 years
* Except century exceptions

---

## 🎯 Questions

* When will same calendar repeat?

---

# 🔥 SECTION 5: BROWSER AUTOMATION (LIGHT)

---

## 🧩 What is it?

👉 Automating browser tasks using Python

---

## 🧩 Tools

* Selenium

---

## 🧩 Use Cases

* Auto login
* Form filling
* Scraping

---

## 🎯 Questions

* What is Selenium used for?
* Why browser automation?

---

# 🧪 PRACTICE SECTION

---

## 🔥 10 Calendar Problems

1. Day of 1 Jan 2026
2. Day of 15 Aug 1947
3. 100 days after Monday
4. 365 days after Sunday
5. 730 days after Tuesday
6. Next day of Saturday
7. Previous day of Monday
8. Day of 29 Feb 2024
9. Day of 1 Mar 2023
10. Day of 31 Dec 2025

---

## 🔥 10 Output Questions

1.

```python
print((2 + 365) % 7)
```

2.

```python
print((6 + 366) % 7)
```

3.

```python
print((1 + 30) % 7)
```

... (practice similar)

---

## 🔥 5 Leap Year Questions

1. 1800
2. 2000
3. 2100
4. 2028
5. 2023

---

## 🔥 5 Tricky Logic

* What day repeats after 1000 days?
* Difference between two dates
* Feb edge case
* Century leap logic
* Multi-year jumps

---

# 📌 FINAL SECTION

---

# 🎯 Top 25 Most Important Questions

1. Day of given date
2. Leap year check
3. Days after N days
4. Month transitions
5. Output of mod 7
6. Calendar repetition
7. Feb logic
8. Year shift logic
9. Multi-year shift
10. Edge year cases
    ... (focus on these patterns)

---

# 🔁 Most Repeated Patterns (Assignment)

* `% 7` logic
* Leap year condition
* Adding days
* Month-day arrays
* Day shifting

---

# ⚡ LAST MINUTE CHEAT SHEET

---

## 🚀 SUPER QUICK REVISION

* Normal year → +1
* Leap year → +2
* Use `% 7` ALWAYS
* Feb = 28/29
* Century rule IMPORTANT

---

## 🧠 ONE-LINE FORMULA

```
Final Day = (Base + Year shift + Month shift + Date) % 7
```

---

## 💀 AVOID THESE

* Ignoring leap year
* Wrong mod
* Counting full days (instead of mod)

---

# 🎯 FINAL GOAL (YOU WILL ACHIEVE THIS)

After this, you can:

✅ Find day of any date
✅ Solve tricky calendar logic
✅ Handle assignment questions
✅ Crack output-based MCQs
✅ Score **80–90% easily** 🔥

---

If you want next step, I can give you **“Top 30 MOST EXPECTED Week 11 QUESTIONS (exact exam-level)”** or solve these practice ones with you step-by-step.
