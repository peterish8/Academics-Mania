# 6️⃣ Array Manipulation

---

## 📌 Minimum Swaps to Sort Array

> **Goal**: Find the minimum number of swaps needed to sort an unsorted array.

> [!TIP] **Key Insight**: Find cycles in the array. Each cycle of length k needs (k-1) swaps.

---

## 💻 Code

```python
def minSwaps(arr):
    n = len(arr)
    # Create (value, index) pairs
    arr_pos = [(arr[i], i) for i in range(n)]
    
    # Sort by value
    arr_pos.sort(key=lambda x: x[0])
    
    # Track visited positions
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        # Already visited or already in correct position
        if visited[i] or arr_pos[i][1] == i:
            continue
        
        # Count cycle length
        cycle_length = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]  # Go to original position
            cycle_length += 1
        
        # Cycle of length k needs (k-1) swaps
        if cycle_length > 1:
            swaps += cycle_length - 1
    
    return swaps

# TEST
arr = [4, 3, 2, 1]
print("Array:", arr)
print("Min swaps:", minSwaps(arr))  # 2

arr2 = [1, 5, 4, 3, 2]
print("Array:", arr2)
print("Min swaps:", minSwaps(arr2))  # 2
```

---

## 🏃 Dry Run

**Array:** `[4, 3, 2, 1]`

After sorting: `[(1,3), (2,2), (3,1), (4,0)]`

| i | Value | Should be at | Cycle |
|---|-------|--------------|-------|
| 0 | 1 | index 3 | 0→3→0 (length 2) |
| 1 | 2 | index 2 | 1→2→1 (length 2) |

Cycles: 2 + 2 = 4 elements
Swaps: (2-1) + (2-1) = **2 swaps**

---

## 🧠 Key Points
- **Formula**: Cycle of length k = (k-1) swaps
- **Time**: O(n log n) for sorting
- **Space**: O(n) for visited array

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
