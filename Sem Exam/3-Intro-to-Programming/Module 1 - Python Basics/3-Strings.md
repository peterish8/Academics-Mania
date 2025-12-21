# 🧶 Strings (Methods, Slicing, f-strings)

## 📌 1. String Basics
Strings are immutable sequences of characters.

### **Indexing**
Access individual characters using square brackets `[]`. Indexing starts at 0.
```python
s = "Python"
print(s[0])  # 'P'
print(s[-1]) # 'n' (Last character)
```

### **Slicing**
Get a substring using `[start:stop:step]`.
- `start`: Inclusive (default 0)
- `stop`: Exclusive (default length)
- `step`: Increment (default 1)

```python
text = "Hello, World!"
print(text[0:5])   # "Hello"
print(text[7:])    # "World!"
print(text[::-1])  # "!dlroW ,olleH" (Reverse string)
```

---

## 🛠️ 2. String Methods
Common built-in methods:

- **Searching**:
  - `find(substring)`: Returns index of first occurrence (or -1 if not found).
  - `count(substring)`: Returns number of occurrences.
  
- **Transformation**:
  - `upper()`, `lower()`, `capitalize()`
  - `strip()`: Removes leading/trailing whitespace.
  - `replace(old, new)`: Replaces occurrences of a substring.
  - `split(delimiter)`: Splits string into a list.
  - `join(iterable)`: Joins elements of an iterable into a string.

```python
s = "  data science  "
print(s.strip().upper())  # "DATA SCIENCE"
print("apple,banana,grape".split(",")) # ['apple', 'banana', 'grape']
```

---

## 🎨 3. String Formatting (f-strings)
Introduced in Python 3.6, f-strings are the preferred way to format strings.

```python
name = "Alice"
age = 25
score = 95.5

# Basic f-string
print(f"Name: {name}, Age: {age}")

# Expressions inside f-strings
print(f"Next year, you will be {age + 1}.")

# Formatting decimals
print(f"Score: {score:.2f}")  # 95.50
```

---

## 🧠 Practice Exercises
1. **Email Slicer**: Extract the username and domain from an email address (e.g., `user@example.com` -> `user`, `example.com`).
2. **Word Counter**: Take a sentence input and count the number of words using `split()`.
3. **Vowel Replacer**: Replace all vowels in a string with `*`.

---
> [[Sem Exam/3-Intro-to-Programming/Module 1 - Python Basics/README|🔙 Back to Module 1 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
