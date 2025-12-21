# PDF 9: Lists in Python - Quick Summary

## 🎯 List Essentials

### Definition & Properties
- **List**: Ordered, mutable collection of items
- **Syntax**: `my_list = [item1, item2, item3]`
- **Key Properties**: Ordered, Mutable, Allows duplicates, Indexed (starts at 0)

### Indexing & Access
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # "apple" (first item)
print(fruits[-1])   # "cherry" (last item)
print("apple" in fruits)  # True (membership test)
```

## 🔥 Essential Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `append(item)` | Add to end | `list.append("new")` |
| `insert(index, item)` | Add at position | `list.insert(0, "first")` |
| `extend(iterable)` | Add multiple items | `list.extend([1,2,3])` |
| `remove(item)` | Remove first occurrence | `list.remove("item")` |
| `pop(index)` | Remove & return by index | `item = list.pop()` |
| `count(item)` | Count occurrences | `list.count("item")` |
| `sort()` | Sort in place | `list.sort()` |
| `reverse()` | Reverse in place | `list.reverse()` |

### Key Differences
- **append()** vs **extend()**: `append([1,2])` adds list as single item, `extend([1,2])` adds items individually
- **remove()** vs **pop()**: `remove()` by value, `pop()` by index and returns item
- **del** vs **pop()**: `del` doesn't return, `pop()` returns removed item

## ⚡ List Comprehension
```python
# Basic syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(5)]           # [0,1,4,9,16]
evens = [x for x in range(10) if x % 2 == 0] # [0,2,4,6,8]
upper = [w.upper() for w in words]           # Convert to uppercase
```

## 🎯 Common Exam Patterns

### 1. Remove Duplicates (Keep First)
```python
unique = []
for item in original:
    if item not in unique:
        unique.append(item)
```

### 2. Find Most Frequent Element
```python
most_frequent = nums[0]
highest_count = 0
for n in nums:
    count = nums.count(n)
    if count > highest_count:
        highest_count = count
        most_frequent = n
```

### 3. Second Largest Without Built-ins
```python
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
unique.sort()
second_largest = unique[-2]
```

### 4. Even Numbers Filter
```python
evens = [n for n in nums if n % 2 == 0]
```

## ⚠️ Key Points
- **Mutable**: Can change after creation
- **Zero-indexed**: First element at index 0
- **Negative indexing**: -1 is last element
- **Slicing**: `list[start:end:step]`
- **Error handling**: `remove()` raises ValueError if item not found

## 🔥 Quick Operations
```python
# Multiple operations in sequence
cart = ["milk", "bread"]
cart.extend(["jam", "cheese"])    # Add multiple
cart.insert(0, "honey")           # Add at start
cart.remove("bread")              # Remove by value
cart.pop()                        # Remove last
cart.sort()                       # Sort alphabetically
```

---
*Previous: [[PDF-8-String-Functions-Quick-Summary]] | Next: [[PDF-10-Tuples-Quick-Summary]]*

#lists #python #data-structures #exam-prep #list-comprehension