# ═══════════════════════════════════════
# 📌 [121] - Best Time to Buy and Sell Stock
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Max profit from one buy and sell. Buy must come before sell.

## 💡 **Key Insight:**
Track min price seen. At each day, calculate profit if sold today. Track max profit.

## 🔧 **Optimal Approach:**
**Algorithm:** One Pass Min Tracking

**Steps:**
- minPrice = inf, maxProfit = 0
- For each price: update minPrice if lower
- Calculate profit, update maxProfit if higher

## 💻 **Code (Run Directly):**
```python
def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    return maxProfit

# TEST
prices = [7, 1, 5, 3, 6, 4]
print("Input:", prices)
print("Output:", maxProfit(prices))
```

## 🏃 **Dry Run:**
**Example:** prices = [7, 1, 5, 3, 6, 4]

```
price | minPrice | profit | maxProfit
------|----------|--------|----------
7     | 7        | 0      | 0
1     | 1        | 0      | 0
5     | 1        | 4      | 4
3     | 1        | 2      | 4
6     | 1        | 5      | 5
4     | 1        | 3      | 5
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Greedy, DP

## ⚠️ **Gotcha:**
If only decreasing, return 0.
