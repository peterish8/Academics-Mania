# 👉👈 Two Pointer Technique

## 🎯 What You'll Learn
- When and how to use two pointers
- Different two-pointer patterns
- Solving array problems efficiently
- Intersection and stock trading problems

**Previous**: [[05-Prefix-Sum-Technique]] | **Next**: [[07-Array-Manipulation-Advanced]]

---

## 📚 Problems Covered

1. [[Two-Sum-II-Sorted]]
2. [[Intersection-of-Arrays]]
3. [[Best-Time-to-Buy-Sell-Stock]]

---

## 🎨 Understanding Two Pointers

### What is Two Pointer Technique?

**Definition:** Using two index variables to traverse an array, usually to find pairs or subarrays.

**Common Patterns:**

1. **Opposite Direction** (left & right)
   ```
   [1, 2, 3, 4, 5]
    ↑           ↑
    left      right
   ```

2. **Same Direction** (slow & fast)
   ```
   [1, 2, 3, 4, 5]
    ↑  ↑
    slow fast
   ```

3. **Sliding Window** (left & right expanding)
   ```
   [1, 2, 3, 4, 5]
    ↑     ↑
    left  right (grows)
   ```

---

## 🎯 Problem 1: Two Sum II (LeetCode 167)

### Problem Statement
Given a **1-indexed sorted array** and a `target`, return indices of two numbers that add up to target.

**Key:** Array is already sorted!

**Examples:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: 2 + 4 = 6

Input: numbers = [-1,0], target = -1
Output: [1,2]
```

---

### 💡 Approach

**Why Two Pointers Work Here:**
- Array is sorted!
- If sum too small → move left pointer right (increase sum)
- If sum too large → move right pointer left (decrease sum)

**Algorithm:**
1. Start: `left = 0`, `right = n-1`
2. Calculate sum
3. If sum == target → found!
4. If sum < target → left++
5. If sum > target → right--

---

### 🔍 Dry Run

**Input:** `numbers = [2, 7, 11, 15]`, `target = 9`

```
Initialize:
  left = 0, right = 3

Step 1:
  numbers[0] = 2, numbers[3] = 15
  sum = 2 + 15 = 17
  17 > 9? YES → move right left
  right = 2

Step 2:
  numbers[0] = 2, numbers[2] = 11
  sum = 2 + 11 = 13
  13 > 9? YES → move right left
  right = 1

Step 3:
  numbers[0] = 2, numbers[1] = 7
  sum = 2 + 7 = 9
  9 == 9? YES ✓
  
  Return [0+1, 1+1] = [1, 2]
  (Add 1 because 1-indexed)
```

---

### 🎨 Visual Representation

```
[2, 7, 11, 15]  target = 9
 ↑          ↑
 L          R    2+15=17 > 9, R--

[2, 7, 11, 15]
 ↑      ↑
 L      R        2+11=13 > 9, R--

[2, 7, 11, 15]
 ↑  ↑
 L  R            2+7=9 ✓ Found!
```

---

### ✅ Solution Code

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # No solution found
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single pass with two pointers |
| Space | O(1) | Only two variables |

**Why O(n)?**
- Each pointer moves at most n times
- No nested loops!

---

## 🔗 Problem 2: Intersection of Two Arrays (LeetCode 349)

### Problem Statement
Find the **unique** common elements between two arrays.

**Examples:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4] or [4,9]
```

---

### 💡 Approach

**Using Sets:** Simplest and most efficient!

```python
# Convert both to sets
set1 = set(nums1)
set2 = set(nums2)

# Find intersection
result = set1 & set2  # or set1.intersection(set2)
```

**Why sets?**
- Automatically removes duplicates
- O(1) lookup
- Built-in intersection operation

---

### 🔍 Dry Run

**Input:** `nums1 = [1,2,2,1]`, `nums2 = [2,2]`

```
Step 1: Convert to sets
  set1 = {1, 2}
  set2 = {2}

Step 2: Find intersection
  set1 & set2 = {2}

Step 3: Convert to list
  result = [2] ✓
```

---

### ✅ Solution Code

```python
def intersection(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    return list(set1 & set2)
```

**Alternative explicit approach:**
```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()
    
    for num in nums2:
        if num in set1:
            result.add(num)
    
    return list(result)
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n + m) | Creating both sets |
| Space | O(n + m) | Storing both sets |

---

## 📈 Problem 3: Best Time to Buy and Sell Stock (LeetCode 121)

### Problem Statement
Find maximum profit from **one** buy and **one** sell transaction.

**Examples:**
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy at 1, sell at 6 → profit = 5

Input: [7,6,4,3,1]
Output: 0
Explanation: No profit possible (always decreasing)
```

