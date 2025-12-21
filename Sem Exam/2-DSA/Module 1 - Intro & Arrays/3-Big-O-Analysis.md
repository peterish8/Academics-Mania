# ⏱️ Intro to Big-O & Complexity

## 🎯 **What is Big-O?**

> [!SUCCESS] **Definition**: A standard way to measure how the **Runtime** or **Space** requirements grow as the **Input Size (n)** grows.
> It measures **Efficiency**, not seconds.

---

## 📈 **Common Complexities (The Hierarchy)**

| Notation | Name | Analogy 🚗 | Example |
|----------|------|------------|---------|
| **O(1)** | Constant | Teleporting ⚡ | Access `arr[5]` |
| **O(log n)** | Logarithmic | Looking up a word in a Dictionary 📖 | Binary Search |
| **O(n)** | Linear | Reading a book page by page 🚶 | Loop through list |
| **O(n log n)** | Log Linear | Sorting a deck of cards 🃏 | Merit Sort, Quick Sort |
| **O(n²)** | Quadratic | Checking every person against every other person 🤝 | Nested Loops |

---

## 🔢 **How to Estimate (Real-Life)**

1.  **Loops**: Look for `for` or `while`.
    *   1 loop = `n`
    *   2 nested loops = `n * n` = `n²`
2.  **Halving**: If loop cuts problem in half (`i = i * 2` or `n = n / 2`), it's **O(log n)**.
3.  **Drop Constants**: `O(2n + 50)` -> **O(n)**. We care about the *Growth Rate*, not exact math.

---

## 🧠 **Space Complexity**

> How much **Extra** memory do you need?
- **O(1)**: Only a few variables (`count`, `total`).
- **O(n)**: Creating a new list/map of size n.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **O(1)** = Instant.
> - **O(n)** = Fair (Depends on input).
> - **O(n²)** = Slow (Avoid for large n).
> - **Log n** = The Gold Standard for search 🏆.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: If you have two separate loops one after another, is it O(n²)?
> > [!SUCCESS]- Answer
> > No. `O(n) + O(n) = O(2n)`. We drop constants, so it's **O(n)**.

> [!QUESTION] **Q2**: What is the complexity of sorting in Python (`sorted()` or `.sort()`)?
> > [!SUCCESS]- Answer
> > **O(n log n)** (Uses Timsort).

> [!QUESTION] **Q3**: What is the worst-case complexity of `.append()` in Python?
> > [!SUCCESS]- Answer
> > **O(n)** (Worst case, when resize happens). But **O(1)** Amortized (Average).

> [!QUESTION] **Q4**: Does O(1) space mean you use NO memory?
> > [!SUCCESS]- Answer
> > No, it means memory usage stays **Constant** regardless of input size `n`.

> [!QUESTION] **Q5**: Which is better: O(n log n) or O(n)?
> > [!SUCCESS]- Answer
> > **O(n)** is better (faster).

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
