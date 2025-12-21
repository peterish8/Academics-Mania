# ⏱️ Time and Space Complexity

## 🎯 What You'll Learn
- How to measure algorithm efficiency
- Big O notation for time and space
- Analyzing loops and nested loops
- Practical problem: Power of Two

**Previous**: [[00-Getting-Started]] | **Next**: [[02-Basic-Array-Operations]]

---

## 📖 Understanding Complexity

### Why Does It Matter?
Imagine two ways to solve a problem:
- Solution A: Works in 1 second for 1000 items
- Solution B: Takes 10 minutes for 1000 items

**Complexity analysis** helps us choose Solution A!

---

## ⏰ Time Complexity

Time complexity measures **how many operations** run as input grows.

### O(1) - Constant Time
**No loops, fixed operations**

```python
# Always runs once, no matter what n is
def print_first(arr):
    print(arr[0])  # O(1)
```

**Example**: Accessing an array element by index
- `arr[5]` takes same time whether array has 10 or 10,000 elements

---

### O(n) - Linear Time
**One loop through n items**

```python
# Runs exactly n times
def print_all(arr):
    for item in arr:  # Loop runs n times
        print(item)
    # Time: O(n)
```

**Dry Run Example:**
```
arr = [1, 2, 3, 4, 5]  # n = 5
Loop runs: 5 times
```

**Real usage**: Searching for an item in unsorted array

---

### O(log n) - Logarithmic Time
**Input halves each iteration**

```python
# i doubles each time: 1 → 2 → 4 → 8 → 16...
def logarithmic_example(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2  # Doubles each time
    # Time: O(log n)
```

**Dry Run Example:**
```
n = 16
Step 1: i = 1  (1 < 16) ✓
Step 2: i = 2  (2 < 16) ✓
Step 3: i = 4  (4 < 16) ✓
Step 4: i = 8  (8 < 16) ✓
Step 5: i = 16 (16 < 16) ✗ STOP

Total steps: 4 = log₂(16)
```

**Real usage**: Binary search

---

### O(√n) - Square Root Time
**Loop until square root of n**

```python
# Loop runs until i² > n
def square_root_time(n):
    i = 1
    while i * i <= n:
        print(i)
        i += 1
    # Time: O(√n)
```

**Dry Run Example:**
```
n = 25
Step 1: i=1, 1×1=1   (1 ≤ 25) ✓
Step 2: i=2, 2×2=4   (4 ≤ 25) ✓
Step 3: i=3, 3×3=9   (9 ≤ 25) ✓
Step 4: i=4, 4×4=16  (16 ≤ 25) ✓
Step 5: i=5, 5×5=25  (25 ≤ 25) ✓
Step 6: i=6, 6×6=36  (36 ≤ 25) ✗ STOP

Total steps: 5 = √25
```

**Real usage**: Checking if number is prime

---

### O(n²) - Quadratic Time
**Nested loops, both run n times**

```python
# Outer loop: n times, Inner loop: n times
def print_pairs(arr):
    n = len(arr)
    for i in range(n):      # n times
        for j in range(n):  # n times for each i
            print(arr[i], arr[j])
    # Time: O(n × n) = O(n²)
```

**Dry Run Example:**
```
arr = [1, 2, 3]  # n = 3

Outer i=0: inner j=0,1,2 → 3 iterations
Outer i=1: inner j=0,1,2 → 3 iterations  
Outer i=2: inner j=0,1,2 → 3 iterations

Total: 3 × 3 = 9 = n²
```

**Real usage**: Bubble sort, comparing all pairs

---

## 📊 Comparison Chart

| Notation | Name | Example | n=10 | n=100 | n=1000 |
|----------|------|---------|------|-------|--------|
| O(1) | Constant | Array access | 1 | 1 | 1 |
| O(log n) | Logarithmic | Binary search | 3 | 7 | 10 |
| O(√n) | Square root | Prime check | 3 | 10 | 31 |
| O(n) | Linear | Simple loop | 10 | 100 | 1000 |
| O(n log n) | Linearithmic | Merge sort | 30 | 700 | 10000 |
| O(n²) | Quadratic | Nested loop | 100 | 10000 | 1000000 |

---

## 💾 Space Complexity

Space complexity measures **extra memory** used.

### O(1) - Constant Space
```python
def sum_array(arr):
    total = 0  # Only one variable
    for num in arr:
        total += num
    return total
# Space: O(1) - no extra arrays
```

### O(n) - Linear Space
```python
def create_copy(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr
# Space: O(n) - new array of size n
```

---

## 🔥 Problem: Power of Two (LeetCode 231)

### Problem Statement
Check if a number `n` is a power of two.

**Examples:**
- 1 → True (2⁰)
- 2 → True (2¹)
- 4 → True (2²)
- 16 → True (2⁴)
- 3 → False
- 10 → False

---

### 💡 Intuition: Binary Representation

**Key Insight**: Powers of 2 have **exactly ONE** bit set to 1 in binary.

```
Number  Decimal  Binary   Power of 2?
1       1        0001     ✓ (2⁰)
2       2        0010     ✓ (2¹)
3       3        0011     ✗ (two 1s)
4       4        0100     ✓ (2²)
5       5        0101     ✗ (two 1s)
8       8        1000     ✓ (2³)
10      10       1010     ✗ (two 1s)
16      16       10000    ✓ (2⁴)
```

---

### 🎯 The Bit Trick: `n & (n-1)`

**Rule**: If `n` is power of 2, then `n & (n-1) == 0`

**Why?**
- `n` has one 1 bit
- `n-1` flips all bits after that 1
- AND of these two = 0

---

### 🔍 Dry Run Example 1: n = 8 (Power of 2)

```
n   = 8  → Binary: 1000
n-1 = 7  → Binary: 0111

AND operation:
  1000  (8)
& 0111  (7)
------
  0000  (0) ✓

Since result = 0, 8 IS a power of 2
```

---

### 🔍 Dry Run Example 2: n = 10 (NOT Power of 2)

```
n   = 10 → Binary: 1010
n-1 = 9  → Binary: 1001

AND operation:
  1010  (10)
& 1001  (9)
------
  1000  (8) ✗

Since result ≠ 0, 10 is NOT a power of 2
```

---

### ✅ Final Solution

```python
def isPowerOfTwo(n: int) -> bool:
    # n must be positive and n & (n-1) must be 0
    return n > 0 and (n & (n - 1)) == 0
```

**Why `n > 0`?**
- 0 is not a power of 2
- Negative numbers are not powers of 2

---

### 📊 Complexity Analysis

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(1) | Single bit operation |
| Space | O(1) | No extra memory |

---

## 🎓 Key Takeaways

### ✅ DO
- Count loops to determine time complexity
- Consider extra memory for space complexity
- Use bit tricks when working with powers of 2
- Always check edge cases (negative, zero)

### ❌ AVOID
- Ignoring nested loops in time analysis
- Forgetting that dictionary/set lookups are O(1) on average
- Assuming faster code is always better (readability matters!)

---

## 🔗 Related Topics
- [[09-Bit-Manipulation]] - More bit tricks
- [[02-Basic-Array-Operations]] - Apply complexity analysis
- [[Complexity-Cheatsheet]] - Quick reference

---

## 📝 Practice Problems
1. **Easy**: LeetCode 231 - Power of Two
2. **Easy**: LeetCode 326 - Power of Three
3. **Medium**: LeetCode 342 - Power of Four

---

**Previous**: [[00-Getting-Started]] | **Next**: [[02-Basic-Array-Operations]]

Back to: [[README of Frontend]]
