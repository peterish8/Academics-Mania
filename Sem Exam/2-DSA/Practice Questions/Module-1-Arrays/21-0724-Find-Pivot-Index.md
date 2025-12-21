# ═══════════════════════════════════════
# 📌 [724] - Find Pivot Index
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find index where left sum equals right sum.

## 💡 **Key Insight:**
Precompute total sum. At each index: leftSum == total - leftSum - nums[i]

## 🔧 **Optimal Approach:**
**Algorithm:** Prefix Sum

**Steps:**
- Calculate total sum
- leftSum = 0
- For each i: if leftSum == total - leftSum - nums[i], return i
- Add nums[i] to leftSum
- Return -1 if not found

## 💻 **Code (Run Directly):**
```python
def pivotIndex(nums):
    total = sum(nums)
    leftSum = 0
    
    for i, num in enumerate(nums):
        if leftSum == total - leftSum - num:
            return i
        leftSum += num
    return -1

# TEST
nums = [1, 7, 3, 6, 5, 6]
print("Input:", nums)
print("Output:", pivotIndex(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 7, 3, 6, 5, 6], total = 28

```
i | num | leftSum | rightSum | match?
--|-----|---------|----------|--------
0 | 1   | 0       | 27       | No
1 | 7   | 1       | 20       | No
2 | 3   | 8       | 17       | No
3 | 6   | 11      | 11       | Yes!
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Prefix Sum, Array

## ⚠️ **Gotcha:**
Pivot element itself is not included in either sum.
