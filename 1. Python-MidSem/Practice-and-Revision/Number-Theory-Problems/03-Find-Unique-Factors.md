# Find Unique Factors of a Number

#number-theory #factors #divisors #for-loop #modulus #lists

---

## Problem Statement

Find all unique factors (divisors) of a given positive integer. A factor of n is a number that divides n completely (remainder = 0).

**Examples**: 
- Factors of 12: [1, 2, 3, 4, 6, 12]
- Factors of 28: [1, 2, 4, 7, 14, 28]
- Factors of 7: [1, 7] (prime number)

---

## Algorithm Approach

### Core Concept
A number `i` is a factor of `n` if `n % i == 0` (no remainder when n is divided by i).

### Step-by-Step Logic
1. **Initialize** empty list to store factors
2. **Iterate** from 1 to n (inclusive)
3. **Check** if `n % i == 0`
4. **If yes**, add `i` to factors list
5. **Return** the complete list of factors

### Mathematical Insight
```
For n = 12:
12 % 1 = 0 → 1 is a factor
12 % 2 = 0 → 2 is a factor  
12 % 3 = 0 → 3 is a factor
12 % 4 = 0 → 4 is a factor
12 % 5 = 2 → 5 is NOT a factor
12 % 6 = 0 → 6 is a factor
...and so on
```

---

## Code Implementation

```python
def unique_factors(n):
    """
    Find all unique factors of a positive integer.
    
    Args:
        n (int): Positive integer to find factors for
    
    Returns:
        list: List of all factors in ascending order
    """
    factors = []
    
    for i in range(1, n + 1):
        if n % i == 0:  # i divides n completely
            factors.append(i)
    
    return factors

# Example usage
numbers = [12, 28, 7, 1, 36]

for num in numbers:
    factors = unique_factors(num)
    print(f"Factors of {num}: {factors}")
```

---

## Detailed Dry Run

### Example 1: n = 12

**Initial Setup:**
```
n = 12
factors = []
```

**Iteration Process:**

| i | n % i | n % i == 0? | Action | factors |
|---|-------|-------------|--------|---------|
| 1 | 12 % 1 = 0 | ✓ Yes | Add 1 | [1] |
| 2 | 12 % 2 = 0 | ✓ Yes | Add 2 | [1, 2] |
| 3 | 12 % 3 = 0 | ✓ Yes | Add 3 | [1, 2, 3] |
| 4 | 12 % 4 = 0 | ✓ Yes | Add 4 | [1, 2, 3, 4] |
| 5 | 12 % 5 = 2 | ✗ No | Skip | [1, 2, 3, 4] |
| 6 | 12 % 6 = 0 | ✓ Yes | Add 6 | [1, 2, 3, 4, 6] |
| 7 | 12 % 7 = 5 | ✗ No | Skip | [1, 2, 3, 4, 6] |
| 8 | 12 % 8 = 4 | ✗ No | Skip | [1, 2, 3, 4, 6] |
| 9 | 12 % 9 = 3 | ✗ No | Skip | [1, 2, 3, 4, 6] |
| 10 | 12 % 10 = 2 | ✗ No | Skip | [1, 2, 3, 4, 6] |
| 11 | 12 % 11 = 1 | ✗ No | Skip | [1, 2, 3, 4, 6] |
| 12 | 12 % 12 = 0 | ✓ Yes | Add 12 | [1, 2, 3, 4, 6, 12] |

**Final Result:** `[1, 2, 3, 4, 6, 12]`

### Example 2: n = 7 (Prime Number)

| i | n % i | n % i == 0? | Action | factors |
|---|-------|-------------|--------|---------|
| 1 | 7 % 1 = 0 | ✓ Yes | Add 1 | [1] |
| 2 | 7 % 2 = 1 | ✗ No | Skip | [1] |
| 3 | 7 % 3 = 1 | ✗ No | Skip | [1] |
| 4 | 7 % 4 = 3 | ✗ No | Skip | [1] |
| 5 | 7 % 5 = 2 | ✗ No | Skip | [1] |
| 6 | 7 % 6 = 1 | ✗ No | Skip | [1] |
| 7 | 7 % 7 = 0 | ✓ Yes | Add 7 | [1, 7] |

**Final Result:** `[1, 7]` (Only 2 factors → Prime number)

---

## Enhanced Implementation with Debugging

