# 🪟 Sliding Window Technique

## 🌟 What You'll Master
- **Fixed-size** sliding window patterns
- **Variable-size** sliding window optimization
- **Two-pointer** window management
- **Optimization problems** using windows

**Previous**: [[09-Bit-Manipulation]] | **Next**: [[Pattern-Recognition-Guide]]

---

## 🎨 Color-Coded Difficulty Guide

> [!SUCCESS] **🟢 Beginner Level**
> - Fixed-size window problems
> - Simple sum/average calculations

> [!WARNING] **🟡 Intermediate Level**
> - Variable-size windows
> - Condition-based expansion/contraction

> [!DANGER] **🔴 Advanced Level**
> - Multiple windows
> - Complex optimization problems

---

## 🔍 What is Sliding Window?

### 💡 Core Concept
A **sliding window** is a technique where we maintain a "window" (subarray) that slides through the array to solve problems efficiently.

> [!TIP] **🎯 When to Use Sliding Window**
> - Finding **maximum/minimum** in subarrays
> - **Substring/subarray** problems with conditions
> - **Optimization** problems on contiguous elements
> - **Avoiding nested loops** for better time complexity

---

### 🎨 Visual Representation

```python
Array: [1, 2, 3, 4, 5, 6, 7, 8]
Window size = 3

Position 1: [1, 2, 3] 4  5  6  7  8
Position 2:  1 [2, 3, 4] 5  6  7  8  
Position 3:  1  2 [3, 4, 5] 6  7  8
Position 4:  1  2  3 [4, 5, 6] 7  8
Position 5:  1  2  3  4 [5, 6, 7] 8
Position 6:  1  2  3  4  5 [6, 7, 8]
```

---

## 🎯 Problem 1: Maximum Sum Subarray of Size K

### 📋 Problem Statement
Find the maximum sum of any contiguous subarray of size `k`.

**Examples:**
```python
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: [5, 1, 3] has sum = 9

Input: arr = [2, 3, 4, 1, 5], k = 2  
Output: 7
Explanation: [3, 4] has sum = 7
```

---

### 🐌 Brute Force Approach (Inefficient)

```python
def max_sum_brute_force(arr, k):
    n = len(arr)
    max_sum = float('-inf')
    
    # Check every possible subarray of size k
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Time: O(n*k), Space: O(1)
```

---

### 🚀 Sliding Window Approach (Optimal)

> [!SUCCESS] **🎯 Key Insight**
> Instead of recalculating sum from scratch:
> **New Sum = Old Sum - Left Element + Right Element**

```python
def max_sum_sliding_window(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, n):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Time: O(n), Space: O(1)
```

---

### 🔍 Detailed Dry Run

```python
arr = [2, 1, 5, 1, 3, 2], k = 3

Step 1: Calculate first window sum
window_sum = arr[0] + arr[1] + arr[2] = 2 + 1 + 5 = 8
max_sum = 8

Step 2: Slide window (i = 3)
Remove arr[0] = 2, Add arr[3] = 1
window_sum = 8 - 2 + 1 = 7
max_sum = max(8, 7) = 8

Step 3: Slide window (i = 4)  
Remove arr[1] = 1, Add arr[4] = 3
window_sum = 7 - 1 + 3 = 9
max_sum = max(8, 9) = 9

Step 4: Slide window (i = 5)
Remove arr[2] = 5, Add arr[5] = 2  
window_sum = 9 - 5 + 2 = 6
max_sum = max(9, 6) = 9

Final answer: 9 ✅
```

---

### 🎨 Visual Window Movement

```python
arr = [2, 1, 5, 1, 3, 2]

Window 1: [2, 1, 5] → sum = 8
Window 2:    [1, 5, 1] → sum = 7  
Window 3:       [5, 1, 3] → sum = 9 ← MAX
Window 4:          [1, 3, 2] → sum = 6
```

---

## 🎯 Problem 2: Longest Substring Without Repeating Characters

### 📋 Problem Statement
Find the length of the longest substring without repeating characters.

**Examples:**
```python
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest

Input: s = "bbbbb"
Output: 1  
Explanation: "b" is the longest

Input: s = "pwwkew"
Output: 3
Explanation: "wke" is the longest
```

---

### 💡 Variable Window Approach

> [!TIP] **🎯 Strategy**
> - **Expand** window by moving right pointer
> - **Contract** window when duplicate found
> - Use **set/dictionary** to track characters

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Contract window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character and update max
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

---

### 🔍 Detailed Dry Run

