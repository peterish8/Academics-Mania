 0, 0, 0]

Index 1:
  res[1] = res[0] + nums[1]
         = 1 + 2 = 3
  res = [1, 3, 0, 0]

Index 2:
  res[2] = res[1] + nums[2]
         = 3 + 3 = 6
  res = [1, 3, 6, 0]

Index 3:
  res[3] = res[2] + nums[3]
         = 6 + 4 = 10
  res = [1, 3, 6, 10] ✓
```

---

### 🎨 Visual Representation

```
Original: [1,    2,    3,    4]
           ↓     ↓     ↓     ↓
Result:   [1, 1+2, 1+2+3, 1+2+3+4]
          [1,   3,     6,      10]

Pattern:
res[i] = res[i-1] + nums[i]
```python

---

### ✅ Solution Code

```python
class Solution:
    def runningSum(self, nums):
        n = len(nums)
        res = [0] * n
        
        # First element stays same
        res[0] = nums[0]
        
        # Each element = previous + current
        for i in range(1, n):
            res[i] = res[i-1] + nums[i]
        
        return res
```

**In-place version (saves space):**
```python
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single pass through array |
| Space | O(1) | In-place modification (or O(n) for new array) |

---

## ⚖️ Problem 2: Find Middle Index (LeetCode 1991)

### Problem Statement
Find the **smallest** index where `left_sum == right_sum`.

**Definition:**
- `left_sum` = sum of all elements to the left of index
- `right_sum` = sum of all elements to the right of index
- Element at index is NOT included in either sum

**Examples:**
```python
Input: [2,3,-1,8,4]
Output: 3
Explanation: 
  At index 3: left=[2,3,-1] sum=4, right=[4] sum=4

Input: [1,-1,4]
Output: 2
Explanation:
  At index 2: left=[1,-1] sum=0, right=[] sum=0

Input: [2,5]
Output: -1
(No such index exists)
```

---

### 💡 Approach

**Key Insight:** Use total sum to calculate right sum!

```python
total_sum = sum of entire array
left_sum = sum of elements before index i
right_sum = total_sum - left_sum - nums[i]

If left_sum == right_sum:
  return i
```

**Process:**
1. Calculate total sum
2. Iterate with running left_sum
3. At each index, check if left == right
4. Update left_sum after checking

---

### 🔍 Dry Run

**Input:** `[2, 3, -1, 8, 4]`

**Setup:**
```python
total = 2 + 3 + (-1) + 8 + 4 = 16
left = 0
```

**Iteration:**

```
Index 0: nums[0] = 2
  left = 0
  right = total - left - nums[0]
        = 16 - 0 - 2 = 14
  left == right? 0 == 14? NO
  Update: left = 0 + 2 = 2

Index 1: nums[1] = 3
  left = 2
  right = 16 - 2 - 3 = 11
  left == right? 2 == 11? NO
  Update: left = 2 + 3 = 5

Index 2: nums[2] = -1
  left = 5
  right = 16 - 5 - (-1) = 12
  left == right? 5 == 12? NO
  Update: left = 5 + (-1) = 4

Index 3: nums[3] = 8
  left = 4
  right = 16 - 4 - 8 = 4
  left == right? 4 == 4? YES ✓
  RETURN 3
```

---

### 🎨 Visual Understanding

```
Array: [2, 3, -1, 8, 4]
        ←-left-→ ↑ ←right→
                 pivot

At index 3:
  Left side: [2, 3, -1] → sum = 4
  Right side: [4]       → sum = 4
  Balanced! ⚖️
```

---

### ✅ Solution Code

```python
class Solution:
    def findMiddleIndex(self, nums):
        total = sum(nums)  # Total sum of array
        left = 0           # Running left sum
        
        for i, val in enumerate(nums):
            # Calculate right sum
            right = total - left - val
            
            # Check if balanced
            if left == right:
                return i
            
            # Update left sum for next iteration
            left += val
        
        return -1  # No middle index found
```

---

### 📊 Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | One pass to sum + one pass to find |
| Space | O(1) | Only variables used |

---

**Previous**: [[04-String-Dictionary-Problems]] | **Next**: [[06-Two-Pointer-Technique]]

Back to: [[README of Frontend]]
