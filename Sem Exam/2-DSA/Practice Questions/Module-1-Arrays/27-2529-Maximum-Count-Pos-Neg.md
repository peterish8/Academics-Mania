# ═══════════════════════════════════════
# 📌 [2529] - Maximum Count of Positive and Negative
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Return max of (count of positives, count of negatives). Array is sorted.

## 💡 **Key Insight:**
Binary search for first positive and last negative.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search

**Steps:**
- Binary search for first index >= 1 (positives start)
- Binary search for first index >= 0 (negatives end before this)
- Count and return max

## 💻 **Code (Run Directly):**
```python
import bisect

def maximumCount(nums):
    pos_count = len(nums) - bisect.bisect_left(nums, 1)
    neg_count = bisect.bisect_left(nums, 0)
    return max(pos_count, neg_count)

# TEST
nums = [-2, -1, -1, 1, 2, 3]
print("Input:", nums)
print("Output:", maximumCount(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [-2, -1, -1, 1, 2, 3]

```
First index >= 1: index 3
Positives: 6 - 3 = 3

First index >= 0: index 3
Negatives: 3

max(3, 3) = 3
```

## ⏱️ **Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search, Array

## ⚠️ **Gotcha:**
Don't count zeros - they're neither positive nor negative.
