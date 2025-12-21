# 🎯 Advanced Array Manipulation

## 🌟 What You'll Master
- **Matrix operations** and 2D array traversal
- **Array rotation** techniques
- **In-place algorithms** for space optimization
- **Advanced indexing** patterns

**Previous**: [[06-Two-Pointer-Technique]] | **Next**: [[08-Kadanes-Algorithm]]

---

## 🎨 Color-Coded Learning Guide

> [!SUCCESS] **🟢 Easy Concepts**
> - Basic matrix traversal
> - Simple array rotation

> [!WARNING] **🟡 Medium Concepts** 
> - In-place matrix operations
> - Complex rotation patterns

> [!DANGER] **🔴 Advanced Concepts**
> - Space-optimized algorithms
> - Multi-dimensional manipulations

---

## 🔄 Problem 1: Rotate Array (LeetCode 189)

### 📋 Problem Statement
Rotate array to the right by `k` steps.

**Examples:**
```python
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2  
Output: [3,99,-1,-100]
```

---

### 💡 Approach 1: Extra Array (Simple)

> [!TIP] **🎯 Strategy**
> Create new array and place each element at `(i + k) % n` position

```python
def rotate_simple(nums, k):
    n = len(nums)
    k = k % n  # Handle k > n
    result = [0] * n
    
    for i in range(n):
        new_pos = (i + k) % n
        result[new_pos] = nums[i]
    
    # Copy back to original
    for i in range(n):
        nums[i] = result[i]
```

**🔍 Dry Run:**
```
nums = [1,2,3,4,5,6,7], k = 3, n = 7

i=0: new_pos = (0+3)%7 = 3, result[3] = 1
i=1: new_pos = (1+3)%7 = 4, result[4] = 2  
i=2: new_pos = (2+3)%7 = 5, result[5] = 3
i=3: new_pos = (3+3)%7 = 6, result[6] = 4
i=4: new_pos = (4+3)%7 = 0, result[0] = 5
i=5: new_pos = (5+3)%7 = 1, result[1] = 6
i=6: new_pos = (6+3)%7 = 2, result[2] = 7

result = [5,6,7,1,2,3,4] ✅
```

---

### 🚀 Approach 2: Reverse Method (Optimal)

> [!SUCCESS] **🎯 Key Insight**
> Three reversals can achieve rotation!
> 1. Reverse entire array
> 2. Reverse first k elements  
> 3. Reverse remaining elements

```python
def rotate_optimal(nums, k):
    n = len(nums)
    k = k % n
    
    # Helper function to reverse array segment
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)
```

**🔍 Detailed Dry Run:**
```
Original: [1,2,3,4,5,6,7], k = 3

Step 1 - Reverse entire array:
[1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]

Step 2 - Reverse first k=3 elements:
[7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
 ↑---↑ reversed

Step 3 - Reverse remaining elements (index 3 to 6):
[5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]
       ↑-----↑ reversed

Final: [5,6,7,1,2,3,4] ✅
```

---

### 📊 Complexity Comparison

| Method | Time | Space | Pros | Cons |
|--------|------|-------|------|------|
| **🟡 Extra Array** | O(n) | O(n) | Easy to understand | Uses extra space |
| **🟢 Reverse** | O(n) | O(1) | Space optimal | Less intuitive |

---

## 🌀 Problem 2: Spiral Matrix (LeetCode 54)

### 📋 Problem Statement
Return all elements of matrix in spiral order.

**Example:**
```python
Input: matrix = [
  [1, 2, 3],
  [4, 5, 6], 
  [7, 8, 9]
]
Output: [1,2,3,6,9,8,7,4,5]
```

---

### 💡 Approach: Four Boundaries

> [!TIP] **🎯 Strategy**
> Maintain four boundaries and move in spiral pattern:
> **Right → Down → Left → Up → Repeat**

```python
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    rows, cols = len(matrix), len(matrix[0])
    
    # Define boundaries
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    while top <= bottom and left <= right:
        # 1. Move RIGHT along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # 2. Move DOWN along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # 3. Move LEFT along bottom row (if exists)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # 4. Move UP along left column (if exists)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result
```

---

### 🎨 Visual Dry Run

```
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Initial boundaries:
top=0, bottom=2, left=0, right=2

🔄 Iteration 1:
┌─→─→─┐
│ 1 2 3 │  Step 1: RIGHT (1,2,3)
│ 4 5 6 ↓  Step 2: DOWN (6,9)  
│ 7 8 9 │  Step 3: LEFT (8,7)
└─←─←─┘   Step 4: UP (4)

Result so far: [1,2,3,6,9,8,7,4]
New boundaries: top=1, bottom=1, left=1, right=1

🔄 Iteration 2:
Only center element (5) remains
Result: [1,2,3,6,9,8,7,4,5] ✅
```

---

