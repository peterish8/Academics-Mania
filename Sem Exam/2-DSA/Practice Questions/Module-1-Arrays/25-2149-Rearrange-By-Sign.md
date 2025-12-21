# ═══════════════════════════════════════
# 📌 [2149] - Rearrange Array Elements by Sign
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Rearrange to [pos, neg, pos, neg, ...]. Equal positive and negative count.

## 💡 **Key Insight:**
Two pointers: one for next positive position (0, 2, 4...), one for negative (1, 3, 5...).

## 🔧 **Optimal Approach:**
**Algorithm:** Two Index Pointers

**Steps:**
- posIdx = 0, negIdx = 1
- For each num: place at posIdx or negIdx, increment by 2

## 💻 **Code (Run Directly):**
```python
def rearrangeArray(nums):
    n = len(nums)
    result = [0] * n
    posIdx, negIdx = 0, 1
    
    for num in nums:
        if num > 0:
            result[posIdx] = num
            posIdx += 2
        else:
            result[negIdx] = num
            negIdx += 2
    
    return result

# TEST
nums = [3, 1, -2, -5, 2, -4]
print("Input:", nums)
print("Output:", rearrangeArray(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [3, 1, -2, -5, 2, -4]

```
num | posIdx | negIdx | result
----|--------|--------|------------------
3   | 0->2   | 1      | [3,_,_,_,_,_]
1   | 2->4   | 1      | [3,_,1,_,_,_]
-2  | 4      | 1->3   | [3,-2,1,_,_,_]
-5  | 4      | 3->5   | [3,-2,1,-5,_,_]
2   | 4->6   | 5      | [3,-2,1,-5,2,_]
-4  | 6      | 5->7   | [3,-2,1,-5,2,-4]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
Array, Two Pointers

## ⚠️ **Gotcha:**
Maintain relative order of positives and negatives.
