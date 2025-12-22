# 1️⃣ Prefix Sum & Two Pointers

---

## 📌 Prefix Sum

> [!SUCCESS] **Concept**: Pre-compute cumulative sums to answer range queries in O(1).

### Running Sum of 1D Array
```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

# TEST
print(runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
```

### Subarray Sum Equals K
```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}  # Base case
    
    for num in nums:
        prefix_sum += num
        # If (prefix_sum - k) exists, we found subarrays
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count

# TEST
print(subarraySum([1, 1, 1], 2))  # 2
```

---

## 📌 Two Pointers

> [!SUCCESS] **Concept**: Use two indices moving towards each other or same direction.

### Best Time to Buy and Sell Stock
```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# TEST
print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5
```

### Two Sum II (Sorted Array)
```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

# TEST
print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
```

### Remove Duplicates from Sorted Array
```python
def removeDuplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1

# TEST
nums = [1, 1, 2, 2, 3]
k = removeDuplicates(nums)
print(f"Length: {k}, Array: {nums[:k]}")
```

---

## 🧠 Key Points
- **Prefix Sum**: `prefix[i] = prefix[i-1] + nums[i]`
- **Range Query**: `sum(L, R) = prefix[R] - prefix[L-1]`
- **Two Pointers**: Move based on comparison (sorted = move towards each other)

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
