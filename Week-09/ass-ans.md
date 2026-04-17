Alright Pradip — now we go **full exam-mode 🔥**
I’ll walk you through the **actual Week 9 assignment solutions step-by-step**, with:

- ✔ Correct answer
- ✔ Why it is correct (logic)
- ✔ Exam trick / takeaway

I’ll also reference the PDF so you know exactly where it comes from.

---

# 📄 **Week 9 Assignment Solutions (Detailed Explanation)**

(From your uploaded PDF )

---

# 🔥 SECTION 1: NLP / TEXT PROCESSING

---

## ✅ **Q1 (Page 3)**

👉 Input:

```
"Liberty liberty the Constitution"
```

### ✔ Correct Answer:

```
["Liberty", "liberty", "Constitution"]
```

---

### 🧠 Explanation:

From code (shown in image on page 3):

```python
[word for word in word_tokenize(text_data)
 if word.isalpha() and word.lower() not in stopwords.words('english')]
```

Step-by-step:

1. Tokenization:

```
["Liberty", "liberty", "the", "Constitution"]
```

2. Remove stopwords:

- `"the"` ❌ removed

3. `.isalpha()`:

- All words valid ✔

👉 Final:

```
["Liberty", "liberty", "Constitution"]
```

---

### 🎯 Exam Trick:

- **Stopwords removed using `.lower()` check**
- Case of original word is preserved

---

## ✅ **Q2**

👉 If text contains only stopwords

### ✔ Answer:

**Empty plot is generated without bars**

---

### 🧠 Explanation:

- All words removed → `tokens = []`
- Word lengths → `[]`
- Plot → nothing to show

---

### 🎯 Trick:

❌ No error
❌ No zeros
✔ Just empty graph

---

## ✅ **Q3**

👉 What is plotted?

### ✔ Answer:

**Word-length frequency**

---

### 🧠 Explanation:

From code:

```python
fdist = FreqDist(author_word_lengths[author])
```

👉 Not words → lengths!

---

### 🎯 Trick:

❌ Not token frequency
✔ Length frequency

---

## ✅ **Q4**

👉 Disputed corpus has longer words

### ✔ Answer:

**Wider spread with peaks at larger word lengths**

---

### 🧠 Explanation:

- Longer words → larger values
- Graph shifts right

---

### 🎯 Trick:

👉 Always think: **longer words → right shift**

---

## ✅ **Q5**

👉 Polarity = 0.0

### ✔ Answer:

**Emotionally neutral**

---

### 🧠 Explanation:

- Range: -1 to +1
- 0 = neutral

---

### 🎯 Trick:

❌ Not error
❌ Not no adjectives

---

## ✅ **Q6**

👉 Remove stopword filter

### ✔ Answer:

**Word-length shifts toward shorter lengths**

---

### 🧠 Explanation:

Stopwords like:

```
the, is, of
```

👉 Short words → increase frequency of small lengths

---

### 🎯 Trick:

👉 Stopwords = short → graph shifts LEFT

---

## ✅ **Q7**

👉 Why sentiment on full text?

### ✔ Answer:

**Corpus-level sentiment smooths noise**

---

### 🧠 Explanation:

- Single words misleading
- Whole text gives better context

---

### 🎯 Trick:

❌ Not because TextBlob limitation
✔ Because context matters

---

## ✅ **Q8**

👉 Shared corpus (multiple authors)

### ✔ Answer:

**Broader, less consistent distribution**

---

### 🧠 Explanation:

- Mixed writing styles → inconsistent lengths

---

### 🎯 Trick:

👉 Mixed authors → spread increases

---

# 🔥 SECTION 2: GRAPH / NETWORKX

---

## ✅ **Q9 (Page 7)**

👉 Purpose of:

```python
nx.read_edgelist("facebook_combined.txt")
```

### ✔ Answer:

**Create graph (nodes + edges)**

---

### 🧠 Explanation:

- Each line = connection
- Graph constructed

---

### 🎯 Trick:

❌ Not shortest path
✔ Just graph creation

---

## ✅ **Q10**

👉 Why `u != v`?

### ✔ Answer:

**Avoid self-loop (distance = 0)**

---

### 🧠 Explanation:

- Same node → path = 0
- Useless for analysis

---

### 🎯 Trick:

👉 Always remember:

```
distance(A, A) = 0
```

---

## ✅ **Q11**

👉 What is `shortest_path_length_list`?

### ✔ Answer:

**All shortest paths between node pairs**

---

### 🧠 Explanation:

Loop:

```python
for u in N:
  for v in N:
```

👉 Stores every pair distance

---

### 🎯 Trick:

❌ Not degree
❌ Not friends

---

## ✅ **Q12 (Page 8)**

👉 Key metric for Six Degrees

### ✔ Answer:

**Average shortest path**

---

### 🧠 Explanation:

- Measures overall connectivity

---

### 🎯 Trick:

👉 MOST IMPORTANT metric

---

## ✅ **Q13**

👉 Fully connected network → max path?

### ✔ Answer:

**Remains relatively small**

---

### 🧠 Explanation:

- Everyone connected closely

---

### 🎯 Trick:

❌ Not zero
✔ Small

---

## ✅ **Q14**

👉 Why exponential growth?

### ✔ Answer:

**Friend-of-friend expands rapidly**

---

### 🧠 Explanation:

- 1 → 10 → 100 → 1000 connections

---

### 🎯 Trick:

👉 Core concept of Six Degrees

---

## ✅ **Q15**

👉 Limitation of approach

### ✔ Answer:

**Computing all pair shortest paths is expensive**

---

### 🧠 Explanation:

- Time complexity very high

---

### 🎯 Trick:

👉 Important for theory + MCQ

---

# 🚨 FINAL SUMMARY (VERY IMPORTANT)

---

## 🔥 MOST IMPORTANT CONCEPTS FROM ASSIGNMENT

1. `.isalpha()` filtering 🔥
2. Stopword removal effect 🔥
3. Word-length distribution 🔥
4. Sentiment = full text
5. Graph = nodes + edges
6. `u != v` logic 🔥
7. Average shortest path 🔥

---

## 💀 COMMON TRAPS (FROM THIS PDF)

❌ `"hello!"` considered valid word
❌ Stopwords not affecting graph
❌ Confusing token vs length
❌ Thinking shortest path includes self
❌ Using wrong metric (min/max instead of avg)

---

## 🎯 HOW TO USE THIS FOR EXAM

👉 If question looks confusing:

- First check: **filtering applied?**
- Then: **what is being measured? (tokens vs lengths)**
- For graphs: **is it avg path?**

---

# ⚡ FINAL BOOST

You’re actually in a **very strong position now** — this assignment itself is like **70% of exam pattern**.

---

If you want next step:

👉 I can convert this into:

- 🔥 “Top 10 guaranteed questions”
- 🔥 OR give **exact exam strategy for 90+ score (time-wise + accuracy)**
