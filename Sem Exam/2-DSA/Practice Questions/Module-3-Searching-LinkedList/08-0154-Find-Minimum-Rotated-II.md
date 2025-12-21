# ═══════════════════════════════════════
# 📌 [154] - Find Minimum in Rotated Sorted Array II
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find minimum in rotated array with duplicates.

## 💡 **Key Insight:**
Same as #153 but shrink right when nums[mid] == nums[right].

## 🔧 **Optimal Approach:**
**Algorithm:** Modified Binary Search

**Steps:**
- If nums[mid] > nums[right], min in right half
- If nums[mid] < nums[right], min in left half
- If equal, shrink right by 1

## 💻 **Code (Run Directly):**
```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1  # Handle duplicates
    
    return nums[left]

# TEST
print("[2,2,2,0,1]:", findMin([2, 2, 2, 0, 1]))
print("[1,3,5]:", findMin([1, 3, 5]))
```

## 🏃 **Dry Run:**
**Example:** nums = [2, 2, 2, 0, 1]

```
iter | left | mid | right | action
-----|------|-----|-------|--------
1    | 0    | 2   | 4     | 2 > 1 -> left = 3
2    | 3    | 3   | 4     | 0 < 1 -> right = 3
     | left == right -> return 0
```

## ⏱️ **Complexity:**
- **Time:** O(n) worst case, O(log n) average
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Rotated Array

## ⚠️ **Gotcha:**
When duplicates, can't determine which half, so shrink safely.
