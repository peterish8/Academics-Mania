# ═══════════════════════════════════════
# 📌 [217] - Contains Duplicate
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Return True if any value appears at least twice.

## 💡 **Key Insight:**
HashSet for O(1) lookups. Check if number in set, if yes = duplicate.

## 🔧 **Optimal Approach:**
**Algorithm:** HashSet

**Steps:**
- Create empty set
- For each num: if in set, return True
- Otherwise add to set
- Return False if loop ends

## 💻 **Code (Run Directly):**
```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# TEST
print("Test 1:", containsDuplicate([1, 2, 3, 1]))
print("Test 2:", containsDuplicate([1, 2, 3, 4]))
```

## 🏃 **Dry Run:**
**Example:** nums = [1, 2, 3, 1]

```
iter | num | seen        | action
-----|-----|-------------|-------------------
1    | 1   | {}          | Add -> {1}
2    | 2   | {1}         | Add -> {1, 2}
3    | 3   | {1, 2}      | Add -> {1, 2, 3}
4    | 1   | {1, 2, 3}   | Found! Return True
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashSet, Array

## ⚠️ **Gotcha:**
Loop approach returns early on first duplicate - more efficient.
