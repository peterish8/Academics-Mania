# ═══════════════════════════════════════
# 📌 [153] - Find Minimum in Rotated Sorted Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find minimum element in rotated sorted array (no duplicates).

## 💡 **Key Insight:**
Binary search - minimum is where rotation point is.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- Compare mid with right
- If nums[mid] > nums[right], min is in right half
- Else min is in left half (including mid)

## 💻 **Code (Run Directly):**
```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

# TEST
print("[3,4,5,1,2]:", findMin([3, 4, 5, 1, 2]))
print("[4,5,6,7,0,1,2]:", findMin([4, 5, 6, 7, 0, 1, 2]))
print("[1]:", findMin([1]))
```

## 🏃 **Dry Run:**
**Example:** nums = [3, 4, 5, 1, 2]

```
iter | left | mid | right | nums[mid] vs nums[right]
-----|------|-----|-------|------------------------
1    | 0    | 2   | 4     | 5 > 2 -> left = 3
2    | 3    | 3   | 4     | 1 < 2 -> right = 3
     | left == right      | return nums[3] = 1
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Rotated Array

## ⚠️ **Gotcha:**
Use left < right (not <=) and right = mid (not mid-1).
