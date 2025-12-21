# ═══════════════════════════════════════
# 📌 [560] - Subarray Sum Equals K
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Count subarrays with sum equal to k.

## 💡 **Key Insight:**
Prefix sum + HashMap. If prefixSum - k exists in map, those represent valid subarrays.

## 🔧 **Optimal Approach:**
**Algorithm:** Prefix Sum + HashMap

**Steps:**
- Track running prefixSum
- Store count of each prefixSum in map
- If (prefixSum - k) in map, add its count
- Start with {0: 1}

## 💻 **Code (Run Directly):**
```python
def subarraySum(nums, k):
    count = 0
    prefixSum = 0
    sumCount = {0: 1}
    
    for num in nums:
        prefixSum += num
        if prefixSum - k in sumCount:
            count += sumCount[prefixSum - k]
        sumCount[prefixSum] = sumCount.get(prefixSum, 0) + 1
    
    return count

# TEST
nums = [1, 1, 1]
k = 2
print("Input:", nums, "k:", k)
print("Output:", subarraySum(nums, k))
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 1, 1], k = 2

```
num | prefixSum | prefixSum-k | sumCount       | count
----|-----------|-------------|----------------|------
1   | 1         | -1          | {0:1, 1:1}     | 0
1   | 2         | 0           | {0:1, 1:1, 2:1}| 1
1   | 3         | 1           | {..., 3:1}     | 2
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
Prefix Sum, HashMap

## ⚠️ **Gotcha:**
Initialize {0: 1} for subarrays starting from index 0.
