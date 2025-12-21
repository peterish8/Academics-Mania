# ═══════════════════════════════════════
# 📌 [1979] - Find Greatest Common Divisor of Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find GCD of smallest and largest elements in array.

## 💡 **Key Insight:**
Find min and max, then calculate their GCD.

## 🔧 **Optimal Approach:**
**Algorithm:** Min/Max + GCD

**Steps:**
- Find minimum and maximum
- Return gcd(min, max)

## 💻 **Code (Run Directly):**
```python
from math import gcd

def findGCD(nums):
    return gcd(min(nums), max(nums))

# TEST
print("[2,5,6,9,10]:", findGCD([2, 5, 6, 9, 10]))
print("[7,5,6,8,3]:", findGCD([7, 5, 6, 8, 3]))
print("[3,3]:", findGCD([3, 3]))
```

## 🏃 **Dry Run:**
**Example:** nums = [2, 5, 6, 9, 10]

```
min = 2
max = 10
gcd(2, 10) = 2
```

## ⏱️ **Complexity:**
- **Time:** O(n + log(min))
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Math, Array

## ⚠️ **Gotcha:**
Use built-in math.gcd for efficiency.
