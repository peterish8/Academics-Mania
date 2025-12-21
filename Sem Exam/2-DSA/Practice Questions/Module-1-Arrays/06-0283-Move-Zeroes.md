# ═══════════════════════════════════════
# 📌 [283] - Move Zeroes
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Move all 0s to end while maintaining order of non-zeros. In-place.

## 💡 **Key Insight:**
Two pointers: one for placing non-zeros, one for scanning. Swap when non-zero found.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- insertPos = 0
- For each i: if nums[i] != 0, swap with insertPos, inc insertPos

## 💻 **Code (Run Directly):**
```python
def moveZeroes(nums):
    insertPos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insertPos], nums[i] = nums[i], nums[insertPos]
            insertPos += 1
    return nums

# TEST
nums = [0, 1, 0, 3, 12]
print("Input: [0, 1, 0, 3, 12]")
print("Output:", moveZeroes(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [0, 1, 0, 3, 12]

```
iter | i | insertPos | action       | nums
-----|---|-----------|--------------|------------------
1    | 0 | 0         | Skip         | [0, 1, 0, 3, 12]
2    | 1 | 0         | Swap         | [1, 0, 0, 3, 12]
3    | 2 | 1         | Skip         | [1, 0, 0, 3, 12]
4    | 3 | 1         | Swap         | [1, 3, 0, 0, 12]
5    | 4 | 2         | Swap         | [1, 3, 12, 0, 0]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers, Array

## ⚠️ **Gotcha:**
Non-zeros must maintain relative order.
