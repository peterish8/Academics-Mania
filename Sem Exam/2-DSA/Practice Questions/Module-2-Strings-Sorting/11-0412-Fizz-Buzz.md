# ═══════════════════════════════════════
# 📌 [412] - Fizz Buzz
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Return array where: divisible by 3 = "Fizz", by 5 = "Buzz", both = "FizzBuzz".

## 💡 **Key Insight:**
Check divisibility with modulo. Check 15 first (or build string).

## 🔧 **Optimal Approach:**
**Algorithm:** String Concatenation

**Steps:**
- For each number 1 to n
- Build string: add "Fizz" if %3==0, add "Buzz" if %5==0
- If empty, use number

## 💻 **Code (Run Directly):**
```python
def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if not s:
            s = str(i)
        result.append(s)
    return result

# TEST
print("n=15:", fizzBuzz(15))
```

## 🏃 **Dry Run:**
**Example:** n = 15

```
i  | %3 | %5 | result
---|----|----|--------
1  | 1  | 1  | "1"
3  | 0  | 3  | "Fizz"
5  | 2  | 0  | "Buzz"
15 | 0  | 0  | "FizzBuzz"
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1) excluding output

## 🏷️ **Pattern Tag:** 
Math, Simulation

## ⚠️ **Gotcha:**
String concatenation avoids checking 15 separately.
