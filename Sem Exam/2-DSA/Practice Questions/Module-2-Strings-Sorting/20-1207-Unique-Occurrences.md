# ═══════════════════════════════════════
# 📌 [1207] - Unique Number of Occurrences
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if number of occurrences of each value is unique.

## 💡 **Key Insight:**
Count occurrences, check if all counts are unique using set.

## 🔧 **Optimal Approach:**
**Algorithm:** Counter + Set

**Steps:**
- Count occurrences of each value
- Check if length of counts == length of set(counts)

## 💻 **Code (Run Directly):**
```python
from collections import Counter

def uniqueOccurrences(arr):
    counts = Counter(arr).values()
    return len(counts) == len(set(counts))

# TEST
print("[1,2,2,1,1,3]:", uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print("[1,2]:", uniqueOccurrences([1, 2]))
print("[-3,0,1,-3,1,1,1,-3,10,0]:", uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
```

## 🏃 **Dry Run:**
**Example:** arr = [1, 2, 2, 1, 1, 3]

```
Counter = {1:3, 2:2, 3:1}
counts = [3, 2, 1]
set(counts) = {3, 2, 1}
len(3) == len(3) -> True
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashMap, Set

## ⚠️ **Gotcha:**
Comparing lengths catches duplicates in counts.
