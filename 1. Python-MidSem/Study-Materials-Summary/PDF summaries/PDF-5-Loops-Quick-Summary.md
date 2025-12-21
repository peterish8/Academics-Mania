# PDF 5: Loops in Python - Quick Summary

#last-minute-prep #summary #loops #for-loop #while-loop #control-keywords

---

## 🎯 What are Loops?

### Key Points
- **Repeat tasks** automatically until condition met
- **Avoid repetition** - write code once, run multiple times
- **Two types**: `for` (known repetitions), `while` (unknown repetitions)

---

## 🎯 for Loop

### Key Points
- **Use when**: You know how many times to repeat
- **Works with**: ranges, lists, strings, sequences
- **range() function**: `range(start, stop, step)`

### Essential Code
```python
# Basic range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)

# Iterate over sequences
for char in "Python":       # P, y, t, h, o, n
    print(char)

for item in [1, 2, 3]:      # 1, 2, 3
    print(item)
```

### Common Patterns
```python
# Multiplication table
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Sum of numbers
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
```

---

## 🎯 while Loop

### Key Points
- **Use when**: You don't know exact number of repetitions
- **Continues**: Until condition becomes False
- **Must update**: Counter variable to avoid infinite loop

### Essential Code
```python
# Basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1      # MUST update counter

# Password check
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted!")

# User input until 0
num = 1
total = 0
while num != 0:
    num = int(input("Enter number (0 to stop): "))
    total += num
print(f"Total: {total}")
```

---

## 🎯 Control Keywords

### break - Exit Loop Early
```python
for i in range(1, 10):
    if i == 5:
        break       # Stop loop at 5
    print(i)        # Prints: 1, 2, 3, 4
```

### continue - Skip Current Iteration
```python
for i in range(1, 6):
    if i == 3:
        continue    # Skip 3
    print(i)        # Prints: 1, 2, 4, 5
```

### pass - Placeholder (Do Nothing)
```python
for i in range(5):
    pass           # Placeholder, does nothing
```

---

## 🎯 Essential Algorithms

### 1. Reverse a Number
```python
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)  # 4321
```

### 2. Check Palindrome
```python
num = 121
original = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
```

### 3. Factorial
```python
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)  # 120
```

### 4. Fibonacci Series
```python
n = 7
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# Output: 0 1 1 2 3 5 8
```

### 5. Sum of Digits
```python
num = 547
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)  # 16
```

### 6. Count Digits
```python
num = 12345
count = 0
while num > 0:
    num //= 10
    count += 1
print(count)  # 5
```

---

## ⚡ Quick Reference

### Loop Choice Guide
```python
# Use FOR when:
for i in range(10):         # Known repetitions
for char in "hello":        # Iterating sequences
for item in [1,2,3]:        # Iterating collections

# Use WHILE when:
while condition:            # Unknown repetitions
while user_input != "quit": # User-controlled loops
while num > 0:              # Condition-based loops
```

### Common range() Patterns
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
range(10, 0, -1)# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Nested Loop Pattern
```python
# Triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

---

## 🚨 Common Mistakes to Avoid

### Infinite Loops
```python
# Wrong - infinite loop
i = 1
while i <= 5:
    print(i)
    # Missing: i += 1

# Correct
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Off-by-One Errors
```python
# Wrong - misses last number
for i in range(1, 5):    # 1, 2, 3, 4 (missing 5)

# Correct - includes last number
for i in range(1, 6):    # 1, 2, 3, 4, 5
```

### Variable Scope Issues
```python
# Wrong - using loop variable outside
for i in range(5):
    pass
print(i)  # Works but not recommended

# Better - define variable outside if needed
result = 0
for i in range(5):
    result += i
print(result)
```

---

## 🎯 Exam Tips

### Must Remember Algorithms
- **Reverse number**: `rev = rev * 10 + digit`
- **Sum of digits**: `total += num % 10`
- **Factorial**: `fact *= i`
- **Fibonacci**: `a, b = b, a + b`

### Quick Test Patterns
```python
# Even numbers 1-10
for i in range(2, 11, 2):
    print(i)

# Odd numbers 1-10
for i in range(1, 11, 2):
    print(i)

# Countdown
for i in range(10, 0, -1):
    print(i)
```

### Memory Aids
- **for**: "For known repetitions"
- **while**: "While condition is true"
- **break**: "Break out of loop"
- **continue**: "Continue to next iteration"
- **range(start, stop, step)**: "Start included, stop excluded"

---

## 📝 Last-Minute Checklist

### Before Exam
- [ ] Know when to use for vs while
- [ ] Remember range(start, stop, step) syntax
- [ ] Can write reverse number algorithm
- [ ] Understand break vs continue
- [ ] Know common patterns (factorial, fibonacci)

### During Exam
- [ ] Always update counter in while loops
- [ ] Check range bounds (inclusive/exclusive)
- [ ] Use meaningful variable names
- [ ] Test loop logic with small examples
- [ ] Remember to handle edge cases (empty input, zero)

### Algorithm Checklist
- [ ] **Reverse**: `digit = num % 10`, `rev = rev * 10 + digit`, `num //= 10`
- [ ] **Digits**: Use `% 10` to get last digit, `// 10` to remove it
- [ ] **Factorial**: Multiply all numbers from 1 to n
- [ ] **Fibonacci**: Each number is sum of previous two

**⏰ Practice Time: 2 minutes per algorithm**

---
*Previous: [[PDF-4-Operators-Quick-Summary]] | Next: [[PDF-6-Functions-Scope-Quick-Summary]]*

#loops #for-loop #while-loop #algorithms #exam-prep