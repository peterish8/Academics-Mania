# 🗺️ Frequency Map (Reference/Hashing)

## 🎯 **The Concept**

> [!SUCCESS] **Definition**: Storing how many times each item appears.
> **Tool**: Dictionary (HashMap) in Python. 📖

**Input**: `[1, 2, 2, 3, 1, 1]`
**Frequency Map**: `{1: 3, 2: 2, 3: 1}`

---

## 🛠️ **Implementation**

### **1. Manual Loop (The Classic)**
```python
counts = {}
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
```

### **2. `get()` Method (Cleaner)**
```python
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
```

### **3. `Counter` (The Pro Move) 🌟**
```python
from collections import Counter

# TEST
nums = [1, 2, 2, 3, 1, 1]
counts = Counter(nums)
print("Input:", nums)
print("Frequency Map:", dict(counts))
print("Most Common:", counts.most_common(2))
```

---

## ⚡ **Use Cases**

1.  **Anagram Check**: Do strings have same char counts?
2.  **Majority Element**: Which item appears > n/2 times?
3.  **Two Sum (Unsorted)**: Map value -> index.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **O(1)** Access/Search.
> - **Counter** is your best friend in Python interviews.
> - Trade **Space** (Memory) for **Time** (Speed).

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the Time Complexity to build a frequency map?
> > [!SUCCESS]- Answer
> > **O(n)**. You pass through the list once.

> [!QUESTION] **Q2**: What is the Space Complexity?
> > [!SUCCESS]- Answer
> > **O(n)** (or O(k) unique elements).

> [!QUESTION] **Q3**: How to check if two strings are Anagrams using maps?
> > [!SUCCESS]- Answer
> > `Counter(str1) == Counter(str2)`.

> [!QUESTION] **Q4**: Why use a Map instead of nested loops for counting?
> > [!SUCCESS]- Answer
> > Time Complexity drops from **O(n²)** to **O(n)**.

> [!QUESTION] **Q5**: Can you hash a list in Python (use a list as a key)?
> > [!SUCCESS]- Answer
> > No! Lists are mutable and unhashable. You must use Tuples or primitive types as keys.

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
