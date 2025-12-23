# 8️⃣ List

---

## 📌 Introduction

> **Definition**: Ordered, mutable collection that allows duplicate elements.

| Property | Description |
|----------|-------------|
| **Ordered** | Elements maintain insertion order |
| **Mutable** | Can add, remove, modify elements |
| **Indexed** | Access by index (0-based) |
| **Duplicates** | Allowed |

---

## 📌 Creating Lists

```python
# Different ways to create lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

# Using list()
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]
```

---

## 📌 Accessing Elements

```python
lst = [10, 20, 30, 40, 50]

# Positive indexing
print(lst[0])   # 10 (first)
print(lst[2])   # 30

# Negative indexing
print(lst[-1])  # 50 (last)
print(lst[-2])  # 40

# Slicing
print(lst[1:4])  # [20, 30, 40]
print(lst[:3])   # [10, 20, 30]
print(lst[2:])   # [30, 40, 50]
```

---

## 📌 Updating Elements

```python
lst = [1, 2, 3, 4, 5]

lst[0] = 100      # Change first element
print(lst)        # [100, 2, 3, 4, 5]

lst[1:3] = [200, 300]  # Change slice
print(lst)        # [100, 200, 300, 4, 5]
```

---

## 📌 Deleting Elements

```python
lst = [1, 2, 3, 4, 5]

del lst[0]        # Delete by index
print(lst)        # [2, 3, 4, 5]

lst.remove(3)     # Delete by value
print(lst)        # [2, 4, 5]

popped = lst.pop()  # Remove & return last
print(popped)       # 5
```

---

## 📌 List Methods

### append() - Add to end
```python
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]
```

### insert() - Add at specific index
```python
lst = [1, 2, 4]
lst.insert(2, 3)  # Insert 3 at index 2
print(lst)  # [1, 2, 3, 4]
```

### extend() - Add multiple elements
```python
lst = [1, 2]
lst.extend([3, 4, 5])
print(lst)  # [1, 2, 3, 4, 5]
```

### remove() - Remove by value
```python
lst = [1, 2, 3, 2]
lst.remove(2)  # Removes first occurrence
print(lst)  # [1, 3, 2]
```

### pop() - Remove by index (returns value)
```python
lst = [1, 2, 3]
val = lst.pop(1)  # Remove index 1
print(val, lst)   # 2, [1, 3]
```

### sort() - Sort in-place
```python
lst = [3, 1, 4, 1, 5]
lst.sort()
print(lst)  # [1, 1, 3, 4, 5]

lst.sort(reverse=True)
print(lst)  # [5, 4, 3, 1, 1]
```

### reverse() - Reverse in-place
```python
lst = [1, 2, 3]
lst.reverse()
print(lst)  # [3, 2, 1]
```

---

## 📊 Methods Summary

| Method | Purpose | Returns |
|--------|---------|---------|
| `append(x)` | Add to end | None |
| `insert(i, x)` | Add at index | None |
| `extend(lst)` | Add all from list | None |
| `remove(x)` | Remove first x | None |
| `pop(i)` | Remove at index | Value |
| `sort()` | Sort ascending | None |
| `reverse()` | Reverse order | None |

---

## 🧠 Key Points
- **Mutable** = Can modify after creation
- **append()** adds one, **extend()** adds many
- **pop()** returns value, **remove()** doesn't
- **sort()** and **reverse()** modify in-place

---

[[7-Exception-Handling|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[9-Tuple|Next →]]
