# ═══════════════════════════════════════
# 📌 [162] - Find Peak Element
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find any peak (greater than neighbors) in O(log n).

## 💡 **Key Insight:**
Binary search - if mid < mid+1, peak is on right. Else on left.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- If nums[mid] < nums[mid+1], peak on right
- Else peak on left (including mid)

## 💻 **Code (Run Directly):**
```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# TEST
print("[1,2,3,1]:", findPeakElement([1, 2, 3, 1]))
print("[1,2,1,3,5,6,4]:", findPeakElement([1, 2, 1, 3, 5, 6, 4]))
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 2, 3, 1]

```
iter | left | mid | right | nums[mid] vs nums[mid+1]
-----|------|-----|-------|------------------------
1    | 0    | 1   | 3     | 2 < 3 -> left = 2
2    | 2    | 2   | 3     | 3 > 1 -> right = 2
     | left == right -> return 2 (peak at index 2)
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search

## ⚠️ **Gotcha:**
Problem guarantees nums[-1] and nums[n] are -infinity.
