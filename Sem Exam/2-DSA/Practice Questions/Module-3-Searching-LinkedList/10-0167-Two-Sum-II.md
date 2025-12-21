# ═══════════════════════════════════════
# 📌 [167] - Two Sum II (Input Array Is Sorted)
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find two numbers that sum to target. Array is sorted. 1-indexed answer.

## 💡 **Key Insight:**
Two pointers from ends. If sum < target, move left. If > target, move right.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers

**Steps:**
- left = 0, right = n-1
- If sum == target, return [left+1, right+1]
- If sum < target, left++
- If sum > target, right--

## 💻 **Code (Run Directly):**
```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# TEST
numbers = [2, 7, 11, 15]
print("numbers:", numbers, "target: 9")
print("Output:", twoSum(numbers, 9))
```

## 🏃 **Dry Run:**
**Example:** numbers = [2, 7, 11, 15], target = 9

```
left | right | sum | action
-----|-------|-----|--------
0    | 3     | 17  | > 9, right--
0    | 2     | 13  | > 9, right--
0    | 1     | 9   | == 9, return [1, 2]
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Two Pointers

## ⚠️ **Gotcha:**
1-indexed answer - add 1 to both indices.
