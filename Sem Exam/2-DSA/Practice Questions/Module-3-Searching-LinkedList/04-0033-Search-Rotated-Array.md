# ═══════════════════════════════════════
# 📌 [33] - Search in Rotated Sorted Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Search in rotated sorted array (no duplicates). O(log n).

## 💡 **Key Insight:**
Binary search - one half is always sorted. Check which half and if target is in it.

## 🔧 **Optimal Approach:**
**Algorithm:** Modified Binary Search

**Steps:**
- Find which half is sorted
- Check if target in sorted half
- Search appropriate half

## 💻 **Code (Run Directly):**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# TEST
nums = [4, 5, 6, 7, 0, 1, 2]
print("nums:", nums)
print("target 0:", search(nums, 0))
print("target 3:", search(nums, 3))
```

## 🏃 **Dry Run:**
**Example:** nums = [4,5,6,7,0,1,2], target = 0

```
iter | left | mid | right | sorted half
-----|------|-----|-------|-------------
1    | 0    | 3   | 6     | left [4,5,6,7]
     | 0 not in [4,7)     | go right
2    | 4    | 5   | 6     | left [0,1]
     | 0 in [0,1)         | go left
3    | 4    | 4   | 4     | nums[4]=0 -> Found!
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Rotated Array

## ⚠️ **Gotcha:**
Use <= for left boundary check (nums[left] <= nums[mid]).
