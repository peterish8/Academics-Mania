# ═══════════════════════════════════════
# 📌 [875] - Koko Eating Bananas
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find minimum eating speed k to finish all piles in h hours.

## 💡 **Key Insight:**
Binary search on speed k. Check if can finish with that speed.

## 🔧 **Optimal Approach:**
**Algorithm:** Binary Search on Answer

**Steps:**
- Binary search k from 1 to max(piles)
- For each k, calculate hours needed
- Find minimum k where hours <= h

## 💻 **Code (Run Directly):**
```python
import math

def minEatingSpeed(piles, h):
    def canFinish(k):
        hours = sum(math.ceil(pile / k) for pile in piles)
        return hours <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# TEST
print("[3,6,7,11] h=8:", minEatingSpeed([3, 6, 7, 11], 8))
print("[30,11,23,4,20] h=5:", minEatingSpeed([30, 11, 23, 4, 20], 5))
```

## 🏃 **Dry Run:**
**Example:** piles = [3, 6, 7, 11], h = 8

```
k=4: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8 -> valid
k=3: 1+2+3+4 = 10 > 8 -> too slow

Binary search finds k=4
```

## ⏱️ **Complexity:**
- **Time:** O(n * log(max))
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Binary Search on Answer

## ⚠️ **Gotcha:**
Use math.ceil for rounding up hours per pile.
