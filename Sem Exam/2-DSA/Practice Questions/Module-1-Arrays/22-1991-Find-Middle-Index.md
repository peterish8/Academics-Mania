# ═══════════════════════════════════════
# 📌 [1991] - Find the Middle Index in Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find leftmost index where left sum equals right sum.

## 💡 **Key Insight:**
Same as Pivot Index. Prefix sum approach.

## 🔧 **Optimal Approach:**
**Algorithm:** Prefix Sum

**Steps:**
- Calculate total sum
- leftSum = 0
- Check if leftSum == total - leftSum - nums[i]

## 💻 **Code (Run Directly):**
```python
def findMiddleIndex(nums):
    total = sum(nums)
    leftSum = 0
    
    for i, num in enumerate(nums):
        if leftSum == total - leftSum - num:
            return i
        leftSum += num
    return -1

# TEST
nums = [2, 3, -1, 8, 4]
print("Input:", nums)
print("Output:", findMiddleIndex(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [2, 3, -1, 8, 4], total = 16

```
i | num | leftSum | rightSum | match?
--|-----|---------|----------|--------
0 | 2   | 0       | 14       | No
1 | 3   | 2       | 11       | No
2 | -1  | 5       | 12       | No
3 | 8   | 4       | 4        | Yes!
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Prefix Sum, Array

## ⚠️ **Gotcha:**
Return leftmost index if multiple exist.
