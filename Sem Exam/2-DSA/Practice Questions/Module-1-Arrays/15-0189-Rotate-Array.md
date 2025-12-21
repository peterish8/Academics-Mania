# ═══════════════════════════════════════
# 📌 [189] - Rotate Array
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Rotate array right by k steps.

## 💡 **Key Insight:**
Three reversals: reverse all, reverse first k, reverse rest.

## 🔧 **Optimal Approach:**
**Algorithm:** Three Reversals

**Steps:**
- k = k % n
- Reverse entire array
- Reverse first k elements
- Reverse remaining n-k

## 💻 **Code (Run Directly):**
```python
def rotate(nums, k):
    n = len(nums)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

# TEST
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Input:", [1, 2, 3, 4, 5, 6, 7], "k:", k)
print("Output:", rotate(nums, k))
```

## 🏃 **Dry Run:**
**Example:** nums = [1,2,3,4,5,6,7], k = 3

```
Step 1: Reverse all    -> [7,6,5,4,3,2,1]
Step 2: Reverse 0..2   -> [5,6,7,4,3,2,1]
Step 3: Reverse 3..6   -> [5,6,7,1,2,3,4]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Array, Reversal

## ⚠️ **Gotcha:**
Always do k = k % n first!
