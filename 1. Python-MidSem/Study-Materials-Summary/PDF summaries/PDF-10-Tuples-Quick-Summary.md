# PDF 10: Tuples in Python - Quick Summary

## 🎯 Tuple Essentials

### Definition & Key Property
- **Tuple**: Ordered, **IMMUTABLE** collection of elements
- **Syntax**: `t = (1, 2, 3)` or `t = 1, 2, 3`
- **Key Difference from Lists**: Cannot be changed after creation

### Creation Patterns
```python
t1 = ()                    # Empty tuple
t2 = (1, 2, 3)            # With parentheses
t3 = 1, 2, 3              # Without parentheses
t4 = (10,)                # Single element (comma required!)
t5 = (1, (2, 3), 4)       # Nested tuple
t6 = (10, "apple", 3.14)  # Mixed data types
```

### Accessing Elements
```python
t = (10, 20, 30, 40, 50)
t[0]      # 10 (first element)
t[-1]     # 50 (last element)
t[1:4]    # (20, 30, 40) (slicing)
t[::2]    # (10, 30, 50) (step slicing)
```

## 🔥 Tuple Operations

| Operation | Syntax | Example |
|-----------|--------|---------|
| **Concatenation** | `+` | `(1,2) + (3,4)` → `(1,2,3,4)` |
| **Repetition** | `*` | `(1,2) * 3` → `(1,2,1,2,1,2)` |
| **Membership** | `in` | `2 in (1,2,3)` → `True` |
| **Length** | `len()` | `len((1,2,3))` → `3` |

## ⚡ Built-in Functions & Methods

### Functions
```python
t = (5, 10, 15, 20)
len(t)    # 4
min(t)    # 5
max(t)    # 20
sum(t)    # 50
```

### Methods (Only 2!)
```python
t = (10, 20, 10, 30, 10)
t.count(10)    # 3 (count occurrences)
t.index(30)    # 3 (first index of value)
```

## 🎯 Packing & Unpacking

### Packing (Create tuple)
```python
t = 10, 20, 30        # Packed into tuple
coordinates = x, y    # Pack variables
```

### Unpacking (Extract values)
```python
t = (10, 20, 30)
a, b, c = t          # a=10, b=20, c=30

# Extended unpacking with *
t = (1, 2, 3, 4, 5)
first, *middle, last = t    # first=1, middle=[2,3,4], last=5
```

## ⚠️ Immutability Rules

### Cannot Change
```python
t = (1, 2, 3)
# t[0] = 100        # ERROR: TypeError
# t.append(4)       # ERROR: No such method
# del t[1]          # ERROR: Cannot delete
```

### Exception: Mutable Objects Inside
```python
t = (1, [2, 3], 4)
t[1][0] = 99         # OK: Modifying list inside tuple
print(t)             # (1, [99, 3], 4)
```

## 🔥 Common Exam Patterns

### 1. Single Element Tuple
```python
# Wrong way
t = (10)      # This is just an integer!
# Right way  
t = (10,)     # Comma makes it a tuple
```

### 2. Tuple vs List Comparison
| Feature | Tuple | List |
|---------|-------|------|
| **Mutability** | Immutable | Mutable |
| **Syntax** | `()` | `[]` |
| **Methods** | 2 (count, index) | Many (append, remove, etc.) |
| **Performance** | Faster | Slower |
| **Use Case** | Fixed data | Changing data |

### 3. Multiple Assignment
```python
# Swap variables
a, b = 10, 20
a, b = b, a          # Now a=20, b=10

# Function returning multiple values
def get_name_age():
    return "Alice", 25
name, age = get_name_age()
```

## ⚡ Quick Tips
- **Parentheses optional** for creation (comma is key)
- **Single element**: Must include comma `(item,)`
- **Immutable**: Cannot change, but can contain mutable objects
- **Faster than lists** for read-only operations
- **Perfect for coordinates**: `point = (x, y)`

---
*Previous: [[PDF-9-Lists-Quick-Summary]] | Next: [[PDF-11-Dictionaries-Quick-Summary]]*

#tuples #python #immutable #data-structures #exam-prep