# ⚡ Kadane's Algorithm

## 🎆 Master the Art of Maximum Subarray Optimization

Unlock the power of **dynamic programming** with Kadane's legendary algorithm - the key to solving optimization problems in O(n) time!

**Previous**: [[07-Array-Manipulation-Advanced]] | **Next**: [[09-Bit-Manipulation]]

---

## 🎨 Color-Coded Learning Guide

> [!SUCCESS] **🟢 Core Concept**
> Maximum subarray sum - the foundation

> [!WARNING] **🟡 Advanced Technique** 
> Array index marking for O(1) space

> [!DANGER] **🔴 Master Level**
> Complex variations and optimizations

---

## 🎯 What You'll Master
- **Maximum subarray sum** problem (LeetCode 53)
- **Dynamic programming** intuition behind Kadane's
- **Array index marking** technique for duplicates
- **Space optimization** tricks

---

## 📚 Problems Covered

1. Maximum Subarray Sum (LeetCode 53)
2. Find All Duplicates in Array (LeetCode 442)

---

## 🎨 Understanding Kadane's Algorithm

### The Problem: Maximum Subarray Sum

**Question:** Find the maximum sum of any contiguous subarray.

**Example:**
```
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

All possible subarrays... too many!
But maximum sum subarray: [4, -1, 2, 1] = 6
```

**Naive approach:** Check all subarrays → O(n²) or O(n³)

**Kadane's approach:** One pass → O(n) 🚀

---

### 💡 The Core Intuition

**At each position, you have a choice:**
1. **Extend** the previous subarray (include current element)
2. **Start fresh** from current element

**Formula:**
```python
current_sum = max(nums[i], current_sum + nums[i])
```

**Why this works:**
- If `current_sum + nums[i]` is negative, starting fresh is better!
- We're building the best subarray ending at position i

---

## 📈 Problem 1: Maximum Subarray (LeetCode 53)

### Problem Statement
Find the subarray with the largest sum.

**Examples:**
```python
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Subarray: [4,-1,2,1]

Input: [1]
Output: 1

Input: [5,4,-1,7,8]
Output: 23
Subarray: [5,4,-1,7,8] (entire array)
```

---

### 🔍 Detailed Dry Run

**Input:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

```python
Initialize:
  current_sum = -2  (first element)
  max_sum = -2

Index 1: nums[1] = 1
  Choice: start at 1 OR extend -2+1=-1
  current_sum = max(1, -1) = 1 ✓ (start fresh!)
  max_sum = max(-2, 1) = 1

Index 2: nums[2] = -3
  Choice: start at -3 OR extend 1+(-3)=-2
  current_sum = max(-3, -2) = -2 ✓ (extend)
  max_sum = max(1, -2) = 1

Index 3: nums[3] = 4
  Choice: start at 4 OR extend -2+4=2
  current_sum = max(4, 2) = 4 ✓ (start fresh!)
  max_sum = max(1, 4) = 4

Index 4: nums[4] = -1
  Choice: start at -1 OR extend 4+(-1)=3
  current_sum = max(-1, 3) = 3 ✓ (extend)
  max_sum = max(4, 3) = 4

Index 5: nums[5] = 2
  Choice: start at 2 OR extend 3+2=5
  current_sum = max(2, 5) = 5 ✓ (extend)
  max_sum = max(4, 5) = 5

Index 6: nums[6] = 1
  Choice: start at 1 OR extend 5+1=6
  current_sum = max(1, 6) = 6 ✓ (extend)
  max_sum = max(5, 6) = 6

Index 7: nums[7] = -5
  Choice: start at -5 OR extend 6+(-5)=1
  current_sum = max(-5, 1) = 1 ✓ (extend)
  max_sum = max(6, 1) = 6

Index 8: nums[8] = 4
  Choice: start at 4 OR extend 1+4=5
  current_sum = max(4, 5) = 5 ✓ (extend)
  max_sum = max(6, 5) = 6

Final answer: 6
Best subarray: [4, -1, 2, 1]
```

---

### 🎨 Visual Representation

