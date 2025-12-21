# Print Function

#module1 #python-basics #print #output

---

## What is print()?

The `print()` function displays output to the console/screen. It's the most basic way to show results in Python.

---

## Basic Syntax

```python
print(value1, value2, ..., sep=' ', end='\n')
```

**Parameters:**
- `value1, value2, ...`: Values to print (can be multiple)
- `sep`: Separator between values (default: space)
- `end`: What to print at the end (default: newline)

---

## Basic Examples

```python
# Simple print
print("Hello, World!")
# Output: Hello, World!

# Print variables
name = "Alice"
print(name)
# Output: Alice

# Print multiple values
print("Name:", name, "Age:", 20)
# Output: Name: Alice Age: 20
```

---

## Print with Different Data Types

```python
# Strings
print("Python Programming")

# Numbers
print(42)
print(3.14)

# Boolean
print(True)
print(False)

# Mixed types
print("Age:", 25, "Height:", 5.8, "Student:", True)
# Output: Age: 25 Height: 5.8 Student: True
```

---

## Customizing Output

### Using sep Parameter
```python
# Default separator (space)
print("A", "B", "C")
# Output: A B C

# Custom separator
print("A", "B", "C", sep="-")
# Output: A-B-C

print("2024", "12", "25", sep="/")
# Output: 2024/12/25

# No separator
print("Hello", "World", sep="")
# Output: HelloWorld
```

### Using end Parameter
```python
# Default end (newline)
print("First line")
print("Second line")
# Output:
# First line
# Second line

# Custom end
print("Hello", end=" ")
print("World")
# Output: Hello World

# No newline
print("Loading", end="...")
print("Done")
# Output: Loading...Done
```

---

## Printing Special Characters

```python
# Newline
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# Tab
print("Name:\tAlice")
# Output: Name:    Alice

# Quotes
print("She said, \"Hello!\"")
# Output: She said, "Hello!"

print('He said, "Hi there!"')
# Output: He said, "Hi there!"
```

---

## Print with Expressions

```python
# Arithmetic
print(5 + 3)        # Output: 8
print(10 - 4)       # Output: 6
print(3 * 7)        # Output: 21

# String operations
print("Hello" + " " + "World")  # Output: Hello World
print("Python" * 3)             # Output: PythonPythonPython

# Variables in expressions
x = 10
y = 5
print("Sum:", x + y)            # Output: Sum: 15
```

---

## Important Points

> [!NOTE] **Key Features**
> - `print()` automatically converts values to strings
> - Multiple values are separated by spaces by default
> - Each `print()` ends with a newline by default
> - Can print any data type

> [!TIP] **Best Practices**
> - Use descriptive text with values: `print("Age:", age)`
> - Use `sep` and `end` parameters for formatting
> - Combine with variables for dynamic output

> [!WARNING] **Common Mistakes**
> - Forgetting quotes around strings
> - Not using commas between multiple values
> - Confusing `print()` with `return` in functions

---

## Related Topics
- [[Input-Function]] - Getting user input
- [[Variables]] - Storing values to print
- [[String-Formatting-f-strings]] - Advanced formatting

---

## Practice Questions

1. Print your name and age on the same line
2. Print three numbers separated by dashes
3. Print "Loading..." without a newline, then "Complete!" on the same line

```python
# Practice solutions
print("Name: John, Age: 20")
print(1, 2, 3, sep="-")
print("Loading...", end="")
print("Complete!")
```

**Next**: Learn about the [[Input-Function]] →