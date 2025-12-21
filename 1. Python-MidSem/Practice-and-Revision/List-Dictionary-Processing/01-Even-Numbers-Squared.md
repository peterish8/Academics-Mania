# Even Numbers Squared

#list-processing #filtering #loops #conditionals #mathematical-operations

---

## Problem Statement

Given a list of numbers, return a new list containing only the even numbers, squared.

**Example**: 
- Input: `[1, 2, 3, 4, 5, 6]`
- Output: `[4, 16, 36]`
- Explanation: Even numbers are 2, 4, 6 → Squared: 4, 16, 36

---

## Algorithm Approach

### Core Concept
Filter even numbers from the input list and square each even number.

### Step-by-Step Logic
1. **Initialize** empty result list
2. **Loop** through each number in input list
3. **Check** if number is even using `num % 2 == 0`
4. **If even** → square it (`num ** 2`) and add to result
5. **Return** the final result list

### Visual Representation
```
Input: [1, 2, 3, 4, 5, 6]

Process each number:
1 → 1 % 2 = 1 (odd) → Skip
2 → 2 % 2 = 0 (even) → 2² = 4 → Add to result
3 → 3 % 2 = 1 (odd) → Skip  
4 → 4 % 2 = 0 (even) → 4² = 16 → Add to result
5 → 5 % 2 = 1 (odd) → Skip
6 → 6 % 2 = 0 (even) → 6² = 36 → Add to result

Result: [4, 16, 36]
```

---

## Code Implementation

```python
def even_squares(numbers):
    """
    Filter even numbers and return their squares.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        list: List of squared even numbers
    """
    result = []
    
    for num in numbers:
        if num % 2 == 0:  # Check if even
            result.append(num ** 2)  # Square and add
    
    return result

# Example usage
input_list = [1, 2, 3, 4, 5, 6]
output = even_squares(input_list)
print(f"Input: {input_list}")
print(f"Output: {output}")
```

---

## Detailed Dry Run

### Example: numbers = [1, 2, 3, 4, 5, 6]

**Initial Setup:**
```
numbers = [1, 2, 3, 4, 5, 6]
result = []
```

**Iteration Process:**

| Iteration | num | num % 2 | Even? | Action | result |
|-----------|-----|---------|-------|--------|--------|
| 1 | 1 | 1 % 2 = 1 | ✗ No | Skip | [] |
| 2 | 2 | 2 % 2 = 0 | ✓ Yes | Add 2² = 4 | [4] |
| 3 | 3 | 3 % 2 = 1 | ✗ No | Skip | [4] |
| 4 | 4 | 4 % 2 = 0 | ✓ Yes | Add 4² = 16 | [4, 16] |
| 5 | 5 | 5 % 2 = 1 | ✗ No | Skip | [4, 16] |
| 6 | 6 | 6 % 2 = 0 | ✓ Yes | Add 6² = 36 | [4, 16, 36] |

**Final Result:** `[4, 16, 36]`

### Example 2: numbers = [1, 3, 5, 7] (All Odd)

| Iteration | num | num % 2 | Even? | Action | result |
|-----------|-----|---------|-------|--------|--------|
| 1 | 1 | 1 % 2 = 1 | ✗ No | Skip | [] |
| 2 | 3 | 3 % 2 = 1 | ✗ No | Skip | [] |
| 3 | 5 | 5 % 2 = 1 | ✗ No | Skip | [] |
| 4 | 7 | 7 % 2 = 1 | ✗ No | Skip | [] |

**Final Result:** `[]` (Empty list)

---

## Enhanced Implementation with Debugging

```python
def even_squares_debug(numbers):
    """
    Even squares with step-by-step debugging output.
    """
    print(f"Processing list: {numbers}")
    print("-" * 50)
    
    result = []
    
    for i, num in enumerate(numbers, 1):
        remainder = num % 2
        is_even = remainder == 0
        
        if is_even:
            squared = num ** 2
            result.append(squared)
            print(f"Step {i}: {num} % 2 = {remainder} → Even → {num}² = {squared} → Add")
        else:
            print(f"Step {i}: {num} % 2 = {remainder} → Odd → Skip")
        
        print(f"         Current result: {result}")
    
    print("-" * 50)
    print(f"Final result: {result}")
    return result

# Test with debugging
test_cases = [
    [1, 2, 3, 4, 5, 6],
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    []
]

for test_list in test_cases:
    even_squares_debug(test_list)
    print()
```