### 📊 Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| **Time** | O(m×n) | Visit each element once |
| **Space** | O(1) | Only boundary variables (excluding result) |

---

## 🔄 Problem 3: Rotate Matrix 90° (LeetCode 48)

### 📋 Problem Statement
Rotate n×n matrix 90 degrees clockwise **in-place**.

**Example:**
```python
Input:
[1,2,3]
[4,5,6]
[7,8,9]

Output:
[7,4,1]
[8,5,2]
[9,6,3]
```

---

### 💡 Two-Step Approach

> [!SUCCESS] **🎯 Key Insight**
> **Transpose + Reverse** each row = 90° rotation!

**Step 1:** Transpose (swap across diagonal)
**Step 2:** Reverse each row

```python
def rotate(matrix):
    n = len(matrix)
    
    # Step 1: Transpose matrix
    for i in range(n):
        for j in range(i, n):  # Only upper triangle
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

---

### 🔍 Detailed Dry Run

```
Original:
[1,2,3]
[4,5,6]  
[7,8,9]

🔄 Step 1 - Transpose:
Swap (0,1)↔(1,0): 2↔4
Swap (0,2)↔(2,0): 3↔7  
Swap (1,2)↔(2,1): 6↔8

After transpose:
[1,4,7]
[2,5,8]
[3,6,9]

🔄 Step 2 - Reverse each row:
Row 0: [1,4,7] → [7,4,1]
Row 1: [2,5,8] → [8,5,2]  
Row 2: [3,6,9] → [9,6,3]

Final result:
[7,4,1]
[8,5,2]
[9,6,3] ✅
```

---

### 🎨 Visual Pattern Recognition

```
Original positions → Final positions
(0,0) → (0,2)    (0,1) → (1,2)    (0,2) → (2,2)
(1,0) → (0,1)    (1,1) → (1,1)    (1,2) → (2,1)  
(2,0) → (0,0)    (2,1) → (1,0)    (2,2) → (2,0)

Pattern: (i,j) → (j, n-1-i)
```

---

## 🎯 Advanced Pattern: In-Place Algorithms

### 🔑 Key Principles

> [!NOTE] **🟦 Space Optimization Rules**
> 1. **Swap instead of copy** when possible
> 2. **Use mathematical relationships** to avoid extra arrays
> 3. **Process in specific order** to avoid overwriting needed data
> 4. **Utilize array properties** (like symmetry)

---

### 🎨 Pattern Recognition Guide

| Pattern | When to Use | Key Technique |
|---------|-------------|---------------|
| **🔄 Rotation** | Shifting elements | Reverse method |
| **🌀 Spiral** | Matrix traversal | Boundary tracking |
| **↔️ Transpose** | Matrix operations | Diagonal swapping |
| **🔀 In-place** | Space constraints | Mathematical mapping |

---

## 🏆 Master Challenge: Set Matrix Zeroes (LeetCode 73)

### 📋 Problem Statement
If element is 0, set entire row and column to 0. Do it **in-place**.

**Example:**
```python
Input:
[1,1,1]
[1,0,1]
[1,1,1]

Output:
[1,0,1]
[0,0,0]
[1,0,1]
```

---

### 🚀 Optimal Solution: Use First Row/Column as Markers

```python
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row/column should be zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # Use first row/column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0  # Mark column
                matrix[i][0] = 0  # Mark row
    
    # Set zeros based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    
    # Handle first row/column
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
```

---

## 🎓 Key Takeaways

### ✅ **Master These Patterns**

> [!SUCCESS] **🟢 Essential Techniques**
> - **Reverse method** for rotations
> - **Boundary tracking** for spiral traversal  
> - **In-place swapping** for space optimization
> - **First row/column** as marker arrays

### 🎯 **Problem-Solving Framework**

1. **🔍 Identify the pattern** (rotation, spiral, etc.)
2. **📐 Draw the transformation** visually
3. **🧮 Find mathematical relationship** 
4. **⚡ Optimize for space** if possible
5. **🧪 Test with edge cases**

---

## 🔗 Related Topics
- [[05-Prefix-Sum-Technique]] - Array preprocessing
- [[06-Two-Pointer-Technique]] - Array traversal patterns
- [[08-Kadanes-Algorithm]] - Advanced array algorithms

---

## 📝 Practice Problems

> [!TIP] **🎯 Recommended Practice Order**
> 1. **🟢 Easy**: LeetCode 189 - Rotate Array
> 2. **🟡 Medium**: LeetCode 54 - Spiral Matrix  
> 3. **🟡 Medium**: LeetCode 48 - Rotate Image
> 4. **🔴 Hard**: LeetCode 73 - Set Matrix Zeroes

---

**Previous**: [[06-Two-Pointer-Technique]] | **Next**: [[08-Kadanes-Algorithm]]

Back to: [[README of Frontend]]