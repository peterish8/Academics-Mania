# 📊 Prefix Sum - Quick Ref

## 🎯 Core Pattern

### **Running Sum**
```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums
```

### **Range Sum Query**
```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]
```

### **Find Middle Index**
```python
def findMiddleIndex(nums):
    total = sum(nums)
    left_sum = 0
    
    for i, val in enumerate(nums):
        right_sum = total - left_sum - val
        if left_sum == right_sum:
            return i
        left_sum += val
    return -1
```

---

## ⚡ **Templates**

**Build Prefix**:
```python
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)
```

**Range Sum**:
```python
range_sum = prefix[j+1] - prefix[i]  # Sum from i to j
```

**Balance Point**:
```python
total = sum(nums)
left = 0
for i, val in enumerate(nums):
    right = total - left - val
    if left == right:
        return i
    left += val
```

---

## 🧠 **Key Points**
- **Prefix[i]** = sum of elements 0 to i-1
- **Range sum** = prefix[j+1] - prefix[i]
- **Balance** = left_sum == right_sum

Back to: [[README of DSA Quick Ref]]