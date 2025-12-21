# ═══════════════════════════════════════
# 📌 [13] - Roman to Integer
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Convert Roman numeral string to integer.

## 💡 **Key Insight:**
If current value < next value, subtract it. Otherwise add it.

## 🔧 **Optimal Approach:**
**Algorithm:** Left to Right with Lookup

**Steps:**
- Create value map for each Roman numeral
- For each char: if less than next, subtract; else add

## 💻 **Code (Run Directly):**
```python
def romanToInt(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
              'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            result -= values[s[i]]
        else:
            result += values[s[i]]
    
    return result

# TEST
print("III:", romanToInt("III"))
print("IV:", romanToInt("IV"))
print("MCMXCIV:", romanToInt("MCMXCIV"))
```

## 🏃 **Dry Run:**
**Example:** s = "MCMXCIV" (1994)

```
i | char | next | action
--|------|------|--------
0 | M    | C    | +1000
1 | C    | M    | -100
2 | M    | X    | +1000
3 | X    | C    | -10
4 | C    | I    | +100
5 | I    | V    | -1
6 | V    | -    | +5

Total: 1994
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
String, HashMap

## ⚠️ **Gotcha:**
IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
