# Check Palindrome Number

#number-theory #palindrome #loops #conditionals #comparison

---

## Problem Statement

A palindrome number reads the same forwards and backwards. Check if a given number is a palindrome.

**Examples**: 
- 121 → Palindrome (reads same: 1-2-1)
- 1234 → Not palindrome (1234 ≠ 4321)
- 7 → Palindrome (single digit)
- 1001 → Palindrome (1-0-0-1)

---

## Algorithm Approach

### Core Concept
Compare the original number with its reversed version. If they're equal, it's a palindrome.

### Step-by-Step Logic
1. **Store** original number for comparison
2. **Reverse** the number using the reversal algorithm
3. **Compare** original with reversed
4. **Return** True if equal, False otherwise

### Mathematical Insight
```
Original: 121
Reversed: 121
121 == 121 → Palindrome ✓

Original: 1234  
Reversed: 4321
1234 ≠ 4321 → Not Palindrome ✗
```

---

## Code Implementation

```python
def is_palindrome(num):
    """
    Check if a number is a palindrome.
    
    Args:
        num (int): Positive integer to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    original = num  # Store original for comparison
    rev = 0
    
    # Reverse the number
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    
    # Compare original with reversed
    return original == rev

# Example usage
test_numbers = [121, 1234, 7, 1001, 12321]

for num in test_numbers:
    if is_palindrome(num):
        print(f"{num} is a Palindrome ✓")
    else:
        print(f"{num} is NOT a Palindrome ✗")
```

---

## Detailed Dry Run

### Example 1: num = 121 (Palindrome)

**Phase 1: Store Original**
```
original = 121
num = 121
rev = 0
```

**Phase 2: Reverse Process**

| Iteration | num | digit = num % 10 | rev = rev * 10 + digit | num //= 10 |
|-----------|-----|------------------|------------------------|------------|
| Initial   | 121 | -                | rev = 0                | -          |
| 1         | 121 | 1                | 0 * 10 + 1 = 1         | 12         |
| 2         | 12  | 2                | 1 * 10 + 2 = 12        | 1          |
| 3         | 1   | 1                | 12 * 10 + 1 = 121      | 0          |
| End       | 0   | Loop exits       | **rev = 121**          | -          |

**Phase 3: Comparison**
```
original = 121
rev = 121
121 == 121 → True (Palindrome)
```

### Example 2: num = 1234 (Not Palindrome)

**Phase 1: Store Original**
```
original = 1234
num = 1234
rev = 0
```

**Phase 2: Reverse Process**

| Iteration | num  | digit = num % 10 | rev = rev * 10 + digit | num //= 10 |
|-----------|------|------------------|------------------------|------------|
| Initial   | 1234 | -                | rev = 0                | -          |
| 1         | 1234 | 4                | 0 * 10 + 4 = 4         | 123        |
| 2         | 123  | 3                | 4 * 10 + 3 = 43        | 12         |
| 3         | 12   | 2                | 43 * 10 + 2 = 432      | 1          |
| 4         | 1    | 1                | 432 * 10 + 1 = 4321    | 0          |
| End       | 0    | Loop exits       | **rev = 4321**         | -          |

**Phase 3: Comparison**
```
original = 1234
rev = 4321
1234 ≠ 4321 → False (Not Palindrome)
```

---

## Enhanced Implementation with Debugging

```python
def is_palindrome_debug(num):
    """
    Check palindrome with step-by-step debugging output.
    """
    print(f"Checking if {num} is a palindrome...")
    print("-" * 50)
    
    original = num
    rev = 0
    step = 1
    
    print(f"Original number: {original}")
    print("Reversing process:")
    
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        
        print(f"  Step {step}: digit={digit}, rev={rev}, remaining={num}")
        step += 1
    
    print(f"Reversed number: {rev}")
    print(f"Comparison: {original} == {rev} → {original == rev}")
    
    result = original == rev
    print(f"Result: {'Palindrome ✓' if result else 'Not Palindrome ✗'}")
    print("-" * 50)
    
    return result

# Test with debugging
test_cases = [121, 1234, 7, 1001]
for num in test_cases:
    is_palindrome_debug(num)
    print()
```

**Sample Output:**
```
Checking if 121 is a palindrome...
--------------------------------------------------
Original number: 121
Reversing process:
  Step 1: digit=1, rev=1, remaining=12
  Step 2: digit=2, rev=12, remaining=1
  Step 3: digit=1, rev=121, remaining=0
Reversed number: 121
Comparison: 121 == 121 → True
Result: Palindrome ✓
```

---

## Alternative Approaches

### Method 1: String Comparison (Simple but Less Efficient)
```python
def is_palindrome_string(num):
    """Check palindrome using string reversal."""
    str_num = str(num)
    return str_num == str_num[::-1]

# Test
print(is_palindrome_string(121))  # True
print(is_palindrome_string(1234)) # False
```