```python
s = "abcabcbb"

Initial: left=0, right=0, char_set={}, max_length=0

right=0, s[0]='a':
  'a' not in set → add 'a'
  char_set = {'a'}, window = "a", length = 1
  max_length = 1

right=1, s[1]='b':  
  'b' not in set → add 'b'
  char_set = {'a','b'}, window = "ab", length = 2
  max_length = 2

right=2, s[2]='c':
  'c' not in set → add 'c'  
  char_set = {'a','b','c'}, window = "abc", length = 3
  max_length = 3

right=3, s[3]='a':
  'a' in set! Contract window:
    Remove s[0]='a', left=1
    char_set = {'b','c'}
  Add 'a' → char_set = {'b','c','a'}
  window = "bca", length = 3
  max_length = 3

right=4, s[4]='b':
  'b' in set! Contract window:
    Remove s[1]='b', left=2  
    char_set = {'c','a'}
  Add 'b' → char_set = {'c','a','b'}
  window = "cab", length = 3
  max_length = 3

...continuing...

Final answer: 3 ✅
```

---

### 🎨 Visual Window Expansion/Contraction

```python
s = "abcabcbb"

Step 1: [a]bcabcbb          → length = 1
Step 2: [ab]cabcbb          → length = 2  
Step 3: [abc]abcbb          → length = 3
Step 4: abc[a]bcbb          → duplicate! contract
Step 5:  bc[ab]cbb          → length = 3
Step 6:   c[abc]bb          → duplicate! contract  
Step 7:    [cab]cbb         → length = 3
```

---

## 🎯 Problem 3: Minimum Window Substring (Hard)

### 📋 Problem Statement
Find the minimum window in string `s` that contains all characters of string `t`.

**Example:**
```python
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: "BANC" is the smallest window containing A, B, C
```

---

### 🚀 Advanced Sliding Window Solution

```python
def minWindow(s, t):
    if not s or not t:
        return ""
    
    # Count characters in t
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    required = len(dict_t)  # Unique characters in t
    formed = 0              # Characters matched so far
    
    window_counts = {}
    left = right = 0
    
    # Result: (window length, left, right)
    ans = float('inf'), None, None
    
    while right < len(s):
        # Add character from right to window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if current character's frequency matches t
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        # Contract window until it's no longer valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update result if this window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Remove leftmost character
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
```

---

## 🎨 Sliding Window Patterns Summary

### 🔧 Pattern 1: Fixed Size Window
```python
def fixed_window_template(arr, k):
    window_sum = sum(arr[:k])  # Initial window
    result = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result = update_result(result, window_sum)
    
    return result
```

### 🔧 Pattern 2: Variable Size Window
```python
def variable_window_template(arr):
    left = 0
    result = 0
    
    for right in range(len(arr)):
        # Expand window
        add_to_window(arr[right])
        
        # Contract window if needed
        while window_invalid():
            remove_from_window(arr[left])
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```

---

## 📊 Complexity Analysis

| Problem Type | Time Complexity | Space Complexity | Key Insight |
|--------------|----------------|------------------|-------------|
| **🟢 Fixed Window** | O(n) | O(1) | Slide and update |
| **🟡 Variable Window** | O(n) | O(k) | Expand/contract with conditions |
| **🔴 Complex Window** | O(n) | O(k) | Multiple conditions tracking |

---

## 🎯 Pattern Recognition Guide

> [!NOTE] **🔍 How to Identify Sliding Window Problems**
> 
> **Look for these keywords:**
> - "contiguous subarray/substring"
> - "maximum/minimum of size k"  
> - "longest/shortest satisfying condition"
> - "all subarrays of size k"

### 🎨 Decision Tree

```
Is it about contiguous elements?
├─ YES: Potential sliding window
│   ├─ Fixed size? → Use fixed window pattern
│   └─ Variable size? → Use two-pointer expansion/contraction
└─ NO: Consider other techniques
```

---

## 🏆 Master Challenge Problems

> [!TIP] **🎯 Practice Progression**
> 
> **🟢 Beginner:**
> 1. Maximum sum subarray of size K
> 2. Average of subarrays of size K
> 
> **🟡 Intermediate:**  
> 3. Longest substring without repeating characters
> 4. Fruits into baskets
> 5. Longest substring with K distinct characters
> 
> **🔴 Advanced:**
> 6. Minimum window substring
> 7. Sliding window maximum
> 8. Permutation in string

---

## 🎓 Key Takeaways

### ✅ **Essential Concepts**

> [!SUCCESS] **🟢 Master These Techniques**
> - **Fixed window**: Slide and update incrementally
> - **Variable window**: Expand right, contract left when needed
> - **Condition tracking**: Use hashmaps/sets for complex conditions
> - **Two-pointer management**: Left and right pointer coordination

### 🎯 **Problem-Solving Steps**

1. **🔍 Identify** if it's a sliding window problem
2. **📏 Determine** if window size is fixed or variable
3. **🎯 Choose** appropriate template
4. **🧮 Track** necessary state (sum, count, etc.)
5. **⚡ Optimize** by avoiding redundant calculations

---

## 🔗 Related Topics
- [[06-Two-Pointer-Technique]] - Foundation for sliding window
- [[04-String-Dictionary-Problems]] - String manipulation patterns
- [[Pattern-Recognition-Guide]] - When to use which technique

---

**Previous**: [[09-Bit-Manipulation]] | **Next**: [[Pattern-Recognition-Guide]]

Back to: [[README of Frontend]]