# ═══════════════════════════════════════
# 📌 [1539] - Kth Missing Positive Number
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find kth missing positive number from sorted array.

## 💡 **Key Insight:**
Binary search on "how many missing numbers before index i". Missing count = arr[i] - (i + 1).

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- Binary search for position where missing count >= k
- At arr[i], missing = arr[i] - (i + 1)
- After finding position, calculate actual missing number

## 💻 **Code (Run Directly):**
```python
def findKthPositive(arr, k):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            left = mid + 1
        else:
            right = mid
    
    return left + k

# TEST
arr = [2, 3, 4, 7, 11]
k = 5
print("arr:", arr, "k:", k)
print("Output:", findKthPositive(arr, k))
```

## 🏃 **Dry Run:**
**Example:** arr = [2, 3, 4, 7, 11], k = 5

```
Missing: [1, 5, 6, 8, 9, 10, ...]

At each index:
i=0: arr[0]=2, missing = 2-1 = 1
i=1: arr[1]=3, missing = 3-2 = 1
i=2: arr[2]=4, missing = 4-3 = 1
i=3: arr[3]=7, missing = 7-4 = 3
i=4: arr[4]=11, missing = 11-5 = 6

Binary search finds left=4, answer = 4 + 5 = 9
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Array

## ⚠️ **Gotcha:**
Formula: answer = left + k