```python
def unique_factors_debug(n):
    """
    Find factors with step-by-step debugging output.
    """
    print(f"Finding factors of {n}")
    print("-" * 40)
    
    factors = []
    
    for i in range(1, n + 1):
        remainder = n % i
        is_factor = remainder == 0
        
        if is_factor:
            factors.append(i)
            print(f"i={i:2d}: {n} % {i} = {remainder} → Factor ✓")
        else:
            print(f"i={i:2d}: {n} % {i} = {remainder} → Not factor")
    
    print("-" * 40)
    print(f"All factors of {n}: {factors}")
    print(f"Total factors: {len(factors)}")
    
    return factors

# Test with debugging
unique_factors_debug(12)
```

**Sample Output:**
```
Finding factors of 12
----------------------------------------
i= 1: 12 % 1 = 0 → Factor ✓
i= 2: 12 % 2 = 0 → Factor ✓
i= 3: 12 % 3 = 0 → Factor ✓
i= 4: 12 % 4 = 0 → Factor ✓
i= 5: 12 % 5 = 2 → Not factor
i= 6: 12 % 6 = 0 → Factor ✓
i= 7: 12 % 7 = 5 → Not factor
i= 8: 12 % 8 = 4 → Not factor
i= 9: 12 % 9 = 3 → Not factor
i=10: 12 % 10 = 2 → Not factor
i=11: 12 % 11 = 1 → Not factor
i=12: 12 % 12 = 0 → Factor ✓
----------------------------------------
All factors of 12: [1, 2, 3, 4, 6, 12]
Total factors: 6
```

---

## Optimized Approaches

### Method 1: Square Root Optimization
```python
import math

def unique_factors_optimized(n):
    """
    Find factors efficiently using square root optimization.
    Time complexity: O(√n) instead of O(n)
    """
    factors = []
    
    # Check factors up to square root
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)  # Add the factor
            
            # Add the corresponding factor (n/i) if it's different
            if i != n // i:
                factors.append(n // i)
    
    # Sort factors in ascending order
    factors.sort()
    return factors

# Test optimized version
print(unique_factors_optimized(36))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
```

**How Square Root Optimization Works:**
```
For n = 36:
√36 = 6, so check i from 1 to 6

i=1: 36%1=0 → Add 1 and 36/1=36 → factors=[1,36]
i=2: 36%2=0 → Add 2 and 36/2=18 → factors=[1,36,2,18]  
i=3: 36%3=0 → Add 3 and 36/3=12 → factors=[1,36,2,18,3,12]
i=4: 36%4=0 → Add 4 and 36/4=9  → factors=[1,36,2,18,3,12,4,9]
i=5: 36%5=1 → Skip
i=6: 36%6=0 → Add 6, but 36/6=6 (same), so add only once

After sorting: [1,2,3,4,6,9,12,18,36]
```

### Method 2: Using List Comprehension
```python
def unique_factors_comprehension(n):
    """Find factors using list comprehension (concise but less readable)."""
    return [i for i in range(1, n + 1) if n % i == 0]

# Test
print(unique_factors_comprehension(28))  # [1, 2, 4, 7, 14, 28]
```

---

## Factor Analysis Functions

### Count Total Factors
```python
def count_factors(n):
    """Count total number of factors."""
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Test
print(f"12 has {count_factors(12)} factors")  # 12 has 6 factors
```

### Find Proper Factors (Excluding the number itself)
```python
def proper_factors(n):
    """Find all factors except the number itself."""
    factors = []
    for i in range(1, n):  # Note: range goes up to n-1
        if n % i == 0:
            factors.append(i)
    return factors

# Test
print(f"Proper factors of 12: {proper_factors(12)}")  # [1, 2, 3, 4, 6]
```

### Check Perfect Number
```python
def is_perfect_number(n):
    """
    A perfect number equals the sum of its proper factors.
    Example: 6 = 1 + 2 + 3 (proper factors of 6)
    """
    proper_factors_list = proper_factors(n)
    return sum(proper_factors_list) == n

# Test perfect numbers
perfect_candidates = [6, 28, 12, 496]
for num in perfect_candidates:
    if is_perfect_number(num):
        print(f"{num} is a perfect number")
        print(f"  Proper factors: {proper_factors(num)}")
        print(f"  Sum: {sum(proper_factors(num))}")
```

---

## Complete Analysis Suite

