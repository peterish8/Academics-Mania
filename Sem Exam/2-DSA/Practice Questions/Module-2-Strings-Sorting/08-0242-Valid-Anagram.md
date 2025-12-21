# ═══════════════════════════════════════
# 📌 [242] - Valid Anagram
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if t is anagram of s.

## 💡 **Key Insight:**
Same characters, same frequencies. Use Counter or sort.

## 🔧 **Optimal Approach:**
**Algorithm:** Character Count

**Steps:**
- Count frequency of each char in s
- Decrement for each char in t
- All counts should be 0

## 💻 **Code (Run Directly):**
```python
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

# Alternative without Counter
def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True

# TEST
print("anagram, nagaram:", isAnagram("anagram", "nagaram"))
print("rat, car:", isAnagram("rat", "car"))
```

## 🏃 **Dry Run:**
**Example:** s = "anagram", t = "nagaram"

```
Counter(s) = {a:3, n:1, g:1, r:1, m:1}
Counter(t) = {n:1, a:3, g:1, r:1, m:1}
Equal -> True
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1) - 26 letters max

## 🏷️ **Pattern Tag:** 
HashMap, String

## ⚠️ **Gotcha:**
Check length first for early exit.
