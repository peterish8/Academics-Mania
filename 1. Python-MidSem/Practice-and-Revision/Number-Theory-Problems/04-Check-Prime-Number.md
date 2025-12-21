# Check if Number is Prime

#number-theory #prime-numbers #loops #optimization #math

---

## Problem Statement

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Check if a given number is prime.

**Examples**: 
- 2 → Prime (only factors: 1, 2)
- 7 → Prime (only factors: 1, 7)  
- 9 → Not Prime (factors: 1, 3, 9)
- 1 → Not Prime (by definition)
- 0 → Not Prime (by definition)

---

## Algorithm Approach

### Core Concept
A number is prime if it has exactly 2 factors: 1 and itself.

### Step-by-Step Logic
1. **Handle special cases**: 0, 1 are not prime
2. **Handle base case**: 2 is the only even prime
3. **Check divisibility** from 2 to √n
4. **If any divisor found** → Not prime
5. **If no divisors found** → Prime

### Mathematical Insight
```
Why check only up to √n?
If n has a divisor > √n, then n/divisor < √n
So we would have already found the smaller divisor.

Example: For n = 36
√36 = 6
If we find divisor 2, then 36/2 = 18 is also a divisor
We don't need to check beyond 6.
```

---

## Code Implementation

```python
def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if prime, False otherwise
    """
    # Handle special cases
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Even numbers > 2 are not prime
    if n % 2 == 0:
        return False
    
    # Check odd divisors from 3 to √n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Example usage
test_numbers = [2, 7, 9, 17, 25, 29, 1, 0]

for num in test_numbers:
    if is_prime(num):
        print(f"{num} is Prime ✓")
    else:
        print(f"{num} is NOT Prime ✗")
```

---

## Detailed Dry Run

### Example 1: n = 17 (Prime Number)

**Step 1: Special Cases**
```
n = 17
17 <= 1? No → Continue
17 == 2? No → Continue  
17 % 2 == 0? No (17 % 2 = 1) → Continue
```

**Step 2: Check Divisors**
```
√17 ≈ 4.12, so check up to 4
Check odd numbers: 3
```

| i | n % i | n % i == 0? | Action |
|---|-------|-------------|--------|
| 3 | 17 % 3 = 2 | ✗ No | Continue |

**Step 3: Result**
```
No divisors found → 17 is Prime ✓
```

### Example 2: n = 25 (Not Prime)

**Step 1: Special Cases**
```
n = 25
25 <= 1? No → Continue
25 == 2? No → Continue
25 % 2 == 0? No (25 % 2 = 1) → Continue
```

**Step 2: Check Divisors**
```
√25 = 5, so check up to 5
Check odd numbers: 3, 5
```

| i | n % i | n % i == 0? | Action |
|---|-------|-------------|--------|
| 3 | 25 % 3 = 1 | ✗ No | Continue |
| 5 | 25 % 5 = 0 | ✓ Yes | **Return False** |

**Step 3: Result**
```
Divisor found (5) → 25 is NOT Prime ✗
```

### Example 3: n = 2 (Special Case)

**Step 1: Special Cases**
```
n = 2
2 <= 1? No → Continue
2 == 2? Yes → Return True
```

**Result:** `2 is Prime ✓`

---

## Enhanced Implementation with Debugging

```python
def is_prime_debug(n):
    """
    Check primality with step-by-step debugging output.
    """
    print(f"Checking if {n} is prime...")
    print("-" * 40)
    
    # Handle special cases
    if n <= 1:
        print(f"{n} ≤ 1 → Not prime by definition")
        return False
    
    if n == 2:
        print("2 is the only even prime number")
        return True
    
    if n % 2 == 0:
        print(f"{n} is even and > 2 → Not prime")
        return False
    
    # Check odd divisors
    limit = int(n**0.5) + 1
    print(f"Checking divisors from 3 to {limit-1} (√{n} ≈ {n**0.5:.2f})")
    
    for i in range(3, limit, 2):
        remainder = n % i
        print(f"  {n} % {i} = {remainder}", end="")
        
        if remainder == 0:
            print(f" → Divisible! {n} = {i} × {n//i}")
            print(f"Result: {n} is NOT Prime ✗")
            return False
        else:
            print(" → Not divisible")
    
    print(f"No divisors found → {n} is Prime ✓")
    return True

# Test with debugging
test_cases = [17, 25, 29, 49]
for num in test_cases:
    is_prime_debug(num)
    print()
```

