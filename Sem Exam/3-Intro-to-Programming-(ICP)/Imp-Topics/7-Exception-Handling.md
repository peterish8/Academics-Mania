# 7️⃣ Exception Handling

---

## 📌 Errors vs Exceptions

| Type | When | Example |
|------|------|---------|
| **Syntax Error** | Code writing (before running) | `print "hello"` |
| **Exception** | During execution (runtime) | Division by zero |

```python
# Syntax Error - detected before running
# if x == 5  # Missing colon

# Exception - happens during running
x = 10 / 0  # ZeroDivisionError
```

---

## 📌 Common Built-in Exceptions

| Exception | Cause |
|-----------|-------|
| **ZeroDivisionError** | Division by zero |
| **TypeError** | Wrong type operation |
| **ValueError** | Wrong value |
| **IndexError** | List index out of range |
| **KeyError** | Dict key not found |
| **FileNotFoundError** | File doesn't exist |
| **AttributeError** | Object has no such attribute |

---

## 📌 try-except Block

> **Goal**: Handle exceptions gracefully without crashing.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program continues...")  # Still runs!
```

---

## 📌 try-except-else-finally

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")  # Runs if NO exception
finally:
    print("Execution complete")  # ALWAYS runs
```

### Flow:
1. **try**: Code that might fail
2. **except**: Handle specific exceptions
3. **else**: Runs if NO exception occurred
4. **finally**: ALWAYS runs (cleanup code)

---

## 📌 Multiple except Blocks

> **Goal**: Handle different exceptions differently.

```python
try:
    lst = [1, 2, 3]
    print(lst[10])     # IndexError
    x = 10 / 0         # ZeroDivisionError
except IndexError:
    print("Index out of range!")
except ZeroDivisionError:
    print("Division by zero!")
except Exception as e:  # Catch-all
    print(f"Error: {e}")
```

---

## 📌 Raising Exceptions

> **Goal**: Manually raise an exception using `raise`.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

# TEST
try:
    set_age(-5)
except ValueError as e:
    print(e)  # "Age cannot be negative!"
```

---

## 📌 User-Defined Exceptions

> **Goal**: Create custom exception classes.

```python
class InvalidAgeError(Exception):  # Custom exception
    def __init__(self, age, message="Age must be 0-120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return True

# TEST
try:
    validate_age(150)
except InvalidAgeError as e:
    print(f"Error: {e.message}, got {e.age}")
```

---

## 📊 Summary

| Keyword | Purpose |
|---------|---------|
| **try** | Code that might raise exception |
| **except** | Handle the exception |
| **else** | Runs if no exception |
| **finally** | Always runs (cleanup) |
| **raise** | Manually raise exception |

---

## 🧠 Key Points
- **try-except** prevents program crash
- **finally** always runs (even if exception occurs)
- **raise** to manually throw exceptions
- Create custom exceptions by inheriting `Exception`

---

[[6-File-Handling|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[8-List|Next →]]
