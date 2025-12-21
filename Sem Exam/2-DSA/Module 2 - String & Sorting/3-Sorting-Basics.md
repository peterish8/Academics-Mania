# 🧹 Basic Sorting Algorithms

## 🎯 **Sorting: The Mechanics**

> [!SUCCESS] **Goal**: Arrange data in ascending order.
> These are **O(n²)** algorithms. Slow, but educational. 🎓

---

## 🧼 **1. Bubble Sort (Optimized)**
> **Idea**: Compare adjacent pair. Swap if wrong order. Largest element "bubbles" to end.
> **Optimization**: If no swaps in a pass, array is sorted - exit early! ⚡

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization flag
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no swaps happened, array is already sorted!
        if not swapped:
            break
            
    return arr

# TEST
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort (Optimized)")
print("Input:", [64, 34, 25, 12, 22, 11, 90])
print("Output:", bubble_sort(arr))
```

**Why the optimization?**
- Without `swapped` flag: Always runs O(n²) even if sorted
- With `swapped` flag: Best case becomes O(n) for nearly sorted arrays!

---

## 👉 **2. Selection Sort (Optimized)**
> **Idea**: Find the **Minimum** in the unsorted part. Swap it to the front.
> **Optimization**: Only swap if min_idx changed - avoids unnecessary self-swaps! ⚡

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Only swap if we found a smaller element (optimization!)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

# TEST
arr = [64, 25, 12, 22, 11]
print("Selection Sort (Optimized)")
print("Input:", [64, 25, 12, 22, 11])
print("Output:", selection_sort(arr))
```

**Why `if min_idx != i`?**
- Without check: `arr[i], arr[i] = arr[i], arr[i]` - Useless self-swap!
- With check: Skips swap when element is already in correct position
- Saves write operations (important for memory/flash storage)

---

## 🃏 **3. Insertion Sort (Optimized)**
> **Idea**: Pick an element, look BACKWARDS, and insert it into the correct spot (shift others).
> **Best**: Very fast for small arrays or nearly sorted data! Already optimal O(n) best case.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to insert
        j = i - 1
        
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key at correct position
        arr[j + 1] = key
        
    return arr

# TEST
arr = [12, 11, 13, 5, 6]
print("Insertion Sort")
print("Input:", [12, 11, 13, 5, 6])
print("Output:", insertion_sort(arr))

# Test with nearly sorted - very fast!
arr2 = [1, 2, 4, 3, 5]
print("Nearly sorted:", insertion_sort(arr2))
```

**Why is Insertion sort special?**
- **Best Case O(n)**: When array is nearly sorted, inner while barely runs
- **Adaptive**: Faster when input has some order
- **Online**: Can sort as data arrives (stream)

---

## 📊 **Comparison Table**

| Algorithm | Best | Average | Worst | Stable? | When to Use |
|-----------|------|---------|-------|---------|-------------|
| **Bubble** | O(n) | O(n²) | O(n²) | ✅ Yes | Detecting sorted arrays |
| **Selection** | O(n²) | O(n²) | O(n²) | ❌ No | Minimizing swaps |
| **Insertion** | O(n) | O(n²) | O(n²) | ✅ Yes | Small/nearly sorted |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Bubble** = Swap neighbors, `swapped` flag for early exit 👯
> - **Selection** = Hunt for small, `if min_idx != i` to skip useless swaps 🔎
> - **Insertion** = Slide back (Like sorting cards in hand) 🔙

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Worst case Time Complexity for all three?
> > [!SUCCESS]- Answer
> > **O(n²)**.

> [!QUESTION] **Q2**: Which one is fastest if array is ALREADY sorted?
> > [!SUCCESS]- Answer
> > **Insertion Sort** and **Bubble Sort (with swapped flag)** - both O(n). Selection is always O(n²).

> [!QUESTION] **Q3**: Which one performs minimum number of swaps?
> > [!SUCCESS]- Answer
> > **Selection Sort** (At most n-1 swaps, one per pass).

> [!QUESTION] **Q4**: Is Bubble Sort "Stable"?
> > [!SUCCESS]- Answer
> > Yes. Equal elements don't cross each other.

> [!QUESTION] **Q5**: What is "Stability" in sorting?
> > [!SUCCESS]- Answer
> > If two items have equal value, their relative order is preserved (original 5a stays before 5b).

---

Back to: [[Sem Exam/2-DSA/Module 2 - String & Sorting/README|Module 2 Hub]] | [[../DSA-Hub|DSA Hub]]
