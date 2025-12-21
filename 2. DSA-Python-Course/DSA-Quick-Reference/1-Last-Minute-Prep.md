# ⚡ Last-Minute Prep

## 🎯 5-Minute Pattern Review

### **Two Pointer**
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition: left += 1
    else: right -= 1
```

### **Prefix Sum**
```python
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)
# Range sum: prefix[j+1] - prefix[i]
```

### **HashMap Frequency**
```python
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

### **Kadane's Algorithm**
```python
current = nums[0]
max_sum = nums[0]
for i in range(1, len(nums)):
    current = max(nums[i], current + nums[i])
    max_sum = max(max_sum, current)
```

### **Sliding Window**
```python
left = 0
for right in range(len(arr)):
    # Expand
    while invalid_condition:
        # Contract
        left += 1
```

### **Bit Manipulation**
```python
# Power of 2: n > 0 and (n & (n-1)) == 0
# Single number: result ^= num (XOR all)
# Count bits: while n: count += 1; n &= n-1
```

---

## 🧠 **Quick Recall**

**See "sorted array"** → Two Pointer
**See "subarray sum"** → Prefix Sum or Kadane's
**See "frequency/count"** → HashMap
**See "maximum subarray"** → Kadane's
**See "power of 2"** → Bit Manipulation
**See "substring/window"** → Sliding Window

---

## ⚡ **Common Mistakes to Avoid**

- **Two Pointer**: Check `left < right` condition
- **Prefix Sum**: Remember `prefix[j+1] - prefix[i]` for range [i,j]
- **HashMap**: Use `dict.get(key, 0)` to avoid KeyError
- **Kadane's**: Initialize with `nums[0]`, not 0
- **Sliding Window**: Contract window when condition violated
- **Bit Manipulation**: Use `abs(num)` when array modified

Back to: [[README of DSA Quick Ref]]