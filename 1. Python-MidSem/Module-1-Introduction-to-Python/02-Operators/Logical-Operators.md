# Logical Operators

#module1 #operators #logical #boolean

---

## What are Logical Operators?

Logical operators combine or modify boolean values (True/False). They help create complex conditions by connecting multiple comparisons.

---

## The Three Logical Operators

### AND Operator (and)
Returns True only if both conditions are True.

```python
# Basic AND usage
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# With comparisons
age = 25
has_license = True
print(age >= 18 and has_license)  # True

# Multiple conditions
score = 85
attendance = 90
print(score >= 80 and attendance >= 85)  # True
```

### OR Operator (or)
Returns True if at least one condition is True.

```python
# Basic OR usage
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# With comparisons
day = "Saturday"
print(day == "Saturday" or day == "Sunday")  # True

# Emergency conditions
temperature = 40
humidity = 95
print(temperature > 35 or humidity > 90)  # True
```

### NOT Operator (not)
Reverses the boolean value.

```python
# Basic NOT usage
print(not True)         # False
print(not False)        # True

# With variables
is_raining = False
print(not is_raining)   # True (not raining)

# With comparisons
age = 16
print(not (age >= 18))  # True (is minor)
```

---

## Truth Tables

### AND Truth Table
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### OR Truth Table
| A     | B     | A or B |
|-------|--------|--------|
| True  | True   | True   |
| True  | False  | True   |
| False | True   | True   |
| False | False  | False  |

### NOT Truth Table
| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

---

## Combining Logical Operators

### Multiple AND Conditions
```python
# All conditions must be True
age = 25
has_license = True
has_car = True
has_insurance = True

can_drive = age >= 18 and has_license and has_car and has_insurance
print(can_drive)  # True

# Student eligibility
gpa = 3.5
attendance = 95
behavior = "good"
eligible = gpa >= 3.0 and attendance >= 90 and behavior == "good"
print(eligible)  # True
```

### Multiple OR Conditions
```python
# At least one condition must be True
payment_method = "credit"
valid_payment = (payment_method == "cash" or 
                payment_method == "credit" or 
                payment_method == "debit")
print(valid_payment)  # True

# Weekend check
day = "Sunday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True
```

### Mixing AND and OR
```python
# Complex conditions with precedence
age = 20
student = True
senior = False

# Student discount: (student AND age < 25) OR senior
discount = (student and age < 25) or senior
print(discount)  # True

# Access control
is_admin = False
is_owner = True
has_permission = True

access = is_admin or (is_owner and has_permission)
print(access)  # True
```

---

## Operator Precedence

**Order (highest to lowest):**
1. `not`
2. `and`
3. `or`

```python
# Without parentheses
result = True or False and False
# Evaluated as: True or (False and False) = True or False = True
print(result)  # True

# With parentheses for clarity
result = (True or False) and False
# Evaluated as: True and False = False
print(result)  # False

# Complex example
a, b, c = True, False, True
result = not a or b and c
# Evaluated as: (not a) or (b and c) = False or False = False
print(result)  # False
```

---

## Practical Examples

### Login System
```python
username = input("Username: ")
password = input("Password: ")

# Valid credentials
valid_admin = username == "admin" and password == "admin123"
valid_user = username == "user" and password == "user123"

if valid_admin or valid_user:
    print("Login successful")
else:
    print("Invalid credentials")
```

### Grade Requirements
```python
midterm = float(input("Midterm score: "))
final = float(input("Final score: "))
attendance = float(input("Attendance %: "))

# Pass requirements: (midterm >= 60 AND final >= 60) AND attendance >= 75
passed = (midterm >= 60 and final >= 60) and attendance >= 75

if passed:
    print("You passed the course!")
else:
    print("You did not meet the requirements")
```

### Weather Advisory
```python
temperature = int(input("Temperature: "))
humidity = int(input("Humidity %: "))
wind_speed = int(input("Wind speed: "))

# Dangerous conditions
too_hot = temperature > 40
too_humid = humidity > 90
too_windy = wind_speed > 50

dangerous = too_hot or too_humid or too_windy

if dangerous:
    print("Weather advisory: Stay indoors")
else:
    print("Weather is safe")
```

---

## Short-Circuit Evaluation

Python uses short-circuit evaluation for efficiency:

### AND Short-Circuit
```python
# If first condition is False, second is not evaluated
x = 0
result = (x != 0) and (10 / x > 5)  # Safe: division not executed
print(result)  # False

# Without short-circuit, this would cause ZeroDivisionError
```

### OR Short-Circuit
```python
# If first condition is True, second is not evaluated
user_type = "admin"
result = (user_type == "admin") or (len(password) > 8)
print(result)  # True (password not checked)
```

---

## Truthy and Falsy Values

```python
# Falsy values (evaluate to False)
falsy_values = [False, 0, 0.0, "", [], {}, None]

# Truthy values (evaluate to True)
truthy_values = [True, 1, -1, "hello", [1], {"a": 1}]

# Using in logical operations
name = ""
age = 25

if name and age > 0:
    print("Valid user")  # Won't print (name is empty string = False)
else:
    print("Invalid user")  # This will print

# Better approach
if name != "" and age > 0:
    print("Valid user")
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - `and` requires ALL conditions to be True
> - `or` requires AT LEAST ONE condition to be True
> - `not` reverses the boolean value
> - Python uses short-circuit evaluation
> - Precedence: not > and > or

> [!TIP] **Best Practices**
> - Use parentheses for complex conditions
> - Break complex conditions into variables
> - Consider short-circuit evaluation for safety
> - Use meaningful variable names for conditions

> [!WARNING] **Common Mistakes**
> - Confusing and/or logic
> - Forgetting operator precedence
> - Not using parentheses in complex expressions
> - Mixing up truthy/falsy values

---

## Related Topics
- [[Comparison-Operators]] - Creating conditions to combine
- [[If-Elif-Else]] - Using logical operators in decisions
- [[Variables]] - Storing boolean values

---

## Practice Questions

1. Check if a number is between 10-20 OR between 30-40
2. Validate user: age >= 18 AND (has_id OR has_passport)
3. Emergency alert: temperature > 45 OR humidity < 10 OR wind > 60

```python
# Practice solutions
# 1. Number range check
num = 15
in_range = (10 <= num <= 20) or (30 <= num <= 40)
print(in_range)  # True

# 2. User validation
age = 20
has_id = False
has_passport = True
valid_user = age >= 18 and (has_id or has_passport)
print(valid_user)  # True

# 3. Emergency conditions
temp, humidity, wind = 50, 15, 70
emergency = temp > 45 or humidity < 10 or wind > 60
print(emergency)  # True
```

**Next**: Learn about [[For-Loops]] →