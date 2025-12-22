# 5️⃣ Binary Search & Variations

---

## 📌 Basic Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# TEST
print(binary_search([1, 3, 5, 7, 9], 5))  # 2
```

---

## 📌 Search Insert Position

> Find index where target is OR where it should be inserted.

```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # Insert position!

# TEST
print(searchInsert([1, 3, 5, 6], 5))  # 2
print(searchInsert([1, 3, 5, 6], 2))  # 1
```

---

## 📌 Sqrt(x)

> Find floor of square root.

```python
def mySqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Floor value

# TEST
print(mySqrt(8))   # 2
print(mySqrt(16))  # 4
```

---

## 📌 Find Peak Element

> Find ANY peak (element greater than neighbors).

```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # Peak on right
        else:
            right = mid     # Peak on left (including mid)
    
    return left

# TEST
print(findPeakElement([1, 2, 3, 1]))  # 2
```

---

## 📌 Search in Rotated Sorted Array

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# TEST
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
```

---

## 📌 Find Minimum in Rotated Array

```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

# TEST
print(findMin([3, 4, 5, 1, 2]))  # 1
```

---

## 🧠 Key Points
- **Basic**: `while left <= right`, return `mid`
- **Insert Position**: Return `left` when not found
- **Peak**: `while left < right`, compare with `mid+1`
- **Rotated**: Check which half is sorted

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
