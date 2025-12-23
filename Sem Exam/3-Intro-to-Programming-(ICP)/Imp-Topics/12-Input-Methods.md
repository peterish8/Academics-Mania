# 📥 Input Methods - Complete Guide

---

## 📌 Basic Input

> **Goal**: Read a single value from user.

```python
name = input()           # Returns string
print(f"Hello {name}")

# TEST (hardcoded)
name = "Alice"
print(f"Hello {name}")
```

---

## 📌 Input with Prompt

> **Goal**: Show message while asking for input.

```python
name = input("Enter name: ")  # Shows prompt
print(f"Hello {name}")

# TEST
name = "Bob"
print(f"Hello {name}")
```

---

## 📌 Convert Input to Integer

> **Goal**: Read a number (input() returns string, so we convert).

```python
n = int(input())    # String → Integer
print(n * 2)

# TEST
n = 5
print(n * 2)  # 10
```

---

## 📌 Convert Input to Float

> **Goal**: Read decimal number.

```python
price = float(input())
print(f"Total: {price * 1.18}")  # Add 18% tax

# TEST
price = 100.0
print(f"Total: {price * 1.18}")  # 118.0
```

---

## 📌 split() - Read Multiple Values

> **Goal**: Read multiple space-separated values as a list of strings.

```python
# Input: "hello world python"
words = input().split()
print(words)  # ['hello', 'world', 'python']

# TEST
line = "hello world python"
words = line.split()
print(words)
```

### Split by Custom Separator

```python
# Input: "apple,banana,cherry"
fruits = input().split(',')
print(fruits)  # ['apple', 'banana', 'cherry']

# TEST
line = "apple,banana,cherry"
fruits = line.split(',')
print(fruits)
```

---

## 📌 map() - Apply Function to Each Element

> **Goal**: Convert each element of a list using a function.

```python
# Syntax: map(function, iterable)

# Input: "1 2 3 4 5"
numbers = map(int, input().split())
print(list(numbers))  # [1, 2, 3, 4, 5]

# TEST
line = "1 2 3 4 5"
numbers = list(map(int, line.split()))
print(numbers)  # [1, 2, 3, 4, 5]
```

---

## 📌 The Magic Combo: map + int + split

> **Goal**: Read multiple integers in one line.

```python
# Input: "10 20 30"
a, b, c = map(int, input().split())
print(a, b, c)  # 10 20 30
print(a + b + c)  # 60

# TEST
line = "10 20 30"
a, b, c = map(int, line.split())
print(a, b, c)
print(a + b + c)
```

### As a List

```python
# Input: "1 2 3 4 5"
arr = list(map(int, input().split()))
print(arr)  # [1, 2, 3, 4, 5]
print(sum(arr))  # 15

# TEST
line = "1 2 3 4 5"
arr = list(map(int, line.split()))
print(arr)
print(sum(arr))
```

---

## 📌 Multiple Test Cases

> **Goal**: Handle T test cases in competitive programming.

```python
T = int(input())  # Number of test cases

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))

# TEST (simulated)
test_cases = [
    [3, [1, 2, 3]],
    [4, [10, 20, 30, 40]]
]
for n, arr in test_cases:
    print(sum(arr))  # 6, 100
```

---

## 📊 Quick Reference Table

| Pattern | Use Case | Example Input |
|---------|----------|---------------|
| `input()` | Single string | `hello` |
| `int(input())` | Single integer | `5` |
| `float(input())` | Single decimal | `3.14` |
| `input().split()` | Multiple strings | `a b c` |
| `map(int, input().split())` | Multiple integers | `1 2 3` |
| `list(map(int, input().split()))` | Integer list | `1 2 3 4 5` |
| `a, b = map(int, input().split())` | Unpack 2 integers | `10 20` |

---

## 📌 Common Exam Patterns

### Pattern 1: Read n, then n numbers
```python
n = int(input())
arr = list(map(int, input().split()))

# TEST
n = 5
arr = [1, 2, 3, 4, 5]
print(f"n={n}, arr={arr}")
```

### Pattern 2: Read T test cases
```python
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    # solve and print

# TEST
T = 2
test_data = [(3, [1,2,3]), (4, [1,2,3,4])]
for n, arr in test_data:
    print(sum(arr))
```

### Pattern 3: Read 2D matrix
```python
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# TEST
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix)
```

---

## 🧠 Key Points
- **input()** always returns string
- **int()** converts string to integer
- **split()** breaks string by spaces (or custom separator)
- **map()** applies function to each element
- **list()** converts map object to list
- `a, b, c = ...` unpacks into variables

---

[[11-Set|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | Next: None
