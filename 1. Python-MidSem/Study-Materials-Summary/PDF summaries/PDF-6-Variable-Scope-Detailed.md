# Variable Scope in Python - Detailed Guide

#variable-scope #local #global #enclosing #nonlocal #LEGB

---

## 🎯 LEGB Rule - Scope Resolution Order

Python follows **LEGB** rule to find variables:
1. **L**ocal - Inside current function
2. **E**nclosing - In outer function (nested functions)
3. **G**lobal - At module level
4. **B**uilt-in - Python's built-in names

---

## 🎯 1. Local Scope

### Key Points
- **Variables declared inside a function**
- **Only accessible within that function**
- **Created when function is called, destroyed when function ends**

### Essential Code
```python
def demo():
    x = 10  # Local variable
    print("Inside function:", x)

demo()  # Output: Inside function: 10

# print(x)  # NameError: name 'x' is not defined
```

### Multiple Local Variables
```python
def calculate():
    a = 5    # Local
    b = 10   # Local
    result = a + b  # Local
    return result

print(calculate())  # 15
# print(a)  # Error - local variables not accessible outside
```

---

## 🎯 2. Global Scope

### Key Points
- **Variables declared outside all functions**
- **Accessible anywhere in the program**
- **Exist throughout program execution**

### Essential Code
```python
x = 50  # Global variable

def demo():
    print("Inside function:", x)  # Can access global

def another():
    print("Another function:", x)  # Can access global

demo()      # Output: Inside function: 50
another()   # Output: Another function: 50
print("Outside:", x)  # Output: Outside: 50
```

### Reading vs Modifying Global Variables
```python
count = 0  # Global

def read_global():
    print("Count is:", count)  # Reading global - OK

def try_modify():
    count = 5  # Creates LOCAL variable, doesn't modify global
    print("Local count:", count)

def modify_global():
    global count
    count = 10  # Modifies global variable
    print("Modified global:", count)

read_global()    # Count is: 0
try_modify()     # Local count: 5
print(count)     # 0 (global unchanged)
modify_global()  # Modified global: 10
print(count)     # 10 (global changed)
```

---

## 🎯 3. Enclosing Scope (Nested Functions)

### Key Points
- **Variable in outer function accessible to inner function**
- **Inner function can read outer function's variables**
- **Used in nested function definitions**

### Essential Code
```python
def outer_function():
    x = "outer value"  # Enclosing scope
    
    def inner_function():
        print("Inner can access:", x)  # Accessing enclosing variable
    
    inner_function()
    print("Outer variable:", x)

outer_function()
# Output:
# Inner can access: outer value
# Outer variable: outer value
```

### Multiple Levels of Nesting
```python
def level1():
    a = "Level 1"
    
    def level2():
        b = "Level 2"
        
        def level3():
            c = "Level 3"
            print(f"Level 3 can access: {a}, {b}, {c}")
        
        level3()
        print(f"Level 2 can access: {a}, {b}")
    
    level2()
    print(f"Level 1 can access: {a}")

level1()
```

---

## 🎯 4. Nonlocal Scope

### Key Points
- **Used to modify enclosing function's variable**
- **Only works in nested functions**
- **Similar to global, but for enclosing scope**

### Essential Code
```python
def outer():
    x = "original"  # Enclosing variable
    
    def inner():
        nonlocal x  # Declare intention to modify enclosing variable
        x = "modified by inner"  # Modifies enclosing x
        print("Inner modified x to:", x)
    
    print("Before inner call:", x)
    inner()
    print("After inner call:", x)

outer()
# Output:
# Before inner call: original
# Inner modified x to: modified by inner
# After inner call: modified by inner
```

### Without nonlocal (Creates Local Variable)
```python
def outer():
    x = "original"
    
    def inner():
        x = "local to inner"  # Creates new local variable
        print("Inner x:", x)
    
    print("Before inner:", x)
    inner()
    print("After inner:", x)  # Unchanged

outer()
# Output:
# Before inner: original
# Inner x: local to inner
# After inner: original
```

