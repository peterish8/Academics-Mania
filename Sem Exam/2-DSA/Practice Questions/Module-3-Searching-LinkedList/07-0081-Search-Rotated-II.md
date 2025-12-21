# ═══════════════════════════════════════
# 📌 [81] - Search in Rotated Sorted Array II
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Search in rotated array with duplicates.

## 💡 **Key Insight:**
Same as #33 but handle duplicates by shrinking when nums[left] == nums[mid].

## 🔧 **Optimal Approach:**
**Algorithm:** Modified Binary Search

**Steps:**
- When nums[left] == nums[mid] == nums[right], shrink both
- Otherwise same logic as #33

## 💻 **Code (Run Directly):**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        
        # Handle duplicates
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False

# TEST
print("[2,5,6,0,0,1,2] target 0:", search([2,5,6,0,0,1,2], 0))
print("[2,5,6,0,0,1,2] target 3:", search([2,5,6,0,0,1,2], 3))
```

## 🏃 **Dry Run:**
**Example:** nums = [2,5,6,0,0,1,2], target = 0

```
Binary search finds 0 -> True
```

## ⏱️ **Complexity:**
- **Time:** O(n) worst case (all duplicates), O(log n) average
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Rotated Array

## ⚠️ **Gotcha:**
Duplicates break the sorted-half detection. Shrink when ambiguous.
