# Exam Practice Problems

#exam-prep #practice #problems #coding-exercises

---

## 🎯 Python Mid-Semester Practice Problems

### Problem Categories
- **Basic**: Variables, I/O, operators, conditionals
- **Intermediate**: Loops, functions, strings
- **Advanced**: Lists, dictionaries, sets, file handling
- **Combined**: Multiple concepts together

---

## 📝 Basic Problems (Module 1)

### Problem 1: Personal Information System
**Difficulty**: Easy | **Topics**: Variables, Input, Print, Type Conversion

Write a program that:
1. Asks user for name, age, and city
2. Calculates birth year
3. Displays formatted information

```python
# Expected Output:
# Enter your name: Alice
# Enter your age: 20
# Enter your city: New York
# 
# === Personal Information ===
# Name: Alice
# Age: 20 years old
# Birth Year: 2004
# City: New York
```

<details>
<summary>Solution</summary>

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

birth_year = 2024 - age

print("\n=== Personal Information ===")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Birth Year: {birth_year}")
print(f"City: {city}")
```
</details>

### Problem 2: Grade Calculator
**Difficulty**: Easy | **Topics**: If-elif-else, Comparison operators

Create a grade calculator that converts numeric scores to letter grades:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

```python
# Test cases:
# Input: 95 → Output: "Grade: A"
# Input: 75 → Output: "Grade: C"
# Input: 45 → Output: "Grade: F"
```

<details>
<summary>Solution</summary>

```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```
</details>

### Problem 3: Simple Calculator
**Difficulty**: Easy | **Topics**: Arithmetic operators, If-elif-else

Build a calculator that performs basic operations (+, -, *, /, %) and handles division by zero.

<details>
<summary>Solution</summary>

```python
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/" and num2 != 0:
    result = num1 / num2
elif operator == "%" and num2 != 0:
    result = num1 % num2
elif num2 == 0 and operator in ["/", "%"]:
    result = "Error: Cannot divide by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
```
</details>

---

## 🔄 Intermediate Problems (Loops & Functions)

### Problem 4: Number Pattern
**Difficulty**: Medium | **Topics**: For loops, Nested loops

Print this pattern for n=5:
```
1
12
123
1234
12345
```

<details>
<summary>Solution</summary>

```python
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # New line after each row
```
</details>

### Problem 5: Prime Number Checker
**Difficulty**: Medium | **Topics**: Functions, Loops, Conditionals

Write a function that checks if a number is prime.

<details>
<summary>Solution</summary>

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
```
</details>

### Problem 6: Password Validator
**Difficulty**: Medium | **Topics**: Strings, Functions, Logical operators

Create a function that validates passwords with these rules:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit

<details>
<summary>Solution</summary>

```python
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"
    
    return True, "Password is valid"

# Test
password = input("Enter password: ")
is_valid, message = validate_password(password)
print(message)
```
</details>

---

## 📊 Advanced Problems (Module 2)

### Problem 7: Student Management System
**Difficulty**: Hard | **Topics**: Lists, Dictionaries, Functions

Create a student management system with these features:
1. Add student (name, age, grades list)
2. Calculate average grade for a student
3. Find student with highest average
4. Display all students

<details>
<summary>Solution</summary>

```python
students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = []
    
    while True:
        grade = input("Enter grade (or 'done' to finish): ")
        if grade.lower() == 'done':
            break
        grades.append(float(grade))
    
    student = {
        'name': name,
        'age': age,
        'grades': grades
    }
    students.append(student)
    print(f"Student {name} added successfully!")

def calculate_average(student):
    if student['grades']:
        return sum(student['grades']) / len(student['grades'])
    return 0

def find_top_student():
    if not students:
        return None
    
    top_student = students[0]
    top_average = calculate_average(top_student)
    
    for student in students[1:]:
        avg = calculate_average(student)
        if avg > top_average:
            top_average = avg
            top_student = student
    
    return top_student, top_average

def display_all_students():
    if not students:
        print("No students found.")
        return
    
    for student in students:
        avg = calculate_average(student)
        print(f"Name: {student['name']}, Age: {student['age']}, Average: {avg:.2f}")

# Menu system
while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Find Top Student")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_all_students()
    elif choice == "3":
        top = find_top_student()
        if top:
            student, avg = top
            print(f"Top student: {student['name']} with average {avg:.2f}")
        else:
            print("No students found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
```
</details>

