# ═══════════════════════════════════════
# 📌 [14] - Longest Common Prefix
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find longest common prefix among array of strings.

## 💡 **Key Insight:**
Compare character by character across all strings.

## 🔧 **Optimal Approach:**
**Algorithm:** Vertical Scanning

**Steps:**
- Use first string as reference
- For each position, check if all strings have same char
- Stop when mismatch found

## 💻 **Code (Run Directly):**
```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]

# TEST
print("Test 1:", longestCommonPrefix(["flower", "flow", "flight"]))
print("Test 2:", longestCommonPrefix(["dog", "racecar", "car"]))
```

## 🏃 **Dry Run:**
**Example:** strs = ["flower", "flow", "flight"]

```
i | char | flower | flow | flight | match?
--|------|--------|------|--------|-------
0 | f    | f      | f    | f      | Yes
1 | l    | l      | l    | l      | Yes
2 | o    | o      | o    | i      | No!

Return "fl"
```

## ⏱️ **Complexity:**
- **Time:** O(S) where S = sum of all chars
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
String

## ⚠️ **Gotcha:**
Handle empty array and strings of different lengths.
