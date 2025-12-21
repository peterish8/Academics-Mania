# 🔢 Bit Manipulation - Quick Ref

## 🎯 Core Tricks

### **Power of Two**
```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n-1)) == 0
```
**Why**: Powers of 2 have exactly one bit set

### **Single Number (XOR)**
```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```
**Why**: `a ^ a = 0`, `a ^ 0 = a`

### **Count 1 Bits**
```python
def hammingWeight(n):
    count = 0
    while n:
        count += 1
        n &= n - 1  # Remove rightmost 1
    return count
```

### **Missing Number**
```python
def missingNumber(nums):
    n = len(nums)
    result = n
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

---

## ⚡ **Bit Operations**

```python
# Basic operations
x & 1        # Check if odd
x & (x-1)    # Remove rightmost 1 bit
x | (1 << i) # Set bit i
x & ~(1 << i)# Clear bit i
x ^ (1 << i) # Toggle bit i

# Common patterns
a ^ a = 0    # Cancel out
a ^ 0 = a    # Identity
a & (a-1)    # Remove rightmost 1
```

---

## 🧠 **When to Use**
- **Powers of 2**: Use `n & (n-1) == 0`
- **Find unique**: Use XOR cancellation
- **Count bits**: Use `n & (n-1)` trick
- **Missing number**: XOR all indices and values

Back to: [[README of DSA Quick Ref]]