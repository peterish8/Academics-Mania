# Type Conversion

#module1 #python-basics #type-conversion #casting #int #float #str #bool

---

## What is Type Conversion?

Type conversion (also called casting) is changing data from one type to another. Python provides built-in functions to convert between data types.

---

## Conversion Functions

### int() - Convert to Integer
```python
# From string
age_str = "25"
age_int = int(age_str)
print(age_int)  # 25
print(type(age_int))  # <class 'int'>

# From float (truncates decimal)
height_float = 5.8
height_int = int(height_float)
print(height_int)  # 5 (not 6!)

# From boolean
print(int(True))   # 1
print(int(False))  # 0
```

### float() - Convert to Float
```python
# From string
price_str = "19.99"
price_float = float(price_str)
print(price_float)  # 19.99

# From integer
age_int = 25
age_float = float(age_int)
print(age_float)  # 25.0

# From boolean
print(float(True))   # 1.0
print(float(False))  # 0.0
```

### str() - Convert to String
```python
# From integer
age = 25
age_str = str(age)
print(age_str)  # "25"
print(type(age_str))  # <class 'str'>

# From float
price = 19.99
price_str = str(price)
print(price_str)  # "19.99"

# From boolean
print(str(True))   # "True"
print(str(False))  # "False"
```

### bool() - Convert to Boolean
```python
# From numbers
print(bool(1))      # True
print(bool(0))      # False
print(bool(-5))     # True (any non-zero)
print(bool(3.14))   # True

# From strings
print(bool("Hello"))  # True
print(bool(""))       # False (empty string)
print(bool(" "))      # True (space is not empty)

# From None
print(bool(None))     # False
```

---

## Common Conversion Scenarios

### User Input Conversion
```python
# Input is always string, convert as needed
name = input("Enter your name: ")  # Already string
age = int(input("Enter your age: "))  # Convert to int
height = float(input("Enter your height: "))  # Convert to float

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
```

### Mathematical Operations
```python
# Convert for calculations
num1_str = "10"
num2_str = "5"

# Convert to numbers for math
num1 = int(num1_str)
num2 = int(num2_str)
result = num1 + num2
print(result)  # 15

# Without conversion (string concatenation)
result_str = num1_str + num2_str
print(result_str)  # "105"
```

### Display Formatting
```python
# Convert numbers to strings for display
score = 95
percentage = 87.5
passed = True

message = "Score: " + str(score) + ", Percentage: " + str(percentage)
print(message)

# Better with f-strings (covered in Strings module)
message = f"Score: {score}, Percentage: {percentage}, Passed: {passed}"
print(message)
```

---

## Conversion Errors

### ValueError Examples
```python
# These will cause ValueError
try:
    invalid_int = int("hello")  # Can't convert "hello" to int
except ValueError:
    print("Cannot convert 'hello' to integer")

try:
    invalid_float = float("abc")  # Can't convert "abc" to float
except ValueError:
    print("Cannot convert 'abc' to float")

# Valid conversions
print(int("123"))      # 123
print(float("12.34"))  # 12.34
print(int("  45  "))   # 45 (strips whitespace)
```

### Safe Conversion
```python
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        return None

# Test safe conversion
print(safe_int_convert("123"))    # 123
print(safe_int_convert("hello"))  # None
print(safe_int_convert("12.5"))   # None
```

---

## Implicit vs Explicit Conversion

### Implicit (Automatic)
```python
# Python automatically converts when needed
result1 = 5 + 3.0    # int + float = float (8.0)
result2 = True + 1   # bool + int = int (2)
result3 = False * 5  # bool * int = int (0)

print(result1, type(result1))  # 8.0 <class 'float'>
print(result2, type(result2))  # 2 <class 'int'>
print(result3, type(result3))  # 0 <class 'int'>
```

### Explicit (Manual)
```python
# You manually convert using functions
x = "10"
y = "5"

# Explicit conversion needed for math
sum_result = int(x) + int(y)  # 15
concat_result = x + y         # "105"

print(sum_result)    # 15
print(concat_result) # "105"
```

---

## Practical Examples

### Calculator with Input
```python
# Get numbers from user and perform calculations
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
```

### Grade Converter
```python
# Convert between different grade formats
numeric_grade = int(input("Enter numeric grade (0-100): "))

# Convert to letter grade
if numeric_grade >= 90:
    letter_grade = "A"
elif numeric_grade >= 80:
    letter_grade = "B"
elif numeric_grade >= 70:
    letter_grade = "C"
elif numeric_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Convert to GPA (4.0 scale)
gpa = numeric_grade / 25.0

print(f"Numeric: {numeric_grade}")
print(f"Letter: {letter_grade}")
print(f"GPA: {gpa:.2f}")
```

---

## Important Points

> [!NOTE] **Key Functions**
> - `int()`: Convert to integer (truncates decimals)
> - `float()`: Convert to decimal number
> - `str()`: Convert to text/string
> - `bool()`: Convert to True/False

> [!TIP] **Best Practices**
> - Always convert user input to appropriate type
> - Use try/except for potentially invalid conversions
> - Remember int() truncates, doesn't round
> - Empty strings and zero are "falsy" in bool()

> [!WARNING] **Common Mistakes**
> - Forgetting to convert input() strings
> - Assuming int("12.5") works (it doesn't)
> - Not handling conversion errors
> - Mixing string and number operations

---

## Related Topics
- [[Data-Types]] - Understanding different data types
- [[Input-Function]] - Converting user input
- [[Variables]] - Storing converted values

---

## Practice Questions

1. Convert "123" to integer and add 77
2. Convert 3.14159 to integer - what happens?
3. What does bool("0") return and why?

```python
# Practice solutions
# 1. String to int conversion
result = int("123") + 77
print(result)  # 200

# 2. Float to int (truncation)
pi_int = int(3.14159)
print(pi_int)  # 3 (truncated, not rounded)

# 3. Boolean conversion
result = bool("0")
print(result)  # True (non-empty string is True)
print(bool(0))  # False (zero is False)
```

**Next**: Learn about [[Arithmetic-Operators]] →