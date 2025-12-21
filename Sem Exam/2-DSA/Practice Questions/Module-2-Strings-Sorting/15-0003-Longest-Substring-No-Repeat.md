# ═══════════════════════════════════════
# 📌 [3] - Longest Substring Without Repeating Characters
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find length of longest substring without repeating characters.

## 💡 **Key Insight:**
Sliding window with HashSet/HashMap. Expand right, shrink left when duplicate found.

## 🔧 **Optimal Approach:**
**Algorithm:** Sliding Window + HashMap

**Steps:**
- HashMap stores last index of each char
- When duplicate found, move left past previous occurrence
- Track max length

## 💻 **Code (Run Directly):**
```python
def lengthOfLongestSubstring(s):
    charIndex = {}
    maxLen = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in charIndex and charIndex[char] >= left:
            left = charIndex[char] + 1
        charIndex[char] = right
        maxLen = max(maxLen, right - left + 1)
    
    return maxLen

# TEST
print("abcabcbb:", lengthOfLongestSubstring("abcabcbb"))
print("bbbbb:", lengthOfLongestSubstring("bbbbb"))
print("pwwkew:", lengthOfLongestSubstring("pwwkew"))
```

## 🏃 **Dry Run:**
**Example:** s = "abcabcbb"

```
right | char | left | charIndex      | maxLen
------|------|------|----------------|-------
0     | a    | 0    | {a:0}          | 1
1     | b    | 0    | {a:0,b:1}      | 2
2     | c    | 0    | {a:0,b:1,c:2}  | 3
3     | a    | 1    | {a:3,b:1,c:2}  | 3
4     | b    | 2    | {a:3,b:4,c:2}  | 3
5     | c    | 3    | {a:3,b:4,c:5}  | 3
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(min(n, 26))

## 🏷️ **Pattern Tag:** 
Sliding Window, HashMap

## ⚠️ **Gotcha:**
Only move left if duplicate is in current window (>= left).
