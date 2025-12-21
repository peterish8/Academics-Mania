# 🎯 Pattern Recognition Guide

## 🌟 Master Problem-Solving with Visual Pattern Recognition

This comprehensive guide helps you **instantly identify** which DSA pattern to use for any problem!

**Back to**: [[README DSA Complete]]

---

## 🎨 Color-Coded Pattern Categories

> [!SUCCESS] **🟢 Array Patterns**
> Perfect for list/array manipulations

> [!INFO] **🔵 String Patterns** 
> Specialized for text processing

> [!WARNING] **🟡 Mathematical Patterns**
> For numerical computations

> [!DANGER] **🔴 Advanced Patterns**
> Complex optimization techniques

---

## 🔍 How to Identify Patterns

### 🎯 Step 1: Read the Problem Carefully
Look for **keywords** that hint at the pattern.

### 📊 Step 2: Check Constraints
- Array size and value ranges
- Time/space complexity limits
- Input characteristics (sorted, etc.)

### 🧩 Step 3: Match Pattern
Use decision tree to find the right technique.

---

## 📖 Pattern Index

### 1️⃣ Array Patterns → [[02-Basic-Array-Operations]]

**Keywords to look for:**
- "contiguous elements"
- "in-place"
- "remove duplicates"
- "rotate"
- "merge sorted"

**Example Problems:**
- Remove Duplicates from Sorted Array
- Rotate Array
- Merge Sorted Arrays
- Plus One

**When to use:**
- Need O(1) space
- Array is sorted
- In-place modification allowed

---

### 2️⃣ Two Pointer Pattern → [[06-Two-Pointer-Technique]]

**Keywords to look for:**
- "sorted array"
- "find pair"
- "target sum"
- "two elements"
- "opposite ends"

**Example Problems:**
- Two Sum II (sorted input)
- Best Time to Buy and Sell Stock
- Remove Duplicates

**When to use:**
- Array is sorted
- Looking for pairs
- Need to reduce from both ends
- O(n) time required

**Visual:**
```
[1, 2, 3, 4, 5]
 ↑           ↑
left       right
```

---

### 3️⃣ Frequency Map Pattern → [[03-Character-Frequency-Problems]]

**Keywords to look for:**
- "count occurrences"
- "frequency"
- "most common"
- "duplicates"
- "anagram"

**Example Problems:**
- Sort Characters by Frequency
- Top K Frequent Elements
- Jewels and Stones
- Valid Anagram

**When to use:**
- Need to count elements
- Finding duplicates/unique elements
- Grouping by value
- O(1) lookup needed

**Template:**
```python
freq = {}
for item in collection:
    freq[item] = freq.get(item, 0) + 1
```

---

### 4️⃣ Prefix Sum Pattern → [[05-Prefix-Sum-Technique]]

**Keywords to look for:**
- "subarray sum"
- "range sum"
- "cumulative"
- "running total"
- "balance point"

**Example Problems:**
- Running Sum of Array
- Find Middle Index
- Subarray Sum Equals K

**When to use:**
- Multiple range sum queries
- Finding balance/pivot points
- Subarray problems
- Need O(1) range queries

**Formula:**
```python
prefix[i] = prefix[i-1] + nums[i]
range_sum(i, j) = prefix[j] - prefix[i-1]
```

---

### 5️⃣ Sliding Window Pattern → [[05-Prefix-Sum-Technique]]

**Keywords to look for:**
- "minimum/maximum subarray"
- "substring"
- "consecutive elements"
- "window size"
- "at most K"

**Example Problems:**
- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters
- Maximum Average Subarray

**When to use:**
- Dynamic window size
- Contiguous elements
- Optimization over subarrays
- O(n) solution needed

**Visual:**
```
[1, 2, 3, 4, 5]
 ↑     ↑
 L     R  (window expands/shrinks)
```

---

### 6️⃣ Kadane's Algorithm → [[08-Kadanes-Algorithm]]

**Keywords to look for:**
- "maximum subarray sum"
- "maximum product"
- "contiguous subarray"
- "largest sum"

**Example Problems:**
- Maximum Subarray
- Maximum Product Subarray
- Maximum Sum Circular Subarray

**When to use:**
- Finding optimal subarray
- Need O(n) time
- "Extend vs restart" decision

**Core idea:**
```python
current = max(nums[i], current + nums[i])
max_sum = max(max_sum, current)
```

---

### 7️⃣ Bit Manipulation → [[09-Bit-Manipulation]]

**Keywords to look for:**
- "power of two"
- "single number"
- "XOR"
- "binary"
- "O(1) space, no extra structures"

**Example Problems:**
- Power of Two
- Single Number
- Number of 1 Bits

**When to use:**
- Numbers are powers of 2
- Finding unique element
- O(1) time/space needed
- Binary representation matters

