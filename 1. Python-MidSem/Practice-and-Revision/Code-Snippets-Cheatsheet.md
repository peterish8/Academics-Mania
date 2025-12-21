# Code Snippets Cheatsheet

#cheatsheet #quick-reference #exam-prep #code-snippets

---

## 🚀 Quick Reference for Python Mid-Sem Exam

### Basic I/O
```python
# Output
print("Hello World")
print(var1, var2, sep="-", end="!\n")

# Input (always returns string)
name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
```

### Variables & Data Types
```python
# Assignment
x = 10              # int
y = 3.14           # float
name = "Alice"     # str
is_valid = True    # bool

# Type checking
type(x)            # <class 'int'>
isinstance(x, int) # True
```

### Type Conversion
```python
int("123")         # 123
float("12.5")      # 12.5
str(42)           # "42"
bool(1)           # True
bool(0)           # False
bool("")          # False
```

---

## 🔢 Operators

### Arithmetic
```python
+    # Addition
-    # Subtraction
*    # Multiplication
/    # Division (always float)
//   # Floor division
%    # Modulus (remainder)
**   # Exponentiation

# Shortcuts
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
```

### Comparison
```python
==   # Equal
!=   # Not equal
>    # Greater than
<    # Less than
>=   # Greater than or equal
<=   # Less than or equal
```

### Logical
```python
and  # Both conditions true
or   # At least one condition true
not  # Reverse condition

# Examples
age >= 18 and has_license
day == "Sat" or day == "Sun"
not is_raining
```

---

## 🔀 Control Flow

### If-Elif-Else
```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# One-liner
result = "adult" if age >= 18 else "minor"
```

### For Loops
```python
# Range loops
for i in range(5):        # 0,1,2,3,4
for i in range(1, 6):     # 1,2,3,4,5
for i in range(0, 10, 2): # 0,2,4,6,8

# List iteration
for item in my_list:
    print(item)

# With index
for i, item in enumerate(my_list):
    print(i, item)
```

### While Loops
```python
while condition:
    # code
    
# Counter pattern
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
```python
break     # Exit loop
continue  # Skip to next iteration
pass      # Do nothing (placeholder)
```

---

## 🔧 Functions

### Basic Function
```python
def function_name(parameters):
    """Docstring"""
    # code
    return value

# Example
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
```

### Function Arguments
```python
# Positional arguments
def add(a, b):
    return a + b

# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Keyword arguments
greet(name="Alice", greeting="Hi")
```

---

## 📝 Strings

### String Basics
```python
text = "Python Programming"
text[0]        # "P" (first character)
text[-1]       # "g" (last character)
text[2:8]      # "thon P" (slicing)
len(text)      # 18 (length)
```

### Essential String Methods
```python
text = "  Hello World  "

# Case methods
text.upper()      # "  HELLO WORLD  "
text.lower()      # "  hello world  "
text.title()      # "  Hello World  "

# Cleaning methods
text.strip()      # "Hello World"
text.lstrip()     # "Hello World  "
text.rstrip()     # "  Hello World"

# Search methods
text.find("World")    # 8 (index) or -1 if not found
text.replace("Hello", "Hi")  # "  Hi World  "

# Split and join
words = text.split()  # ["Hello", "World"]
" ".join(words)       # "Hello World"
```

### String Formatting
```python
name = "Alice"
age = 25

# f-strings (preferred)
f"Name: {name}, Age: {age}"

# format() method
"Name: {}, Age: {}".format(name, age)
"Name: {n}, Age: {a}".format(n=name, a=age)
```

---

## 📋 Lists

### List Creation
```python
# Empty list
my_list = []
my_list = list()

# With items
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# From range
list(range(5))        # [0, 1, 2, 3, 4]
list(range(1, 6))     # [1, 2, 3, 4, 5]
```

### List Indexing & Slicing
```python
my_list = [0, 1, 2, 3, 4, 5]

# Indexing
my_list[0]     # 0 (first)
my_list[-1]    # 5 (last)

# Slicing
my_list[1:4]   # [1, 2, 3]
my_list[:3]    # [0, 1, 2]
my_list[2:]    # [2, 3, 4, 5]
my_list[::-1]  # [5, 4, 3, 2, 1, 0] (reverse)
```

### Essential List Methods
```python
my_list = [1, 2, 3]

# Adding elements
my_list.append(4)        # [1, 2, 3, 4]
my_list.insert(0, 0)     # [0, 1, 2, 3, 4]
my_list.extend([5, 6])   # [0, 1, 2, 3, 4, 5, 6]

# Removing elements
my_list.pop()            # Removes and returns last
my_list.pop(0)           # Removes and returns first
my_list.remove(3)        # Removes first occurrence of 3

