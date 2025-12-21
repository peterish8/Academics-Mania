# Bitwise Operators - Detailed Explanation

#bitwise-operators #binary #detailed-explanation #advanced

---

## 🎯 What are Bitwise Operators?

Bitwise operators work on the **binary representation** of numbers. They perform operations on individual bits (0s and 1s) that make up numbers in computer memory.

### Why Learn Bitwise Operators?
- **Computer Science**: Understanding how computers work internally
- **Optimization**: Some operations are faster using bitwise
- **Cryptography**: Used in encryption algorithms
- **Graphics**: Image processing and game development

---

## 🔢 Binary Number System Basics

### Understanding Binary
Every number in a computer is stored as binary (base-2):

```
Decimal → Binary
0       → 0000
1       → 0001
2       → 0010
3       → 0011
4       → 0100
5       → 0101
6       → 0110
7       → 0111
8       → 1000
```

### Converting Decimal to Binary
```python
# Python built-in function
print(bin(5))    # '0b101' (0b means binary)
print(bin(10))   # '0b1010'

# Manual method: Keep dividing by 2
# 5 ÷ 2 = 2 remainder 1
# 2 ÷ 2 = 1 remainder 0  
# 1 ÷ 2 = 0 remainder 1
# Read remainders bottom to top: 101
```

---

## 🎯 Bitwise AND (&)

### How it Works
- **Rule**: Result is 1 only if BOTH bits are 1
- **Otherwise**: Result is 0

### Truth Table
```
Bit A | Bit B | A & B
------|-------|------
  0   |   0   |   0
  0   |   1   |   0
  1   |   0   |   0
  1   |   1   |   1
```

### Step-by-Step Example: 5 & 3
```
Step 1: Convert to binary
5 = 101
3 = 011

Step 2: Compare each bit position
Position: 2 1 0
5:        1 0 1
3:        0 1 1
Result:   0 0 1  (only rightmost position has both 1s)

Step 3: Convert back to decimal
001 = 1

Therefore: 5 & 3 = 1
```

### Code Examples
```python
print(5 & 3)    # 1
print(10 & 5)   # 0
print(12 & 7)   # 4

# Practical use: Check if number is even
def is_even(n):
    return (n & 1) == 0  # If last bit is 0, number is even

print(is_even(4))   # True
print(is_even(5))   # False
```

---

## 🎯 Bitwise OR (|)

### How it Works
- **Rule**: Result is 1 if AT LEAST ONE bit is 1
- **Only 0**: When both bits are 0

### Truth Table
```
Bit A | Bit B | A | B
------|-------|------
  0   |   0   |   0
  0   |   1   |   1
  1   |   0   |   1
  1   |   1   |   1
```

### Step-by-Step Example: 5 | 3
```
Step 1: Convert to binary
5 = 101
3 = 011

Step 2: Compare each bit position
Position: 2 1 0
5:        1 0 1
3:        0 1 1
Result:   1 1 1  (at least one 1 in each position)

Step 3: Convert back to decimal
111 = 7

Therefore: 5 | 3 = 7
```

### Code Examples
```python
print(5 | 3)    # 7
print(9 | 5)    # 13
print(12 | 7)   # 15

# Practical use: Set specific bits
def set_bit(number, position):
    return number | (1 << position)

print(set_bit(5, 1))  # Sets bit at position 1: 5 | 2 = 7
```

---

## 🎯 Bitwise XOR (^)

### How it Works
- **Rule**: Result is 1 only if bits are DIFFERENT
- **Same bits**: Result is 0

### Truth Table
```
Bit A | Bit B | A ^ B
------|-------|------
  0   |   0   |   0
  0   |   1   |   1
  1   |   0   |   1
  1   |   1   |   0
```

### Step-by-Step Example: 5 ^ 3
```
Step 1: Convert to binary
5 = 101
3 = 011

Step 2: Compare each bit position
Position: 2 1 0
5:        1 0 1
3:        0 1 1
Result:   1 1 0  (different bits give 1)

Step 3: Convert back to decimal
110 = 6

Therefore: 5 ^ 3 = 6
```

### Code Examples
```python
print(5 ^ 3)    # 6
print(12 ^ 7)   # 11
print(8 ^ 8)    # 0 (same numbers give 0)

# Practical use: Swap variables without temp
a, b = 5, 3
a = a ^ b  # a = 5 ^ 3 = 6
b = a ^ b  # b = 6 ^ 3 = 5
a = a ^ b  # a = 6 ^ 5 = 3
print(a, b)  # 3, 5 (swapped!)
```

---

## 🎯 Bitwise NOT (~)

### How it Works
- **Rule**: Flips all bits (0 becomes 1, 1 becomes 0)
- **Result**: Usually negative due to two's complement

### Step-by-Step Example: ~5
```
Step 1: 5 in binary (8-bit representation)
5 = 00000101

Step 2: Flip all bits
~5 = 11111010

Step 3: This is -6 in two's complement
Therefore: ~5 = -6
```

