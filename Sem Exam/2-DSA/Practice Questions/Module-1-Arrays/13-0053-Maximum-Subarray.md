# ═══════════════════════════════════════
# 📌 [53] - Maximum Subarray
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find contiguous subarray with largest sum.

## 💡 **Key Insight:**
Kadane's: At each position, extend or start fresh. If current sum negative, start fresh.

## 🔧 **Optimal Approach:**
**Algorithm:** Kadane's Algorithm

**Steps:**
- currentSum = maxSum = nums[0]
- For each num: currentSum = max(num, currentSum + num)
- Update maxSum if higher

## 💻 **Code (Run Directly):**
```python
def maxSubArray(nums):
    currentSum = maxSum = nums[0]
    for num in nums[1:]:
        currentSum = max(num, currentSum + num)
        maxSum = max(maxSum, currentSum)
    return maxSum

# TEST
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Input:", nums)
print("Output:", maxSubArray(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

```
num | currentSum | maxSum | decision
----|------------|--------|----------
-2  | -2         | -2     | start
1   | 1          | 1      | fresh
-3  | -2         | 1      | extend
4   | 4          | 4      | fresh
-1  | 3          | 4      | extend
2   | 5          | 5      | extend
1   | 6          | 6      | extend
-5  | 1          | 6      | extend
4   | 5          | 6      | extend
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Kadane's Algorithm, DP

## ⚠️ **Gotcha:**
Initialize with nums[0], not 0. Array might be all negatives.
