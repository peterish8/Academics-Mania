# ═══════════════════════════════════════
# 📌 [442] - Find All Duplicates in an Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find all elements appearing twice. 1 <= nums[i] <= n. O(1) extra space.

## 💡 **Key Insight:**
Use array as hash by negating at index (num-1). If already negative, it's duplicate.

## 🔧 **Optimal Approach:**
**Algorithm:** Index Marking

**Steps:**
- For each num, go to index |num| - 1
- If value negative, num is duplicate
- Otherwise, negate value at that index

## 💻 **Code (Run Directly):**
```python
def findDuplicates(nums):
    result = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]
    return result

# TEST
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print("Input:", [4, 3, 2, 7, 8, 2, 3, 1])
print("Output:", findDuplicates(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [4, 3, 2, 7, 8, 2, 3, 1]

```
num | idx | nums[idx] | action
----|-----|-----------|--------
4   | 3   | 7 > 0     | negate
3   | 2   | 2 > 0     | negate
2   | 1   | 3 > 0     | negate
7   | 6   | 3 > 0     | negate
8   | 7   | 1 > 0     | negate
2   | 1   | -3 < 0    | add 2
3   | 2   | -2 < 0    | add 3
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Array, Index Marking

## ⚠️ **Gotcha:**
Use abs() since values can become negative during marking.
