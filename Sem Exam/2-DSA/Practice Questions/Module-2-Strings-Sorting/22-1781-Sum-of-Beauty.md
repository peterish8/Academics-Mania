# ═══════════════════════════════════════
# 📌 [1781] - Sum of Beauty of All Substrings
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Beauty = max frequency - min frequency. Sum beauty of all substrings.

## 💡 **Key Insight:**
Brute force all substrings, track char frequencies incrementally.

## 🔧 **Optimal Approach:**
**Algorithm:** Incremental Counting

**Steps:**
- For each start position
- Extend substring, update frequency count
- Calculate beauty (max - min non-zero)
- Add to total

## 💻 **Code (Run Directly):**
```python
def beautySum(s):
    total = 0
    n = len(s)
    
    for i in range(n):
        count = [0] * 26
        for j in range(i, n):
            count[ord(s[j]) - ord('a')] += 1
            non_zero = [c for c in count if c > 0]
            beauty = max(non_zero) - min(non_zero)
            total += beauty
    
    return total

# TEST
print("aabcb:", beautySum("aabcb"))
print("aabcbaa:", beautySum("aabcbaa"))
```

## 🏃 **Dry Run:**
**Example:** s = "aab"

```
Substrings:
"a" -> max=1, min=1, beauty=0
"aa" -> max=2, min=2, beauty=0
"aab" -> max=2, min=1, beauty=1
"a" -> beauty=0
"ab" -> beauty=0
"b" -> beauty=0

Total = 1
```

## ⏱️ **Complexity:**
- **Time:** O(n^2 * 26)
- **Space:** O(26)

## 🏷️ **Pattern Tag:** 
String, Frequency Count

## ⚠️ **Gotcha:**
Only count non-zero frequencies for min/max.