**Sample Output for n = 25:**
```
Checking if 25 is prime...
----------------------------------------
Checking divisors from 3 to 6 (√25 ≈ 5.00)
  25 % 3 = 1 → Not divisible
  25 % 5 = 0 → Divisible! 25 = 5 × 5
Result: 25 is NOT Prime ✗
```

---

## Algorithm Variations

### Method 1: Basic Approach (Less Efficient)
```python
def is_prime_basic(n):
    """Basic prime check - checks all numbers from 2 to n-1."""
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Time complexity: O(n) - very slow for large numbers
```

### Method 2: Optimized with Early Even Check
```python
def is_prime_optimized(n):
    """Optimized version - our main implementation."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisors of form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Even more optimized - uses the fact that all primes > 3 are of form 6k±1
```

### Method 3: Using Factors Function
```python
def is_prime_using_factors(n):
    """Check primality using factor count."""
    from unique_factors import count_factors  # Assuming previous function
    return count_factors(n) == 2

# Simple but less efficient for large numbers
```

---

## Performance Comparison

```python
import time

def time_prime_methods(n):
    """Compare performance of different prime checking methods."""
    methods = [
        ("Basic O(n)", is_prime_basic),
        ("Optimized O(√n)", is_prime),
        ("Advanced O(√n)", is_prime_optimized)
    ]
    
    print(f"Testing primality of {n}")
    print("-" * 50)
    
    for name, method in methods:
        start_time = time.time()
        result = method(n)
        end_time = time.time()
        
        print(f"{name:15}: {result} ({end_time - start_time:.6f}s)")

# Test with a large number
time_prime_methods(982451653)  # Large prime number
```

---

## Prime Number Applications

### Generate Prime Numbers (Sieve of Eratosthenes)
```python
def sieve_of_eratosthenes(limit):
    """Generate all prime numbers up to limit using sieve method."""
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime_arr[i]:
            # Mark multiples of i as not prime
            for j in range(i*i, limit + 1, i):
                is_prime_arr[j] = False
    
    # Collect all prime numbers
    primes = [i for i in range(2, limit + 1) if is_prime_arr[i]]
    return primes

# Generate primes up to 50
primes_50 = sieve_of_eratosthenes(50)
print(f"Primes up to 50: {primes_50}")
```

### Find Next Prime Number
```python
def next_prime(n):
    """Find the next prime number after n."""
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

# Test
print(f"Next prime after 20: {next_prime(20)}")  # 23
print(f"Next prime after 100: {next_prime(100)}")  # 101
```

### Prime Factorization
```python
def prime_factorization(n):
    """Find prime factorization of a number."""
    factors = []
    divisor = 2
    
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

# Test
print(f"Prime factors of 60: {prime_factorization(60)}")  # [2, 2, 3, 5]
print(f"Prime factors of 17: {prime_factorization(17)}")  # [17]
```

---

## Complete Prime Analysis Suite

```python
def prime_analysis(n):
    """Complete prime number analysis."""
    print(f"Prime Analysis for {n}")
    print("=" * 50)
    
    # Basic prime check
    is_prime_result = is_prime(n)
    print(f"Is {n} prime? {is_prime_result}")
    
    if not is_prime_result:
        # Find factors if not prime
        factors = []
        for i in range(2, n):
            if n % i == 0:
                factors.append(i)
        print(f"Factors (excluding 1 and {n}): {factors}")
        
        # Prime factorization
        prime_factors = prime_factorization(n)
        print(f"Prime factorization: {prime_factors}")
        
        # Express as product
        factor_str = " × ".join(map(str, prime_factors))
        print(f"{n} = {factor_str}")
    
    else:
        print(f"{n} is prime - only divisible by 1 and {n}")
        
        # Find previous and next primes
        prev_prime = n - 1
        while prev_prime > 1 and not is_prime(prev_prime):
            prev_prime -= 1
        
        next_prime_num = next_prime(n)
        
        if prev_prime > 1:
            print(f"Previous prime: {prev_prime}")
        print(f"Next prime: {next_prime_num}")
        print(f"Prime gap: {next_prime_num - n}")
    
    print("=" * 50)

# Test comprehensive analysis
test_numbers = [17, 25, 97, 100]
for num in test_numbers:
    prime_analysis(num)
    print()
```

