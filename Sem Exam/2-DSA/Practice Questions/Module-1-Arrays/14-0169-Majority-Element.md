# ═══════════════════════════════════════
# 📌 [169] - Majority Element
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find element appearing more than n/2 times.

## 💡 **Key Insight:**
Boyer-Moore: Maintain candidate with count. Same = inc, diff = dec. Count 0 = new candidate.

## 🔧 **Optimal Approach:**
**Algorithm:** Boyer-Moore Voting

**Steps:**
- candidate = None, count = 0
- If count 0, pick new candidate
- Same = count++, diff = count--
- Return candidate

## 💻 **Code (Run Directly):**
```python
def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

# TEST
nums = [2, 2, 1, 1, 1, 2, 2]
print("Input:", nums)
print("Output:", majorityElement(nums))
```

## 🏃 **Dry Run:**
**Example:** nums = [2, 2, 1, 1, 1, 2, 2]

```
num | candidate | count
----|-----------|------
2   | 2         | 1
2   | 2         | 2
1   | 2         | 1
1   | 2         | 0
1   | 1         | 1
2   | 1         | 0
2   | 2         | 1
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Boyer-Moore Voting

## ⚠️ **Gotcha:**
Only works when majority guaranteed to exist.
