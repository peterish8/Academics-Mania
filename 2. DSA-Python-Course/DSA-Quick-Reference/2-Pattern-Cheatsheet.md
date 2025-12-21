# 🎯 Pattern Recognition Cheatsheet

## ⚡ Quick Pattern Identification

### 🔍 **Keywords → Pattern**

| **Keywords** | **Pattern** | **Template** |
|--------------|-------------|--------------|
| "sorted array", "two sum" | Two Pointer | `left=0, right=n-1` |
| "subarray sum", "range query" | Prefix Sum | `prefix[i] = prefix[i-1] + nums[i]` |
| "frequency", "count", "anagram" | HashMap | `freq[x] = freq.get(x, 0) + 1` |
| "maximum subarray" | Kadane's | `max(nums[i], current + nums[i])` |
| "power of 2", "single number" | Bit Manipulation | `n & (n-1) == 0`, `a ^ a = 0` |
| "window", "substring" | Sliding Window | `left=0; for right in range(n)` |

---

## 🎨 **Visual Decision Tree**

```
Problem Type?
├── Array
│   ├── Sorted? → Two Pointer
│   ├── Range sum? → Prefix Sum
│   ├── Max subarray? → Kadane's
│   └── Contiguous? → Sliding Window
├── String
│   ├── Count chars? → HashMap
│   ├── Substring? → Sliding Window
│   └── Pattern? → Two Pointer
└── Math
    ├── Binary ops? → Bit Manipulation
    └── Optimization? → Kadane's/DP
```

---

## ⚡ **Time Complexity Guide**

| **Pattern** | **Time** | **Space** | **Use When** |
|-------------|----------|-----------|--------------|
| Two Pointer | O(n) | O(1) | Sorted arrays, pairs |
| Prefix Sum | O(n) | O(n) | Range queries |
| HashMap | O(n) | O(k) | Counting, frequency |
| Kadane's | O(n) | O(1) | Max subarray |
| Bit Manipulation | O(1) | O(1) | Binary operations |
| Sliding Window | O(n) | O(k) | Subarray/substring |

---

## 🧠 **Memory Triggers**

- **Two Pointer**: "Meet in the middle"
- **Prefix Sum**: "Running total"
- **HashMap**: "Count everything"
- **Kadane's**: "Extend or restart"
- **Bit Manipulation**: "XOR cancels out"
- **Sliding Window**: "Expand and contract"

Back to: [[README of DSA Quick Ref]]