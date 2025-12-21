# ═══════════════════════════════════════
# 📌 [9] - Palindrome Number
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if integer reads same forwards and backwards.

## 💡 **Key Insight:**
Reverse half the number and compare. Or convert to string.

## 🔧 **Optimal Approach:**
**Algorithm:** Reverse Half

**Steps:**
- Negative or ends with 0 (except 0) = not palindrome
- Reverse second half by building reversed number
- Compare with first half

## 💻 **Code (Run Directly):**
```python
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    return x == reversed_half or x == reversed_half // 10

# TEST
print("121:", isPalindrome(121))
print("-121:", isPalindrome(-121))
print("10:", isPalindrome(10))
```

## 🏃 **Dry Run:**
**Example:** x = 12321

```
iter | x    | reversed_half
-----|------|---------------
1    | 1232 | 1
2    | 123  | 12
3    | 12   | 123

x(12) == reversed_half//10(12) -> True
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Math

## ⚠️ **Gotcha:**
Odd digits: compare x with reversed_half // 10.