```python
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Decision at each step:
-2: Start here (no choice)        sum=-2
 1: Start fresh!                   sum=1
-3: Extend (1-3=-2)                sum=-2
 4: Start fresh!                   sum=4  ←┐
-1: Extend (4-1=3)                 sum=3   │
 2: Extend (3+2=5)                 sum=5   │ Best
 1: Extend (5+1=6)                 sum=6   │ Subarray
-5: Extend (6-5=1)                 sum=1  ←┘
 4: Extend (1+4=5)                 sum=5

Maximum sum = 6
```

---

### ✅ Solution Code

```python
def maxSubArray(nums):
    # Initialize with first element
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Process remaining elements
    for i in range(1, len(nums)):
        # Decision: extend or start fresh
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**More explicit version:**
```python
def maxSubArray(nums):
    if not nums:
        return 0
    
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # If adding current makes it worse, start fresh
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
        else:
            current_sum += nums[i]
        
        # Track maximum seen so far
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single pass through array |
| Space | O(1) | Only two variables |

---

### 🎯 Another Example

**Input:** `[5, 4, -1, 7, 8]`

```
Index 0: current=5, max=5
Index 1: max(4, 5+4=9) = 9, max=9
Index 2: max(-1, 9-1=8) = 8, max=9
Index 3: max(7, 8+7=15) = 15, max=15
Index 4: max(8, 15+8=23) = 23, max=23

Result: 23 (entire array!)
```

---

## 🔍 Problem 2: Find All Duplicates (LeetCode 442)

### Problem Statement
Given array where `1 ≤ nums[i] ≤ n`, find all duplicates.

**Constraint:** Must run in O(n) time and O(1) extra space!

**Examples:**
```
Input: [4,3,2,7,8,2,3,1]
Output: [2,3]

Input: [1,1,2]
Output: [1]

Input: [1]
Output: []
```

---

### 💡 Clever Approach: Use Array as Hash Map!

**Key Insight:** Since all numbers are between 1 and n, we can use indices!

**Strategy:**
1. For each number `num`, go to index `abs(num) - 1`
2. If element at that index is **negative** → duplicate found!
3. Otherwise, **negate** the element (mark as seen)

**Why this works:**
- Numbers 1-n map to indices 0-(n-1)
- We use sign to mark "visited"
- Negative = already seen = duplicate!

---

### 🔍 Detailed Dry Run

**Input:** `[4, 3, 2, 7, 8, 2, 3, 1]`

```python
Initialize: result = []

Index 0: num = 4
  Check index 4-1 = 3
  nums[3] = 7 (positive)
  → Mark: nums[3] = -7
  Array: [4, 3, 2, -7, 8, 2, 3, 1]

Index 1: num = 3
  Check index 3-1 = 2
  nums[2] = 2 (positive)
  → Mark: nums[2] = -2
  Array: [4, 3, -2, -7, 8, 2, 3, 1]

Index 2: num = -2 (use abs = 2)
  Check index 2-1 = 1
  nums[1] = 3 (positive)
  → Mark: nums[1] = -3
  Array: [4, -3, -2, -7, 8, 2, 3, 1]

Index 3: num = -7 (use abs = 7)
  Check index 7-1 = 6
  nums[6] = 3 (positive)
  → Mark: nums[6] = -3
  Array: [4, -3, -2, -7, 8, 2, -3, 1]

Index 4: num = 8
  Check index 8-1 = 7
  nums[7] = 1 (positive)
  → Mark: nums[7] = -1
  Array: [4, -3, -2, -7, 8, 2, -3, -1]

Index 5: num = 2
  Check index 2-1 = 1
  nums[1] = -3 (NEGATIVE!) ← Duplicate!
  → Add 2 to result
  result = [2]

Index 6: num = -3 (use abs = 3)
  Check index 3-1 = 2
  nums[2] = -2 (NEGATIVE!) ← Duplicate!
  → Add 3 to result
  result = [2, 3]

Index 7: num = -1 (use abs = 1)
  Check index 1-1 = 0
  nums[0] = 4 (positive)
  → Mark: nums[0] = -4
  Array: [-4, -3, -2, -7, 8, 2, -3, -1]

Final result: [2, 3] ✓
```

---

### 🎨 Visual Understanding