# Sorting and organizing
my_list.sort()           # Sort in place
my_list.reverse()        # Reverse in place
sorted(my_list)          # Returns new sorted list

# Information
len(my_list)             # Length
my_list.count(2)         # Count occurrences
my_list.index(3)         # Find index of first occurrence
```

### List Comprehension
```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(5)]        # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

## 🔗 Tuples

### Tuple Basics
```python
# Creation
my_tuple = (1, 2, 3)
my_tuple = 1, 2, 3      # Parentheses optional
single = (1,)           # Single element tuple

# Immutable - cannot change
# my_tuple[0] = 5       # TypeError

# Methods
my_tuple.count(2)       # Count occurrences
my_tuple.index(3)       # Find index
```

### Tuple Unpacking
```python
point = (10, 20)
x, y = point           # x=10, y=20

# Swapping
a, b = b, a

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers  # first=1, middle=[2,3,4], last=5
```

---

## 📚 Dictionaries

### Dictionary Basics
```python
# Creation
student = {"name": "Alice", "age": 20, "grade": "A"}
student = dict(name="Alice", age=20, grade="A")

# Access
student["name"]           # "Alice"
student.get("name")       # "Alice"
student.get("city", "Unknown")  # "Unknown" (default)

# Modify
student["age"] = 21       # Update
student["city"] = "NYC"   # Add new key
```

### Essential Dictionary Methods
```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Keys, values, items
student.keys()            # dict_keys(['name', 'age', 'grade'])
student.values()          # dict_values(['Alice', 20, 'A'])
student.items()           # dict_items([('name', 'Alice'), ...])

# Removing
student.pop("grade")      # Remove and return value
student.popitem()         # Remove and return last item
del student["age"]        # Delete key

# Updating
student.update({"city": "NYC", "major": "CS"})

# Checking
"name" in student         # True
len(student)              # Number of key-value pairs
```

---

## 🎯 Sets

### Set Basics
```python
# Creation
my_set = {1, 2, 3, 4, 5}
my_set = set([1, 2, 2, 3])  # {1, 2, 3} (duplicates removed)

# Adding/removing
my_set.add(6)             # Add single element
my_set.update([7, 8])     # Add multiple elements
my_set.remove(3)          # Remove (KeyError if not found)
my_set.discard(3)         # Remove (no error if not found)
```

### Set Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements)
set1 | set2               # {1, 2, 3, 4, 5, 6}
set1.union(set2)

# Intersection (common elements)
set1 & set2               # {3, 4}
set1.intersection(set2)

# Difference
set1 - set2               # {1, 2}
set1.difference(set2)

# Symmetric difference
set1 ^ set2               # {1, 2, 5, 6}
set1.symmetric_difference(set2)

# Subset/superset
{1, 2}.issubset(set1)     # True
set1.issuperset({1, 2})   # True
```

---

## 📁 File Handling

### Basic File Operations
```python
# Reading
with open("file.txt", "r") as file:
    content = file.read()        # Read entire file
    lines = file.readlines()     # Read all lines as list
    line = file.readline()       # Read one line

# Writing
with open("file.txt", "w") as file:
    file.write("Hello World")    # Write string
    file.writelines(["Line 1\n", "Line 2\n"])  # Write list

# Appending
with open("file.txt", "a") as file:
    file.write("New content")
```

---

## 🎯 Common Patterns

### Input Validation
```python
while True:
    try:
        age = int(input("Enter age: "))
        if 0 <= age <= 120:
            break
        print("Age must be 0-120")
    except ValueError:
        print("Please enter a number")
```

### Menu System
```python
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        # Option 1 code
        pass
    elif choice == "2":
        # Option 2 code
        pass
    elif choice == "3":
        break
    else:
        print("Invalid choice")
```

### List Processing
```python
# Find max/min
numbers = [3, 1, 4, 1, 5, 9]
max_num = max(numbers)
min_num = min(numbers)

# Sum and average
total = sum(numbers)
average = total / len(numbers)

# Filter and map
evens = [x for x in numbers if x % 2 == 0]
squares = [x**2 for x in numbers]
```

---

## 🚨 Common Exam Mistakes to Avoid

1. **Input conversion**: `age = int(input("Age: "))`
2. **Indentation**: Use 4 spaces consistently
3. **Comparison**: Use `==` not `=` for comparison
4. **List methods**: `append()` vs `extend()` vs `insert()`
5. **String immutability**: Strings don't change, methods return new strings
6. **Dictionary access**: Use `get()` to avoid KeyError
7. **Range function**: `range(5)` gives 0-4, not 1-5
8. **Boolean values**: `True`/`False` are capitalized

---

**💡 Pro Tip**: Practice these patterns until they become automatic!