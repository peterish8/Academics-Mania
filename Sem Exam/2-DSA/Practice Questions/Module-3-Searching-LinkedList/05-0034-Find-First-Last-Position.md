# ═══════════════════════════════════════
# 📌 [34] - Find First and Last Position
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find starting and ending position of target in sorted array.

## 💡 **Key Insight:**
Two binary searches: one for leftmost, one for rightmost.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Binary Searches

**Steps:**
- Binary search for leftmost occurrence
- Binary search for rightmost occurrence
- Return [left, right] or [-1, -1]

## 💻 **Code (Run Directly):**
```python
def searchRange(nums, target):
    def findLeft():
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Keep searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    def findRight():
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Keep searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    return [findLeft(), findRight()]

# TEST
nums = [5, 7, 7, 8, 8, 10]
print("nums:", nums)
print("target 8:", searchRange(nums, 8))
print("target 6:", searchRange(nums, 6))
```

## 🏃 **Dry Run:**
**Example:** nums = [5,7,7,8,8,10], target = 8

```
findLeft: Found 8 at 3, search left, found at 3
findRight: Found 8 at 3, search right, found at 4
Result: [3, 4]
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search

## ⚠️ **Gotcha:**
After finding target, continue searching in one direction.
