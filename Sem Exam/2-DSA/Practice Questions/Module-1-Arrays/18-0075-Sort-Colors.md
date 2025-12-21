# ═══════════════════════════════════════
# 📌 [75] - Sort Colors
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Sort array with only 0s, 1s, 2s in-place. (Dutch National Flag)

## 💡 **Key Insight:**
Three pointers: low (0s), mid (current), high (2s). Swap to correct regions.

## 🔧 **Optimal Approach:**
**Algorithm:** Dutch National Flag

**Steps:**
- low = mid = 0, high = n-1
- If 0: swap low, inc both
- If 1: inc mid
- If 2: swap high, dec high

## 💻 **Code (Run Directly):**
```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# TEST
nums = [2, 0, 2, 1, 1, 0]
print("Input:", [2, 0, 2, 1, 1, 0])
print("Output:", sortColors(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [2, 0, 2, 1, 1, 0]

```
low | mid | high | nums[mid] | action
----|-----|------|-----------|--------
0   | 0   | 5    | 2         | swap high
0   | 0   | 4    | 0         | swap low
1   | 1   | 4    | 0         | swap low
2   | 2   | 4    | 2         | swap high
2   | 2   | 3    | 1         | mid++
2   | 3   | 3    | 1         | mid++
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Three Pointers, Dutch National Flag

## ⚠️ **Gotcha:**
Don't inc mid when swapping with high - check swapped element.