### Method 2: Half-Number Comparison (Optimized)
```python
def is_palindrome_optimized(num):
    """
    Check palindrome by comparing only half the digits.
    More efficient for large numbers.
    """
    if num < 0:
        return False
    
    original = num
    rev = 0
    
    # Reverse only half the number
    while num > rev:
        rev = rev * 10 + num % 10
        num //= 10
    
    # For even digits: num == rev
    # For odd digits: num == rev // 10 (ignore middle digit)
    return num == rev or num == rev // 10

# Test
print(is_palindrome_optimized(12321))  # True
print(is_palindrome_optimized(1234))   # False
```

### Method 3: Recursive Approach
```python
def reverse_recursive(num, rev=0):
    """Recursively reverse a number."""
    if num == 0:
        return rev
    return reverse_recursive(num // 10, rev * 10 + num % 10)

def is_palindrome_recursive(num):
    """Check palindrome using recursion."""
    return num == reverse_recursive(num)

# Test
print(is_palindrome_recursive(121))   # True
print(is_palindrome_recursive(1234))  # False
```

---

## Complete Test Suite

```python
def comprehensive_palindrome_test():
    """Test palindrome function with various cases."""
    
    test_cases = [
        # (number, expected_result, description)
        (0, True, "Zero"),
        (7, True, "Single digit"),
        (11, True, "Two identical digits"),
        (121, True, "Three digit palindrome"),
        (1234, False, "Four digit non-palindrome"),
        (12321, True, "Five digit palindrome"),
        (123454321, True, "Nine digit palindrome"),
        (1001, True, "Palindrome with zeros"),
        (10, False, "Two digit non-palindrome")
    ]
    
    print("Comprehensive Palindrome Test")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for num, expected, description in test_cases:
        result = is_palindrome(num)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"{num:>10} | {description:<25} | {result:<5} | {status}")
        
        if result == expected:
            passed += 1
    
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    print(f"Success rate: {(passed/total)*100:.1f}%")

# Run comprehensive test
comprehensive_palindrome_test()
```

---

## Edge Cases & Special Considerations

### Handling Edge Cases
```python
def is_palindrome_robust(num):
    """Robust palindrome checker with edge case handling."""
    
    # Handle negative numbers
    if num < 0:
        return False  # Negative numbers are not palindromes
    
    # Handle single digit (always palindrome)
    if num < 10:
        return True
    
    # Handle numbers ending with 0 (except 0 itself)
    if num % 10 == 0:
        return False  # Can't be palindrome (leading zeros issue)
    
    # Standard palindrome check
    original = num
    rev = 0
    
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    
    return original == rev

# Test edge cases
edge_cases = [-121, 0, 7, 10, 100, 1001]
for num in edge_cases:
    result = is_palindrome_robust(num)
    print(f"{num}: {'Palindrome' if result else 'Not Palindrome'}")
```

---

## Time & Space Complexity

- **Time Complexity**: O(log n)
  - We process each digit once
  - Number of digits = log₁₀(n)

- **Space Complexity**: O(1)
  - Only using constant extra space

**Comparison with String Method:**
- String method: O(log n) time, O(log n) space
- Mathematical method: O(log n) time, O(1) space

---

## Common Applications

### Finding Palindromic Numbers in Range
```python
def find_palindromes_in_range(start, end):
    """Find all palindromic numbers in a given range."""
    palindromes = []
    
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    
    return palindromes

# Find palindromes between 100 and 200
result = find_palindromes_in_range(100, 200)
print(f"Palindromes between 100-200: {result}")
# Output: [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
```

### Largest Palindrome Product
```python
def largest_palindrome_product(digits):
    """Find largest palindrome made from product of two n-digit numbers."""
    max_num = 10**digits - 1
    min_num = 10**(digits-1)
    
    largest_palindrome = 0
    
    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product
    
    return largest_palindrome

# Find largest palindrome from product of two 2-digit numbers
result = largest_palindrome_product(2)
print(f"Largest palindrome from 2-digit products: {result}")
```

---

## Practice Problems

1. **Count** palindromic numbers in a range
2. **Find** the next palindromic number after a given number
3. **Check** if sum of a number and its reverse is a palindrome
4. **Generate** palindromic numbers of specific length

```python
# Practice solutions
def next_palindrome(num):
    """Find the next palindromic number after num."""
    num += 1
    while not is_palindrome(num):
        num += 1
    return num

def is_sum_palindrome(num):
    """Check if num + reverse(num) is palindrome."""
    reversed_num = int(str(num)[::-1])
    sum_result = num + reversed_num
    return is_palindrome(sum_result)

# Test
print(next_palindrome(121))  # 131
print(is_sum_palindrome(89)) # True (89 + 98 = 187, not palindrome, but 187 + 781 = 968...)
```

---

## Related Topics
- [[01-Reverse-Number]] - Core algorithm used here
- [[While-Loops]] - Loop structure
- [[Comparison-Operators]] - Equality checking

**Next**: Learn about [[03-Find-Unique-Factors]] →