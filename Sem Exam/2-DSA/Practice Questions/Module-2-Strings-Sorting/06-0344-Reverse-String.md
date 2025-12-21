# ═══════════════════════════════════════
# 📌 [344] - Reverse String
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Reverse array of characters in-place.

## 💡 **Key Insight:**
Two pointers, swap from ends moving inward.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- left = 0, right = len-1
- Swap s[left] and s[right]
- Move pointers inward

## 💻 **Code (Run Directly):**
```python
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# TEST
s = ["h", "e", "l", "l", "o"]
print("Input:", ["h", "e", "l", "l", "o"])
print("Output:", reverseString(s))
```

## 🏃 **Dry Run:**
**Example:** s = ["h", "e", "l", "l", "o"]

```
iter | left | right | swap    | result
-----|------|-------|---------|------------------
1    | 0    | 4     | h <-> o | [o, e, l, l, h]
2    | 1    | 3     | e <-> l | [o, l, l, e, h]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers, String

## ⚠️ **Gotcha:**
Must be in-place, don't create new array.
