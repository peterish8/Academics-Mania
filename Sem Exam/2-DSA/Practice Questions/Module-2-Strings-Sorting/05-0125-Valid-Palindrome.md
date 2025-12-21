# ═══════════════════════════════════════
# 📌 [125] - Valid Palindrome
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if string is palindrome considering only alphanumeric, case-insensitive.

## 💡 **Key Insight:**
Two pointers from ends, skip non-alphanumeric, compare lowercase.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- left = 0, right = len-1
- Skip non-alphanumeric chars
- Compare lowercase chars
- Move pointers inward

## 💻 **Code (Run Directly):**
```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

# TEST
print("'A man, a plan, a canal: Panama':", isPalindrome("A man, a plan, a canal: Panama"))
print("'race a car':", isPalindrome("race a car"))
```

## 🏃 **Dry Run:**
**Example:** s = "A man, a plan, a canal: Panama"

```
Compare pairs (after cleaning):
A <-> a -> match
m <-> m -> match
a <-> a -> match
n <-> n -> match
... all match -> True
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers, String

## ⚠️ **Gotcha:**
Use isalnum() to check alphanumeric, lower() for case.
