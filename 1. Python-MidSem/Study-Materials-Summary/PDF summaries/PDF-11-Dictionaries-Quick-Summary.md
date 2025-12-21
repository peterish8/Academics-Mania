# PDF 11: Dictionaries in Python - Quick Summary

## 🎯 Dictionary Essentials

### Definition & Properties
- **Dictionary**: Unordered, mutable collection of key-value pairs
- **Keys**: Must be unique and immutable (string, number, tuple)
- **Values**: Can be anything (any data type)
- **Ordered**: Since Python 3.7+ (insertion order preserved)

### Creation & Access
```python
# Creation
d = {}                                    # Empty
student = {"name": "Ravi", "age": 20}    # With values
d2 = dict(name="Priya", age=22)          # Using dict()

# Access
print(student["name"])           # Direct access (KeyError if missing)
print(student.get("age"))        # Safe access (None if missing)
print(student.get("roll", 0))    # With default value
```

## 🔥 Essential Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `get(key, default)` | Safe access | `d.get("key", 0)` |
| `pop(key)` | Remove & return by key | `value = d.pop("key")` |
| `popitem()` | Remove & return last pair | `key, value = d.popitem()` |
| `update(dict)` | Merge dictionaries | `d1.update(d2)` |
| `keys()` | Get all keys | `d.keys()` |
| `values()` | Get all values | `d.values()` |
| `items()` | Get key-value pairs | `d.items()` |

### Key Operations
```python
# Add/Update
student["city"] = "Delhi"        # Add new key
student["age"] = 21              # Update existing

# Check membership
print("name" in student)         # True
print("roll" not in student)     # True

# Length
print(len(student))              # Number of key-value pairs
```

## ⚡ Looping Patterns

```python
student = {"name": "Ravi", "age": 20, "course": "Python"}

# Loop keys only
for key in student:
    print(key)

# Loop values only  
for value in student.values():
    print(value)

# Loop both key & value
for key, value in student.items():
    print(key, ":", value)
```

## 🎯 Common Exam Algorithms

### 1. Word Frequency Counter
```python
sentence = "apple banana apple orange banana apple"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
```

### 2. Sorting Dictionary
```python
# Sort by keys
sorted_dict = dict(sorted(d.items()))

# Sort by values
sorted_keys = sorted(d, key=d.get)
sorted_by_values = {k: d[k] for k in sorted_keys}

# Or using lambda
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
```

### 3. Find Min/Max in Nested Dict
```python
students = {
    "Ravi": {"Math": 80, "Science": 70},
    "Priya": {"Math": 85, "Science": 95}
}

# Find student with max total
max_marks = 0
topper = ""
for name, subjects in students.items():
    total = sum(subjects.values())
    if total > max_marks:
        max_marks = total
        topper = name
```

### 4. Remove Duplicate Values
```python
d = {"a": 1, "b": 2, "c": 1, "d": 3}
unique = {}
for k, v in d.items():
    if v not in unique.values():
        unique[k] = v
```

## 🔥 Nested Dictionaries

```python
students = {
    101: {"name": "Ravi", "age": 20},
    102: {"name": "Priya", "age": 22}
}

# Access nested values
print(students[101]["name"])     # "Ravi"

# Add to nested
students[101]["city"] = "Delhi"
```

## ⚠️ Key Points

### get() vs Direct Access
- `dict[key]` → Raises KeyError if key missing
- `dict.get(key)` → Returns None if key missing
- `dict.get(key, default)` → Returns default if key missing

### pop() vs popitem()
- `pop(key)` → Remove specific key, return value
- `popitem()` → Remove last inserted pair, return (key, value)

### Key Requirements
- Keys must be **immutable**: string, number, tuple ✓
- Keys must be **unique**: No duplicates
- Lists/dicts cannot be keys ✗

## 🎯 Quick Patterns
```python
# Multiple operations
student = {"name": "Ravi"}
student.update({"age": 20, "city": "Delhi"})    # Add multiple
removed = student.pop("city")                    # Remove by key
last_item = student.popitem()                    # Remove last

# Comprehension
squares = {x: x**2 for x in range(5)}           # {0:0, 1:1, 2:4, 3:9, 4:16}
```

---
*Previous: [[PDF-10-Tuples-Quick-Summary]] | Next: [[PDF-12-Sets-Quick-Summary]]*

#dictionaries #python #key-value #data-structures #exam-prep