**Sample Output:**
```
Processing list: [1, 2, 3, 4, 5, 6]
--------------------------------------------------
Step 1: 1 % 2 = 1 → Odd → Skip
         Current result: []
Step 2: 2 % 2 = 0 → Even → 2² = 4 → Add
         Current result: [4]
Step 3: 3 % 2 = 1 → Odd → Skip
         Current result: [4]
Step 4: 4 % 2 = 0 → Even → 4² = 16 → Add
         Current result: [4, 16]
Step 5: 5 % 2 = 1 → Odd → Skip
         Current result: [4, 16]
Step 6: 6 % 2 = 0 → Even → 6² = 36 → Add
         Current result: [4, 16, 36]
--------------------------------------------------
Final result: [4, 16, 36]
```

---

## Alternative Implementations

### Method 1: List Comprehension (Pythonic)
```python
def even_squares_comprehension(numbers):
    """Using list comprehension - more concise."""
    return [num ** 2 for num in numbers if num % 2 == 0]

# Test
print(even_squares_comprehension([1, 2, 3, 4, 5, 6]))  # [4, 16, 36]
```

### Method 2: Using Filter and Map
```python
def even_squares_functional(numbers):
    """Using functional programming approach."""
    # Filter even numbers, then map to squares
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(map(lambda x: x ** 2, even_numbers))

# Test
print(even_squares_functional([1, 2, 3, 4, 5, 6]))  # [4, 16, 36]
```

### Method 3: Generator Expression (Memory Efficient)
```python
def even_squares_generator(numbers):
    """Using generator for memory efficiency."""
    return list(num ** 2 for num in numbers if num % 2 == 0)

# Test
print(even_squares_generator([1, 2, 3, 4, 5, 6]))  # [4, 16, 36]
```

---

## Edge Cases & Variations

### Handling Edge Cases
```python
def even_squares_robust(numbers):
    """Robust version with input validation."""
    # Input validation
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:  # Empty list
        return []
    
    result = []
    
    for num in numbers:
        # Check if element is a number
        if not isinstance(num, (int, float)):
            continue  # Skip non-numeric values
        
        if num % 2 == 0:
            result.append(num ** 2)
    
    return result

# Test edge cases
test_cases = [
    [],                           # Empty list
    [1, 3, 5],                   # All odd
    [2, 4, 6],                   # All even
    [0, -2, -4],                 # Zero and negative evens
    [1, 'a', 2, None, 4],       # Mixed types
]

for test in test_cases:
    try:
        result = even_squares_robust(test)
        print(f"{test} → {result}")
    except Exception as e:
        print(f"{test} → Error: {e}")
```

### Handling Negative Numbers
```python
def even_squares_with_negatives(numbers):
    """Handle negative even numbers."""
    result = []
    
    for num in numbers:
        if isinstance(num, (int, float)) and num % 2 == 0:
            result.append(num ** 2)
    
    return result

# Test with negatives
print(even_squares_with_negatives([-4, -3, -2, -1, 0, 1, 2, 3, 4]))
# Output: [16, 4, 0, 4, 16]
```

---

## Performance Analysis

### Time Complexity: O(n)
- We iterate through the list once
- Each operation (modulus, squaring, append) is O(1)
- Total: O(n) where n is the length of input list

### Space Complexity: O(k)
- Where k is the number of even numbers in the input
- In worst case (all even): O(n)
- In best case (no evens): O(1)

### Performance Comparison
```python
import time

def performance_test(size):
    """Compare performance of different implementations."""
    test_list = list(range(size))
    
    methods = [
        ("Loop", even_squares),
        ("List Comprehension", even_squares_comprehension),
        ("Functional", even_squares_functional),
        ("Generator", even_squares_generator)
    ]
    
    print(f"Performance test with {size} elements:")
    print("-" * 40)
    
    for name, method in methods:
        start_time = time.time()
        result = method(test_list)
        end_time = time.time()
        
        print(f"{name:15}: {end_time - start_time:.6f}s")

# Test performance
performance_test(100000)
```

---

## Practical Applications

### Data Processing Example
```python
def process_sensor_data(readings):
    """Process sensor readings - square even values for calibration."""
    calibrated = even_squares(readings)
    
    if calibrated:
        avg_calibrated = sum(calibrated) / len(calibrated)
        return {
            'original_count': len(readings),
            'even_count': len(calibrated),
            'calibrated_values': calibrated,
            'average_calibrated': avg_calibrated
        }
    else:
        return {'message': 'No even readings to calibrate'}

# Test
sensor_readings = [1, 2, 3, 4, 5, 6, 7, 8]
result = process_sensor_data(sensor_readings)
print(result)
```