**Common tricks:**
```python
n & (n-1) == 0  # Power of 2
n & 1           # Check even/odd
a ^ a == 0      # Cancel duplicates
```

---

### 8️⃣ Array Index Marking → [[08-Kadanes-Algorithm]]

**Keywords to look for:**
- "numbers are 1 to n"
- "find duplicates"
- "find missing"
- "O(1) extra space"

**Example Problems:**
- Find All Duplicates in Array
- Find All Disappeared Numbers
- First Missing Positive

**When to use:**
- Values in range [1, n]
- O(1) space constraint
- Can modify input array
- Finding missing/duplicate numbers

**Technique:**
```python
index = abs(num) - 1
if nums[index] < 0:
    # Duplicate found!
nums[index] = -nums[index]
```

---

## 🎯 Decision Tree

```
Start Here
│
├─ Array sorted?
│  ├─ Yes → Try TWO POINTERS
│  └─ No → Continue
│
├─ Need to count/group?
│  └─ Yes → Use FREQUENCY MAP
│
├─ Range sum queries?
│  └─ Yes → Use PREFIX SUM
│
├─ Contiguous subarray optimization?
│  ├─ Sum → KADANE'S ALGORITHM
│  └─ Size → SLIDING WINDOW
│
├─ Binary/powers of 2?
│  └─ Yes → BIT MANIPULATION
│
├─ Values 1 to n, find duplicates?
│  └─ Yes → INDEX MARKING
│
└─ Still stuck? → Review problem constraints
```

---

## 🧩 Pattern Combination Examples

### Example 1: Subarray Sum Equals K
**Patterns:** Prefix Sum + Frequency Map
```
Use prefix sum to calculate cumulative sums
Use hashmap to store prefix sums seen
If (current_sum - k) exists in map → found subarray!
```

### Example 2: 3Sum
**Patterns:** Sorting + Two Pointers
```
Sort array first
Fix one element
Use two pointers on remaining array
```

### Example 3: Longest Substring Without Repeating
**Patterns:** Sliding Window + Frequency Map
```
Window tracks current substring
HashMap tracks character positions
Shrink window when duplicate found
```

---

## ⚡ Quick Pattern Selector

| If you see... | Try this pattern |
|---------------|------------------|
| "sorted array" | Two Pointers |
| "count frequency" | Frequency Map |
| "subarray sum" | Prefix Sum or Kadane's |
| "at most/at least K" | Sliding Window |
| "power of 2" | Bit Manipulation |
| "1 ≤ nums[i] ≤ n" | Index Marking |
| "find pair with sum" | Two Pointers (if sorted) or HashMap |
| "maximum subarray" | Kadane's Algorithm |
| "continuous elements" | Sliding Window |
| "unique element" | XOR / Bit Manipulation |

---

## 🎓 Practice: Identify the Pattern

### Problem 1
**"Find the longest subarray with sum at most K"**

<details>
<summary>Answer</summary>

**Pattern:** Sliding Window

**Why?**
- "longest subarray" → contiguous
- "at most K" → condition-based window
- Need dynamic window size

**Approach:** Expand window while sum ≤ K, shrink when sum > K
</details>

---

### Problem 2
**"Count subarrays where sum equals K"**

<details>
<summary>Answer</summary>

**Pattern:** Prefix Sum + Frequency Map

**Why?**
- "subarray sum" → prefix sum
- "count" → need to track occurrences
- HashMap to store prefix sums

**Approach:** Track (prefix_sum - K) in hashmap
</details>

---

### Problem 3
**"Find three numbers in sorted array that sum to target"**

<details>
<summary>Answer</summary>

**Pattern:** Two Pointers

**Why?**
- "sorted array" → two pointers work
- Fix one element, use two pointers for remaining two

**Approach:** Fix element i, two pointers on [i+1, n-1]
</details>

---

### Problem 4
**"Given array where each element appears twice except one, find the unique one"**

<details>
<summary>Answer</summary>

**Pattern:** Bit Manipulation (XOR)

**Why?**
- "appears twice" → XOR cancels pairs
- a ^ a = 0
- Need O(1) space

**Approach:** XOR all elements together
</details>

---

## 📚 Pattern Cheat Sheet

### Time Complexity by Pattern

| Pattern | Typical Time | Typical Space |
|---------|--------------|---------------|
| Two Pointers | O(n) | O(1) |
| Frequency Map | O(n) | O(k) where k = unique |
| Prefix Sum | O(n) build, O(1) query | O(n) |
| Sliding Window | O(n) | O(1) or O(k) |
| Kadane's | O(n) | O(1) |
| Bit Manipulation | O(1) to O(n) | O(1) |
| Index Marking | O(n) | O(1) |

---

**Back to**: [[README DSA Complete]]
