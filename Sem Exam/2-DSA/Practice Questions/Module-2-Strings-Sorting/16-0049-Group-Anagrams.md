# ═══════════════════════════════════════
# 📌 [49] - Group Anagrams
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Group strings that are anagrams of each other.

## 💡 **Key Insight:**
Anagrams have same sorted string. Use sorted string as key.

## 🔧 **Optimal Approach:**
**Algorithm:** HashMap with Sorted Key

**Steps:**
- For each string, sort it to get key
- Group strings with same key
- Return all groups

## 💻 **Code (Run Directly):**
```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# TEST
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Input:", strs)
print("Output:", groupAnagrams(strs))
```

## 🏃 **Dry Run:**
**Example:** strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

```
s   | key   | groups
----|-------|---------------------------
eat | aet   | {aet: [eat]}
tea | aet   | {aet: [eat, tea]}
tan | ant   | {aet: [...], ant: [tan]}
ate | aet   | {aet: [eat, tea, ate], ...}
nat | ant   | {ant: [tan, nat], ...}
bat | abt   | {abt: [bat], ...}
```

## ⏱️ **Complexity:**
- **Time:** O(n * k log k) where k = max string length
- **Space:** O(n * k)

## 🏷️ **Pattern Tag:** 
HashMap, String, Sorting

## ⚠️ **Gotcha:**
Alternative: use char count tuple as key (O(n*k) time).
