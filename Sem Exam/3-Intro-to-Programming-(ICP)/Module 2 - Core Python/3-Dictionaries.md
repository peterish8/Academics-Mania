# 📕 Dictionaries (Key-Value, Methods)

## 📌 1. Dictionary Basics
Dictionaries store data in `key: value` pairs. Keys must be unique and immutable (strings, numbers, tuples). Valid syntax uses curly braces `{}`.

```python
student = {
    "name": "Jane",
    "age": 22,
    "major": "Computer Science"
}

# Accessing values
print(student["name"])  # Jane
```

---

## 🛠️ 2. Common Methods
- `get(key, default)`: Safely access a key without error if missing.
- `keys()`: Returns all keys.
- `values()`: Returns all values.
- `items()`: Returns key-value pairs as tuples.
- `update(dict2)`: Merges another dictionary (overwrites existing keys).
- `pop(key)`: Removes key and returns value.

```python
# Safer access
print(student.get("gpa", "Not Available"))  # Output: Not Available

# Iterating
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## 🧠 Practice Exercises
1. **Word Frequency**: Given a string, count how often each word appears using a dictionary.
2. **Phonebook**: Create a simple phonebook application (add contact, search contact, delete contact) using a dictionary.
3. **Merge Dictionaries**: Write a script to merge two dictionaries. If a key exists in both, sum their values.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
