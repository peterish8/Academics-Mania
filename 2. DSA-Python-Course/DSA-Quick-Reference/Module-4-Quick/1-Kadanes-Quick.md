# ⚡ Kadane's Algorithm - Quick Ref

## 🎯 Core Pattern

### **Maximum Subarray**
```python
def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### **Maximum Product Subarray**
```python
def maxProduct(nums):
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)
    
    return result
```

---

## ⚡ **Template**

```python
def kadane_pattern(nums):
    current = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)):
        # Decision: extend or restart
        current = max(nums[i], current + nums[i])
        global_max = max(global_max, current)
    
    return global_max
```

---

## 🎯 **Array Index Marking**

### **Find Duplicates (1 ≤ nums[i] ≤ n)**
```python
def findDuplicates(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    return result
```

---

## 🧠 **Key Insights**
- **Extend vs Restart**: Core decision at each step
- **Negatives**: Track both max and min for products
- **Index Marking**: Use array itself as hash when 1 ≤ nums[i] ≤ n

Back to: [[README of DSA Quick Ref]]