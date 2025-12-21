# ═══════════════════════════════════════
# 📌 [2016] - Maximum Difference Between Increasing Elements
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find max difference nums[j] - nums[i] where i < j and nums[i] < nums[j].

## 💡 **Key Insight:**
Track minimum so far. At each position, calculate difference with min (if valid).

## 🔧 **Optimal Approach:**
**Algorithm:** One Pass Min Tracking

**Steps:**
- minVal = nums[0], maxDiff = -1
- For each num from index 1:
  - If num > minVal, update maxDiff
  - Update minVal

## 💻 **Code (Run Directly):**
```python
def maximumDifference(nums):
    minVal = nums[0]
    maxDiff = -1
    
    for num in nums[1:]:
        if num > minVal:
            maxDiff = max(maxDiff, num - minVal)
        minVal = min(minVal, num)
    
    return maxDiff

# TEST
nums = [7, 1, 5, 4]
print("Input:", nums)
print("Output:", maximumDifference(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [7, 1, 5, 4]

```
num | minVal | diff | maxDiff
----|--------|------|--------
7   | 7      | -    | -1
1   | 1      | -    | -1
5   | 1      | 4    | 4
4   | 1      | 3    | 4
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Greedy, Array

## ⚠️ **Gotcha:**
Must be strictly increasing (nums[i] < nums[j]). Return -1 if no valid pair.
