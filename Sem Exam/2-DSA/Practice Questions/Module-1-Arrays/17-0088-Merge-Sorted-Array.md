# ═══════════════════════════════════════
# 📌 [88] - Merge Sorted Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Merge nums2 into nums1 (has extra space). Both sorted. In-place.

## 💡 **Key Insight:**
Start from END. Place larger at end of nums1. Avoids overwriting.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers from End

**Steps:**
- p1 at m-1, p2 at n-1, pos at m+n-1
- Compare, place larger at pos
- Decrement pointers

## 💻 **Code (Run Directly):**
```python
def merge(nums1, m, nums2, n):
    p1, p2, pos = m - 1, n - 1, m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[pos] = nums1[p1]
            p1 -= 1
        else:
            nums1[pos] = nums2[p2]
            p2 -= 1
        pos -= 1
    return nums1

# TEST
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print("nums1:", [1,2,3,0,0,0], "nums2:", nums2)
print("Output:", merge(nums1, m, nums2, n))
```

## 🏃 **Dry Run:**
**Example:** nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]

```
p1 | p2 | pos | compare | nums1
---|----|----|---------|------------------
2  | 2  | 5  | 3 < 6   | [1,2,3,0,0,6]
2  | 1  | 4  | 3 < 5   | [1,2,3,0,5,6]
2  | 0  | 3  | 3 > 2   | [1,2,3,3,5,6]
1  | 0  | 2  | 2 = 2   | [1,2,2,3,5,6]
```

## ⏱️ **Complexity:**
- **Time:** O(m + n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers, Merge

## ⚠️ **Gotcha:**
Only check p2 >= 0. If p2 finishes, p1 elements already in place.
