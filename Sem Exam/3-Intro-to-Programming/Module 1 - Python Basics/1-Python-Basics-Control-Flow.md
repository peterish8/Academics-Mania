# 🐍 Python Basics & Control Flow

## 📌 1. Python Basics
### **Installation & IDEs**
- **Python**: Interpreted, high-level, dynamically typed language.
- **IDEs**: VS Code, PyCharm, Jupyter Notebook.
- **Running Python**: `python script.py` or interactive mode `python`.

### **Input & Output**
```python
print("Hello, World!")  # Output
name = input("Enter your name: ")  # Input (always returns string)
print(f"Hello, {name}")
```

### **Variables & Data Types**
- **Variables**: Containers for storing data values. No command to declare a variable.
- **Data Types**:
  - `int`: Integers (e.g., `10`, `-5`)
  - `float`: Floating point numbers (e.g., `3.14`, `-0.001`)
  - `str`: Strings (e.g., `"Hello"`, `'Python'`)
  - `bool`: Booleans (`True`, `False`)
- **Type Conversion**:
  - `int("10")` -> `10`
  - `str(10)` -> `"10"`
  - `float(10)` -> `10.0`

### **Operators**
- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor div), `%` (modulus), `**` (exponent)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`

---

## 🚦 2. Control Flow
### **Conditionals (if, elif, else)**
Execute code only if a certain condition is met.
```python
age = 18
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")
```

### **Loops**
#### **For Loop** (Iterate over a sequence)
```python
for i in range(5):  # 0 to 4
    print(i)
```

#### **While Loop** (Repeat as long as condition is true)
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### **Control Keywords**
- `break`: Terminate the loop.
- `continue`: Skip the current iteration and continue with the next.
- `pass`: Null operation (placeholder).

---

## 🧠 Practice Exercises
1. **Simple Calculator**: Create a program that takes two numbers and an operator (+, -, *, /) and prints the result.
2. **Number Guessing Game**: Generate a random number between 1-10 (using `import random`) and let the user guess it using a loop.
3. **Even/Odd Checker**: Write a loop that prints numbers 1-20 and states if they are even or odd.

---
> [[Sem Exam/3-Intro-to-Programming/Module 1 - Python Basics/README|🔙 Back to Module 1 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
