# ═══════════════════════════════════════
# 📌 [58] - Length of Last Word
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Return length of last word in string.

## 💡 **Key Insight:**
Strip trailing spaces, then count chars until space.

## 🔧 **Optimal Approach:**
**Algorithm:** Right to Left Scan

**Steps:**
- Strip trailing spaces
- Count from end until space or start

## 💻 **Code (Run Directly):**
```python
def lengthOfLastWord(s):
    s = s.rstrip()
    length = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            break
        length += 1
    return length

# TEST
print("'Hello World':", lengthOfLastWord("Hello World"))
print("'   fly me   to   the moon  ':", lengthOfLastWord("   fly me   to   the moon  "))
```

## 🏃 **Dry Run:**
**Example:** s = "Hello World"

```
After rstrip: "Hello World"

i  | char | length
---|------|-------
10 | d    | 1
9  | l    | 2
8  | r    | 3
7  | o    | 4
6  | W    | 5
5  | ' '  | break
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
String

## ⚠️ **Gotcha:**
Handle trailing spaces with rstrip().
