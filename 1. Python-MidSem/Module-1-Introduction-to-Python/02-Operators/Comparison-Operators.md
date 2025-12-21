# Comparison Operators

#module1 #operators #comparison #relational

---

## What are Comparison Operators?

Comparison operators compare two values and return a boolean result (True or False). They are essential for making decisions in your programs.

---

## Basic Comparison Operators

### Equal To (==)
```python
# Check if values are equal
print(5 == 5)        # True
print(5 == 3)        # False
print("hello" == "hello")  # True
print("Hello" == "hello")  # False (case-sensitive)

# With variables
x = 10
y = 10
print(x == y)        # True

age = 18
print(age == 18)     # True
```

### Not Equal To (!=)
```python
# Check if values are different
print(5 != 3)        # True
print(5 != 5)        # False
print("cat" != "dog") # True

# With variables
name = "Alice"
print(name != "Bob")  # True
```

### Greater Than (>)
```python
# Check if left value is greater
print(10 > 5)        # True
print(3 > 7)         # False
print(5 > 5)         # False (not greater, equal)

# With variables
score = 85
print(score > 80)    # True
print(score > 90)    # False
```

### Less Than (<)
```python
# Check if left value is smaller
print(3 < 7)         # True
print(10 < 5)        # False
print(5 < 5)         # False (not less, equal)

# Age check
age = 16
print(age < 18)      # True
```

### Greater Than or Equal To (>=)
```python
# Check if left value is greater or equal
print(10 >= 5)       # True
print(5 >= 5)        # True (equal counts)
print(3 >= 7)        # False

# Minimum age check
age = 18
print(age >= 18)     # True (can vote)
```

### Less Than or Equal To (<=)
```python
# Check if left value is less or equal
print(3 <= 7)        # True
print(5 <= 5)        # True (equal counts)
print(10 <= 5)       # False

# Maximum limit check
speed = 60
speed_limit = 60
print(speed <= speed_limit)  # True
```

---

## Comparing Different Data Types

### Numbers
```python
# Integer and float comparison
print(5 == 5.0)      # True (values are equal)
print(3 < 3.5)       # True
print(10 >= 10.0)    # True

# Mixed comparisons
x = 15
y = 15.0
print(x == y)        # True
print(type(x) == type(y))  # False (different types)
```

### Strings
```python
# String comparison (lexicographic order)
print("apple" < "banana")    # True (alphabetical order)
print("cat" > "car")         # True ('t' > 'r')
print("Hello" == "hello")    # False (case-sensitive)

# Case-insensitive comparison
name1 = "Alice"
name2 = "alice"
print(name1.lower() == name2.lower())  # True
```

### Boolean Values
```python
# Boolean comparisons
print(True == True)   # True
print(True != False)  # True
print(True > False)   # True (True = 1, False = 0)

# Boolean with numbers
print(True == 1)      # True
print(False == 0)     # True
print(True > 0)       # True
```

---

## Chaining Comparisons

```python
# Multiple comparisons in one expression
x = 15
print(10 < x < 20)    # True (x is between 10 and 20)
print(5 <= x <= 10)   # False

# Equivalent to:
print(10 < x and x < 20)  # True

# More complex chaining
age = 25
print(18 <= age <= 65)    # True (working age)

# Multiple variables
a, b, c = 5, 10, 15
print(a < b < c)          # True (ascending order)
```

---

## Practical Examples

### Grade Checker
```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
```

### Age Category
```python
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

### Password Strength
```python
password = input("Enter password: ")
length = len(password)

if length < 6:
    print("Weak password")
elif length < 10:
    print("Medium password")
else:
    print("Strong password")
```

---

## Common Use Cases

### Range Checking
```python
# Check if number is in range
number = 75
if 0 <= number <= 100:
    print("Valid percentage")

# Temperature range
temp = 25
if 20 <= temp <= 30:
    print("Comfortable temperature")
```

### Validation
```python
# Age validation
age = int(input("Enter age: "))
if age < 0 or age > 150:
    print("Invalid age")
else:
    print("Valid age")

# Score validation
score = float(input("Enter score: "))
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Score must be between 0 and 100")
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - Comparison operators return True or False
> - Use == for equality, not = (assignment)
> - String comparison is case-sensitive
> - Can chain multiple comparisons
> - True equals 1, False equals 0 in numeric context

> [!TIP] **Best Practices**
> - Use parentheses for complex comparisons
> - Be careful with floating-point equality
> - Consider case-sensitivity in string comparisons
> - Use chaining for range checks: `a <= x <= b`

> [!WARNING] **Common Mistakes**
> - Using = instead of == for comparison
> - Forgetting case-sensitivity in strings
> - Comparing incompatible types
> - Not handling edge cases in ranges

---

## Related Topics
- [[Logical-Operators]] - Combining comparisons
- [[If-Elif-Else]] - Using comparisons in decisions
- [[Variables]] - Values being compared

---

## Practice Questions

1. Check if a number is between 10 and 50 (inclusive)
2. Compare two strings ignoring case
3. Validate if a year is between 1900 and 2024

```python
# Practice solutions
# 1. Range check
num = 25
print(10 <= num <= 50)  # True

# 2. Case-insensitive comparison
str1 = "Hello"
str2 = "hello"
print(str1.lower() == str2.lower())  # True

# 3. Year validation
year = 2023
print(1900 <= year <= 2024)  # True
```

**Next**: Learn about [[Logical-Operators]] →