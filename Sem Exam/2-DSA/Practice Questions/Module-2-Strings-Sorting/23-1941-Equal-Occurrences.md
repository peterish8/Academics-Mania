# ═══════════════════════════════════════
# 📌 [1941] - Check if All Characters Have Equal Number of Occurrences
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if all characters appear same number of times.

## 💡 **Key Insight:**
Count frequencies, check if all counts are equal.

## 🔧 **Optimal Approach:**
**Algorithm:** Counter + Set

**Steps:**
- Count character frequencies
- All frequencies should be same (set size = 1)

## 💻 **Code (Run Directly):**
```python
from collections import Counter

def areOccurrencesEqual(s):
    counts = Counter(s).values()
    return len(set(counts)) == 1

# TEST
print("abacbc:", areOccurrencesEqual("abacbc"))
print("aaabb:", areOccurrencesEqual("aaabb"))
```

## 🏃 **Dry Run:**
**Example:** s = "abacbc"

```
Counter = {a:2, b:2, c:2}
counts = [2, 2, 2]
set(counts) = {2}
len == 1 -> True
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1) - 26 chars max

## 🏷️ **Pattern Tag:** 
HashMap, String

## ⚠️ **Gotcha:**
Empty string is technically valid.
