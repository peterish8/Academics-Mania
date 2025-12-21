# ═══════════════════════════════════════
# 📌 [27] - Remove Element
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Remove all occurrences of val in-place. Return remaining count.

## 💡 **Key Insight:**
Two pointer: keep elements != val at insertPos.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- insertPos = 0
- If num != val, place at insertPos, inc
- Return insertPos

## 💻 **Code (Run Directly):**
```python
def removeElement(nums, val):
    insertPos = 0
    for num in nums:
        if num != val:
            nums[insertPos] = num
            insertPos += 1
    return insertPos

# TEST
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("Input: [3, 2, 2, 3], val=3")
print("Remaining:", k)
print("Result:", nums[:k])
```

## 🏃 **Dry Run:**
**Example:** nums = [3, 2, 2, 3], val = 3

```
iter | num | action
-----|-----|-------------------
1    | 3   | Skip
2    | 2   | Place at 0
3    | 2   | Place at 1
4    | 3   | Skip

Result: k=2
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers, Array

## ⚠️ **Gotcha:**
Order doesn't matter in output.
