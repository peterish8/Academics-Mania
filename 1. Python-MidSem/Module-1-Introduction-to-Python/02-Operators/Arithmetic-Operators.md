# Arithmetic Operators

#module1 #operators #arithmetic #math

---

## What are Arithmetic Operators?

Arithmetic operators perform mathematical operations on numbers. Python supports all basic math operations plus some advanced ones.

---

## Basic Arithmetic Operators

### Addition (+)
```python
# Adding numbers
result = 5 + 3      # 8
result = 2.5 + 1.5  # 4.0

# Adding variables
x = 10
y = 20
sum_result = x + y  # 30

# String concatenation (special case)
greeting = "Hello" + " " + "World"  # "Hello World"
```

### Subtraction (-)
```python
# Subtracting numbers
result = 10 - 3     # 7
result = 5.5 - 2.2  # 3.3

# With variables
x = 15
y = 7
difference = x - y  # 8

# Negative numbers
negative = -5       # Unary minus
result = 10 - (-3)  # 13 (same as 10 + 3)
```

### Multiplication (*)
```python
# Multiplying numbers
result = 4 * 5      # 20
result = 2.5 * 4    # 10.0

# With variables
length = 10
width = 5
area = length * width  # 50

# String repetition (special case)
repeated = "Hi! " * 3  # "Hi! Hi! Hi! "
```

### Division (/)
```python
# Division always returns float
result = 10 / 3     # 3.3333333333333335
result = 8 / 2      # 4.0 (still float!)
result = 15 / 4     # 3.75

# With variables
total = 100
parts = 4
per_part = total / parts  # 25.0
```

---

## Advanced Arithmetic Operators

### Floor Division (//)
Returns the largest integer less than or equal to the result.

```python
# Floor division (integer division)
result = 10 // 3    # 3 (not 3.33...)
result = 15 // 4    # 3 (not 3.75)
result = 20 // 6    # 3 (not 3.33...)

# With negative numbers
result = -10 // 3   # -4 (floors toward negative infinity)
result = 10 // -3   # -4

# With floats
result = 10.5 // 2.0  # 5.0 (still returns float)
```

### Modulus (%)
Returns the remainder after division.

```python
# Modulus (remainder)
result = 10 % 3     # 1 (10 ÷ 3 = 3 remainder 1)
result = 15 % 4     # 3 (15 ÷ 4 = 3 remainder 3)
result = 20 % 5     # 0 (20 ÷ 5 = 4 remainder 0)

# Check if number is even or odd
number = 17
if number % 2 == 0:
    print("Even")
else:
    print("Odd")  # This will print

# Check divisibility
if 15 % 3 == 0:
    print("15 is divisible by 3")  # This will print
```

### Exponentiation (**)
Raises a number to a power.

```python
# Power/Exponentiation
result = 2 ** 3     # 8 (2 to the power of 3)
result = 5 ** 2     # 25 (5 squared)
result = 10 ** 0    # 1 (any number to power 0 is 1)

# Square root using fractional exponent
result = 9 ** 0.5   # 3.0 (square root of 9)
result = 8 ** (1/3) # 2.0 (cube root of 8)

# With variables
base = 3
exponent = 4
power = base ** exponent  # 81
```

---

## Operator Precedence

Python follows mathematical order of operations (PEMDAS):

```python
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
result = 2 + 3 * 4      # 14 (not 20)
result = (2 + 3) * 4    # 20
result = 2 ** 3 * 4     # 32 (2³ * 4 = 8 * 4)
result = 2 * 3 ** 2     # 18 (2 * 3² = 2 * 9)

# Complex expression
result = 10 + 5 * 2 ** 3 - 4 / 2
# Step by step: 10 + 5 * 8 - 2 = 10 + 40 - 2 = 48
```

**Order of precedence (highest to lowest):**
1. `()` - Parentheses
2. `**` - Exponentiation
3. `*`, `/`, `//`, `%` - Multiplication, Division, Floor Division, Modulus
4. `+`, `-` - Addition, Subtraction

---

## Assignment Operators (Shorthand)

### Basic Assignment Operators
```python
# Regular assignment
x = 10

# Addition assignment
x += 5    # Same as: x = x + 5 (x becomes 15)

# Subtraction assignment
x -= 3    # Same as: x = x - 3 (x becomes 12)

# Multiplication assignment
x *= 2    # Same as: x = x * 2 (x becomes 24)

# Division assignment
x /= 4    # Same as: x = x / 4 (x becomes 6.0)

# Floor division assignment
x //= 2   # Same as: x = x // 2 (x becomes 3.0)

# Modulus assignment
x %= 2    # Same as: x = x % 2 (x becomes 1.0)

# Exponentiation assignment
x **= 3   # Same as: x = x ** 3 (x becomes 1.0)
```

---

## Practical Examples

### Calculator Functions
```python
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, //, %, **): ")
    num2 = float(input("Enter second number: "))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif operator == "//":
        result = num1 // num2 if num2 != 0 else "Cannot divide by zero"
    elif operator == "%":
        result = num1 % num2 if num2 != 0 else "Cannot divide by zero"
    elif operator == "**":
        result = num1 ** num2
    else:
        result = "Invalid operator"
    
    print(f"Result: {result}")
```

### Area and Perimeter Calculator
```python
# Rectangle calculations
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Circle calculations
import math
radius = float(input("Enter radius: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Circle Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - Division (/) always returns float, even for whole numbers
> - Floor division (//) returns integer part of division
> - Modulus (%) returns remainder after division
> - Exponentiation (**) raises to power
> - Follow PEMDAS order of operations

> [!TIP] **Practical Uses**
> - Use % to check even/odd: `number % 2 == 0`
> - Use // for integer division: `total_pages // pages_per_section`
> - Use ** for powers: `area = side ** 2`
> - Use += for counters: `count += 1`

> [!WARNING] **Common Mistakes**
> - Forgetting operator precedence: `2 + 3 * 4` is 14, not 20
> - Division by zero causes ZeroDivisionError
> - Mixing int and float can give unexpected results
> - Floor division with negatives: `-10 // 3` is -4, not -3

---

## Related Topics
- [[Comparison-Operators]] - Comparing values
- [[Variables]] - Storing calculation results
- [[Data-Types]] - Number types in calculations

---

## Practice Questions

1. Calculate: `(5 + 3) * 2 ** 2 - 10 // 3`
2. Check if 127 is divisible by 7
3. Find the last digit of 12345

```python
# Practice solutions
# 1. Complex calculation
result = (5 + 3) * 2 ** 2 - 10 // 3
# Step by step: 8 * 4 - 3 = 32 - 3 = 29

# 2. Divisibility check
print(127 % 7 == 0)  # False (127 % 7 = 1)

# 3. Last digit
last_digit = 12345 % 10  # 5
```

**Next**: Learn about [[Comparison-Operators]] →