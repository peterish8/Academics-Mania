# ═══════════════════════════════════════
# 📌 [172] - Factorial Trailing Zeroes
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Count trailing zeroes in n! (factorial).

## 💡 **Key Insight:**
Trailing zeros come from 10 = 2*5. Count 5s (always more 2s than 5s).

## 🔧 **Optimal Approach:**
**Algorithm:** Count factors of 5

**Steps:**
- Count n/5 + n/25 + n/125 + ...
- Each division counts multiples of powers of 5

## 💻 **Code (Run Directly):**
```python
def trailingZeroes(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# TEST
print("5!:", trailingZeroes(5))
print("10!:", trailingZeroes(10))
print("25!:", trailingZeroes(25))
```

## 🏃 **Dry Run:**
**Example:** n = 25

```
iter | n  | count
-----|-----|------
1    | 5   | 5
2    | 1   | 6

25! has 6 trailing zeros
(25/5=5, 25/25=1, 5+1=6)
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Math

## ⚠️ **Gotcha:**
25, 125, etc. contribute extra 5s.
