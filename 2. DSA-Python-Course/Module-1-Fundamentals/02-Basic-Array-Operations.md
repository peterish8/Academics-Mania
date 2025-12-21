2

p1 = 2, p2 = 2, p = 5
```

**Step-by-step:**

```
Step 1: Compare nums1[p1] vs nums2[p2]
  nums1[2]=3 vs nums2[2]=6
  6 > 3
  → nums1[5] = 6
  → p2 -= 1, p -= 1
  Array: [1, 2, 3, 0, 0, 6]
  State: p1=2, p2=1, p=4

Step 2: Compare nums1[p1] vs nums2[p2]
  nums1[2]=3 vs nums2[1]=5
  5 > 3
  → nums1[4] = 5
  → p2 -= 1, p -= 1
  Array: [1, 2, 3, 0, 5, 6]
  State: p1=2, p2=0, p=3

Step 3: Compare nums1[p1] vs nums2[p2]
  nums1[2]=3 vs nums2[0]=2
  3 > 2
  → nums1[3] = 3
  → p1 -= 1, p -= 1
  Array: [1, 2, 3, 3, 5, 6]
  State: p1=1, p2=0, p=2

Step 4: Compare nums1[p1] vs nums2[p2]
  nums1[1]=2 vs nums2[0]=2
  2 = 2 (pick from nums2)
  → nums1[2] = 2
  → p2 -= 1, p -= 1
  Array: [1, 2, 2, 3, 5, 6]
  State: p1=1, p2=-1, p=1

Step 5: p2 < 0, so loop ends
  Remaining nums1 elements already in place

Result: [1, 2, 2, 3, 5, 6] ✓
```

---

### ✅ Solution Code

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        # Three pointers
        p1 = m - 1  # Last element of nums1
        p2 = n - 1  # Last element of nums2
        p = m + n - 1  # Last position in merged array
        
        # Compare from back and place larger element
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 has remaining elements, copy them
        # (nums1 elements are already in place)
        nums1[:p2 + 1] = nums2[:p2 + 1]
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(m + n) | Single pass through both arrays |
| Space | O(1) | In-place merge |

---

### 🎯 Why Backwards?

**Forward approach problem:**
```
nums1 = [1,2,3,0,0,0]
If we start from front, we'd overwrite 1,2,3!
```

**Backwards solves this:**
```
Empty space is at the end
We fill from end → no overwriting!
```

---

## 🎓 Key Takeaways

### Pattern Recognition

| Problem | Pattern | Key Technique |
|---------|---------|---------------|
| Second Largest | Single Pass | Track top 2 |
| Plus One | Right to Left | Handle carry |
| Remove Duplicates | Two Pointers | Sorted property |
| Rotate Array | Index Formula | Modulo arithmetic |
| Merge Arrays | Three Pointers | Backwards fill |

---

### ✅ DO

- **Use two pointers** for in-place operations
- **Start from end** when merging/rotating to avoid overwriting
- **Handle edge cases**: empty arrays, k > n, etc.
- **Optimize space**: modify in-place when possible

### ❌ AVOID

- Sorting when array is already sorted
- Using extra space unnecessarily
- Forgetting to handle `k % n` in rotation
- Starting from front in merge (overwrites data!)

---

## 🔗 Related Topics

- [[06-Two-Pointer-Technique]] - More two-pointer patterns
- [[07-Array-Manipulation-Advanced]] - Advanced array operations
- [[Array-Patterns]] - Common array patterns summary

---

## 📝 Practice Problems

### Easy
1. LeetCode 26 - Remove Duplicates from Sorted Array
2. LeetCode 66 - Plus One
3. LeetCode 88 - Merge Sorted Array

### Medium
1. LeetCode 189 - Rotate Array
2. CodeChef - Second Largest
3. LeetCode 283 - Move Zeroes

---

## 🧪 Test Your Understanding

Try these variations:
1. Find **third** largest element
2. Plus One but array represents **binary** number
3. Rotate array **left** instead of right
4. Merge three sorted arrays

---

**Previous**: [[01-Time-and-Space-Complexity]] | **Next**: [[03-Character-Frequency-Problems]]

Back to: [[README of Frontend]]
