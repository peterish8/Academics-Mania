# Variables

#module1 #python-basics #variables #assignment

---

## What are Variables?

Variables are containers that store data values. In Python, you don't need to declare variables before using them.

---

## Variable Assignment

### Basic Assignment
```python
# Syntax: variable_name = value
name = "Alice"
age = 25
height = 5.8
is_student = True

print(name)      # Alice
print(age)       # 25
print(height)    # 5.8
print(is_student) # True
```

### Multiple Assignment
```python
# Assign same value to multiple variables
x = y = z = 0
print(x, y, z)  # 0 0 0

# Assign different values
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap variables
x, y = 10, 20
x, y = y, x  # Swap
print(x, y)  # 20 10
```

---

## Variable Naming Rules

### Valid Names
```python
# Letters, numbers, underscore
name = "Alice"
age2 = 25
first_name = "John"
_private = "hidden"
user_123 = "valid"

# Case sensitive
Name = "Bob"
name = "Alice"  # Different from Name
```

### Invalid Names
```python
# These will cause SyntaxError:
# 2name = "Alice"      # Can't start with digit
# first-name = "John"  # No hyphens allowed
# first name = "Bob"   # No spaces allowed
# class = "Math"       # Can't use keywords
```

### Naming Conventions
```python
# Use snake_case for variables
user_name = "alice"
total_score = 95
max_attempts = 3

# Use UPPER_CASE for constants
PI = 3.14159
MAX_SIZE = 100
DEFAULT_COLOR = "blue"

# Use descriptive names
# Good
student_count = 30
average_grade = 85.5

# Bad
x = 30
y = 85.5
```

---

## Variable Types (Dynamic)

Python variables can hold different types of data and can change type:

```python
# Variable can change type
value = 42        # Integer
print(type(value))  # <class 'int'>

value = "Hello"   # Now string
print(type(value))  # <class 'str'>

value = 3.14      # Now float
print(type(value))  # <class 'float'>

value = True      # Now boolean
print(type(value))  # <class 'bool'>
```

---

## Variable Operations

### Arithmetic with Variables
```python
x = 10
y = 3

sum_result = x + y      # 13
difference = x - y      # 7
product = x * y         # 30
quotient = x / y        # 3.333...
remainder = x % y       # 1
power = x ** y          # 1000
```

### String Operations
```python
first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Repetition
greeting = "Hello! " * 3
print(greeting)  # Hello! Hello! Hello! 
```

### Updating Variables
```python
# Update with new value
score = 85
score = 90  # Now score is 90

# Update using current value
score = score + 5  # score is now 95

# Shorthand operators
score += 5   # Same as score = score + 5
score -= 3   # Same as score = score - 3
score *= 2   # Same as score = score * 2
score /= 4   # Same as score = score / 4
```

---

## Variable Scope (Basic)

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

my_function()
print(global_var)  # Can access global
# print(local_var)  # Error: local_var not defined here
```

---

## Checking Variables

```python
# Check if variable exists
name = "Alice"

# Using 'in' with locals() or globals()
if 'name' in locals():
    print("Variable 'name' exists")

# Check type
print(type(name))        # <class 'str'>
print(isinstance(name, str))  # True

# Check value
if name:  # True if not empty/zero/False
    print("Name has a value")
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - Variables are created when first assigned
> - No need to declare type beforehand
> - Variables can change type during execution
> - Use descriptive names for readability

> [!TIP] **Best Practices**
> - Use meaningful variable names
> - Follow snake_case convention
> - Initialize variables before using them
> - Use constants for fixed values

> [!WARNING] **Common Mistakes**
> - Using undefined variables (NameError)
> - Confusing variable names (case sensitivity)
> - Using keywords as variable names
> - Not initializing variables before use

---

## Practical Examples

### Student Information
```python
# Store student data
student_name = "Alice Johnson"
student_id = 12345
current_grade = 85.5
is_enrolled = True
subjects = 5

# Calculate GPA (assuming 4.0 scale)
gpa = current_grade / 25  # Simple conversion
print(f"Student: {student_name}")
print(f"ID: {student_id}")
print(f"GPA: {gpa:.2f}")
```

### Simple Calculator Variables
```python
# Calculator using variables
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

---

## Related Topics
- [[Data-Types]] - Types of data variables can hold
- [[Type-Conversion]] - Converting between types
- [[Operators]] - Operations with variables

---

## Practice Questions

1. Create variables for your personal information (name, age, city)
2. Swap two variables without using a third variable
3. Calculate the area of a rectangle using variables

```python
# Practice solutions
# 1. Personal info
my_name = "John"
my_age = 20
my_city = "New York"

# 2. Swap without third variable
a, b = 5, 10
a, b = b, a

# 3. Rectangle area
length = 10
width = 5
area = length * width
print(f"Area: {area}")
```

**Next**: Learn about [[Data-Types]] →