# ═══════════════════════════════════════
# 📌 [2154] - Keep Multiplying Found Values by Two
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Start with original, keep doubling if found in array. Return final value.

## 💡 **Key Insight:**
Convert to set for O(1) lookups. Keep doubling until not found.

## 🔧 **Optimal Approach:**
**Algorithm:** HashSet + Loop

**Steps:**
- Convert nums to set
- While original in set, double it
- Return original

## 💻 **Code (Run Directly):**
```python
def findFinalValue(nums, original):
    numSet = set(nums)
    while original in numSet:
        original *= 2
    return original

# TEST
nums = [5, 3, 6, 1, 12]
original = 3
print("nums:", nums, "original:", original)
print("Output:", findFinalValue(nums, original))
```

## 🏃 **Dry Run:**
**Example:** nums = [5, 3, 6, 1, 12], original = 3

```
iter | original | in set? | action
-----|----------|---------|--------
1    | 3        | Yes     | double -> 6
2    | 6        | Yes     | double -> 12
3    | 12       | Yes     | double -> 24
4    | 24       | No      | return 24
```

## ⏱️ **Complexity:**
- **Time:** O(n) for set creation, O(log(max)) for doubling
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashSet, Simulation

## ⚠️ **Gotcha:**
Use set for O(1) lookup, not list (O(n)).