---

## Special Prime Categories

### Twin Primes
```python
def find_twin_primes(limit):
    """Find twin prime pairs (primes that differ by 2)."""
    twin_primes = []
    
    for p in range(2, limit - 2):
        if is_prime(p) and is_prime(p + 2):
            twin_primes.append((p, p + 2))
    
    return twin_primes

# Find twin primes up to 50
twins = find_twin_primes(50)
print(f"Twin primes up to 50: {twins}")
# Output: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
```

### Mersenne Primes
```python
def is_mersenne_prime(p):
    """Check if 2^p - 1 is prime (where p is prime)."""
    if not is_prime(p):
        return False
    
    mersenne_num = 2**p - 1
    return is_prime(mersenne_num)

# Check first few Mersenne primes
for p in [2, 3, 5, 7, 13, 17, 19]:
    mersenne_num = 2**p - 1
    if is_mersenne_prime(p):
        print(f"2^{p} - 1 = {mersenne_num} is a Mersenne prime")
```

---

## Time & Space Complexity

### Different Approaches:

| Method | Time Complexity | Space Complexity | Best For |
|--------|----------------|------------------|----------|
| Basic | O(n) | O(1) | Small numbers |
| Square Root | O(√n) | O(1) | General use |
| Sieve | O(n log log n) | O(n) | Multiple primes |
| Advanced | O(√n) | O(1) | Large numbers |

### Practical Performance:
- For n = 1,000,000:
  - Basic: ~1,000,000 operations
  - Square Root: ~1,000 operations
  - Advanced: ~500 operations

---

## Common Mistakes & Edge Cases

> [!WARNING] **Common Errors**
> - Forgetting that 1 is not prime
> - Not handling 2 as special case (only even prime)
> - Checking even numbers unnecessarily
> - Integer overflow for very large numbers
> - Not optimizing the search range

> [!TIP] **Best Practices**
> - Always handle edge cases (0, 1, 2)
> - Use square root optimization
> - Skip even numbers after 2
> - Consider using sieve for multiple prime checks
> - Add input validation

### Robust Implementation
```python
def is_prime_robust(n):
    """Robust prime checker with comprehensive validation."""
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Optimized checking
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True
```

---

## Practice Problems

1. **Find** the largest prime number less than 1000
2. **Count** how many prime numbers exist between 1 and 100
3. **Check** if the sum of two primes equals a given even number (Goldbach's conjecture)
4. **Find** the smallest prime factor of a composite number

```python
# Practice solutions
def largest_prime_below(limit):
    """Find largest prime below given limit."""
    for num in range(limit - 1, 1, -1):
        if is_prime(num):
            return num
    return None

def count_primes_in_range(start, end):
    """Count primes in given range."""
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

def goldbach_check(even_num):
    """Check if even number can be expressed as sum of two primes."""
    if even_num % 2 != 0 or even_num < 4:
        return False
    
    for p in range(2, even_num // 2 + 1):
        if is_prime(p) and is_prime(even_num - p):
            return True, (p, even_num - p)
    
    return False, None

# Test
print(f"Largest prime < 1000: {largest_prime_below(1000)}")  # 997
print(f"Primes between 1-100: {count_primes_in_range(1, 100)}")  # 25
result, pair = goldbach_check(20)
if result:
    print(f"20 = {pair[0]} + {pair[1]} (both prime)")  # 20 = 3 + 17
```

---

## Related Topics
- [[03-Find-Unique-Factors]] - Prime numbers have exactly 2 factors
- [[For-Loops]] - Iteration for checking divisors
- [[Math-Functions]] - Square root calculations

**Next**: Explore more [[Number-Theory-Problems]] or return to [[Python Todo-s]] →