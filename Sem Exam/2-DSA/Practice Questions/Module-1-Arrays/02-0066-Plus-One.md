# ═══════════════════════════════════════
# 📌 [66] - Plus One
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Add one to a large integer represented as array of digits.

## 💡 **Key Insight:**
Handle carry: if digit is 9, becomes 0 and carry propagates. All 9s need extra digit.

## 🔧 **Optimal Approach:**
**Algorithm:** Right-to-Left Traversal

**Steps:**
- Traverse from rightmost digit
- If < 9, add 1 and return
- If = 9, set to 0 (carry)
- If loop completes, prepend 1

## 💻 **Code (Run Directly):**
```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# TEST
print("Test 1:", plusOne([1, 2, 9]))
print("Test 2:", plusOne([9, 9, 9]))
```

## 🏃 **Dry Run:**
**Example:** digits = [1, 2, 9]

```
iter | i | digits[i] | action          | digits
-----|---|-----------|-----------------|----------
1    | 2 | 9         | Set to 0, carry | [1, 2, 0]
2    | 1 | 2         | Add 1, return   | [1, 3, 0]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Array, Math, Simulation

## ⚠️ **Gotcha:**
Don't convert to int and back - fails for very large numbers.