```python
def factor_analysis(n):
    """Complete factor analysis of a number."""
    print(f"Factor Analysis for {n}")
    print("=" * 50)
    
    # Find all factors
    factors = unique_factors(n)
    proper = proper_factors(n)
    
    print(f"All factors: {factors}")
    print(f"Proper factors: {proper}")
    print(f"Total factors: {len(factors)}")
    
    # Factor properties
    print(f"Sum of all factors: {sum(factors)}")
    print(f"Sum of proper factors: {sum(proper)}")
    
    # Number classifications
    if len(factors) == 2:
        print("Classification: Prime number")
    elif is_perfect_number(n):
        print("Classification: Perfect number")
    elif sum(proper) > n:
        print("Classification: Abundant number")
    elif sum(proper) < n:
        print("Classification: Deficient number")
    
    # Factor pairs
    print("Factor pairs:")
    for i in range(len(factors) // 2 + 1):
        if i < len(factors) - 1 - i:
            print(f"  {factors[i]} × {factors[len(factors) - 1 - i]} = {n}")
        elif i == len(factors) - 1 - i:
            print(f"  {factors[i]} × {factors[i]} = {n} (perfect square)")
    
    print("=" * 50)

# Test comprehensive analysis
test_numbers = [12, 28, 7, 36, 6]
for num in test_numbers:
    factor_analysis(num)
    print()
```

---

## Applications & Use Cases

### Finding Common Factors
```python
def common_factors(a, b):
    """Find common factors of two numbers."""
    factors_a = unique_factors(a)
    factors_b = unique_factors(b)
    
    common = []
    for factor in factors_a:
        if factor in factors_b:
            common.append(factor)
    
    return common

# Test
print(f"Common factors of 12 and 18: {common_factors(12, 18)}")  # [1, 2, 3, 6]
```

### Greatest Common Divisor (GCD)
```python
def gcd_using_factors(a, b):
    """Find GCD using common factors."""
    common = common_factors(a, b)
    return max(common) if common else 1

# Test
print(f"GCD of 12 and 18: {gcd_using_factors(12, 18)}")  # 6
```

### Finding Numbers with Specific Factor Count
```python
def numbers_with_n_factors(limit, target_count):
    """Find all numbers up to limit with exactly target_count factors."""
    result = []
    
    for num in range(1, limit + 1):
        if count_factors(num) == target_count:
            result.append(num)
    
    return result

# Find numbers with exactly 6 factors
print(f"Numbers ≤ 30 with 6 factors: {numbers_with_n_factors(30, 6)}")
# Output: [12, 18, 20, 28, 30]
```

---

## Time & Space Complexity

### Basic Algorithm
- **Time Complexity**: O(n) - Check every number from 1 to n
- **Space Complexity**: O(k) - Where k is the number of factors

### Optimized Algorithm (Square Root)
- **Time Complexity**: O(√n) - Check only up to square root
- **Space Complexity**: O(k) - Where k is the number of factors

### Comparison for n = 1,000,000:
- Basic: 1,000,000 iterations
- Optimized: 1,000 iterations (1000× faster!)

---

## Common Mistakes & Edge Cases

> [!WARNING] **Common Errors**
> - Forgetting to include 1 and n as factors
> - Not handling n = 0 or negative numbers
> - Off-by-one errors in range (should be 1 to n+1)
> - Not sorting factors in optimized version

> [!TIP] **Best Practices**
> - Use optimized version for large numbers
> - Handle edge cases (0, 1, negative numbers)
> - Consider memory usage for very large numbers
> - Add input validation

### Robust Implementation
```python
def unique_factors_robust(n):
    """Robust factor finder with input validation."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return [1]
    
    # Use optimized method for large numbers
    if n > 1000:
        return unique_factors_optimized(n)
    else:
        return unique_factors(n)
```

---

## Practice Problems

1. **Find** the number between 1-100 with the most factors
2. **Check** if a number is a perfect square using its factors
3. **Find** all numbers whose factors sum to a given value
4. **Implement** prime factorization using the factor concept

```python
# Practice solutions
def number_with_most_factors(limit):
    """Find number with maximum factors in range."""
    max_factors = 0
    result_num = 1
    
    for num in range(1, limit + 1):
        factor_count = count_factors(num)
        if factor_count > max_factors:
            max_factors = factor_count
            result_num = num
    
    return result_num, max_factors

def is_perfect_square_by_factors(n):
    """Check if number is perfect square using factor count."""
    # Perfect squares have odd number of factors
    return count_factors(n) % 2 == 1

# Test
num, count = number_with_most_factors(100)
print(f"Number with most factors (1-100): {num} with {count} factors")
print(f"Is 36 a perfect square? {is_perfect_square_by_factors(36)}")  # True
```

---

## Related Topics
- [[04-Check-Prime-Number]] - Numbers with exactly 2 factors
- [[For-Loops]] - Iteration structure used
- [[Lists]] - Storing factors

**Next**: Learn about [[04-Check-Prime-Number]] →