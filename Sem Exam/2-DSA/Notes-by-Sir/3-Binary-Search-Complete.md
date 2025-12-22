# 🔍 Binary Search - Complete Guide

## 🎯 **What is Binary Search?**

> [!SUCCESS] **Definition**: An efficient searching algorithm that repeatedly divides the search space in half.

> [!WARNING] **Non-Negotiable Requirement**
> The array **MUST be sorted**. If not sorted, binary search simply doesn't work!

---

## ⚡ **Why Binary Search Is Better**

Instead of checking elements one by one:
1. Look at the **middle** element
2. Decide if target is in **left half** or **right half**
3. **Eliminate** the other half completely
4. Repeat!

**Analogy:** Finding a word in a dictionary - you don't read every page, you jump halfway and narrow down! 📖

---

## ⏱️ **Time & Space Complexity**

| Case | Time | Explanation |
|------|------|-------------|
| **Best** | O(1) | Target is the middle element |
| **Average** | O(log n) | Halving search space |
| **Worst** | O(log n) | Target at end or not found |

| Version | Space |
|---------|-------|
| **Iterative** | O(1) |
| **Recursive** | O(log n) - recursion stack |

---

## 🛠️ **How Binary Search Works**

**Steps:**
1. Set `low = 0`, `high = len(arr) - 1`
2. Find `mid = (low + high) // 2`
3. If `arr[mid] == target`: return index ✅
4. If `target < arr[mid]`: search left half (high = mid - 1)
5. If `target > arr[mid]`: search right half (low = mid + 1)
6. Repeat until `low > high`

---

## 💻 **Iterative Binary Search (Runnable)**

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  # Found!
        elif target < arr[mid]:
            high = mid - 1  # Search left half
        else:
            low = mid + 1   # Search right half
    
    return -1  # Not found

# TEST
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]
target = 23
print("Array:", arr)
print("Target:", target)
print("Found at index:", binary_search(arr, target))

# Test not found
print("Target 100:", binary_search(arr, 100))
```

---

## 🏃 **Dry Run Example**

**Array:** `[2, 5, 8, 12, 16, 23, 38, 56, 72]`  
**Target:** `23`

| Step | low | high | mid | arr[mid] | Action |
|------|-----|------|-----|----------|--------|
| 1 | 0 | 8 | 4 | 16 | 23 > 16 → search right |
| 2 | 5 | 8 | 6 | 38 | 23 < 38 → search left |
| 3 | 5 | 5 | 5 | 23 | **Found!** Return 5 |

---

## ❌ **When Binary Search Fails**

| Situation | Why it fails |
|-----------|--------------|
| **List not sorted** | Can't determine which half to eliminate |
| **Rotated array** | Need special logic (modified binary search) |
| **Linked List** | No random access - can't jump to middle |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Condition**: `while low <= high` (don't forget the `=`!)
> - **Mid formula**: `(low + high) // 2`
> - **Left half**: `high = mid - 1`
> - **Right half**: `low = mid + 1`
> - **Sorted = Binary Search signal** 📶

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Why must the array be sorted?
> > [!SUCCESS]- Answer
> > Binary search decides which half to search based on comparison. If unsorted, this logic breaks.

> [!QUESTION] **Q2**: What's the difference between O(n) and O(log n)?
> > [!SUCCESS]- Answer
> > For 1 billion elements: Linear = 1 billion checks. Binary = ~30 checks! 🔥

> [!QUESTION] **Q3**: Why `low <= high` and not `low < high`?
> > [!SUCCESS]- Answer
> > When `low == high`, there's still one element to check. Using `<` would skip it!

> [!QUESTION] **Q4**: Why `mid - 1` and `mid + 1` instead of just `mid`?
> > [!SUCCESS]- Answer
> > We already checked `mid`, so we exclude it. Otherwise, we might get stuck in infinite loop.

> [!QUESTION] **Q5**: Can we use Binary Search on a Linked List?
> > [!SUCCESS]- Answer
> > Not efficiently. Linked Lists don't support random access - finding middle is O(n).

---

Back to: [[Sem Exam/2-DSA/DSA-Hub|DSA Hub]]
