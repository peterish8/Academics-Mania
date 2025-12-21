# PDF 4: Python Operators - Quick Summary

#last-minute-prep #summary #operators #arithmetic #logical #comparison

---

## 🎯 Arithmetic Operators

### Key Points
- **Basic math**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Division**: `/` gives float, `//` gives integer
- **Modulus**: `%` gives remainder

### Essential Code
```python
a, b = 10, 3
print(a + b)    # 13 (addition)
print(a - b)    # 7 (subtraction)
print(a * b)    # 30 (multiplication)
print(a / b)    # 3.33... (division - always float)
print(a // b)   # 3 (floor division - integer)
print(a % b)    # 1 (remainder)
print(a ** b)   # 1000 (power)
```

### Quick Applications
```python
# Even/odd check
num % 2 == 0    # Even if True

# Hours and minutes
minutes = 130
hours = minutes // 60      # 2
remaining = minutes % 60   # 10
```

---

## 🎯 Assignment Operators

### Key Points
- **Shorthand**: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- **Updates variable**: `x += 5` same as `x = x + 5`

### Essential Code
```python
x = 10
x += 5     # x = 15 (x = x + 5)
x -= 3     # x = 12 (x = x - 3)
x *= 2     # x = 24 (x = x * 2)
x /= 4     # x = 6.0 (x = x / 4)
x //= 2    # x = 3.0 (x = x // 2)
x %= 2     # x = 1.0 (x = x % 2)
x **= 3    # x = 1.0 (x = x ** 3)
```

---

## 🎯 Comparison Operators

### Key Points
- **Returns boolean**: True or False
- **Common**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Use `==` for comparison**, not `=`

### Essential Code
```python
a, b = 10, 20
print(a == b)   # False (equal to)
print(a != b)   # True (not equal to)
print(a > b)    # False (greater than)
print(a < b)    # True (less than)
print(a >= b)   # False (greater than or equal)
print(a <= b)   # True (less than or equal)
```

---

## 🎯 Logical Operators

### Key Points
- **and**: Both must be True
- **or**: At least one must be True
- **not**: Reverses boolean value

### Truth Tables
```python
# AND operator
True and True    # True
True and False   # False
False and True   # False
False and False  # False

# OR operator
True or True     # True
True or False    # True
False or True    # True
False or False   # False

# NOT operator
not True         # False
not False        # True
```

### Essential Code
```python
age = 20
marks = 85

# Both conditions must be true
if age >= 18 and marks >= 80:
    print("Eligible for scholarship")

# At least one condition must be true
if marks >= 90 or age <= 16:
    print("Special consideration")

# Reverse condition
if not (marks < 40):
    print("Passed")
```

---

## 🎯 Identity Operators

### Key Points
- **is**: Same object in memory
- **is not**: Different objects in memory
- **Different from `==`**: `==` compares values, `is` compares objects

### Essential Code
```python
a = [1, 2, 3]
b = a           # Same object
c = [1, 2, 3]   # Different object, same values

print(a is b)       # True (same object)
print(a is c)       # False (different objects)
print(a == c)       # True (same values)

# Check for None
value = None
print(value is None)     # True
print(value is not None) # False
```

---

## 🎯 Membership Operators

### Key Points
- **in**: Value exists in sequence
- **not in**: Value doesn't exist in sequence
- **Works with**: strings, lists, tuples, sets

### Essential Code
```python
# Lists
print(3 in [1, 2, 3])        # True
print(4 not in [1, 2, 3])    # True

# Strings
print("py" in "python")      # True
print("x" not in "python")   # True

# Common usage
if "python" in sentence:
    print("Found Python!")
```

---

## 🎯 Bitwise Operators (See [[Bitwise-Operators-Detailed]])

### Quick Reference Only
```python
a & b    # AND
a | b    # OR
a ^ b    # XOR
~a       # NOT
a << n   # Left shift (multiply by 2^n)
a >> n   # Right shift (divide by 2^n)
```

**For detailed explanation**: [[Bitwise-Operators-Detailed]]

---

## ⚡ Quick Reference

### Operator Precedence (High to Low)
1. `**` (Exponentiation)
2. `*`, `/`, `//`, `%` (Multiplication, Division)
3. `+`, `-` (Addition, Subtraction)
4. `<<`, `>>` (Shift operators)
5. `&` (Bitwise AND)
6. `^` (Bitwise XOR)
7. `|` (Bitwise OR)
8. `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in`
9. `not` (Logical NOT)
10. `and` (Logical AND)
11. `or` (Logical OR)

### Common Patterns
```python
# Range check
if 0 <= score <= 100:

# Multiple conditions
if age >= 18 and marks >= 80:

# Membership check
if item in shopping_list:

# None check
if value is not None:
```

---

## 🚨 Common Mistakes to Avoid

### Assignment vs Comparison
- Use `=` for assignment: `x = 5`
- Use `==` for comparison: `if x == 5:`

### Logical Operator Confusion
- `and` requires BOTH conditions true
- `or` requires AT LEAST ONE condition true

### Identity vs Equality
- `==` compares values
- `is` compares object identity

---

## 🎯 Exam Tips

### Must Remember
- **Division**: `/` always returns float, `//` returns integer
- **Modulus**: `%` gives remainder (useful for even/odd)
- **Comparison**: Always use `==`, never `=`
- **Logical**: `and` = both, `or` = at least one
- **Identity**: Use `is` only for `None` checks

### Quick Test Cases
```python
print(5 / 2)        # 2.5 (float)
print(5 // 2)       # 2 (integer)
print(5 % 2)        # 1 (remainder)
print(5 == 5)       # True (comparison)
print(True and False)  # False
print(True or False)   # True
```

### Memory Aids
- **Division**: "Slash gives float, double slash gives int"
- **Modulus**: "Percent gives remainder"
- **Logical**: "AND needs all, OR needs one"
- **Identity**: "IS for objects, EQUALS for values"

---

## 📝 Last-Minute Checklist

### Before Exam
- [ ] Know difference between `/` and `//`
- [ ] Remember `%` gives remainder
- [ ] Use `==` for comparison, not `=`
- [ ] Understand `and` vs `or` logic
- [ ] Know when to use `is` vs `==`

### During Exam
- [ ] Check operator precedence in complex expressions
- [ ] Use parentheses for clarity
- [ ] Test logical conditions mentally
- [ ] Remember `is` mainly for `None` checks

**⏰ Practice Time: 1 minute per operator type**

---
*Previous: [[PDF-3-Membership-Shift-Conditionals]] | Next: [[PDF-5-Loops-Quick-Summary]]*

#operators #arithmetic #logical #comparison #exam-prep