### Statistical Analysis
```python
def analyze_even_squares(numbers):
    """Comprehensive analysis of even squares."""
    even_nums = [num for num in numbers if num % 2 == 0]
    squares = [num ** 2 for num in even_nums]
    
    if not squares:
        return "No even numbers found"
    
    analysis = {
        'original_list': numbers,
        'even_numbers': even_nums,
        'squared_values': squares,
        'count_even': len(even_nums),
        'sum_squares': sum(squares),
        'max_square': max(squares),
        'min_square': min(squares),
        'avg_square': sum(squares) / len(squares)
    }
    
    return analysis

# Test comprehensive analysis
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
analysis = analyze_even_squares(data)
for key, value in analysis.items():
    print(f"{key}: {value}")
```

---

## Common Variations

### Problem Variations to Practice
1. **Odd numbers cubed**: Filter odd numbers and cube them
2. **Divisible by 3, doubled**: Numbers divisible by 3, doubled
3. **Positive numbers squared**: Only positive numbers, squared
4. **Multiple conditions**: Even AND greater than 5, squared

```python
# Variation implementations
def odd_cubes(numbers):
    """Filter odd numbers and cube them."""
    return [num ** 3 for num in numbers if num % 2 == 1]

def divisible_by_3_doubled(numbers):
    """Numbers divisible by 3, doubled."""
    return [num * 2 for num in numbers if num % 3 == 0]

def positive_squares(numbers):
    """Positive numbers squared."""
    return [num ** 2 for num in numbers if num > 0]

def even_and_large_squared(numbers):
    """Even numbers greater than 5, squared."""
    return [num ** 2 for num in numbers if num % 2 == 0 and num > 5]

# Test variations
test_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {test_list}")
print(f"Odd cubes: {odd_cubes(test_list)}")
print(f"Div by 3 doubled: {divisible_by_3_doubled(test_list)}")
print(f"Positive squares: {positive_squares(test_list)}")
print(f"Even & >5 squared: {even_and_large_squared(test_list)}")
```

---

## Testing Suite

```python
def test_even_squares():
    """Comprehensive test suite for even_squares function."""
    test_cases = [
        # (input, expected_output, description)
        ([1, 2, 3, 4, 5, 6], [4, 16, 36], "Mixed odd/even"),
        ([2, 4, 6, 8], [4, 16, 36, 64], "All even"),
        ([1, 3, 5, 7], [], "All odd"),
        ([], [], "Empty list"),
        ([0], [0], "Zero"),
        ([-2, -4, 2, 4], [4, 16, 4, 16], "Negative evens"),
        ([10], [100], "Single even"),
        ([11], [], "Single odd")
    ]
    
    print("Testing even_squares function:")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_list, expected, description) in enumerate(test_cases, 1):
        result = even_squares(input_list)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: {input_list}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if result == expected:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    print(f"Success rate: {(passed/total)*100:.1f}%")

# Run comprehensive tests
test_even_squares()
```

---

## Key Concepts Reinforced

> [!NOTE] **Core Concepts**
> - **List iteration**: Using for loops to process elements
> - **Conditional filtering**: Using if statements to select elements
> - **Mathematical operations**: Squaring numbers with `**` operator
> - **List building**: Appending elements to create new lists
> - **Modulus operator**: Using `%` to check even/odd

> [!TIP] **Best Practices**
> - Use descriptive variable names (`result`, `num`)
> - Handle edge cases (empty lists, non-numeric values)
> - Consider list comprehensions for concise code
> - Add input validation for robust functions
> - Test with various input types

> [!WARNING] **Common Mistakes**
> - Forgetting to initialize result list
> - Using `=` instead of `==` in conditions
> - Not handling empty input lists
> - Modifying original list instead of creating new one
> - Off-by-one errors in manual implementations

---

## Related Topics
- [[02-Group-Words-by-First-Letter]] - Dictionary processing
- [[List-Methods-append-pop-sort]] - List manipulation methods
- [[For-Loops]] - Iteration patterns
- [[Conditionals]] - Filtering logic

---

## Practice Problems

1. **Modify** to return odd numbers cubed
2. **Filter** numbers divisible by both 2 and 3, then square them
3. **Create** a function that processes both even squares and odd cubes
4. **Implement** using only while loops instead of for loops

```python
# Practice solutions
def odd_cubes_practice(numbers):
    return [num ** 3 for num in numbers if num % 2 == 1]

def divisible_by_6_squared(numbers):
    return [num ** 2 for num in numbers if num % 6 == 0]

def process_evens_and_odds(numbers):
    evens_squared = [num ** 2 for num in numbers if num % 2 == 0]
    odds_cubed = [num ** 3 for num in numbers if num % 2 == 1]
    return {'evens_squared': evens_squared, 'odds_cubed': odds_cubed}
```

**Next**: Learn about [[02-Group-Words-by-First-Letter]] →