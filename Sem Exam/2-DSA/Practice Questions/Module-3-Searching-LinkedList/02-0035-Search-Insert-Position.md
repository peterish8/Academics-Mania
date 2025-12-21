# ═══════════════════════════════════════
# 📌 [35] - Search Insert Position
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find index where target is or would be inserted.

## 💡 **Key Insight:**
Binary search - when not found, left pointer is the insert position.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- Standard binary search
- When loop ends, left is insert position

## 💻 **Code (Run Directly):**
```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# TEST
nums = [1, 3, 5, 6]
print("nums:", nums)
print("target 5:", searchInsert(nums, 5))
print("target 2:", searchInsert(nums, 2))
print("target 7:", searchInsert(nums, 7))
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 3, 5, 6], target = 2

```
iter | left | right | mid | nums[mid]
-----|------|-------|-----|----------
1    | 0    | 3     | 1   | 3 > 2
2    | 0    | 0     | 0   | 1 < 2
3    | 1    | 0     | -   | left > right

Return left = 1
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search

## ⚠️ **Gotcha:**
Return left, not mid, when target not found.
