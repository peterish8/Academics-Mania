# 📋 Lists & List Comprehension

## 📌 1. creating & Accessing Lists
Lists are ordered, mutable collections of items.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(fruits[0])      # "apple"
print(numbers[-1])    # 5
```

---

## 🛠️ 2. List Methods
Common methods to modify lists:

- `append(item)`: Adds item to the end.
- `extend(iterable)`: Adds all items from iterable to the end.
- `insert(index, item)`: Inserts item at a specific index.
- `remove(value)`: Removes the first occurrence of value.
- `pop(index)`: Removes and returns item at index (default last).
- `sort()`: Sorts the list in place.
- `reverse()`: Reverses the list in place.

```python
nums = [3, 1, 4, 1, 5]
nums.append(9)
nums.sort()
print(nums) # [1, 1, 3, 4, 5, 9]
```

---

## ⚡ 3. List Comprehension
A concise way to create lists.

**Syntax**: `[expression for item in iterable if condition]`

```python
# Standard way
squares = []
for x in range(10):
    squares.append(x**2)

# List Comprehension way (Better!)
squares = [x**2 for x in range(10)]

# With conditional logic
evens = [x for x in range(20) if x % 2 == 0]
```

---

## 🧠 Practice Exercises
1. **Duplicate Remover**: Write a function that takes a list and returns a new list with duplicates removed (try using a loop first, then sets).
2. **List Reverser**: Reverse a list without using `.reverse()` or `[::-1]`.
3. **Squared Evens**: Create a list of squares of even numbers from 1 to 50 using list comprehension.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
