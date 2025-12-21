# 🎯 Two Pointer - Quick Ref

## 🎯 Core Patterns

### **Two Sum (Sorted Array)**
```python
def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### **Container With Most Water**
```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

### **Valid Palindrome**
```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

---

## ⚡ **Templates**

**Opposite Ends**:
```python
left, right = 0, len(arr) - 1
while left < right:
    # Process arr[left] and arr[right]
    if condition:
        left += 1
    else:
        right -= 1
```

**Same Direction**:
```python
slow = fast = 0
for fast in range(len(arr)):
    if condition:
        arr[slow] = arr[fast]
        slow += 1
```

---

## 🧠 **When to Use**
- **Sorted array** + target sum
- **Palindrome** checking
- **Remove duplicates** in-place
- **Container/area** problems

Back to: [[README of DSA Quick Ref]]