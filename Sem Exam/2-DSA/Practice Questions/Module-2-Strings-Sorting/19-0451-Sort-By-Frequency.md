# ═══════════════════════════════════════
# 📌 [451] - Sort Characters By Frequency
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Sort string so characters with higher frequency come first.

## 💡 **Key Insight:**
Count frequencies, sort by frequency, rebuild string.

## 🔧 **Optimal Approach:**
**Algorithm:** Counter + Sorting

**Steps:**
- Count character frequencies
- Sort characters by frequency (descending)
- Build result string

## 💻 **Code (Run Directly):**
```python
from collections import Counter

def frequencySort(s):
    count = Counter(s)
    sorted_chars = sorted(count.items(), key=lambda x: -x[1])
    return ''.join(char * freq for char, freq in sorted_chars)

# TEST
print("tree:", frequencySort("tree"))
print("cccaaa:", frequencySort("cccaaa"))
print("Aabb:", frequencySort("Aabb"))
```

## 🏃 **Dry Run:**
**Example:** s = "tree"

```
count = {t:1, r:1, e:2}
sorted = [(e,2), (t,1), (r,1)]
result = "ee" + "t" + "r" = "eetr"
```

## ⏱️ **Complexity:**
- **Time:** O(n log n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashMap, Sorting, String

## ⚠️ **Gotcha:**
Case sensitive - 'A' and 'a' are different.
