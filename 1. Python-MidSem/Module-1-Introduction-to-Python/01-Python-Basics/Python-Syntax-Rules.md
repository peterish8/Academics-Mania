# Python Syntax Rules

#module1 #python-basics #syntax #rules

---

## What is Syntax?

Syntax refers to the rules that define how Python code must be written. Python has specific rules for structure, indentation, and formatting.

---

## Key Syntax Rules

### 1. Indentation (Most Important!)
Python uses indentation to define code blocks instead of braces `{}`.

```python
# Correct indentation
if True:
    print("This is indented")
    print("This too")

# Incorrect - IndentationError
if True:
print("This will cause an error")

# Nested indentation
if True:
    print("Level 1")
    if True:
        print("Level 2")
        print("Still level 2")
    print("Back to level 1")
```

### 2. Case Sensitivity
Python distinguishes between uppercase and lowercase letters.

```python
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)  # Alice
print(Name)  # Bob  
print(NAME)  # Charlie

# These are all different variables!
```

### 3. Comments
Use `#` for single-line comments, `"""` or `'''` for multi-line.

```python
# This is a single-line comment
print("Hello")  # Comment at end of line

"""
This is a
multi-line comment
"""

'''
This is also a
multi-line comment
'''
```

---

## Statement Rules

### 1. One Statement Per Line
```python
# Correct
print("Hello")
print("World")

# Possible but not recommended
print("Hello"); print("World")
```

### 2. Line Continuation
```python
# Long lines can be continued with \
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Or use parentheses (preferred)
total = (1 + 2 + 3 +
         4 + 5 + 6)

# Lists, tuples, dicts can span multiple lines
my_list = [1, 2, 3,
           4, 5, 6]
```

---

## Naming Rules

### Variables and Functions
```python
# Valid names
name = "Alice"
age = 25
first_name = "John"
_private = "hidden"
number2 = 42

# Invalid names
# 2number = 42      # Can't start with digit
# first-name = "John"  # No hyphens
# class = "Math"    # Can't use keywords
```

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "alice"
def calculate_total():
    pass

# Constants: UPPER_CASE
MAX_SIZE = 100
PI = 3.14159

# Classes: PascalCase (not in syllabus but good to know)
class StudentRecord:
    pass
```

---

## Keywords (Reserved Words)

These words have special meaning and cannot be used as variable names:

```python
# Python keywords (cannot be used as variable names)
and, as, assert, break, class, continue, def, del, elif, else,
except, False, finally, for, from, global, if, import, in,
is, lambda, None, nonlocal, not, or, pass, raise, return,
True, try, while, with, yield
```

---

## String Quotes

```python
# Single quotes
message = 'Hello World'

# Double quotes  
message = "Hello World"

# Triple quotes for multi-line
message = """This is a
multi-line
string"""

# Mixing quotes
message = "She said, 'Hello!'"
message = 'He said, "Hi there!"'
```

---

## Important Syntax Points

> [!NOTE] **Indentation Rules**
> - Use 4 spaces per indentation level (recommended)
> - Be consistent throughout your code
> - Don't mix tabs and spaces
> - All lines at same level must have same indentation

> [!TIP] **Best Practices**
> - Use meaningful variable names
> - Keep lines under 80 characters
> - Add comments to explain complex logic
> - Use consistent naming conventions

> [!WARNING] **Common Syntax Errors**
> - `IndentationError`: Incorrect indentation
> - `SyntaxError`: Missing colons, parentheses, quotes
> - `NameError`: Using undefined variables
> - Using keywords as variable names

---

## Examples of Good Syntax

```python
# Good Python code example
def calculate_grade(score):
    """Calculate letter grade from numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get user input
student_name = input("Enter student name: ")
student_score = int(input("Enter score: "))

# Calculate and display result
grade = calculate_grade(student_score)
print(f"{student_name} received grade: {grade}")
```

---

## Related Topics
- [[Variables]] - Naming and using variables
- [[Print-Function]] - Output syntax
- [[If-Elif-Else]] - Conditional syntax

---

## Practice Questions

1. Identify syntax errors in this code:
```python
if true:
print("Hello")
    print("World")
```

2. Fix the naming issues:
```python
2name = "Alice"
first-name = "Bob"  
class = "Math"
```

**Solutions:**
1. `true` should be `True`, missing indentation
2. Use `name2`, `first_name`, `subject` instead

**Next**: Learn about [[Variables]] →