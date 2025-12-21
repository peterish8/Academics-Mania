# ═══════════════════════════════════════
# 📌 [977] - Squares of a Sorted Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Sorted array (can have negatives), return sorted squares.

## 💡 **Key Insight:**
Squaring negatives makes them large! Largest squares at ends. Two pointers from both ends.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers (from ends)

**Steps:**
- left = 0, right = n-1, fill result from end
- Compare abs values, place larger square at end
- Move pointer that had larger value

## 💻 **Code (Run Directly):**
```python
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1
    return result

# TEST
nums = [-4, -1, 0, 3, 10]
print("Input:", nums)
print("Output:", sortedSquares(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [-4, -1, 0, 3, 10]

```
iter | left | right | compare | result
-----|------|-------|---------|-------------------
1    | 0    | 4     | 4 < 10  | [_,_,_,_,100]
2    | 0    | 3     | 4 > 3   | [_,_,_,16,100]
3    | 1    | 3     | 1 < 3   | [_,_,9,16,100]
4    | 1    | 2     | 1 > 0   | [_,1,9,16,100]
5    | 2    | 2     | 0 = 0   | [0,1,9,16,100]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
Two Pointers, Array

## ⚠️ **Gotcha:**
Two pointer is O(n), square-then-sort is O(n log n).
