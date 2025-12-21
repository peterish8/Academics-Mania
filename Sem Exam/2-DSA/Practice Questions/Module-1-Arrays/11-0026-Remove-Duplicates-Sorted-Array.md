# ═══════════════════════════════════════
# 📌 [26] - Remove Duplicates from Sorted Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Remove duplicates in-place from sorted array. Return new length.

## 💡 **Key Insight:**
Sorted = duplicates adjacent. Two pointers: place unique, scan array.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- insertPos = 1 (first element unique)
- If nums[i] != nums[i-1], place at insertPos
- Return insertPos

## 💻 **Code (Run Directly):**
```python
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    insertPos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[insertPos] = nums[i]
            insertPos += 1
    return insertPos

# TEST
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print("Input: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]")
print("Unique count:", k)
print("Result:", nums[:k])
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 1, 2]

```
iter | i | nums[i] | nums[i-1] | action
-----|---|---------|-----------|--------
1    | 1 | 1       | 1         | Skip
2    | 2 | 2       | 1         | Place at 1

Result: k=2
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers, Array

## ⚠️ **Gotcha:**
Array MUST be sorted.
