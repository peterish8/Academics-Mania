# PDF 3: Membership, Shift Operators & Conditionals - Quick Summary

#last-minute-prep #summary #membership-operators #shift-operators #conditionals

---

## 🎯 Membership Operators

### Key Points
- **in**: Checks if value exists in sequence
- **not in**: Checks if value does NOT exist in sequence
- **Works with**: strings, lists, tuples, sets, dictionaries

### Essential Code
```python
# Basic usage
print(1 in [1, 2, 3])        # True
print(4 not in [1, 2, 3])    # True
print("a" in "apple")        # True
print("x" not in "apple")    # True
```

### Tricky Cases (Exam Favorites)
```python
# Boolean/Number equivalence
print(1 in [True])           # True (1 == True)
print(0 in [False])          # True (0 == False)
print(True in [1])           # True
print(False in [0.0])        # True

# String vs Number
print("1" in [1, 2, 3])      # False (string vs int)
print(1 in ["1", "2", "3"])  # False (int vs string)

# Empty string special case
print("" in "")              # True (empty is substring of empty)
print("" in "Python")        # True (empty is substring of any string)
print(" " in "Python")       # False (space not in "Python")

# Empty collections
print(1 in [])               # False (empty list)
print("" in [])              # False (empty list, not empty string)
```

---

## 🎯 Shift Operators

### Key Points
- **Left Shift (<<)**: Multiply by 2^n
- **Right Shift (>>)**: Divide by 2^n (integer division)
- **Only works with integers**

### Essential Formulas
- **Left Shift**: `x << n` = `x * (2^n)`
- **Right Shift**: `x >> n` = `x // (2^n)`

### Essential Code
```python
# Left Shift (<<)
print(1 << 2)        # 1 * 2^2 = 4
print(5 << 1)        # 5 * 2^1 = 10
print(True << 2)     # 1 * 2^2 = 4
print(False << 2)    # 0 * 2^2 = 0

# Right Shift (>>)
print(10 >> 1)       # 10 // 2^1 = 5
print(10 >> 2)       # 10 // 2^2 = 2
print(True >> 2)     # 1 // 2^2 = 0
```

### What Doesn't Work
```python
# These cause TypeError
print("hello" >> 2)   # Error - strings don't support shift
print(1.0 >> 2)       # Error - floats don't support shift
```

---

## 🎯 Conditional Statements

### Key Points
- **if**: Execute if condition is True
- **else**: Execute if condition is False
- **elif**: Check multiple conditions
- **Indentation matters**: Use 4 spaces

### Essential Code
```python
# Basic if-else
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Multiple conditions with elif
score = int(input("Enter score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
```

### Condition Patterns
```python
# Comparison operators
if x == 5:          # Equal to
if x != 5:          # Not equal to
if x > 5:           # Greater than
if x >= 5:          # Greater than or equal
if x < 5:           # Less than
if x <= 5:          # Less than or equal

# Logical operators
if x > 0 and x < 10:    # Both conditions true
if x < 0 or x > 10:     # At least one condition true
if not (x == 5):        # Reverse condition
```

---

## ⚡ Quick Reference

### Membership Quick Tests
```python
# Lists/Tuples
1 in [1, 2, 3]          # True
"a" in ("a", "b")       # True

# Strings
"py" in "python"        # True
"x" not in "python"     # True

# Sets
1 in {1, 2, 3}          # True
4 not in {1, 2, 3}      # True
```

### Shift Quick Calculations
```python
# Left shift (multiply)
8 << 1                  # 8 * 2 = 16
3 << 2                  # 3 * 4 = 12

# Right shift (divide)
16 >> 1                 # 16 // 2 = 8
20 >> 2                 # 20 // 4 = 5
```

### Conditional Quick Patterns
```python
# Even/Odd check
if num % 2 == 0:        # Even
if num % 2 != 0:        # Odd

# Range check
if 0 <= score <= 100:   # Between 0 and 100
if x in [1, 2, 3]:      # One of specific values
```

---

## 🚨 Common Mistakes to Avoid

### Membership Mistakes
- Confusing `1` and `"1"` (number vs string)
- Forgetting that `True == 1` and `False == 0`
- Not knowing empty string `""` is in every string
- Mixing up `in` and `not in` logic

### Shift Operator Mistakes
- Trying to shift strings or floats (only integers work)
- Confusing left shift (multiply) with right shift (divide)
- Forgetting it's integer division for right shift

### Conditional Mistakes
- Using `=` instead of `==` for comparison
- Wrong indentation (must be consistent)
- Forgetting `:` after if/elif/else
- Not handling all possible cases

---

## 🎯 Exam Tips

### Must Remember
- **Membership**: `1 == True`, `0 == False` in Python
- **Shift**: Only works with integers, not strings/floats
- **Left shift**: multiply by 2^n
- **Right shift**: divide by 2^n (integer division)
- **Conditionals**: Always use `==` for comparison, not `=`

### Quick Test Cases
```python
# Membership tricky cases
print(1 in [True])       # True
print("" in "hello")     # True
print("1" in [1])        # False

# Shift operations
print(4 << 1)            # 8 (4 * 2)
print(8 >> 2)            # 2 (8 // 4)

# Conditional basics
if 5 % 2 == 0:           # False (5 is odd)
if 6 % 2 == 0:           # True (6 is even)
```

### Memory Aids
- **Membership**: "True equals 1, False equals 0"
- **Left shift**: "Left = multiply by 2"
- **Right shift**: "Right = divide by 2"
- **Conditionals**: "Double equals for comparison"

---

## 📝 Last-Minute Checklist

### Before Exam
- [ ] Remember True/False equals 1/0 in membership
- [ ] Know shift operators only work with integers
- [ ] Remember left shift multiplies, right shift divides
- [ ] Use == for comparison, not =

### During Exam
- [ ] Check data types in membership tests
- [ ] Verify integer types for shift operations
- [ ] Use proper indentation in conditionals
- [ ] Test edge cases like empty strings

**⏰ Practice Time: 2 minutes per concept**

---
*Previous: [[PDF-2-Input-TypeConversion-Tuples]] | Next: [[PDF-4-Operators-Quick-Summary]]*

#membership-operators #shift-operators #conditionals #exam-prep