# 🧹 Basic Sorting Algorithms

## 🎯 **Sorting: The Mechanics**

> [!SUCCESS] **Goal**: Arrange data in ascending order.
> These are **O(n²)** algorithms. Slow, but educational. 🎓

---

## 🧼 **1. Bubble Sort (Sinking)**
> **Idea**: Compare adjacent pair. Swap if wrong order. Largest element "bubbles" to end.
> **Pass 1**: Largest guaranteed at end.

```python
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            swap(arr[j], arr[j+1])
```

---

## 👉 **2. Selection Sort (Picking)**
> **Idea**: Find the **Minimum** in the unsorted part. Swap it to the front.
> **Pass 1**: Smallest guaranteed at start.

```python
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    swap(arr[i], arr[min_idx])
```

---

## 🃏 **3. Insertion Sort (Card Game)**
> **Idea**: Pick an element, look BACKWARDS, and insert it into the correct spot (shift others).
> **Best**: Very fast for small arrays or nearly sorted data!

```python
for i in range(1, n):
    key = arr[i]
    j = i - 1
    # Move elements greater than key ahead
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Bubble** = Swap neighbors 👯.
> - **Selection** = Hunt for small 🔎.
> - **Insertion** = Slide back 🔙 (Like sorting cards in hand).

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Worst case Time Complexity for all three?
> > [!SUCCESS]- Answer
> > **O(n²)**.

> [!QUESTION] **Q2**: Which one is fastest if array is ALREADY sorted?
> > [!SUCCESS]- Answer
> > **Insertion Sort** (O(n) best case) and **Bubble Sort** (if optimized with a 'swapped' flag). Selection is always O(n²).

> [!QUESTION] **Q3**: Which one performs minimum number of swaps?
> > [!SUCCESS]- Answer
> > **Selection Sort** (Only 1 swap per pass).

> [!QUESTION] **Q4**: Is Bubble Sort "Stable"?
> > [!SUCCESS]- Answer
> > Yes. Equal elements don't cross each other.

> [!QUESTION] **Q5**: What is "Stability" in sorting?
> > [!SUCCESS]- Answer
> > If two items have equal value, their relative order is preserved (original 5a stays before 5b).

---

Back to: [[Sem Exam/2-DSA/Module 2 - String & Sorting/README|Module 2 Hub]] | [[../DSA-Hub|DSA Hub]]
