# For Loops

#module1 #control-flow #loops #for #iteration

---

## What are For Loops?

For loops repeat a block of code a specific number of times or iterate through a sequence (like a list or string). Use for loops when you know how many times to repeat.

---

## Basic For Loop with range()

### Simple range()
```python
# Loop 5 times (0 to 4)
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Loop with custom start and end
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Loop with step
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

### range() Parameters
```python
# range(stop) - from 0 to stop-1
for i in range(3):
    print(f"Count: {i}")

# range(start, stop) - from start to stop-1
for i in range(2, 7):
    print(f"Number: {i}")

# range(start, stop, step) - with custom increment
for i in range(1, 11, 2):
    print(f"Odd: {i}")

# Negative step (countdown)
for i in range(10, 0, -1):
    print(f"Countdown: {i}")
```

---

## Iterating Through Sequences

### Strings
```python
# Loop through each character
word = "Python"
for char in word:
    print(char)
# Output: P, y, t, h, o, n

# With index
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")
```

### Lists
```python
# Loop through list items
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# With index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

---

## Practical Examples

### Multiplication Table
```python
number = int(input("Enter number: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

### Sum of Numbers
```python
# Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # 55

# Sum of user input numbers
count = int(input("How many numbers? "))
total = 0
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    total += num
print(f"Total sum: {total}")
```

### Pattern Printing
```python
# Triangle pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row

# Number triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

## Nested For Loops

### Basic Nested Loops
```python
# Multiplication table (1-5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)  # Separator

# Grid pattern
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()  # New line
```

### Matrix Operations
```python
# Create and print 2D list
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter value for [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# Print matrix
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```

---

## Loop Control Statements

### break Statement
```python
# Exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# Find first even number
numbers = [1, 3, 7, 8, 9, 12]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
```

### continue Statement
```python
# Skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9

# Print only positive numbers
numbers = [-2, 5, -1, 8, 0, 3]
for num in numbers:
    if num <= 0:
        continue
    print(num)
```

### pass Statement
```python
# Placeholder (do nothing)
for i in range(5):
    if i == 2:
        pass  # TODO: Add special handling later
    else:
        print(i)
```

---

## Advanced For Loop Techniques

### Using enumerate()
```python
# Get both index and value
students = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(students):
    print(f"Student {index + 1}: {name}")

# Start enumeration from different number
for num, name in enumerate(students, 1):
    print(f"Student {num}: {name}")
```

### Using zip()
```python
# Iterate through multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [20, 22, 19]
grades = ["A", "B", "A+"]

for name, age, grade in zip(names, ages, grades):
    print(f"{name} is {age} years old and got grade {grade}")
```

---

## Common Algorithms

### Finding Maximum
```python
numbers = [45, 23, 67, 12, 89, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum: {max_num}")
```

### Counting Elements
```python
text = "hello world"
vowel_count = 0
for char in text:
    if char.lower() in "aeiou":
        vowel_count += 1
print(f"Vowels: {vowel_count}")
```

### Reverse a String
```python
word = "Python"
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)  # nohtyP
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - For loops iterate a specific number of times
> - range(start, stop, step) generates numbers
> - Can iterate through strings, lists, and other sequences
> - Use break to exit early, continue to skip iteration
> - Nested loops create multi-dimensional iterations

> [!TIP] **Best Practices**
> - Use meaningful variable names (not just i, j)
> - Consider using enumerate() when you need indices
> - Use zip() for parallel iteration
> - Break complex nested loops into functions
> - Use range() parameters effectively

> [!WARNING] **Common Mistakes**
> - Off-by-one errors with range()
> - Forgetting that range() excludes the end value
> - Infinite loops with incorrect range parameters
> - Modifying lists while iterating over them
> - Confusing indentation in nested loops

---

## Related Topics
- [[While-Loops]] - Condition-based loops
- [[Break-Continue-Pass]] - Loop control statements
- [[Variables]] - Loop counters and accumulators

---

## Practice Questions

1. Print all even numbers from 2 to 20
2. Calculate factorial of a number using for loop
3. Create a simple guessing game with limited attempts

```python
# Practice solutions
# 1. Even numbers
for i in range(2, 21, 2):
    print(i)

# 2. Factorial
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")

# 3. Guessing game
import random
secret = random.randint(1, 10)
attempts = 3

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    elif attempt == attempts:
        print(f"Game over! The number was {secret}")
    else:
        print("Wrong! Try again.")
```

**Next**: Learn about [[While-Loops]] →