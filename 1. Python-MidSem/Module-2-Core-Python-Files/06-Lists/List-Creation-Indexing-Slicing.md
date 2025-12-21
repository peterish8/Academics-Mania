# List Creation, Indexing, and Slicing

#module2 #lists #creation #indexing #slicing

---

## What are Lists?

Lists are ordered collections that can store multiple items. They are mutable (changeable) and can contain different data types.

---

## List Creation

### Empty Lists
```python
# Empty list
empty_list = []
empty_list2 = list()

print(empty_list)   # []
print(len(empty_list))  # 0
```

### Lists with Items
```python
# List with numbers
numbers = [1, 2, 3, 4, 5]

# List with strings
fruits = ["apple", "banana", "orange"]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]

print(numbers)  # [1, 2, 3, 4, 5]
print(fruits)   # ['apple', 'banana', 'orange']
print(mixed)    # [1, 'hello', 3.14, True]
```

### Creating Lists from Other Iterables
```python
# From string
letters = list("hello")
print(letters)  # ['h', 'e', 'l', 'l', 'o']

# From range
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

# From tuple
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print(list_data)  # [1, 2, 3]
```

---

## List Indexing

### Positive Indexing
```python
fruits = ["apple", "banana", "orange", "grape"]

# Access individual elements (0-based indexing)
print(fruits[0])    # "apple" (first element)
print(fruits[1])    # "banana" (second element)
print(fruits[2])    # "orange" (third element)
print(fruits[3])    # "grape" (fourth element)

# Using variables as index
index = 2
print(fruits[index])  # "orange"
```

### Negative Indexing
```python
fruits = ["apple", "banana", "orange", "grape"]

# Access from the end
print(fruits[-1])   # "grape" (last element)
print(fruits[-2])   # "orange" (second to last)
print(fruits[-3])   # "banana" (third to last)
print(fruits[-4])   # "apple" (fourth to last)

# Relationship: fruits[-1] == fruits[len(fruits)-1]
```

### Index Errors
```python
fruits = ["apple", "banana", "orange"]

# These will cause IndexError
# print(fruits[3])   # Index out of range
# print(fruits[-4])  # Index out of range

# Safe way to check
if len(fruits) > 3:
    print(fruits[3])
else:
    print("Index 3 doesn't exist")
```

---

## List Slicing

### Basic Slicing Syntax
```python
# list[start:end:step]
# start: inclusive, end: exclusive, step: increment
```

### Simple Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive)
print(numbers[2:5])     # [2, 3, 4]

# Get elements from index 1 to 7
print(numbers[1:7])     # [1, 2, 3, 4, 5, 6]

# Get first 3 elements
print(numbers[:3])      # [0, 1, 2]

# Get last 3 elements
print(numbers[-3:])     # [7, 8, 9]

# Get all elements (copy)
print(numbers[:])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Slicing with Step
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every second element
print(numbers[::2])     # [0, 2, 4, 6, 8]

# Every third element starting from index 1
print(numbers[1::3])    # [1, 4, 7]

# Elements from index 2 to 8, every 2nd
print(numbers[2:8:2])   # [2, 4, 6]

# Reverse the list
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Every second element in reverse
print(numbers[::-2])    # [9, 7, 5, 3, 1]
```

### Advanced Slicing
```python
text = "Python Programming"
letters = list(text)

# Get every other character
print(letters[::2])     # ['P', 't', 'o', ' ', 'r', 'g', 'a', 'm', 'n']

# Get substring equivalent
word = letters[0:6]     # ['P', 'y', 't', 'h', 'o', 'n']
print(''.join(word))    # "Python"

# Negative indices in slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-5:-2])   # [5, 6, 7]
print(numbers[-3:])     # [7, 8, 9]
```

---

## Modifying Lists through Indexing

### Changing Single Elements
```python
fruits = ["apple", "banana", "orange"]

# Change single element
fruits[1] = "grape"
print(fruits)  # ['apple', 'grape', 'orange']

# Change using negative index
fruits[-1] = "mango"
print(fruits)  # ['apple', 'grape', 'mango']
```

### Changing Multiple Elements with Slicing
```python
numbers = [1, 2, 3, 4, 5]