```python
Original: [4, 3, 2, 7, 8, 2, 3, 1]
Indices:   0  1  2  3  4  5  6  7

Number 4 → mark index 3
Number 3 → mark index 2
Number 2 → mark index 1
Number 7 → mark index 6
Number 8 → mark index 7
Number 2 → check index 1 → ALREADY MARKED! Duplicate!
Number 3 → check index 2 → ALREADY MARKED! Duplicate!
Number 1 → mark index 0

Duplicates: [2, 3]
```

---

### ✅ Solution Code

```python
def findDuplicates(nums):
    res = []
    
    for num in nums:
        # Get absolute value (in case already negated)
        index = abs(num) - 1
        
        # If already negative, we've seen this number before
        if nums[index] < 0:
            res.append(abs(num))
        else:
            # Mark as seen by negating
            nums[index] = -nums[index]
    
    return res
```

**With comments:**
```python
def findDuplicates(nums):
    result = []
    
    for num in nums:
        # Map number to index (1-indexed → 0-indexed)
        index = abs(num) - 1
        
        # Check if we've visited this index before
        if nums[index] < 0:
            # Negative means duplicate!
            result.append(abs(num))
        else:
            # First time seeing, mark as negative
            nums[index] = -nums[index]
    
    return result
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single pass through array |
| Space | O(1) | In-place marking (output doesn't count) |

**Space note:** We modify the input array, but don't use extra data structures!

---

### 🎯 Why `abs(num)`?

```python
After marking some numbers:
[4, -3, -2, -7, 8, 2, -3, 1]
     ↑   ↑   ↑        ↑
  Negated elements

When we encounter -3 at index 1:
  We need the original value (3)
  abs(-3) = 3
  Then check index 3-1 = 2
```

---

## 🎓 Key Takeaways

### Kadane's Algorithm Pattern

```python
# Template
current_sum = nums[0]
max_sum = nums[0]

for i in range(1, len(nums)):
    # Key decision: extend or restart
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)

return max_sum
```

**Use when:**
- Finding maximum/minimum subarray sum
- Contiguous elements problem
- Need optimal subarray

---

### Array Index Marking Pattern

```python
# Template for finding duplicates (when 1 ≤ nums[i] ≤ n)
result = []

for num in nums:
    index = abs(num) - 1
    
    if nums[index] < 0:
        result.append(abs(num))  # Duplicate!
    else:
        nums[index] = -nums[index]  # Mark as seen

return result
```

**Use when:**
- Numbers in range [1, n]
- Need O(1) space
- Can modify input array
- Finding duplicates/missing numbers

---

## ✅ DO / ❌ AVOID

### ✅ DO - Kadane's

- Understand the "extend vs restart" decision
- Handle all negative arrays correctly
- Think about subarrays ending at each position
- Remember: sometimes restarting is better than extending

### ❌ AVOID - Kadane's

- Using nested loops (O(n²))
- Forgetting to initialize with first element
- Not considering single-element subarrays
- Assuming answer is always positive

### ✅ DO - Array Marking

- Use absolute value when reading marked numbers
- Check array bounds (1 ≤ nums[i] ≤ n)
- Understand you're modifying the input
- Use negative sign as "visited" flag

### ❌ AVOID - Array Marking

- Forgetting `abs()` when reading
- Using this trick when numbers aren't 1 to n
- Assuming array can't be modified
- Off-by-one errors (1-indexed to 0-indexed)

---

## 🔗 Related Topics

- [[05-Prefix-Sum-Technique]] - Related subarray technique
- [[Two-Pointer-Technique]] - Another array pattern
- [[09-Bit-Manipulation]] - More optimization tricks

---

## 📝 Practice Problems

### Easy
1. LeetCode 53 - Maximum Subarray
2. LeetCode 121 - Best Time to Buy and Sell Stock

### Medium
1. LeetCode 442 - Find All Duplicates in Array
2. LeetCode 152 - Maximum Product Subarray
3. LeetCode 918 - Maximum Sum Circular Subarray
4. LeetCode 448 - Find All Numbers Disappeared in Array

### Hard
1. LeetCode 363 - Max Sum of Rectangle No Larger Than K
2. LeetCode 1186 - Maximum Subarray Sum with One Deletion

---

**Previous**: [[06-Two-Pointer-Technique]] | **Next**: [[09-Bit-Manipulation]]

Back to: [[README of Frontend]]