---

## 🎯 Complete Scope Example

```python
# Global scope
global_var = "I'm global"

def outer_func():
    # Enclosing scope
    enclosing_var = "I'm enclosing"
    
    def inner_func():
        # Local scope
        local_var = "I'm local"
        
        # Accessing all scopes
        print("Local:", local_var)
        print("Enclosing:", enclosing_var)
        print("Global:", global_var)
        print("Built-in:", len([1, 2, 3]))  # len is built-in
    
    inner_func()

outer_func()
```

---

## 🎯 Practical Examples

### Example 1: Counter Function
```python
def create_counter():
    count = 0  # Enclosing scope
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# Usage
counter = create_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### Example 2: Configuration Settings
```python
# Global configuration
DEBUG = True
MAX_USERS = 100

def process_user(user_id):
    # Local variables
    user_data = f"User {user_id}"
    
    def log_debug(message):
        if DEBUG:  # Accessing global
            print(f"DEBUG: {message}")
    
    def validate_user():
        if user_id > MAX_USERS:  # Accessing global
            return False
        return True
    
    log_debug(f"Processing {user_data}")
    return validate_user()

# Test
result = process_user(50)
print("Valid user:", result)
```

### Example 3: Scope Resolution Demonstration
```python
x = "global"

def test_scope():
    x = "enclosing"
    
    def inner():
        x = "local"
        print("Inner function x:", x)
    
    inner()
    print("Outer function x:", x)

test_scope()
print("Global x:", x)

# Output:
# Inner function x: local
# Outer function x: enclosing
# Global x: global
```

---

## 🚨 Common Scope Mistakes

### Mistake 1: Trying to Modify Global Without Declaration
```python
count = 0

def increment():
    count += 1  # UnboundLocalError

# Fix:
def increment():
    global count
    count += 1
```

### Mistake 2: Confusing Local and Global
```python
x = 10

def func():
    print(x)  # This works (reading global)
    x = 20    # This creates local x, but causes error above

# Fix: Either read only, or declare global
def func():
    global x
    print(x)
    x = 20
```

### Mistake 3: Nonlocal in Wrong Context
```python
def func():
    nonlocal x  # SyntaxError: no binding for nonlocal 'x'
    x = 10

# Fix: Use nonlocal only in nested functions
def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
```

---

## 🎯 Exam Tips

### Quick Scope Test
```python
# Test your understanding:
a = 1  # Global

def f1():
    a = 2  # Local to f1
    
    def f2():
        a = 3  # Local to f2
        print("f2:", a)
    
    f2()
    print("f1:", a)

f1()
print("global:", a)

# Output: f2: 3, f1: 2, global: 1
```

### Memory Aids
- **Local**: "Lives in function only"
- **Global**: "Goes everywhere"
- **Enclosing**: "Embraces inner functions"
- **Nonlocal**: "Not local, but not global either"
- **LEGB**: "Look Everywhere, Go Back"

### Scope Checklist
- [ ] Local variables only exist inside their function
- [ ] Global variables are accessible everywhere
- [ ] Use `global` keyword to modify global variables
- [ ] Use `nonlocal` keyword to modify enclosing variables
- [ ] Inner functions can access outer function variables
- [ ] Python searches: Local → Enclosing → Global → Built-in

---

## 📝 Quick Reference

### Scope Keywords
```python
global variable_name    # Modify global variable
nonlocal variable_name  # Modify enclosing variable
```

### Scope Testing Pattern
```python
def test_variable_scope():
    # Check if variable exists in different scopes
    try:
        print(variable_name)
        print("Variable found in accessible scope")
    except NameError:
        print("Variable not found in any accessible scope")
```

**Return to main functions summary**: [[PDF-6-Functions-Scope-Quick-Summary]]