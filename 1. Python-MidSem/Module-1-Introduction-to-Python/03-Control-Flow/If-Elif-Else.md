# If-Elif-Else Statements

#module1 #control-flow #conditionals #if #elif #else

---

## What are Conditional Statements?

Conditional statements allow your program to make decisions and execute different code based on conditions. They control the flow of your program.

---

## Basic If Statement

### Syntax
```python
if condition:
    # Code to execute if condition is True
    statement1
    statement2
```

### Simple Examples
```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# With variables
score = 85
if score >= 60:
    print("You passed!")

# Multiple statements in if block
temperature = 30
if temperature > 25:
    print("It's hot today")
    print("Wear light clothes")
    print("Stay hydrated")
```

---

## If-Else Statement

### Syntax
```python
if condition:
    # Code if condition is True
else:
    # Code if condition is False
```

### Examples
```python
# Basic if-else
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# With user input
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Password check
password = input("Enter password: ")
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")
```

---

## If-Elif-Else Statement

### Syntax
```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition2 is True
elif condition3:
    # Code if condition3 is True
else:
    # Code if all conditions are False
```

### Examples
```python
# Grade calculator
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Weather advice
temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("It's very hot! Stay indoors.")
elif temperature > 20:
    print("Nice weather for a walk.")
elif temperature > 10:
    print("A bit cool, wear a jacket.")
elif temperature > 0:
    print("It's cold, bundle up!")
else:
    print("Freezing! Stay warm indoors.")
```

---

## Comparison Operators in Conditions

```python
# Equality and inequality
x = 10
if x == 10:        # Equal to
    print("x is 10")

if x != 5:         # Not equal to
    print("x is not 5")

# Numerical comparisons
age = 25
if age > 18:       # Greater than
    print("Adult")

if age >= 21:      # Greater than or equal
    print("Can drink (US)")

if age < 65:       # Less than
    print("Not senior")

if age <= 30:      # Less than or equal
    print("Young adult")

# String comparisons
name = "Alice"
if name == "Alice":
    print("Hello Alice!")

# Case-sensitive comparison
if name.lower() == "alice":
    print("Hello alice (case-insensitive)!")
```

---

## Logical Operators in Conditions

### AND Operator
```python
# Both conditions must be True
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

# Multiple AND conditions
score = 85
attendance = 90
if score >= 80 and attendance >= 85:
    print("Excellent student")
```

### OR Operator
```python
# At least one condition must be True
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# Multiple OR conditions
grade = "A"
if grade == "A" or grade == "B" or grade == "C":
    print("Passing grade")
```

### NOT Operator
```python
# Reverses the condition
is_raining = False

if not is_raining:
    print("Good day for a picnic")

# NOT with other operators
age = 16
if not (age >= 18):
    print("Minor")
```

---

## Nested If Statements

```python
# If statements inside other if statements
age = 20
has_license = True
has_car = False

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can legally drive")
        if has_car:
            print("You can drive your own car")
        else:
            print("You need to borrow a car")
    else:
        print("You need to get a license")
else:
    print("You are a minor")
```

---

## Practical Examples

### Login System
```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secret123":
    print("Welcome, Administrator!")
elif username == "user" and password == "pass123":
    print("Welcome, User!")
else:
    print("Invalid credentials")
```

### BMI Calculator with Categories
```python
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
```

### Simple ATM System
```python
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    print("PIN correct")
    choice = input("1. Check Balance 2. Withdraw: ")
    
    if choice == "1":
        print(f"Your balance is: ${balance}")
    elif choice == "2":
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance}")
        else:
            print("Insufficient funds")
    else:
        print("Invalid choice")
else:
    print("Incorrect PIN")
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - Conditions evaluate to True or False
> - Indentation defines which code belongs to each block
> - `elif` is short for "else if"
> - Only the first True condition executes
> - `else` is optional and executes if no conditions are True

> [!TIP] **Best Practices**
> - Use meaningful condition names
> - Keep conditions simple and readable
> - Use parentheses for complex conditions
> - Consider the order of elif conditions
> - Use logical operators to combine conditions

> [!WARNING] **Common Mistakes**
> - Using `=` instead of `==` for comparison
> - Forgetting colons `:` after conditions
> - Incorrect indentation
> - Not considering all possible cases
> - Confusing `and`/`or` logic

---

## Related Topics
- [[Comparison-Operators]] - Operators used in conditions
- [[Logical-Operators]] - Combining conditions
- [[Variables]] - Values used in conditions

---

## Practice Questions

1. Write a program to check if a year is a leap year
2. Create a simple calculator that handles division by zero
3. Make a grade system with A+, A, B+, B, C+, C, D, F

```python
# Practice solutions
# 1. Leap year checker
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 2. Safe calculator
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operation (+, -, *, /): ")

if operation == "/" and num2 == 0:
    print("Error: Cannot divide by zero")
elif operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")
```

**Next**: Learn about [[For-Loops]] →