### Code Examples
```python
print(~5)   # -6
print(~0)   # -1
print(~(-1)) # 0

# Formula: ~n = -(n + 1)
print(~10)  # -(10 + 1) = -11
```

---

## 🎯 Left Shift (<<)

### How it Works
- **Rule**: Shifts bits to the left, fills right with 0s
- **Effect**: Multiplies by 2^n (where n is shift amount)

### Step-by-Step Example: 5 << 2
```
Step 1: 5 in binary
5 = 101

Step 2: Shift left by 2 positions, add 0s on right
101 << 2 = 10100

Step 3: Convert back to decimal
10100 = 20

Therefore: 5 << 2 = 20 (same as 5 * 2^2 = 5 * 4 = 20)
```

### Code Examples
```python
print(5 << 1)   # 10 (5 * 2^1 = 10)
print(5 << 2)   # 20 (5 * 2^2 = 20)
print(3 << 3)   # 24 (3 * 2^3 = 24)

# Formula: n << k = n * (2^k)
print(7 << 2)   # 7 * 4 = 28
```

---

## 🎯 Right Shift (>>)

### How it Works
- **Rule**: Shifts bits to the right, discards rightmost bits
- **Effect**: Divides by 2^n (integer division)

### Step-by-Step Example: 20 >> 2
```
Step 1: 20 in binary
20 = 10100

Step 2: Shift right by 2 positions, remove rightmost bits
10100 >> 2 = 101

Step 3: Convert back to decimal
101 = 5

Therefore: 20 >> 2 = 5 (same as 20 // 2^2 = 20 // 4 = 5)
```

### Code Examples
```python
print(10 >> 1)  # 5 (10 // 2^1 = 5)
print(20 >> 2)  # 5 (20 // 2^2 = 5)
print(32 >> 3)  # 4 (32 // 2^3 = 4)

# Formula: n >> k = n // (2^k)
print(15 >> 2)  # 15 // 4 = 3
```

---

## 🎯 Practical Applications

### 1. Fast Multiplication/Division by Powers of 2
```python
# Instead of: n * 8
fast_multiply = n << 3  # Faster

# Instead of: n // 4
fast_divide = n >> 2    # Faster
```

### 2. Check if Number is Power of 2
```python
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_2(8))   # True (8 = 2^3)
print(is_power_of_2(10))  # False
```

### 3. Count Number of 1s in Binary
```python
def count_ones(n):
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1         # Shift right by 1
    return count

print(count_ones(7))  # 3 (binary: 111)
print(count_ones(8))  # 1 (binary: 1000)
```

### 4. Toggle Specific Bit
```python
def toggle_bit(number, position):
    return number ^ (1 << position)

print(toggle_bit(5, 1))  # Toggle bit at position 1
# 5 = 101, toggle position 1: 111 = 7
```

---

## 🎯 Common Exam Problems

### Problem 1: What is 10 & 5?
```
Solution:
10 = 1010
5  = 0101
&  = 0000 = 0
Answer: 0
```

### Problem 2: What is 9 | 5?
```
Solution:
9 = 1001
5 = 0101
| = 1101 = 13
Answer: 13
```

### Problem 3: What is 12 ^ 7?
```
Solution:
12 = 1100
7  = 0111
^  = 1011 = 11
Answer: 11
```

### Problem 4: What is 6 << 1?
```
Solution:
6 << 1 = 6 * 2^1 = 6 * 2 = 12
Answer: 12
```

### Problem 5: What is 32 >> 2?
```
Solution:
32 >> 2 = 32 // 2^2 = 32 // 4 = 8
Answer: 8
```

---

## 🎯 Quick Reference Table

| Operator | Name | Formula | Example | Result |
|----------|------|---------|---------|--------|
| & | AND | Bit-by-bit AND | 5 & 3 | 1 |
| \| | OR | Bit-by-bit OR | 5 \| 3 | 7 |
| ^ | XOR | Bit-by-bit XOR | 5 ^ 3 | 6 |
| ~ | NOT | Flip all bits | ~5 | -6 |
| << | Left Shift | n * 2^k | 5 << 2 | 20 |
| >> | Right Shift | n // 2^k | 20 >> 2 | 5 |

---

## 🚨 Common Mistakes

1. **Confusing with logical operators**: `&` vs `and`, `|` vs `or`
2. **Forgetting operator precedence**: Use parentheses
3. **Not understanding two's complement**: Why ~5 = -6
4. **Mixing up shift directions**: << multiplies, >> divides

---

## 💡 Memory Tips

- **AND (&)**: "Both bits must be 1"
- **OR (|)**: "At least one bit must be 1"  
- **XOR (^)**: "Bits must be different"
- **Left Shift (<<)**: "Left = multiply by 2"
- **Right Shift (>>)**: "Right = divide by 2"

**Return to main summary**: [[PDF-4-Operators-Quick-Summary]]