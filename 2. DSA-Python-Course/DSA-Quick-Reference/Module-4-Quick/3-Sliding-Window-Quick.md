# 🪟 Sliding Window - Quick Ref

## 🎯 Core Patterns

### **Fixed Window - Max Sum K**
```python
def maxSumK(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### **Variable Window - Longest Substring**
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### **Min Window Substring**
```python
def minWindow(s, t):
    from collections import Counter
    
    need = Counter(t)
    window = {}
    left = right = 0
    valid = 0
    start, length = 0, float('inf')
    
    while right < len(s):
        c = s[right]
        right += 1
        
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        
        while valid == len(need):
            if right - left < length:
                start, length = left, right - left
            
            d = s[left]
            left += 1
            
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    
    return "" if length == float('inf') else s[start:start+length]
```

---

## ⚡ **Templates**

**Fixed Window**:
```python
window_sum = sum(arr[:k])
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    # Update result
```

**Variable Window**:
```python
left = 0
for right in range(len(arr)):
    # Expand window
    add_to_window(arr[right])
    
    # Contract if needed
    while window_invalid():
        remove_from_window(arr[left])
        left += 1
    
    # Update result
```

---

## 🧠 **Key Points**
- **Fixed**: Slide by removing left, adding right
- **Variable**: Expand right, contract left when needed
- **Tracking**: Use hash/set for character problems

Back to: [[README of DSA Quick Ref]]