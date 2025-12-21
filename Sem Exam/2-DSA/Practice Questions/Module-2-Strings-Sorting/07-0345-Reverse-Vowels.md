# ═══════════════════════════════════════
# 📌 [345] - Reverse Vowels of a String
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Reverse only the vowels in a string.

## 💡 **Key Insight:**
Two pointers, swap vowels only.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- left = 0, right = len-1
- Skip non-vowels on both sides
- Swap vowels, move inward

## 💻 **Code (Run Directly):**
```python
def reverseVowels(s):
    s = list(s)
    vowels = set('aeiouAEIOU')
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

# TEST
print("hello:", reverseVowels("hello"))
print("leetcode:", reverseVowels("leetcode"))
```

## 🏃 **Dry Run:**
**Example:** s = "hello"

```
Vowels: e, o
left finds 'e' at 1
right finds 'o' at 4
Swap: "holle"
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n) for list conversion

## 🏷️ **Pattern Tag:** 
Two Pointers, String

## ⚠️ **Gotcha:**
Include both uppercase and lowercase vowels.
