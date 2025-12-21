# Input Function

#module1 #python-basics #input #user-input

---

## What is input()?

The `input()` function gets text input from the user. It always returns a string, even if the user enters numbers.

---

## Basic Syntax

```python
variable = input(prompt)
```

**Parameters:**
- `prompt`: Optional message to display to user

**Returns:** String containing user's input

---

## Basic Examples

```python
# Simple input
name = input("Enter your name: ")
print("Hello,", name)

# Input without prompt
age = input()  # User types and presses Enter
print("You entered:", age)

# Multiple inputs
first_name = input("First name: ")
last_name = input("Last name: ")
print("Full name:", first_name, last_name)
```

---

## Input Always Returns String

```python
# Even numbers are returned as strings
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

# This won't work for math:
# result = age + 5  # TypeError: can't add string and int
```

> [!WARNING] **Important**
> `input()` always returns a string. Convert to numbers when needed!

---

## Converting Input to Numbers

```python
# Convert to integer
age = int(input("Enter your age: "))
print("Next year you'll be:", age + 1)

# Convert to float
height = float(input("Enter your height: "))
print("Height in cm:", height * 100)

# Multiple number inputs
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
sum_result = num1 + num2
print("Sum:", sum_result)
```

---

## Handling Input Errors

```python
# Basic error handling
try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid number!")

# Check before converting
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print("Number:", number)
else:
    print("That's not a valid number!")
```

---

## Practical Examples

### Calculator Input
```python
# Simple calculator
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print("Result:", result)
```

### User Information
```python
# Collect user info
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
is_student = input("Are you a student? (yes/no): ").lower()

print(f"\nProfile:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Student: {is_student == 'yes'}")
```

---

## Input with Validation

```python
# Age validation
while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            break
        else:
            print("Age must be between 1 and 120!")
    except ValueError:
        print("Please enter a valid number!")

print("Valid age entered:", age)

# Yes/No validation
while True:
    answer = input("Continue? (yes/no): ").lower()
    if answer in ['yes', 'no', 'y', 'n']:
        break
    print("Please enter yes or no!")
```

---

## Important Points

> [!NOTE] **Key Features**
> - Always returns a string
> - Waits for user to press Enter
> - Can include a prompt message
> - Handles empty input (returns empty string)

> [!TIP] **Best Practices**
> - Always include clear prompts
> - Convert to appropriate data types
> - Validate user input when necessary
> - Handle potential errors with try/except

> [!WARNING] **Common Mistakes**
> - Forgetting to convert strings to numbers
> - Not handling invalid input
> - Using input() in loops without validation

---

## Related Topics
- [[Print-Function]] - Displaying output
- [[Type-Conversion]] - Converting data types
- [[Variables]] - Storing input values

---

## Practice Questions

1. Get user's name and age, then calculate birth year
2. Get two numbers and display their sum, difference, and product
3. Create a simple login system (username and password)

```python
# Practice solutions
# 1. Birth year calculator
name = input("Enter your name: ")
age = int(input("Enter your age: "))
birth_year = 2024 - age
print(f"Hello {name}, you were born in {birth_year}")

# 2. Number operations
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
```

**Next**: Learn about [[Python-Syntax-Rules]] →