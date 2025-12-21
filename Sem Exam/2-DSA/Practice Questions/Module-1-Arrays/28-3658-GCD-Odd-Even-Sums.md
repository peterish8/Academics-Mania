# ═══════════════════════════════════════
# 📌 [3658] - GCD of Odd and Even Sums
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Calculate sum of odd-indexed and even-indexed elements, return their GCD.

## 💡 **Key Insight:**
Simple traversal + math.gcd function.

## 🔧 **Optimal Approach:**
**Algorithm:** Traversal + GCD

**Steps:**
- Sum elements at even indices (0, 2, 4...)
- Sum elements at odd indices (1, 3, 5...)
- Return gcd(evenSum, oddSum)

## 💻 **Code (Run Directly):**
```python
from math import gcd

def gcdOddEven(nums):
    evenSum = sum(nums[::2])
    oddSum = sum(nums[1::2])
    return gcd(evenSum, oddSum)

# TEST
nums = [4, 8, 12, 16]
print("Input:", nums)
print("Even indices (0,2):", nums[::2])
print("Odd indices (1,3):", nums[1::2])
print("Output:", gcdOddEven(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [4, 8, 12, 16]

```
Even indices: [4, 12] -> sum = 16
Odd indices: [8, 16] -> sum = 24
gcd(16, 24) = 8
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Math, Array

## ⚠️ **Gotcha:**
Python slice [::2] gets even indices, [1::2] gets odd indices.
