# 🔢 HCF / GCD - Complete Guide

## 🎯 **What is GCD (HCF)?**

> [!SUCCESS] **Definition**: The **Greatest Common Divisor** (GCD) or **Highest Common Factor** (HCF) is the largest number that can divide two or more numbers exactly, with no remainder.

---

## 📝 **Examples**

**Example 1:** GCD(16, 24)
```
16 → 1, 2, 4, 8, 16
24 → 1, 2, 3, 4, 6, 8, 12, 24
Common: 1, 2, 4, 8
GCD = 8 ✅
```

**Example 2:** GCD(4, 12)
```
4  → 1, 2, 4
12 → 1, 2, 3, 4, 6, 12
Common: 1, 2, 4
GCD = 4 ✅
```

---

## 🐌 **Approach 1: Brute Force (Forward Loop)**

> Check all numbers from 1 to min(a,b). Keep tracking the largest divisor.

```python
def gcd_brute(a, b):
    ans = 0
    min_val = min(a, b)
    
    for i in range(1, min_val + 1):
        if a % i == 0 and b % i == 0:
            ans = i  # Update answer
    
    return ans

# TEST
print("GCD(16, 24):", gcd_brute(16, 24))
print("GCD(4, 12):", gcd_brute(4, 12))
print("GCD(20, 20):", gcd_brute(20, 20))
```

**Time Complexity:** O(min(a, b)) ❌ Slow!

---

## 🚶 **Approach 2: Reverse Loop (Slightly Better)**

> Start from min(a,b) and go backwards. Return immediately when found.

```python
def gcd_reverse(a, b):
    min_val = min(a, b)
    
    for i in range(min_val, 0, -1):
        if a % i == 0 and b % i == 0:
            return i  # Found! Return immediately
    
    return 1

# TEST
print("GCD(16, 24):", gcd_reverse(16, 24))
print("GCD(4, 12):", gcd_reverse(4, 12))
```

> [!WARNING] **Edge Case Problem**
> If both numbers are **prime** (e.g., 7 and 11), GCD = 1.
> Loop runs all the way to 1 → Still O(min(a, b)) in worst case!

---

## ⚡ **Approach 3: Euclidean Algorithm (Optimal)**

> [!TIP] **Key Insight**
> `GCD(a, b) = GCD(b, a % b)` until b becomes 0.
> When b = 0, a is the GCD!

**Why it works:**
- If `d` divides both `a` and `b`, then `d` also divides `a % b`
- So we can keep reducing the problem size

---

### 🏃 **Dry Run: GCD(33, 12)**

| Step | a | b | a % b |
|------|---|---|-------|
| 1 | 33 | 12 | 9 |
| 2 | 12 | 9 | 3 |
| 3 | 9 | 3 | 0 |
| 4 | 3 | **0** | - |

**When b = 0, a = 3 → GCD = 3** ✅

---

### 💻 **Code (Runnable)**

```python
def gcd_euclidean(a, b):
    # Ensure a >= b
    if a < b:
        a, b = b, a
    
    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a

# TEST
print("GCD(33, 12):", gcd_euclidean(33, 12))
print("GCD(16, 24):", gcd_euclidean(16, 24))
print("GCD(48, 18):", gcd_euclidean(48, 18))
print("GCD(7, 11):", gcd_euclidean(7, 11))  # Prime numbers
```

**Time Complexity:** O(log(min(a, b))) ✅ Much faster!

---

## 📊 **Comparison Table**

| Approach | Time Complexity | Space | Notes |
|----------|-----------------|-------|-------|
| **Brute Force** | O(min(a,b)) | O(1) | Too slow |
| **Reverse Loop** | O(min(a,b)) | O(1) | Same worst case |
| **Euclidean** | O(log(min(a,b))) | O(1) | **Optimal!** ⚡ |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Euclidean**: `GCD(a, b) = GCD(b, a % b)`
> - **Stop when**: `b = 0`, answer is `a`
> - **Log time** because problem size reduces by half each step
> - **Swap trick**: `a, b = b, a % b` does it in one line!

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is GCD of any number and itself?
> > [!SUCCESS]- Answer
> > The number itself! GCD(n, n) = n

> [!QUESTION] **Q2**: What is GCD of any number and 1?
> > [!SUCCESS]- Answer
> > Always 1. GCD(n, 1) = 1

> [!QUESTION] **Q3**: Why is Euclidean faster than brute force?
> > [!SUCCESS]- Answer
> > Instead of checking every number, it reduces the problem size exponentially using modulo.

> [!QUESTION] **Q4**: What's the GCD of two prime numbers (e.g., 7 and 11)?
> > [!SUCCESS]- Answer
> > Always 1 (they share no common factors except 1).

> [!QUESTION] **Q5**: How to find LCM using GCD?
> > [!SUCCESS]- Answer
> > `LCM(a, b) = (a * b) / GCD(a, b)`

---

Back to: [[Sem Exam/2-DSA/DSA-Hub|DSA Hub]]
