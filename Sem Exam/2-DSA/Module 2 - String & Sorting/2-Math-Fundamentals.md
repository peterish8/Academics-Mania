# ➗ Math Fundamentals for DSA

## 🎯 **Number Theory Basics**

> [!SUCCESS] **Goal**: Basic math algorithms often show up in "Logic" rounds.

---

## 🔢 **1. Digits Extraction**

> Extract digits from right to left using `%` and `//`.

```python
num = 123
while num > 0:
    digit = num % 10  # Get last digit (3)
    num = num // 10   # Remove last digit (12)
    print(digit)
```
- **Power of Digits**: Armstrong numbers etc.
- **Factorial Trailing Zeroes**: Count factors of 5.

---

## 🤝 **2. GCD & LCM**

> **GCD (Greatest Common Divisor)**: Euclidean Algorithm.
> `GCD(a, b) = GCD(b, a % b)`

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

> **LCM**: `(a * b) // gcd(a, b)`

---

## 🕵️ **3. Prime Numbers (Sieve of Eratosthenes)**

> Find all primes up to N efficiently. **O(n log log n)**.

**Algorithm**:
1.  Assume all are True (Prime).
2.  Start at 2. Mark multiples of 2 as False.
3.  Move to next True (3). Mark multiples of 3 as False.
4.  Repeat up to `sqrt(n)`.

---

## 🕰️ **4. Modular Arithmetic**

> `(a + b) % m = ((a % m) + (b % m)) % m`
> Essential for preventing Integer Overflow in competitive programming (e.g., modulo `10^9 + 7`).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Last Digit** = `% 10`.
> - **Remove Last** = `// 10`.
> - **GCD** = Keep modding until 0.
> - **Sieve** = Mark multiples ❌.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Why do we check primes only up to `sqrt(n)`?
> > [!SUCCESS]- Answer
> > Because if a number `n` has a factor larger than `sqrt(n)`, the OTHER factor must be smaller than `sqrt(n)` (and we already checked it).

> [!QUESTION] **Q2**: What is `123 % 10`?
> > [!SUCCESS]- Answer
> > **3**.

> [!QUESTION] **Q3**: Time complexity of checking Prime naively (loop 2 to n)?
> > [!SUCCESS]- Answer
> > **O(n)**. (Can be improved to O(sqrt(n))).

> [!QUESTION] **Q4**: How many trailing zeroes in 100! (Factorial)?
> > [!SUCCESS]- Answer
> > Count pair of (2*5). Since 5s are rarer, count multiples of 5, 25, 125... logic.

> [!QUESTION] **Q5**: What is the GCD of 12 and 15?
> > [!SUCCESS]- Answer
> > **3**.

---

Back to: [[Sem Exam/2-DSA/Module 2 - String & Sorting/README|Module 2 Hub]] | [[../DSA-Hub|DSA Hub]]
