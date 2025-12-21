# ═══════════════════════════════════════
# 📌 [509] - Fibonacci Number
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Calculate nth Fibonacci number. F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).

## 💡 **Key Insight:**
Iterative with two variables instead of recursion (O(n) vs O(2^n)).

## 🔧 **Optimal Approach:**
**Algorithm:** Iterative

**Steps:**
- prev = 0, curr = 1
- Loop n times, update: prev, curr = curr, prev + curr
- Return prev (after n iterations)

## 💻 **Code (Run Directly):**
```python
def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# TEST
for i in range(10):
    print(f"F({i}) =", fib(i))
```

## 🏃 **Dry Run:**
**Example:** n = 5

```
iter | prev | curr
-----|------|------
init | 0    | 1
2    | 1    | 1
3    | 1    | 2
4    | 2    | 3
5    | 3    | 5

Return 5
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Dynamic Programming, Math

## ⚠️ **Gotcha:**
Recursive is O(2^n). Use iterative or memoization.