### Problem 8: Word Frequency Counter
**Difficulty**: Hard | **Topics**: Strings, Dictionaries, File handling

Write a program that:
1. Reads text from user input
2. Counts frequency of each word (case-insensitive)
3. Displays words sorted by frequency

<details>
<summary>Solution</summary>

```python
def count_word_frequency(text):
    # Clean and split text
    words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    # Count frequencies
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def display_frequency(frequency):
    # Sort by frequency (descending)
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    print("\nWord Frequency:")
    print("-" * 20)
    for word, count in sorted_words:
        print(f"{word}: {count}")

# Main program
text = input("Enter text: ")
freq = count_word_frequency(text)
display_frequency(freq)
```
</details>

### Problem 9: Set Operations Calculator
**Difficulty**: Medium | **Topics**: Sets, Functions

Create a program that performs set operations:
1. Create two sets from user input
2. Display union, intersection, difference
3. Check if one set is subset of another

<details>
<summary>Solution</summary>

```python
def create_set_from_input(prompt):
    elements = input(prompt).split()
    # Convert to appropriate types (try int first, then keep as string)
    result_set = set()
    for element in elements:
        try:
            result_set.add(int(element))
        except ValueError:
            result_set.add(element)
    return result_set

def set_operations():
    print("Enter elements separated by spaces")
    set1 = create_set_from_input("Enter elements for Set 1: ")
    set2 = create_set_from_input("Enter elements for Set 2: ")
    
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}")
    
    print(f"\nUnion: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Set 1 - Set 2: {set1 - set2}")
    print(f"Set 2 - Set 1: {set2 - set1}")
    print(f"Symmetric Difference: {set1 ^ set2}")
    
    print(f"\nSet 1 is subset of Set 2: {set1.issubset(set2)}")
    print(f"Set 2 is subset of Set 1: {set2.issubset(set1)}")
    print(f"Sets are disjoint: {set1.isdisjoint(set2)}")

set_operations()
```
</details>

---

## 🔥 Challenge Problems (Combining Concepts)

### Problem 10: Mini Banking System
**Difficulty**: Very Hard | **Topics**: All concepts combined

Create a banking system with:
- Account creation (name, initial balance)
- Deposit/Withdraw with validation
- Transaction history
- Account summary
- Data persistence (save/load from file)

<details>
<summary>Solution Framework</summary>

```python
import json
from datetime import datetime

class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []
        self.add_transaction("Account created", initial_balance)
    
    def add_transaction(self, description, amount):
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'description': description,
            'amount': amount,
            'balance': self.balance
        }
        self.transactions.append(transaction)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdrawal", -amount)
            return True
        return False
    
    def get_summary(self):
        return {
            'name': self.name,
            'balance': self.balance,
            'transactions': self.transactions
        }

# Banking system implementation would continue...
```
</details>

---

## 📋 Quick Practice Drills

### Drill 1: One-Liners
Write one-line solutions for:
1. Check if number is even: `is_even = num % 2 == 0`
2. Get absolute value: `abs_val = num if num >= 0 else -num`
3. Find max of three numbers: `max_num = max(a, b, c)`
4. Reverse a string: `reversed_str = text[::-1]`
5. Count vowels in string: `vowel_count = sum(1 for c in text.lower() if c in 'aeiou')`

### Drill 2: Common Patterns
Practice these patterns until automatic:
1. Input validation loop
2. Menu-driven program
3. List processing (filter, map, reduce)
4. Dictionary operations
5. File read/write with error handling

---

## 🎯 Exam Strategy Tips

> [!TIP] **Time Management**
> - Spend 2-3 minutes reading the entire problem
> - Start with problems you're most confident about
> - Leave 10 minutes at the end for review

> [!NOTE] **Common Exam Patterns**
> - Input validation and error handling
> - Combining loops with conditionals
> - List/dictionary manipulation
> - String processing
> - Function with multiple parameters

> [!WARNING] **Avoid These Mistakes**
> - Not reading the problem completely
> - Forgetting to convert input types
> - Off-by-one errors in loops
> - Not handling edge cases
> - Poor variable naming

---

**Practice Schedule**: 
- Week 1: Problems 1-3 (Basic)
- Week 2: Problems 4-6 (Intermediate) 
- Week 3: Problems 7-9 (Advanced)
- Final Week: Problem 10 + Review all

**Next**: Review [[Common-Mistakes-to-Avoid]] →