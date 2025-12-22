# 3️⃣ Kadane's Algorithm

---

## 📌 Concept

> [!SUCCESS] **Problem**: Find the contiguous subarray with the largest sum.

> [!TIP] **Key Insight**: "Should I start fresh here, or extend the previous sum?"
> If previous sum is negative → Start fresh!

---

## 📌 Algorithm

```
current_sum = max(nums[i], current_sum + nums[i])
max_sum = max(max_sum, current_sum)
```

**In simple words:**
- If `current_sum + nums[i]` is less than `nums[i]` alone → Reset
- Always track the maximum seen so far

---

## 💻 Code

```python
def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Extend or start fresh?
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# TEST
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Array:", nums)
print("Max Subarray Sum:", maxSubArray(nums))  # 6 → [4, -1, 2, 1]
```

---

## 🏃 Dry Run

**Array:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| i | nums[i] | current_sum | max_sum |
|---|---------|-------------|---------|
| 0 | -2 | -2 | -2 |
| 1 | 1 | max(1, -2+1) = 1 | 1 |
| 2 | -3 | max(-3, 1-3) = -2 | 1 |
| 3 | 4 | max(4, -2+4) = 4 | 4 |
| 4 | -1 | max(-1, 4-1) = 3 | 4 |
| 5 | 2 | max(2, 3+2) = 5 | 5 |
| 6 | 1 | max(1, 5+1) = 6 | **6** |
| 7 | -5 | max(-5, 6-5) = 1 | 6 |
| 8 | 4 | max(4, 1+4) = 5 | 6 |

**Answer:** 6 (subarray: [4, -1, 2, 1])

---

## ⏱️ Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) - Single pass |
| **Space** | O(1) - Only 2 variables |

---

## 🧠 Key Points
- **Reset condition**: Previous sum is negative (dragging us down)
- **Works for all negatives**: Returns least negative number
- **One pass**: Don't need nested loops!

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
