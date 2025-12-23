# 🔟 Dictionary

---

## 📌 Introduction

> **Definition**: Unordered collection of key-value pairs. Keys must be unique.

| Property | Description |
|----------|-------------|
| **Key-Value** | Each item has a key and value |
| **Mutable** | Can add, remove, modify |
| **No Duplicates** | Keys must be unique |
| **Unordered** | No guaranteed order (Python 3.7+ maintains insertion order) |

---

## 📌 Creating Dictionaries

```python
# Different ways
empty = {}
student = {"name": "Alice", "age": 20, "grade": "A"}
mixed = {1: "one", "two": 2, (1,2): "tuple key"}

# Using dict()
d = dict(name="Bob", age=25)
```

---

## 📌 Accessing Values

```python
student = {"name": "Alice", "age": 20}

# Using key
print(student["name"])  # Alice

# Using get() - safe, returns None if not found
print(student.get("name"))        # Alice
print(student.get("address"))     # None
print(student.get("address", "N/A"))  # N/A (default)
```

---

## 📌 Updating Values

```python
student = {"name": "Alice", "age": 20}

# Modify existing
student["age"] = 21
print(student)  # {'name': 'Alice', 'age': 21}

# Add new
student["grade"] = "A"
print(student)  # {'name': 'Alice', 'age': 21, 'grade': 'A'}
```

---

## 📌 Adding & Deleting Key-Value Pairs

```python
d = {"a": 1, "b": 2}

# Add
d["c"] = 3
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Delete using del
del d["a"]
print(d)  # {'b': 2, 'c': 3}

# Delete using pop (returns value)
val = d.pop("b")
print(val, d)  # 2, {'c': 3}
```

---

## 📌 Dictionary Methods

### keys() - Get all keys
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())    # dict_keys(['a', 'b', 'c'])
print(list(d.keys()))  # ['a', 'b', 'c']
```

### values() - Get all values
```python
print(d.values())  # dict_values([1, 2, 3])
print(list(d.values()))  # [1, 2, 3]
```

### items() - Get all key-value pairs
```python
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Useful for iteration
for key, value in d.items():
    print(f"{key}: {value}")
```

### get() - Safe access
```python
d = {"name": "Alice"}
print(d.get("name"))       # Alice
print(d.get("age", 0))     # 0 (default)
```

### update() - Update with another dict
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 20, 'c': 3}
```

### pop() - Remove and return
```python
d = {"a": 1, "b": 2}
val = d.pop("a")
print(val, d)  # 1, {'b': 2}
```

---

## 📊 Methods Summary

| Method | Purpose | Returns |
|--------|---------|---------|
| `keys()` | All keys | dict_keys |
| `values()` | All values | dict_values |
| `items()` | All key-value pairs | dict_items |
| `get(k, default)` | Get value safely | Value or default |
| `update(d)` | Merge dictionaries | None |
| `pop(k)` | Remove and return | Value |

---

## 🧠 Key Points
- **Keys must be unique** and hashable (strings, numbers, tuples)
- Use `get()` to avoid KeyError
- Use `items()` to iterate key-value pairs
- **Mutable** = Can add/remove/modify

---

[[9-Tuple|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[11-Set|Next →]]
