# 📦 Tuples & Unpacking

## 📌 1. Tuple Basics
Tuples are ordered, **immutable** collections. Once created, elements cannot be changed, added, or removed.

```python
point = (10, 20)
colors = ("red", "green", "blue")
single_item = (1,)  # Note the comma!

# Accessing is same as lists
print(point[0])  # 10
```

### **Why use Tuples?**
- Faster than lists.
- Data integrity (cannot be accidentally modified).
- Valid keys for dictionaries (because they are immutable).

---

## 🎁 2. Tuple Unpacking
Assigning tuple elements to variables in a single line.

```python
coordinates = (4, 5)
x, y = coordinates
print(f"x: {x}, y: {y}")

# Swapping variables
a = 10
b = 20
a, b = b, a
print(a, b)  # 20, 10
```

### **Using Asterisk `*`**
Capture remaining items.

```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green) # apple
print(red)   # ['cherry', 'strawberry', 'raspberry']
```

---

## 🧠 Practice Exercises
1. **Coordinate Systems**: Create a list of tuples representing (x, y) coordinates and write a loop to print them formatted.
2. **Tuple Return**: Write a function `get_stats(numbers_list)` that returns a tuple containing `(min, max, average)`.
3. **Unpacking Mastery**: Given nested tuple `data = ('John', 25, (90, 85, 95))`, unpack it into `name`, `age`, and a list of `scores`.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
