# PDF 7: Strings in Python - Quick Summary

## 🎯 Exam Essentials

### String Basics
- **Definition**: Sequence of characters in quotes (`'`, `"`, `'''`)
- **Key Property**: **IMMUTABLE** (cannot change in place)
- **Types**: Single, double, triple quotes for multiline

### Indexing & Slicing
```python
s = "Python"
# Forward: 0,1,2,3,4,5
# Backward: -6,-5,-4,-3,-2,-1
s[0] = 'P', s[-1] = 'n'

# Slicing: string[start:end:step]
s[0:6]   # "Python" 
s[::-1]  # Reverse string
s[::2]   # Every 2nd character
```

### Essential Methods
| Method | Purpose | Example |
|--------|---------|---------|
| `split()` | Break into list | `"a,b,c".split(",")` → `['a','b','c']` |
| `strip()` | Remove whitespace | `" hello ".strip()` → `"hello"` |
| `find()` | Find substring index | `"abc".find("b")` → `1` (returns -1 if not found) |
| `replace()` | Replace substring | `"hi".replace("i","o")` → `"ho"` |

### F-String Formatting
```python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")  # Name: Alice, Age: 25
print(f"Sum: {5+3}")                # Sum: 8
```

## 🔥 Exam Algorithms

### 1. Count Spaces Using split()
```python
def count_spaces(s):
    parts = s.split(" ")
    return len(parts) - 1
```

### 2. Palindrome Check
```python
def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True
```

## ⚡ Quick Tips
- **Immutable**: Use concatenation or methods to create new strings
- **Negative indexing**: `-1` is last character
- **Slicing**: `[start:end]` - end is exclusive
- **find() vs index()**: find() returns -1, index() raises exception
- **F-strings**: Fastest formatting method

## 🎯 Common Exam Patterns
- String reversal using slicing
- Character frequency counting
- Palindrome variations
- String manipulation with methods
- Indexing boundary conditions

---
*Previous: [[PDF-6-Functions-Scope-Quick-Summary]] | Next: [[PDF-8-String-Functions-Quick-Summary]]*

#strings #python #exam-prep #quick-reference