# 9️⃣ Tuple

---

## 📌 Introduction

> **Definition**: Ordered, **immutable** collection that allows duplicate elements.

| Property | Description |
|----------|-------------|
| **Ordered** | Elements maintain insertion order |
| **Immutable** | ❌ Cannot modify after creation |
| **Indexed** | Access by index (0-based) |
| **Duplicates** | Allowed |

---

## 📌 Creating Tuples

```python
# Different ways
empty = ()
single = (1,)  # Note the comma!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14)

# Without parentheses (tuple packing)
coords = 10, 20, 30
print(type(coords))  # <class 'tuple'>

# Using tuple()
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

---

## 📌 Accessing Elements

```python
t = (10, 20, 30, 40, 50)

# Indexing
print(t[0])    # 10
print(t[-1])   # 50

# Slicing
print(t[1:4])  # (20, 30, 40)
```

---

## 📌 Tuple is Immutable!

```python
t = (1, 2, 3)

# This will raise an error!
# t[0] = 100  # TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
t = t + (4, 5)  # (1, 2, 3, 4, 5)
```

---

## 📌 Tuple Packing & Unpacking

### Packing
> **Goal**: Combine multiple values into a tuple.

```python
# Packing
point = 10, 20, 30
print(point)  # (10, 20, 30)
```

### Unpacking
> **Goal**: Extract tuple values into variables.

```python
# Unpacking
point = (10, 20, 30)
x, y, z = point
print(x, y, z)  # 10 20 30

# Swap using unpacking
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
```

---

## 📌 Tuple Methods

### count() - Count occurrences
```python
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))  # 3
```

### index() - Find position
```python
t = (10, 20, 30, 40)
print(t.index(30))  # 2
```

---

## 📊 Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| **Syntax** | `()` | `[]` |
| **Mutable** | ❌ No | ✅ Yes |
| **Speed** | Faster | Slower |
| **Memory** | Less | More |
| **Use case** | Fixed data | Changing data |

---

## 📌 When to Use Tuple?

- **Fixed data** that shouldn't change
- **Dictionary keys** (lists can't be keys!)
- **Function returns** (multiple values)
- **Faster** than lists for iteration

```python
# Multiple return values
def get_coordinates():
    return 10, 20  # Returns tuple

x, y = get_coordinates()
```

---

## 🧠 Key Points
- **Immutable** = Cannot modify after creation
- Use comma for single-element: `(1,)` not `(1)`
- **Unpacking**: `x, y, z = tuple`
- Faster and memory-efficient than lists

---

Back to: [[Imp-Topics-Hub|ICP Topics Hub]]
