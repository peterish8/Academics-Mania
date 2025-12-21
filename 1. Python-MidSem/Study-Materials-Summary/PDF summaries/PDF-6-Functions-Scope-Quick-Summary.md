# PDF 6: Functions & Variable Scope - Quick Summary

#last-minute-prep #summary #functions #def-keyword #scope #parameters

---

## 🎯 What are Functions?

### Key Points
- **Reusable code blocks** that perform specific tasks
- **Avoid repetition** - write once, use many times
- **Input → Process → Output** pattern
- **Defined with `def` keyword**

### Why Use Functions?
- **Code reusability** - DRY principle (Don't Repeat Yourself)
- **Modularity** - break big problems into smaller parts
- **Readability** - easier to understand and maintain
- **Testing** - easier to debug individual parts

---

## 🎯 Function Definition & Calling

### Basic Syntax
```python
def function_name(parameters):
    """Optional docstring"""
    # function body
    return value  # optional
```

### Essential Code
```python
# Basic function
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice

# Function with return
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8

# Function with default parameter
def greet(name="Guest"):
    print("Hello,", name)

greet()         # Hello, Guest
greet("Bob")    # Hello, Bob
```

---

## 🎯 Function Types

### By Parameters & Return
| Type | Parameters | Return | Example |
|------|------------|--------|---------|
| **Type 1** | No | No | `def hello(): print("Hi")` |
| **Type 2** | Yes | No | `def greet(name): print("Hi", name)` |
| **Type 3** | No | Yes | `def pi(): return 3.14159` |
| **Type 4** | Yes | Yes | `def add(a,b): return a+b` |

### By Definition
```python
# Built-in functions (provided by Python)
len([1,2,3])    # 3
max(1,5,3)      # 5
type(42)        # <class 'int'>

# User-defined functions (created by you)
def square(x):
    return x * x
```

---

## 🎯 Variable Scope

### Key Points
- **Local**: Inside function only
- **Global**: Accessible everywhere
- **Enclosing**: Outer function to inner function
- **Built-in**: Python's built-in names

### Essential Code
```python
# Global variable
x = 50  # Global scope

def demo():
    y = 10  # Local scope
    print(x)  # Can access global
    print(y)  # Can access local

demo()
print(x)  # Can access global
# print(y)  # Error - local variable not accessible
```

### Global Keyword
```python
x = 10  # Global

def modify_global():
    global x
    x = 20  # Modifies global x

modify_global()
print(x)  # 20
```

### Nonlocal Keyword (Nested Functions)
```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "modified"
    
    inner()
    print(x)  # "modified"

outer()
```

---

## 🎯 Essential Function Examples

### 1. Prime Number Check
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Usage
print(is_prime(17))  # True
print(is_prime(15))  # False
```

### 2. Sum of Digits
```python
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Usage
print(sum_of_digits(1234))  # 10
```

### 3. Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Usage
print(factorial(5))  # 120
```

### 4. Pattern Printing
```python
def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Usage
print_pattern(4)
# Output:
# 4 3 2 1
# 3 2 1
# 2 1
# 1
```

---

## ⚡ Quick Reference

### Function Call Patterns
```python
# No parameters
function_name()

# With parameters
function_name(arg1, arg2)

# With keyword arguments
function_name(param1=value1, param2=value2)

# Mixed arguments
function_name(arg1, param2=value2)
```

### Return Patterns
```python
# Single return
def add(a, b):
    return a + b

# Multiple returns
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Multiple values
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
```

### Scope Resolution (LEGB Rule)
1. **L**ocal - Inside current function
2. **E**nclosing - In outer function (for nested functions)
3. **G**lobal - At module level
4. **B**uilt-in - Python built-in names

---

## 🚨 Common Mistakes to Avoid

### Function Definition Mistakes
```python
# Wrong - missing colon
def greet(name)
    print("Hello")

# Wrong - incorrect indentation
def greet(name):
print("Hello")

# Correct
def greet(name):
    print("Hello", name)
```

### Scope Mistakes
```python
# Wrong - trying to modify global without keyword
x = 10
def change():
    x = 20  # Creates local x, doesn't modify global

# Correct - using global keyword
x = 10
def change():
    global x
    x = 20  # Modifies global x
```

### Return Mistakes
```python
# Wrong - function doesn't return anything
def add(a, b):
    result = a + b
    # Missing return statement

# Correct
def add(a, b):
    return a + b
```

---

## 🎯 Exam Tips

### Must Remember
- **def keyword** to define functions
- **Indentation** for function body
- **return** to send value back (optional)
- **Local variables** only exist inside function
- **Global variables** accessible everywhere
- **global keyword** to modify global variables

### Function Patterns
```python
# Input validation
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Multiple operations
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Error"
```

### Quick Test Cases
```python
# Function definition
def test():
    return "Hello"

print(test())  # "Hello"

# Scope test
x = 5
def func():
    x = 10
    return x

print(func())  # 10 (local x)
print(x)       # 5 (global x unchanged)
```

### Memory Aids
- **def**: "Define function"
- **Local**: "Lives in function only"
- **Global**: "Goes everywhere"
- **return**: "Result back to caller"
- **LEGB**: "Local, Enclosing, Global, Built-in"

---

## 📝 Last-Minute Checklist

### Before Exam
- [ ] Know function definition syntax with def
- [ ] Understand local vs global scope
- [ ] Remember to use return for output
- [ ] Can write basic algorithms as functions
- [ ] Know when to use global keyword

### During Exam
- [ ] Always use colon after function definition
- [ ] Proper indentation for function body
- [ ] Check if function needs return statement
- [ ] Identify variable scope correctly
- [ ] Use meaningful function names

### Algorithm Functions
- [ ] **Prime check**: Loop from 2 to √n
- [ ] **Sum digits**: Use % 10 and // 10
- [ ] **Factorial**: Multiply 1 to n
- [ ] **Pattern**: Nested loops with range

### Common Function Templates
```python
# Template 1: Processing function
def process_number(num):
    # Process the number
    return result

# Template 2: Validation function
def is_valid(value):
    # Check conditions
    return True/False

# Template 3: Calculation function
def calculate(a, b):
    # Perform calculation
    return result
```

**⏰ Practice Time: 2 minutes per function type**

---
*Previous: [[PDF-5-Loops-Quick-Summary]] | Next: [[PDF-7-Strings-Quick-Summary]]*

#functions #scope #def-keyword #parameters #exam-prep