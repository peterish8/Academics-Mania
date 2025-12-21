# ═══════════════════════════════════════
# 📌 [704] - Binary Search
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Search for target in sorted array. Return index or -1.

## 💡 **Key Insight:**
Classic binary search. Compare mid with target, narrow search space by half.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- left = 0, right = n-1
- While left <= right:
  - mid = (left + right) // 2
  - If nums[mid] == target, return mid
  - If nums[mid] < target, left = mid + 1
  - Else right = mid - 1

## 💻 **Code (Run Directly):**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# TEST
nums = [-1, 0, 3, 5, 9, 12]
print("nums:", nums, "target: 9")
print("Output:", search(nums, 9))
print("target: 2 ->", search(nums, 2))
```

## 🏃 **Dry Run:**
**Example:** nums = [-1, 0, 3, 5, 9, 12], target = 9

```
iter | left | right | mid | nums[mid]
-----|------|-------|-----|----------
1    | 0    | 5     | 2   | 3 < 9
2    | 3    | 5     | 4   | 9 == 9 -> Return 4
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search

## ⚠️ **Gotcha:**
Use (left + right) // 2 or left + (right - left) // 2 to avoid overflow.
