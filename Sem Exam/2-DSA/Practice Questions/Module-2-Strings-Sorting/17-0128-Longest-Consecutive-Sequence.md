# ═══════════════════════════════════════
# 📌 [128] - Longest Consecutive Sequence
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find length of longest consecutive sequence. Must be O(n).

## 💡 **Key Insight:**
Use HashSet. Only start counting from sequence start (num-1 not in set).

## 🔧 **Optimal Approach:**
**Algorithm:** HashSet with Smart Start

**Steps:**
- Put all numbers in set
- For each num, if num-1 not in set, it's sequence start
- Count consecutive nums from start
- Track max length

## 💻 **Code (Run Directly):**
```python
def longestConsecutive(nums):
    numSet = set(nums)
    maxLen = 0
    
    for num in numSet:
        if num - 1 not in numSet:
            current = num
            length = 1
            while current + 1 in numSet:
                current += 1
                length += 1
            maxLen = max(maxLen, length)
    
    return maxLen

# TEST
nums = [100, 4, 200, 1, 3, 2]
print("Input:", nums)
print("Output:", longestConsecutive(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [100, 4, 200, 1, 3, 2]

```
numSet = {100, 4, 200, 1, 3, 2}

num | num-1 in set? | action
----|---------------|--------
100 | 99 not in set | count: 100 -> len=1
4   | 3 in set      | skip
200 | 199 not in set| count: 200 -> len=1
1   | 0 not in set  | count: 1,2,3,4 -> len=4
```

## ⏱️ **Complexity:**
- **Time:** O(n) - each number visited at most twice
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashSet, Sequences

## ⚠️ **Gotcha:**
Only start counting from sequence start to avoid redundant work.
