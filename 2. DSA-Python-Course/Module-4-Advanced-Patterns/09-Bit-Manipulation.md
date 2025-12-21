 by 2 | `n >> 1` | Fast division |
| Remove rightmost 1 | `n & (n-1)` | Count bits, power check |
| Get rightmost 1 | `n & -n` | Isolate lowest bit |

---

## ✅ DO / ❌ AVOID

### ✅ DO

- Use bit manipulation for optimization (often O(1))
- Remember powers of 2 have one bit set
- Use XOR for finding unique elements
- Test with small numbers first (easier to visualize)
- Draw out binary representation when confused

### ❌ AVOID

- Overusing bit tricks (readability matters!)
- Forgetting edge cases (0, negative numbers)
- Assuming all languages handle bits the same way
- Using bit tricks on floating-point numbers
- Ignoring the `n > 0` check for power of 2

---

## 🎨 Binary Representation in Python

```python
# Convert to binary string
bin(5)    # '0b101'
bin(10)   # '0b1010'

# Without '0b' prefix
format(5, 'b')   # '101'
format(10, 'b')  # '1010'

# With leading zeros
format(5, '08b')  # '00000101'

# Convert binary string to int
int('101', 2)     # 5
int('1010', 2)    # 10
```

---

## 🔗 Related Topics

- [[01-Time-and-Space-Complexity]] - O(1) bit operations
- [[08-Kadanes-Algorithm]] - Array optimization
- [[Problem-Index]] - All problems summary

---

## 📝 Practice Problems

### Easy
1. LeetCode 231 - Power of Two
2. LeetCode 326 - Power of Three (similar)
3. LeetCode 342 - Power of Four
4. LeetCode 191 - Number of 1 Bits
5. LeetCode 136 - Single Number

### Medium
1. LeetCode 137 - Single Number II
2. LeetCode 260 - Single Number III
3. LeetCode 371 - Sum of Two Integers (bit addition)
4. LeetCode 318 - Maximum Product of Word Lengths
5. LeetCode 201 - Bitwise AND of Numbers Range

### Hard
1. LeetCode 1009 - Complement of Base 10 Integer
2. LeetCode 898 - Bitwise ORs of Subarrays

---

## 🧪 Quick Reference Table

### Powers of 2 (0-10)

| Power | Decimal | Binary | Hex |
|-------|---------|--------|-----|
| 2⁰ | 1 | 1 | 0x1 |
| 2¹ | 2 | 10 | 0x2 |
| 2² | 4 | 100 | 0x4 |
| 2³ | 8 | 1000 | 0x8 |
| 2⁴ | 16 | 10000 | 0x10 |
| 2⁵ | 32 | 100000 | 0x20 |
| 2⁶ | 64 | 1000000 | 0x40 |
| 2⁷ | 128 | 10000000 | 0x80 |
| 2⁸ | 256 | 100000000 | 0x100 |
| 2⁹ | 512 | 1000000000 | 0x200 |
| 2¹⁰ | 1024 | 10000000000 | 0x400 |

---

## 💡 Fun Bit Facts

1. **XOR is its own inverse:**
   ```python
   a ^ b ^ b = a
   ```

2. **All bits set to 1:**
   ```python
   (1 << n) - 1  # n bits all set to 1
   Example: (1 << 4) - 1 = 15 = 1111
   ```

3. **Check if two numbers have opposite signs:**
   ```python
   def opposite_signs(x, y):
       return (x ^ y) < 0
   ```

4. **Absolute value without condition:**
   ```python
   def abs_value(n):
       mask = n >> 31  # -1 if negative, 0 if positive
       return (n + mask) ^ mask
   ```

5. **Min/Max without branches:**
   ```python
   def min_bitwise(a, b):
       return b ^ ((a ^ b) & -(a < b))
   
   def max_bitwise(a, b):
       return a ^ ((a ^ b) & -(a < b))
   ```

---

**Previous**: [[08-Kadanes-Algorithm]] | **Next**: [[Problem-Index]]

Back to: [[README of Frontend]]
