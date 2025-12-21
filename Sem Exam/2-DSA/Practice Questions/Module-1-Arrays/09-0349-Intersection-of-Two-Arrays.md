# ═══════════════════════════════════════
# 📌 [349] - Intersection of Two Arrays
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Return unique intersection of two arrays.

## 💡 **Key Insight:**
Convert one to set for O(1) lookups. Check second array against set.

## 🔧 **Optimal Approach:**
**Algorithm:** HashSet

**Steps:**
- Convert nums1 to set
- For each in nums2: if in set1, add to result set

## 💻 **Code (Run Directly):**
```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return list(result)

# TEST
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print("nums1:", nums1, "nums2:", nums2)
print("Output:", intersection(nums1, nums2))
```

## 🏃 **Dry Run:**
**Example:** nums1 = [1,2,2,1], nums2 = [2,2]

```
set1 = {1, 2}

iter | num | in set1? | result
-----|-----|----------|--------
1    | 2   | Yes      | {2}
2    | 2   | Yes      | {2}
```

## ⏱️ **Complexity:**
- **Time:** O(n + m)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashSet, Array

## ⚠️ **Gotcha:**
Result must be unique - use set for result.
