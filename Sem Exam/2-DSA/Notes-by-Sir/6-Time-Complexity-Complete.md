# ⏱️ Time Complexity - Complete Guide

## 🎯 **What is Time Complexity?**

> [!SUCCESS] **Definition**: Time complexity tells us how many times a loop (or operation) runs as input size increases.

---

## 📊 **Different Time Complexities**

### **(a) O(1) – Constant Time**

> Runs the **same number of steps**, no matter the input size.

```python
def constant_time(n):
    print("Hello")  # Runs only once
    return n + 1    # Single operation

# TEST
constant_time(5)
constant_time(1000000)
print("Both run in same time!")
```

**Complexity:** O(1) ⚡

---

### **(b) O(n) – Linear Time**

> Loop runs exactly **n times**.

```python
def linear_time(n):
    for i in range(n):
        print(i, end=" ")
    print()

# TEST
print("n=5:")
linear_time(5)
print("n=10:")
linear_time(10)
```

**Complexity:** O(n) - If n doubles, time doubles!

---

### **(c) O(log n) – Logarithmic Time**

> Loop **divides/multiplies** the problem each time (input shrinks quickly).

```python
def logarithmic_time(n):
    i = 1
    steps = 0
    while i < n:
        i = i * 2  # Grows exponentially
        steps += 1
    return steps

# TEST
print("n=16, steps:", logarithmic_time(16))   # 4 steps
print("n=32, steps:", logarithmic_time(32))   # 5 steps
print("n=1024, steps:", logarithmic_time(1024))  # 10 steps
```

**Pattern:** `i = 1 → 2 → 4 → 8 → 16 → ...`
**Steps:** log₂(n)
**Complexity:** O(log n) ⚡

---

### **(d) O(√n) – Square Root Time**

> Loop runs only up to **√n**, not full n.

```python
def sqrt_time(n):
    i = 1
    steps = 0
    while i * i <= n:
        print(i, end=" ")
        i += 1
        steps += 1
    print(f"-> {steps} steps")

# TEST
print("n=25:")
sqrt_time(25)  # 1,2,3,4,5 → 5 steps (√25 = 5)
print("n=100:")
sqrt_time(100)  # 10 steps (√100 = 10)
```

**Complexity:** O(√n)

---

### **(e) O(n²) – Quadratic Time**

> **Two nested loops** - each runs n times.

```python
def quadratic_time(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

# TEST
print("n=3, operations:", quadratic_time(3))   # 9
print("n=5, operations:", quadratic_time(5))   # 25
print("n=10, operations:", quadratic_time(10)) # 100
```

**Total:** n × n = O(n²) ❌ Slow for large n!

---

## 💾 **Space Complexity**

### **O(1) Space** - No extra storage
```python
for i in range(n):
    print(i)  # Only uses loop variable
# Space: O(1)
```

### **O(n) Space** - Stores n elements
```python
arr = [0] * n  # Creates array of size n
# Space: O(n)
```

---

## 🔢 **LeetCode 231: Power of Two**

### 📋 **Problem**
Check if a number `n` is a power of two.

**Examples:**
- ✅ True: 1, 2, 4, 8, 16, 32
- ❌ False: 3, 5, 6, 10

---

### 🧠 **Key Insight: Binary Pattern**

> [!TIP] Powers of two have **only one 1 bit** in binary!

| Number | Binary |
|--------|--------|
| 1 | 0001 |
| 2 | 0010 |
| 4 | 0100 |
| 8 | 1000 |
| 16 | 10000 |

---

### ⚡ **Bit Trick: `n & (n-1) == 0`**

**Why it works:**
- `n` has one 1 in binary
- `n-1` flips all bits after that 1
- `n & (n-1)` = 0

**Example: n = 8**
```
n   = 8  = 1000
n-1 = 7  = 0111
n & (n-1) = 0000 ✅ Power of 2!
```

**Counter-example: n = 10**
```
n   = 10 = 1010
n-1 = 9  = 1001
n & (n-1) = 1000 ≠ 0 ❌ Not power of 2!
```

---

### 💻 **Code (Runnable)**

```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# TEST
print("1:", isPowerOfTwo(1))
print("2:", isPowerOfTwo(2))
print("8:", isPowerOfTwo(8))
print("16:", isPowerOfTwo(16))
print("---")
print("3:", isPowerOfTwo(3))
print("10:", isPowerOfTwo(10))
print("0:", isPowerOfTwo(0))
```

**Time:** O(1) | **Space:** O(1) ⚡

---

## 📊 **Summary Table**

| Complexity | Pattern | Example |
|------------|---------|---------|
| **O(1)** | Fixed operations | Single print |
| **O(log n)** | Loop multiplies/divides | Binary search |
| **O(√n)** | Loop to square root | Factor finding |
| **O(n)** | Single loop | Linear search |
| **O(n²)** | Nested loops | Bubble sort |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **O(1)**: Same time always
> - **O(log n)**: Halving each step (binary search)
> - **O(n)**: One loop
> - **O(n²)**: Two nested loops
> - **Power of 2**: `n & (n-1) == 0` magic trick!

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What's the time complexity of `for i in range(n): for j in range(n):`?
> > [!SUCCESS]- Answer
> > O(n²) - nested loops, each runs n times.

> [!QUESTION] **Q2**: If n=1000, how many steps for O(log n)?
> > [!SUCCESS]- Answer
> > About 10 steps (log₂(1000) ≈ 10).

> [!QUESTION] **Q3**: Why is `n > 0` needed in isPowerOfTwo?
> > [!SUCCESS]- Answer
> > 0 and negative numbers are not powers of 2. Without this check, `0 & -1` would pass.

> [!QUESTION] **Q4**: What's faster: O(n) or O(log n)?
> > [!SUCCESS]- Answer
> > O(log n) is much faster. For n=1000: O(n)=1000 ops, O(log n)=10 ops.

> [!QUESTION] **Q5**: Which data structure operation is O(1)?
> > [!SUCCESS]- Answer
> > Array access by index `arr[5]`, HashMap lookup, Stack push/pop.

---

Back to: [[Sem Exam/2-DSA/DSA-Hub|DSA Hub]]
