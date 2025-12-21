# ═══════════════════════════════════════
# 📌 [367] - Valid Perfect Square
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if num is a perfect square without using sqrt().

## 💡 **Key Insight:**
Binary search between 1 and num. Check mid*mid == num.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- left = 1, right = num
- mid*mid == num -> True
- mid*mid < num -> left = mid + 1
- mid*mid > num -> right = mid - 1

## 💻 **Code (Run Directly):**
```python
def isPerfectSquare(num):
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

# TEST
print("16:", isPerfectSquare(16))
print("14:", isPerfectSquare(14))
print("1:", isPerfectSquare(1))
```

## 🏃 **Dry Run:**
**Example:** num = 16

```
iter | left | right | mid | mid*mid
-----|------|-------|-----|--------
1    | 1    | 16    | 8   | 64 > 16
2    | 1    | 7     | 4   | 16 == 16 -> True
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Math

## ⚠️ **Gotcha:**
Use mid*mid, not sqrt. Handle num=1 edge case.
