# ═══════════════════════════════════════
# 📌 [268] - Missing Number
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find the missing number in range [0, n] from an array of n distinct numbers.

## 💡 **Key Insight:**
Math: Sum of 0 to n = n*(n+1)/2. Missing = expected - actual.

## 🔧 **Optimal Approach:**
**Algorithm:** Gauss Formula

**Steps:**
- Calculate expected sum: n * (n + 1) / 2
- Calculate actual sum of array
- Return expected - actual

## 💻 **Code (Run Directly):**
```python
def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

# TEST
nums = [3, 0, 1]
print("Input:", nums)
print("Output:", missingNumber(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [3, 0, 1] (n = 3)

```
expected = 3 * 4 / 2 = 6
actual = 3 + 0 + 1 = 4
missing = 6 - 4 = 2
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Math, Array

## ⚠️ **Gotcha:**
Use integer division (//) to avoid float issues.
