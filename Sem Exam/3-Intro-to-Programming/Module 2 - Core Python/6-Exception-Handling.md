# ⚠️ Exception Handling

## 📌 1. Basic Structure (try...except)
Prevent your program from crashing when errors occur.

```python
try:
    # Code that might raise an error
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
```

---

## 🛡️ 2. `else` and `finally`
- **`else`**: Runs if **no exceptions** occurred in the try block.
- **`finally`**: Runs **always**, regardless of errors (good for cleanup like closing files).

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
    f.close()
finally:
    print("Execution complete.")
```

---

## 🚫 3. Common Exceptions
- `ValueError`: Function receives argument of correct type but invalid value (e.g., `int('hello')`).
- `TypeError`: Operation applied to object of incorrect type (e.g., `'5' + 5`).
- `IndexError`: List index out of range.
- `KeyError`: Dictionary key not found.
- `NameError`: Variable not defined.

---

## 🧠 Practice Exercises
1. **Safe Input**: Write a function `get_integer()` that repeatedly asks the user for a number until a valid integer is entered.
2. **List Safety**: Write a program that asks for an index and prints the element from a list, handling the case where the index is too large.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
