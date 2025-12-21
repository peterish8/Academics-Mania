# 🎱 Sets (Unordered, Operations)

## 📌 1. Creating Sets
Sets are unordered collections of unique elements.

```python
# Create with curly braces
my_set = {1, 2, 3, 3, 2}
print(my_set)  # {1, 2, 3} (Duplicates removed automatically)

# Empty set (MUST use set(), not {})
empty = set()
```

---

## 🛠️ 2. Adding & Removing
- `add(item)`: Adds an element.
- `update(iterable)`: Adds multiple elements.
- `remove(item)`: Removes item (raises KeyError if missing).
- `discard(item)`: Removes item (no error if missing).
- `pop()`: Removes and returns a random element.
- `clear()`: Removes all elements.

---

## 🔗 3. Set Operations
Powerful mathematical operations.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (All elements from both)
print(A | B)        # {1, 2, 3, 4, 5, 6}
print(A.union(B))

# Intersection (Common elements)
print(A & B)        # {3, 4}
print(A.intersection(B))

# Difference (Elements in A but not B)
print(A - B)        # {1, 2}

# Symmetric Difference (Elements in either A or B, but not both)
print(A ^ B)        # {1, 2, 5, 6}
```

---

## 🧠 Practice Exercises
1. **Unique Visitor Counter**: Simulate a list of visitor IPs (with duplicates) and output the count of *unique* visitors.
2. **Common Interests**: Given two lists of hobbies for two friends, use sets to find common hobbies and unique hobbies.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
