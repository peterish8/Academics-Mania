# PDF 1: Python Basics - Quick Summary

#last-minute-prep #summary #python-basics #variables #data-types

---

## 🎯 What is Python?

### Key Points
- **High-level**: No memory management needed
- **Interpreted**: Runs line by line, no compilation
- **General-purpose**: Web, AI, data science, automation
- **Dynamic typing**: No need to declare variable types

### Why Use Python?
- **Easy syntax**: Looks like English
- **Versatile**: Many applications (Django, Pandas, TensorFlow)
- **Large community**: Thousands of libraries
- **Cross-platform**: Windows, macOS, Linux

---

## 🎯 print() Function

### Key Points
- **Purpose**: Display output to console
- **Multiple values**: Separated by commas
- **Customizable**: Use `sep` and `end` parameters

### Essential Code
```python
# Basic print
print("Hello, World!")

# Multiple values
print("I am", 20, "years old")

# Custom separator
print("2025", "08", "08", sep="-")  # 2025-08-08

# Escape characters
print("Hello\nWorld")     # \n = newline
print("Item1\tItem2")     # \t = tab
print("\"Code\"")          # \" = quote
```

### Quick Patterns
```python
# Pattern printing
print("*\n* *\n* * *")    # Triangle
print("Item1\tPrice1\nItem2\tPrice2")  # Table
```

---

## 🎯 Variables

### Key Points
- **Containers**: Store data values
- **Dynamic**: Type can change
- **Case-sensitive**: `age` ≠ `Age`
- **Snake_case**: Use for variable names

### Rules
- Start with letter or underscore
- Can contain letters, digits, underscores
- No Python keywords (`if`, `for`, etc.)

### Essential Code
```python
# Basic assignment
age = 25
name = "Python"

# Multiple assignment
x = y = z = 100

# Unpacking
a, b, c = 1, 2, 3

# Swapping
a, b = b, a
```

---

## 🎯 Data Types

### 1. int (Integer)
- **Purpose**: Whole numbers
- **Examples**: `10, -5, 0`
```python
age = 25
count = 0
```

### 2. float (Decimal)
- **Purpose**: Numbers with decimal point
- **Examples**: `3.14, -2.5, 0.0`
```python
price = 19.99
pi = 3.14159
```

### 3. str (String)
- **Purpose**: Text data
- **Examples**: `"Hello", 'Python', "123"`
```python
name = "Python"
message = 'Hello World'
```

### 4. bool (Boolean)
- **Purpose**: True/False values
- **Examples**: `True, False`
```python
is_valid = True
is_empty = False
```

### 5. complex (Complex Numbers)
- **Purpose**: Real + imaginary parts
- **Format**: `a + bj`
```python
num = 2 + 3j
print(num.real)  # 2.0
print(num.imag)  # 3.0
```

---

## ⚡ Quick Reference

### Type Checking
```python
variable = "this is a string"
print(type(variable))           # Get type, <class 'str'>
print(isinstance(variable, int))     # Check if specific type, here its False as its not a int , its a string
```

### Common Operations
```python
# String operations
len("hello")            # Length
"hello"[0]              # First character

# Numeric operations
10 + 5                  # Addition
10 ** 2                 # Power (100)
10 % 3                  # Modulus (1)
```

### Variable Patterns
```python
# Constants
PI = 3.14159
MAX_SIZE = 100

# Good naming
student_name = "Alice"
total_price = 299.99
```

---

## 🚨 Common Mistakes to Avoid

### Variable Mistakes
- Starting with number: `1name` ❌
- Using hyphens: `my-name` ❌
- Using keywords: `for = 5` ❌
- Case confusion: `Age` vs `age`

### Print Mistakes
- Forgetting quotes for strings
- Wrong escape sequences
- Not using `sep` parameter correctly

### Data Type Mistakes
- Confusing `"123"` (string) vs `123` (int)
- Not knowing when to use each type
- Forgetting `.real` and `.imag` for complex numbers

---

## 🎯 Exam Tips

### Must Remember
- **print()**: `sep` and escape characters (`\n`, `\t`, `\"`)
- **Variables**: Naming rules and conventions
- **Data types**: int, float, str, bool, complex
- **Complex numbers**: `.real` and `.imag` attributes

### Quick Test Cases
```python
# Variable tests
age = 20                    # int
price = 19.99              # float
name = "Python"            # str
is_valid = True            # bool
num = 2 + 3j               # complex

# Print tests
print("Hello\nWorld")       # Newline
print("A", "B", sep="-")    # Custom separator
print("\"Quote\"")          # Quote inside string
```

### Memory Aids
- **Variables**: "Container for data"
- **int**: "Whole numbers only"
- **float**: "Decimal point numbers"
- **str**: "Text in quotes"
- **bool**: "True or False only"
- **complex**: "Real + imaginary (a + bj)"

---

## 📝 Last-Minute Checklist

### Before Exam
- [ ] Know all 5 data types and their purposes
- [ ] Remember variable naming rules
- [ ] Can use print() with sep and escape characters
- [ ] Understand complex number attributes (.real, .imag)

### During Exam
- [ ] Check variable names for validity
- [ ] Use correct data type for the problem
- [ ] Remember quotes for strings
- [ ] Use proper escape sequences in print()

**⏰ Practice Time: 3 minutes per concept**

---
*Next: [[PDF-2-Input-TypeConversion-Tuples]]*

#python-basics #variables #data-types #print #exam-prep