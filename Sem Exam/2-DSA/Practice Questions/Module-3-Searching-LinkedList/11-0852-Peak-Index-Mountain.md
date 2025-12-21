# ═══════════════════════════════════════
# 📌 [852] - Peak Index in a Mountain Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find peak (max) index in mountain array (increases then decreases).

## 💡 **Key Insight:**
Binary search - if increasing (mid < mid+1), peak on right.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- Same as Find Peak Element
- If nums[mid] < nums[mid+1], left = mid + 1
- Else right = mid

## 💻 **Code (Run Directly):**
```python
def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# TEST
print("[0,1,0]:", peakIndexInMountainArray([0, 1, 0]))
print("[0,2,1,0]:", peakIndexInMountainArray([0, 2, 1, 0]))
print("[0,10,5,2]:", peakIndexInMountainArray([0, 10, 5, 2]))
```

## 🏃 **Dry Run:**
**Example:** arr = [0, 2, 1, 0]

```
iter | left | mid | right | arr[mid] vs arr[mid+1]
-----|------|-----|-------|----------------------
1    | 0    | 1   | 3     | 2 > 1 -> right = 1
     | left == right -> return 1
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search

## ⚠️ **Gotcha:**
Mountain array guaranteed - no edge case handling needed.
