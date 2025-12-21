# 🛠️ functions (def, return, scope)

## 📌 1. Defining Functions
A function is a block of reusable code that runs when it is called.

### **Syntax**
```python
def function_name(parameters):
    """Docstring: Explain what the function does."""
    # body of the function
    return result
```

### **Example**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

---

## 🎯 2. Arguments & Parameters
### **Positional Arguments**
Arguments must be passed in the correct order.
```python
def add(a, b):
    return a + b

print(add(5, 3))  # 5 is a, 3 is b
```

### **Default Arguments**
Parameters can have default values if no argument is provided.
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # 9 (3^2)
print(power(3, 3)) # 27 (3^3)
```

### **Keyword Arguments**
Arguments passed by name, order doesn't matter.
```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Harry", animal_type="hamster")
```

---

## 🔒 3. Scope (Local vs Global)
- **Local Scope**: Variables created inside a function are available only inside that function.
- **Global Scope**: Variables created in the main body of the script are global and available everywhere.

```python
x = "global"

def my_func():
    x = "local"
    print("Inside:", x)

my_func()      # Output: Inside: local
print("Outside:", x) # Output: Outside: global
```

---

## 🧠 Practice Exercises
1. **Factorial Function**: Write a function `factorial(n)` that returns the factorial of a number using recursion or a loop.
2. **Temperature Converter**: Write a function to convert Celsius to Fahrenheit and vice versa based on a second argument.
3. **Palindrome Checker**: Write a function that checks if a given string is a palindrome.

---
> [[Sem Exam/3-Intro-to-Programming/Module 1 - Python Basics/README|🔙 Back to Module 1 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
