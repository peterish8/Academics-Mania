# Reverse a Number

#number-theory #loops #while-loop #modulus #math

---

## Problem Statement

Given a positive integer, reverse its digits and return the reversed number.

**Example**: 
- Input: 1234 → Output: 4321
- Input: 5670 → Output: 765 (leading zeros are dropped)

---

## Algorithm Approach

### Core Concept
To reverse a number, we extract digits from right to left and build the reversed number from left to right.

### Step-by-Step Logic
1. **Initialize** `rev = 0` (to store reversed number)
2. **Extract** last digit using `num % 10`
3. **Append** digit to reversed number: `rev = rev * 10 + digit`
4. **Remove** last digit from original: `num //= 10`
5. **Repeat** until `num` becomes 0

### Visual Representation
```
Original: 1234
Step 1: digit = 4, rev = 0*10 + 4 = 4,    num = 123
Step 2: digit = 3, rev = 4*10 + 3 = 43,   num = 12
Step 3: digit = 2, rev = 43*10 + 2 = 432, num = 1
Step 4: digit = 1, rev = 432*10 + 1 = 4321, num = 0
Result: 4321
```

---

## Code Implementation

```python
def reverse_number(num):
    """
    Reverse the digits of a positive integer.
    
    Args:
        num (int): Positive integer to reverse
    
    Returns:
        int: Reversed number
    """
    rev = 0
    while num > 0:
        digit = num % 10        # Extract last digit
        rev = rev * 10 + digit  # Append to reversed number
        num //= 10              # Remove last digit
    return rev

# Example usage
num = 1234
result = reverse_number(num)
print(f"Original: {1234}")
print(f"Reversed: {result}")
```

---

## Detailed Dry Run

### Example 1: num = 1234

| Iteration | num | digit = num % 10 | rev = rev * 10 + digit | num //= 10 |
|-----------|-----|------------------|------------------------|------------|
| Initial   | 1234| -                | rev = 0                | -          |
| 1         | 1234| 4                | 0 * 10 + 4 = 4         | 123        |
| 2         | 123 | 3                | 4 * 10 + 3 = 43        | 12         |
| 3         | 12  | 2                | 43 * 10 + 2 = 432      | 1          |
| 4         | 1   | 1                | 432 * 10 + 1 = 4321    | 0          |
| End       | 0   | Loop exits       | **Final: 4321**        | -          |

### Example 2: num = 5670

| Iteration | num | digit = num % 10 | rev = rev * 10 + digit | num //= 10 |
|-----------|-----|------------------|------------------------|------------|
| Initial   | 5670| -                | rev = 0                | -          |
| 1         | 5670| 0                | 0 * 10 + 0 = 0         | 567        |
| 2         | 567 | 7                | 0 * 10 + 7 = 7         | 56         |
| 3         | 56  | 6                | 7 * 10 + 6 = 76        | 5          |
| 4         | 5   | 5                | 76 * 10 + 5 = 765      | 0          |
| End       | 0   | Loop exits       | **Final: 765**         | -          |

---

## Key Operations Explained

### Modulus Operator (%)
```python
1234 % 10 = 4    # Gets last digit
123 % 10 = 3     # Gets last digit
12 % 10 = 2      # Gets last digit
1 % 10 = 1       # Gets last digit
```

### Floor Division (//)
```python
1234 // 10 = 123  # Removes last digit
123 // 10 = 12    # Removes last digit
12 // 10 = 1      # Removes last digit
1 // 10 = 0       # Removes last digit
```

### Building Reversed Number
```python
rev = 0
rev = 0 * 10 + 4 = 4      # First digit becomes 4
rev = 4 * 10 + 3 = 43     # 4 shifts left, 3 added
rev = 43 * 10 + 2 = 432   # 43 shifts left, 2 added
rev = 432 * 10 + 1 = 4321 # 432 shifts left, 1 added
```

---

## Complete Working Example

```python
def reverse_number(num):
    """Reverse digits of a positive integer with step-by-step output."""
    print(f"Reversing number: {num}")
    print("-" * 40)
    
    original = num
    rev = 0
    step = 1
    
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        
        print(f"Step {step}: digit={digit}, rev={rev}, remaining={num}")
        step += 1
    
    print("-" * 40)
    print(f"Original: {original} → Reversed: {rev}")
    return rev

# Test cases
test_numbers = [1234, 5670, 9, 100, 12321]

for number in test_numbers:
    result = reverse_number(number)
    print(f"✓ {number} reversed is {result}\n")
```

**Output:**
```
Reversing number: 1234
----------------------------------------
Step 1: digit=4, rev=4, remaining=123
Step 2: digit=3, rev=43, remaining=12
Step 3: digit=2, rev=432, remaining=1
Step 4: digit=1, rev=4321, remaining=0
----------------------------------------
Original: 1234 → Reversed: 4321
✓ 1234 reversed is 4321
```

---

## Edge Cases & Variations

### Handling Negative Numbers
```python
def reverse_number_with_sign(num):
    """Reverse number while preserving sign."""
    if num < 0:
        return -reverse_number(-num)
    return reverse_number(num)

# Test
print(reverse_number_with_sign(-1234))  # Output: -4321
```

### Alternative Approach (String Method)
```python
def reverse_number_string(num):
    """Reverse using string manipulation (less efficient)."""
    return int(str(num)[::-1])

# Test
print(reverse_number_string(1234))  # Output: 4321
```

---

## Time & Space Complexity

- **Time Complexity**: O(log n) where n is the input number
  - We process each digit once
  - Number of digits = log₁₀(n)

- **Space Complexity**: O(1)
  - Only using constant extra space (rev, digit variables)

---

## Common Mistakes

> [!WARNING] **Avoid These Errors**
> - Forgetting to handle the case when num = 0
> - Using `num % 10` incorrectly
> - Not updating `num` with `num //= 10`
> - Integer overflow for very large numbers

> [!TIP] **Best Practices**
> - Always test with edge cases (0, single digit, trailing zeros)
> - Use meaningful variable names
> - Add input validation for negative numbers

---

## Practice Problems

1. **Modify** the function to handle negative numbers
2. **Count** how many steps it takes to reverse a number
3. **Find** the largest digit in the reversed number
4. **Check** if reversing a number twice gives the original

```python
# Practice solutions
def count_reverse_steps(num):
    steps = 0
    while num > 0:
        num //= 10
        steps += 1
    return steps

def largest_digit_in_reverse(num):
    max_digit = 0
    while num > 0:
        digit = num % 10
        max_digit = max(max_digit, digit)
        num //= 10
    return max_digit
```

---

## Related Topics
- [[02-Check-Palindrome-Number]] - Uses number reversal
- [[While-Loops]] - Loop structure used
- [[Arithmetic-Operators]] - Modulus and floor division

**Next**: Learn about [[02-Check-Palindrome-Number]] →