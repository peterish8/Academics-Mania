# 1️⃣1️⃣ Set

---

## 📌 Introduction

> **Definition**: Unordered collection of **unique** elements.

| Property | Description |
|----------|-------------|
| **Unique** | No duplicate elements |
| **Unordered** | No index, no guaranteed order |
| **Mutable** | Can add/remove elements |

---

## 📌 Creating Sets

```python
# Different ways
empty = set()  # NOT {} (that's empty dict!)
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}

# From list (removes duplicates!)
lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)
print(unique)  # {1, 2, 3}

# From string
chars = set("hello")
print(chars)  # {'h', 'e', 'l', 'o'}
```

---

## 📌 Adding Elements

### add() - Add single element
```python
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

s.add(2)  # Already exists, no change
print(s)  # {1, 2, 3, 4}
```

---

## 📌 Removing Elements

### remove() - Remove (error if not found)
```python
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}
# s.remove(10)  # KeyError!
```

### discard() - Remove (no error if not found)
```python
s = {1, 2, 3}
s.discard(2)
s.discard(10)  # No error
print(s)  # {1, 3}
```

### pop() - Remove arbitrary element
```python
s = {1, 2, 3}
val = s.pop()  # Random element
print(val, s)
```

---

## 📌 Set Operations

### Union (|) - All elements from both
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)         # {1, 2, 3, 4, 5}
print(a.union(b))    # Same
```

### Intersection (&) - Common elements
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)              # {2, 3}
print(a.intersection(b))  # Same
```

### Difference (-) - Elements in a but not in b
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)            # {1}
print(a.difference(b))  # Same
```

### Symmetric Difference (^) - Elements in either, but not both
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)                       # {1, 4}
print(a.symmetric_difference(b))   # Same
```

---

## 📊 Set Operations Summary

| Operation | Symbol | Method | Result |
|-----------|--------|--------|--------|
| **Union** | `\|` | `union()` | All elements |
| **Intersection** | `&` | `intersection()` | Common |
| **Difference** | `-` | `difference()` | In A, not in B |
| **Symmetric Diff** | `^` | `symmetric_difference()` | In either, not both |

---

## 📌 Visual Example

```
A = {1, 2, 3}
B = {2, 3, 4}

A | B = {1, 2, 3, 4}     Union
A & B = {2, 3}           Intersection  
A - B = {1}              Difference
A ^ B = {1, 4}           Symmetric Difference
```

---

## 📊 Methods Summary

| Method | Purpose |
|--------|---------|
| `add(x)` | Add element |
| `remove(x)` | Remove (error if not found) |
| `discard(x)` | Remove (no error) |
| `pop()` | Remove random element |
| `union(s)` | All elements from both |
| `intersection(s)` | Common elements |
| `difference(s)` | In self, not in s |

---

## 🧠 Key Points
- **No duplicates** - automatically removed
- **No index** - can't do `set[0]`
- Use `discard()` for safe removal
- Use `set()` to remove duplicates from list

---

Back to: [[Imp-Topics-Hub|ICP Topics Hub]]