# Replace multiple elements
numbers[1:3] = [20, 30]
print(numbers)  # [1, 20, 30, 4, 5]

# Replace with different number of elements
numbers[1:3] = [100, 200, 300]
print(numbers)  # [1, 100, 200, 300, 4, 5]

# Insert elements
numbers[2:2] = [150, 175]  # Insert at index 2
print(numbers)  # [1, 100, 150, 175, 200, 300, 4, 5]
```

---

## Practical Examples

### Student Grades System
```python
# Store student grades
grades = [85, 92, 78, 96, 88]

# Access specific grades
first_grade = grades[0]
last_grade = grades[-1]
print(f"First grade: {first_grade}")
print(f"Last grade: {last_grade}")

# Get top 3 grades (assuming sorted)
grades.sort(reverse=True)
top_three = grades[:3]
print(f"Top 3 grades: {top_three}")

# Get failing grades (below 60)
all_grades = [85, 92, 45, 78, 55, 96, 88]
failing = [grade for grade in all_grades if grade < 60]
print(f"Failing grades: {failing}")
```

### Text Processing
```python
# Process a sentence
sentence = "Python is awesome for programming"
words = sentence.split()  # Convert to list of words

# Get first and last words
first_word = words[0]
last_word = words[-1]
print(f"First: {first_word}, Last: {last_word}")

# Get middle words
middle_words = words[1:-1]
print(f"Middle words: {middle_words}")

# Reverse word order
reversed_words = words[::-1]
reversed_sentence = " ".join(reversed_words)
print(f"Reversed: {reversed_sentence}")
```

### Data Analysis Example
```python
# Monthly sales data
sales = [1200, 1500, 1800, 1600, 2000, 2200, 1900, 2100, 1750, 1950, 2300, 2500]

# Get quarterly data
q1 = sales[:3]      # First quarter
q2 = sales[3:6]     # Second quarter
q3 = sales[6:9]     # Third quarter
q4 = sales[9:]      # Fourth quarter

print(f"Q1 Sales: {q1}, Total: {sum(q1)}")
print(f"Q2 Sales: {q2}, Total: {sum(q2)}")
print(f"Q3 Sales: {q3}, Total: {sum(q3)}")
print(f"Q4 Sales: {q4}, Total: {sum(q4)}")

# Get every other month
alternate_months = sales[::2]
print(f"Alternate months: {alternate_months}")
```

---

## Important Points

> [!NOTE] **Key Concepts**
> - Lists use 0-based indexing (first element is index 0)
> - Negative indices count from the end (-1 is last element)
> - Slicing creates a new list (doesn't modify original)
> - Slicing syntax: `[start:end:step]` where end is exclusive
> - Empty slices return empty lists

> [!TIP] **Best Practices**
> - Use meaningful variable names for lists
> - Check list length before accessing indices
> - Use negative indices to access from end
> - Use slicing to get sublists efficiently
> - Remember that slicing creates copies

> [!WARNING] **Common Mistakes**
> - IndexError when accessing non-existent indices
> - Forgetting that slicing end is exclusive
> - Confusing positive and negative indices
> - Modifying list while iterating over it
> - Assuming slicing modifies original list

---

## Related Topics
- [[List-Methods-append-pop-sort]] - Modifying lists with methods
- [[List-Comprehension]] - Creating lists efficiently
- [[Variables]] - Storing lists in variables

---

## Practice Questions

1. Create a list of your favorite movies and access the second and last movie
2. From the list [1,2,3,4,5,6,7,8,9,10], get all even-indexed elements
3. Reverse a list without using reverse() method

```python
# Practice solutions
# 1. Movie list
movies = ["Inception", "The Matrix", "Interstellar", "Avatar"]
second_movie = movies[1]
last_movie = movies[-1]
print(f"Second: {second_movie}, Last: {last_movie}")

# 2. Even-indexed elements
numbers = [1,2,3,4,5,6,7,8,9,10]
even_indexed = numbers[::2]  # [1, 3, 5, 7, 9]

# 3. Reverse without reverse()
original = [1, 2, 3, 4, 5]
reversed_list = original[::-1]  # [5, 4, 3, 2, 1]
```

**Next**: Learn about [[List-Methods-append-pop-sort]] →