# Data Types

#module1 #python-basics #data-types #int #float #str #bool

---

## What are Data Types?

Data types define the kind of data a variable can hold. Python has several built-in data types that are automatically determined when you assign values.

---

## Basic Data Types

### 1. Integer (int)
Whole numbers, positive or negative.

```python
# Integer examples
age = 25
temperature = -5
year = 2024
big_number = 1000000

print(type(age))  # <class 'int'>

# Integer operations
x = 10
y = 3
print(x + y)    # 13
print(x - y)    # 7
print(x * y)    # 30
print(x // y)   # 3 (floor division)
print(x % y)    # 1 (remainder)
print(x ** y)   # 1000 (power)
```

### 2. Float (float)
Decimal numbers.

```python
# Float examples
height = 5.8
price = 19.99
pi = 3.14159
negative = -2.5

print(type(height))  # <class 'float'>

# Float operations
x = 10.5
y = 2.0
print(x + y)    # 12.5
print(x / y)    # 5.25
print(x * y)    # 21.0

# Scientific notation
large = 1.5e6   # 1500000.0
small = 2.3e-4  # 0.00023
```

### 3. String (str)
Text data enclosed in quotes.

```python
# String examples
name = "Alice"
message = 'Hello World'
multiline = """This is a
multi-line string"""

print(type(name))  # <class 'str'>

# String operations
first = "Hello"
last = "World"
combined = first + " " + last  # "Hello World"
repeated = "Hi! " * 3          # "Hi! Hi! Hi! "

# String properties
text = "Python"
print(len(text))    # 6 (length)
print(text[0])      # "P" (first character)
print(text[-1])     # "n" (last character)
```

### 4. Boolean (bool)
True or False values.

```python
# Boolean examples
is_student = True
is_adult = False
has_license = True

print(type(is_student))  # <class 'bool'>

# Boolean operations
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Comparison results are boolean
age = 20
print(age >= 18)    # True
print(age == 25)    # False
```

---

## Type Checking

```python
# Check type of variable
name = "Alice"
age = 25
height = 5.8
is_student = True

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# Check if variable is specific type
print(isinstance(name, str))    # True
print(isinstance(age, int))     # True
print(isinstance(height, float)) # True
print(isinstance(is_student, bool)) # True
```

---

## Automatic Type Determination

```python
# Python automatically determines type
a = 42          # int
b = 42.0        # float
c = "42"        # str
d = True        # bool

print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'str'> <class 'bool'>

# Mixed operations
result1 = 5 + 3.0    # int + float = float (8.0)
result2 = "Hello" + " World"  # str + str = str
result3 = True + 1   # bool + int = int (2)

print(type(result1))  # <class 'float'>
print(type(result2))  # <class 'str'>
print(type(result3))  # <class 'int'>
```

---

## Special Values

```python
# None - represents absence of value
result = None
print(type(result))  # <class 'NoneType'>

# Empty values
empty_string = ""
zero = 0
false_value = False

# All these are "falsy" in boolean context
if not empty_string:
    print("Empty string is falsy")

if not zero:
    print("Zero is falsy")

if not false_value:
    print("False is falsy")
```

---

## Data Type Conversion Preview

```python
# Converting between types (covered in detail in Type-Conversion)
num_str = "123"
num_int = int(num_str)      # Convert to integer
num_float = float(num_str)  # Convert to float

print(num_int)    # 123 (int)
print(num_float)  # 123.0 (float)

# Boolean conversions
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("Hi"))   # True
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - Python automatically determines data type
> - Variables can change type during execution
> - Each type has specific operations and methods
> - Type determines how operations behave

> [!TIP] **Memory Tips**
> - **int**: Whole numbers (1, 2, 100, -5)
> - **float**: Decimal numbers (3.14, -2.5, 0.0)
> - **str**: Text in quotes ("hello", 'world')
> - **bool**: True or False only

> [!WARNING] **Common Mistakes**
> - Mixing incompatible types without conversion
> - Assuming "123" is a number (it's a string)
> - Forgetting that True/False are case-sensitive
> - Using = instead of == for comparison

---

## Practical Examples

### Student Grade System
```python
# Different data types for student info
student_name = "Alice Johnson"    # str
student_id = 12345               # int
gpa = 3.85                       # float
is_honors = True                 # bool
graduation_year = None           # None (not decided yet)

print(f"Student: {student_name}")
print(f"ID: {student_id}")
print(f"GPA: {gpa}")
print(f"Honors Student: {is_honors}")
```

### Shopping Cart
```python
# Shopping cart with different data types
item_name = "Laptop"             # str
quantity = 2                     # int
price_per_item = 999.99         # float
in_stock = True                 # bool

total_cost = quantity * price_per_item
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Total: ${total_cost}")
print(f"Available: {in_stock}")
```

---

## Related Topics
- [[Type-Conversion]] - Converting between data types
- [[Variables]] - Storing different types of data
- [[Operators]] - Operations with different types

---

## Practice Questions

1. Create variables of each data type and print their types
2. What will be the type of these expressions?
   - `5 + 3.0`
   - `"Hello" + "World"`
   - `True + False`

```python
# Practice solutions
# 1. Variables of each type
my_int = 42
my_float = 3.14
my_str = "Hello"
my_bool = True

print(type(my_int), type(my_float), type(my_str), type(my_bool))

# 2. Expression types
print(type(5 + 3.0))        # <class 'float'>
print(type("Hello" + "World"))  # <class 'str'>
print(type(True + False))   # <class 'int'>
```

**Next**: Learn about [[Type-Conversion]] →