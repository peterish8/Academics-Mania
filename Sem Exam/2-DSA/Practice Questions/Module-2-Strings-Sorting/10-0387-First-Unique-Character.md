# ═══════════════════════════════════════
# 📌 [387] - First Unique Character in a String
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find index of first non-repeating character.

## 💡 **Key Insight:**
Count frequencies first, then find first with count 1.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pass with Counter

**Steps:**
- First pass: count all characters
- Second pass: find first with count == 1

## 💻 **Code (Run Directly):**
```python
from collections import Counter

def firstUniqChar(s):
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

# TEST
print("leetcode:", firstUniqChar("leetcode"))
print("loveleetcode:", firstUniqChar("loveleetcode"))
print("aabb:", firstUniqChar("aabb"))
```

## 🏃 **Dry Run:**
**Example:** s = "leetcode"

```
count = {l:1, e:3, t:1, c:1, o:1, d:1}

i | c | count[c] | unique?
--|---|----------|--------
0 | l | 1        | Yes! Return 0
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1) - 26 letters max

## 🏷️ **Pattern Tag:** 
HashMap, String

## ⚠️ **Gotcha:**
Return -1 if no unique character exists.
