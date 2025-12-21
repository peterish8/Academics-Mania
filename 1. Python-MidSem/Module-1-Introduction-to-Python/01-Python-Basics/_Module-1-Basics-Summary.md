# Module 1 - Python Basics Summary

#module1 #summary #quick-reference #python-basics

---

## 📋 Quick Reference

### Installation & Setup
- Download Python from python.org
- Add Python to PATH during installation
- Use IDLE, PyCharm, VS Code, or Jupyter Notebook
- Verify: `python --version`

### Print Function
```python
print(value1, value2, sep=' ', end='\n')
print("Hello", "World", sep="-", end="!\n")  # Hello-World!
```

### Input Function
```python
name = input("Enter name: ")        # Always returns string
age = int(input("Enter age: "))     # Convert to integer
height = float(input("Height: "))   # Convert to float
```

### Variables
```python
# Assignment
name = "Alice"
age = 25
x = y = z = 0           # Multiple assignment
a, b, c = 1, 2, 3       # Tuple unpacking

# Naming rules: letters, numbers, underscore, can't start with digit
# Use snake_case: first_name, total_score
```

### Data Types
| Type | Example | Description |
|------|---------|-------------|
| `int` | `42`, `-5` | Whole numbers |
| `float` | `3.14`, `-2.5` | Decimal numbers |
| `str` | `"Hello"`, `'World'` | Text in quotes |
| `bool` | `True`, `False` | Boolean values |

### Type Conversion
```python
int("123")      # String to integer: 123
float("12.5")   # String to float: 12.5
str(42)         # Number to string: "42"
bool(1)         # Number to boolean: True
bool(0)         # Zero to boolean: False
bool("")        # Empty string: False
```

### Syntax Rules
- **Indentation**: Use 4 spaces, be consistent
- **Case sensitive**: `name` ≠ `Name`
- **Comments**: `# single line` or `"""multi-line"""`
- **Keywords**: Can't use `if`, `for`, `def`, etc. as variable names

---

## 🔧 Essential Functions

### Built-in Functions
```python
type(variable)          # Check data type
len(string)            # Length of string
isinstance(var, type)   # Check if variable is specific type
```

### String Basics (Preview)
```python
text = "Python"
text[0]        # First character: "P"
text[-1]       # Last character: "n"
text.upper()   # Convert to uppercase
text.lower()   # Convert to lowercase
```

---

## ⚠️ Common Mistakes

1. **Indentation Errors**
   ```python
   # Wrong
   if True:
   print("Hello")  # IndentationError
   
   # Correct
   if True:
       print("Hello")
   ```

2. **Type Mixing**
   ```python
   # Wrong
   age = input("Age: ")
   next_year = age + 1  # TypeError
   
   # Correct
   age = int(input("Age: "))
   next_year = age + 1
   ```

3. **Variable Names**
   ```python
   # Wrong
   2name = "Alice"      # SyntaxError
   first-name = "Bob"   # SyntaxError
   
   # Correct
   name2 = "Alice"
   first_name = "Bob"
   ```

---

## 🎯 Key Concepts to Remember

> [!NOTE] **For Exams**
> - `input()` always returns string - convert when needed
> - Python is case-sensitive: `True` not `true`
> - Indentation defines code blocks
> - Variables don't need type declaration
> - `int()` truncates decimals, doesn't round

> [!TIP] **Best Practices**
> - Use descriptive variable names
> - Convert input to appropriate types
> - Add comments to explain complex logic
> - Follow consistent indentation

---

## 🧪 Practice Checklist

- [x] Install Python and run first program
- [x] Use print() with different parameters
- [x] Get user input and convert types
- [x] Create variables of all data types
- [x] Practice type conversions
- [x] Write code with proper indentation
- [x] Use meaningful variable names

---

## 📚 Next Steps

Ready for operators? Continue to:
- [[Arithmetic-Operators]] - Math operations
- [[Comparison-Operators]] - Comparing values  
- [[Logical-Operators]] - Boolean logic

**Module Progress**: Python Basics ✅ → [[02-Operators]] →