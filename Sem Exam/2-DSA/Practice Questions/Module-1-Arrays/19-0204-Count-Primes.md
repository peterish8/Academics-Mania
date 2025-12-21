# ═══════════════════════════════════════
# 📌 [204] - Count Primes
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Count prime numbers less than n.

## 💡 **Key Insight:**
Sieve of Eratosthenes: Mark all multiples of primes as non-prime.

## 🔧 **Optimal Approach:**
**Algorithm:** Sieve of Eratosthenes

**Steps:**
- Create isPrime array, all True
- Mark 0, 1 as False
- For i from 2 to sqrt(n): mark i*i, i*i+i, ... as False
- Count remaining True

## 💻 **Code (Run Directly):**
```python
def countPrimes(n):
    if n < 2:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n, i):
                isPrime[j] = False
    
    return sum(isPrime)

# TEST
n = 10
print("Input: n =", n)
print("Output:", countPrimes(n))
```

## 🏃 **Dry Run:**
**Example:** n = 10

```
i=2: Mark 4,6,8 as False
i=3: Mark 9 as False
isPrime = [F,F,T,T,F,T,F,T,F,F]

Primes: 2, 3, 5, 7 -> Count: 4
```

## ⏱️ **Complexity:**
- **Time:** O(n log log n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
Math, Sieve

## ⚠️ **Gotcha:**
Start marking from i*i, smaller multiples already marked.
