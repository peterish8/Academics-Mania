# ═══════════════════════════════════════
# 📌 [1480] - Running Sum of 1D Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Given an array `nums`, return a running sum where `runningSum[i] = sum(nums[0]...nums[i])`.

## 💡 **Key Insight:**
Each running sum = previous running sum + current element. O(n) instead of O(n²).

## 🔧 **Optimal Approach:**
**Algorithm:** Prefix Sum (In-place)

**Steps:**
- Start from index 1
- For each i, add nums[i-1] to nums[i]
- Return modified array

## 💻 **Code (Run Directly):**
```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

# TEST
nums = [1, 2, 3, 4]
print("Input:", [1, 2, 3, 4])
print("Output:", runningSum(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 2, 3, 4]

```
iter | i | nums[i-1] | nums[i] | nums after
-----|---|-----------|---------|------------------
1    | 1 | 1         | 2       | [1, 3, 3, 4]
2    | 2 | 3         | 3       | [1, 3, 6, 4]
3    | 3 | 6         | 4       | [1, 3, 6, 10]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Prefix Sum, Array

## ⚠️ **Gotcha:**
In-place modification destroys original. Create copy if needed.
