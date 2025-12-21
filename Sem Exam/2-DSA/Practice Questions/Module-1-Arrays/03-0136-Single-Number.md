# ═══════════════════════════════════════
# 📌 [136] - Single Number
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find the element that appears only once. All others appear twice.

## 💡 **Key Insight:**
XOR magic: a ^ a = 0, a ^ 0 = a. XOR all numbers - pairs cancel, single remains.

## 🔧 **Optimal Approach:**
**Algorithm:** Bit Manipulation (XOR)

**Steps:**
- Initialize result = 0
- XOR every number with result
- Return result

## 💻 **Code (Run Directly):**
```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# TEST
nums = [4, 1, 2, 1, 2]
print("Input:", nums)
print("Output:", singleNumber(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [4, 1, 2, 1, 2]

```
iter | num | result
-----|-----|--------
0    | -   | 0
1    | 4   | 4
2    | 1   | 5
3    | 2   | 7
4    | 1   | 6
5    | 2   | 4
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Bit Manipulation, XOR

## ⚠️ **Gotcha:**
Only works when exactly one appears once, others exactly twice.
