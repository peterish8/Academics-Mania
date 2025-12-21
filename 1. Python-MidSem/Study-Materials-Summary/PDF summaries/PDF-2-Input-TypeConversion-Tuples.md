# PDF 2: Input, Type Conversion & Tuples - Quick Summary

#last-minute-prep #summary #input #type-conversion #tuples

---

## 🎯 input() Function

### Key Points
- **Always returns string** - no matter what user types
- **Takes user input** during program execution
- **Must convert** to other types for calculations

### Essential Code
```python
# Basic input (returns string)
name = input("Enter your name: ")

# Input with conversion for calculations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print(sum)
```

### Common Mistake
```python
# Wrong - concatenates strings
a = input("Enter first number: ")  # "5"
b = input("Enter second number: ")  # "3"
sum = a + b  # "53" not 8

# Correct - converts to int first
a = int(input("Enter first number: "))  # 5
b = int(input("Enter second number: "))  # 3
sum = a + b  # 8
```

---

## 🎯 Type Conversion

### Key Points
- **Implicit**: Python does automatically
- **Explicit**: Programmer does manually using functions
- **Common functions**: `int()`, `float()`, `str()`, `bool()`, `chr()`

### Essential Conversions

#### To Integer
```python
int(10.9)      # 10 (truncates)
int("123")     # 123
int(True)      # 1
int(False)     # 0
```

#### To Float
```python
float(10)      # 10.0
float("3.14")  # 3.14
float(True)    # 1.0
```

#### To String
```python
str(123)       # "123"
str(3.14)      # "3.14"
str(True)      # "True"
```

#### To Boolean
```python
bool(0)        # False
bool(1)        # True
bool("")       # False (empty string)
bool("hello")  # True (non-empty string)
bool(0.0)      # False
bool(2.5)      # True
```

#### Special Conversions
```python
chr(65)        # 'A' (ASCII to character)
```

### Conversion Errors
```python
int("abc")     # ValueError - can't convert
int("12.5")    # ValueError - use float() first
```

---

## 🎯 Single Value Tuple

### Key Points
- **Must use comma** after single element
- **Without comma** = just parentheses around value
- **Common exam trap** - forgetting the comma

### Essential Code
```python
# Correct - single value tuple
t1 = (5,)
print(type(t1))  # <class 'tuple'>

# Wrong - just integer in parentheses
t2 = (5)
print(type(t2))  # <class 'int'>

# Also correct ways
t3 = 5,          # Comma makes it tuple
t4 = (5, )       # Space before comma is fine
```

---

## ⚡ Quick Reference

### Input Patterns
```python
# String input
name = input("Name: ")

# Number input
age = int(input("Age: "))
price = float(input("Price: "))

# Multiple inputs
a, b = input("Two numbers: ").split()
a, b = int(a), int(b)

#leetcode way
a, b = map(int, input().split())
```

### Type Conversion Chain
```python
# String → Int → Float
s = "123"
i = int(s)      # 123
f = float(i)    # 123.0

# Float → Int (truncates)
f = 5.9
i = int(f)      # 5 (not 6!)
```

### Boolean Conversion Rules
```python
# Falsy values
bool(0)         # False
bool(0.0)       # False
bool("")        # False
bool(None)      # False

# Everything else is True
bool(1)         # True
bool(-1)        # True
bool("0")       # True (string "0", not number 0)
bool(" ")       # True (space is not empty)
```

---

## 🚨 Common Mistakes to Avoid

### Input Mistakes
- Forgetting to convert input to int/float for calculations
- Assuming input() returns numbers
- Not handling invalid input (like letters when expecting numbers)

### Type Conversion Mistakes
- Using `int("12.5")` instead of `int(float("12.5"))`
- Confusing `"0"` (string) with `0` (number) in bool conversion
- Forgetting that `int()` truncates, doesn't round

### Tuple Mistakes
- Writing `(5)` instead of `(5,)` for single tuple
- Forgetting the comma in single-element tuples
- Confusing tuple with just parentheses around expression

---

## 🎯 Exam Tips

### Must Remember
- **input()** always returns string
- **int()** truncates decimals (5.9 → 5)
- **Single tuple** needs comma: `(5,)`
- **Empty string** and **zero** are False in bool()

### Quick Test Cases
```python
# Input tests
a = input("Number: ")  # User types "5"
print(type(a))         # <class 'str'>
print(a + a)           # "55" (string concatenation)

# Conversion tests
print(int(5.9))        # 5 (truncates)
print(bool("0"))       # True (non-empty string)
print(bool(0))         # False (number zero)

# Tuple tests
t1 = (5,)              # tuple
t2 = (5)               # int
print(type(t1), type(t2))  # <class 'tuple'> <class 'int'>
```

### Memory Aids
- **input()**: "Always String Input"
- **int()**: "Truncates, doesn't round"
- **bool()**: "Empty and Zero are False"
- **Single tuple**: "Comma makes the tuple"

---

## 📝 Last-Minute Checklist

### Before Exam
- [ ] Remember input() returns string always
- [ ] Know int() truncates, float() for decimals
- [ ] Remember comma for single-element tuple
- [ ] Know what values are False in bool()

### During Exam
- [ ] Convert input() to int/float for math
- [ ] Use int(float(x)) for string decimals
- [ ] Add comma for single tuple: (value,)
- [ ] Check bool() conversion carefully

**⏰ Practice Time: 2 minutes per concept**

---
*Previous: [[PDF-1-Python-Basics]] | Next: [[PDF-3-Membership-Shift-Conditionals]]*

#input #type-conversion #tuples #exam-prep