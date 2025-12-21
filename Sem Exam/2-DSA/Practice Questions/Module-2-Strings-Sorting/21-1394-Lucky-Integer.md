# ═══════════════════════════════════════
# 📌 [1394] - Find Lucky Integer in an Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find largest integer where frequency equals value.

## 💡 **Key Insight:**
Count frequencies, find max where count[x] == x.

## 🔧 **Optimal Approach:**
**Algorithm:** Counter

**Steps:**
- Count occurrences
- Find max x where count[x] == x
- Return -1 if none found

## 💻 **Code (Run Directly):**
```python
from collections import Counter

def findLucky(arr):
    count = Counter(arr)
    lucky = -1
    for num, freq in count.items():
        if num == freq:
            lucky = max(lucky, num)
    return lucky

# TEST
print("[2,2,3,4]:", findLucky([2, 2, 3, 4]))
print("[1,2,2,3,3,3]:", findLucky([1, 2, 2, 3, 3, 3]))
print("[2,2,2,3,3]:", findLucky([2, 2, 2, 3, 3]))
```

## 🏃 **Dry Run:**
**Example:** arr = [2, 2, 3, 4]

```
count = {2:2, 3:1, 4:1}

num | freq | num == freq?
----|------|-------------
2   | 2    | Yes, lucky=2
3   | 1    | No
4   | 1    | No

Return 2
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashMap

## ⚠️ **Gotcha:**
Return largest lucky number, not first found.