---

### 💡 Approach

**Key Insight:** Track minimum price seen so far!

**Algorithm:**
1. Keep track of `min_price` (cheapest stock so far)
2. For each price:
   - Calculate potential profit: `price - min_price`
   - Update `max_profit` if better
   - Update `min_price` if current price is lower

---

### 🔍 Dry Run

**Input:** `prices = [7, 1, 5, 3, 6, 4]`

```
Initialize:
  min_price = infinity
  max_profit = 0

Day 0: price = 7
  min_price = min(inf, 7) = 7
  profit = 7 - 7 = 0
  max_profit = max(0, 0) = 0

Day 1: price = 1
  min_price = min(7, 1) = 1
  profit = 1 - 1 = 0
  max_profit = max(0, 0) = 0

Day 2: price = 5
  min_price = min(1, 5) = 1
  profit = 5 - 1 = 4
  max_profit = max(0, 4) = 4 ✓

Day 3: price = 3
  min_price = min(1, 3) = 1
  profit = 3 - 1 = 2
  max_profit = max(4, 2) = 4

Day 4: price = 6
  min_price = min(1, 6) = 1
  profit = 6 - 1 = 5
  max_profit = max(4, 5) = 5 ✓

Day 5: price = 4
  min_price = min(1, 4) = 1
  profit = 4 - 1 = 3
  max_profit = max(5, 3) = 5

Final: max_profit = 5
Buy at day 1 (price=1), sell at day 4 (price=6)
```

---

### 🎨 Visual Understanding

```
Prices: [7, 1, 5, 3, 6, 4]

         7
           ╲           6
            ╲       ⬈ ╱ ╲
             ╲   5 ╱   ╲ 4
              ╲ ⬈ ╱ 3   ╲
               1 ◄───────┤
               ↑         ↑
             BUY       SELL
            Profit = 6 - 1 = 5
```

---

### ✅ Solution Code

```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        
        # Calculate profit if we sell today
        profit = price - min_price
        
        # Update maximum profit
        max_profit = max(max_profit, profit)
    
    return max_profit
```

**Alternative with comments:**
```python
def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        # If we found cheaper price, update
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            # Calculate profit if we sell now
            max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single pass through array |
| Space | O(1) | Only two variables |

---

## 🎓 Two Pointer Patterns Summary

### Pattern 1: Opposite Ends (Two Sum II)

```python
left, right = 0, n - 1
while left < right:
    # Check condition
    if condition_met:
        return result
    elif need_increase:
        left += 1
    else:
        right -= 1
```

**Use when:**
- Array is sorted
- Looking for pair with specific sum
- Need to reduce search space from both ends

---

### Pattern 2: Same Direction (Remove Duplicates)

```python
slow = 0
for fast in range(n):
    if condition:
        arr[slow] = arr[fast]
        slow += 1
```

**Use when:**
- In-place array modification
- Removing elements
- Partitioning array

---

### Pattern 3: Min/Max Tracking (Stock Problem)

```python
min_val = float('inf')
max_result = 0

for val in arr:
    min_val = min(min_val, val)
    max_result = max(max_result, val - min_val)
```

**Use when:**
- Buy low, sell high problems
- Finding maximum difference
- Tracking extremes

---

## ✅ DO / ❌ AVOID

### ✅ DO

- Use two pointers when array is sorted
- Consider sets for intersection/union problems
- Track min/max values for optimization problems
- Think about what each pointer represents
- Test with edge cases (empty, single element)

### ❌ AVOID

- Using two pointers on unsorted arrays (unless problem allows)
- Nested loops when two pointers work
- Forgetting to handle 0-indexed vs 1-indexed
- Moving both pointers simultaneously without condition
- Ignoring the "no solution" case

---

## 🔗 Related Topics

- [[02-Basic-Array-Operations]] - Array fundamentals
- [[05-Prefix-Sum-Technique]] - Another array technique
- [[10-Sliding-Window]] - Advanced two-pointer pattern

---

## 📝 Practice Problems

### Easy
1. LeetCode 167 - Two Sum II
2. LeetCode 121 - Best Time to Buy and Sell Stock
3. LeetCode 349 - Intersection of Two Arrays
4. LeetCode 283 - Move Zeroes

### Medium
1. LeetCode 15 - 3Sum
2. LeetCode 11 - Container With Most Water
3. LeetCode 75 - Sort Colors

### Hard
1. LeetCode 42 - Trapping Rain Water
2. LeetCode 76 - Minimum Window Substring

---

**Previous**: [[05-Prefix-Sum-Technique]] | **Next**: [[07-Array-Manipulation-Advanced]]

Back to: [[README of Frontend]]
