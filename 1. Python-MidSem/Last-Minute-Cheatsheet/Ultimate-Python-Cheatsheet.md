# 🐍 Ultimate Python Cheatsheet - Last Minute Prep 🚀

## 🎯 Module 1: Introduction to Programming using Python

### 🔧 Python Basics + Control Flow
- 🖥️ **Installing Python & IDEs**: Download from python.org, use PyCharm/VS Code/IDLE
- 📺 **print()**: Displays output to console, use sep and end parameters
- ⌨️ **input()**: Gets user input as string, always convert for calculations
- 📝 **syntax**: Use 4-space indentation, colon after if/for/while/def
- 📦 **variables**: Containers for data, snake_case naming, case-sensitive
- 🏷️ **data types**: int (whole numbers), float (decimals), str (text), bool (True/False), complex (a+bj)
- 🔄 **type conversion**: int(), float(), str(), bool() to change data types
- ➕ **operators**: +,-,*,/,//,%,** for math; ==,!=,<,>,<=,>= for comparison
- 🤔 **Conditionals (if, elif, else)**: Execute code based on True/False conditions
- ⚖️ **Conditional operators**: == (equal), != (not equal), < > <= >= (comparison)
- 🧠 **Logical operators**: and (both true), or (one true), not (reverse)
- 🔁 **Loops (for, while)**: for = known repetitions, while = condition-based repetitions
- 🎮 **control keywords**: break (exit loop), continue (skip iteration), pass (do nothing)

### ⚙️ Function
- 🏗️ **def**: Keyword to define reusable code blocks
- 📤 **return**: Send value back from function (optional)
- 🌍 **scope**: Local (inside function) vs Global (everywhere accessible)
- 📋 **arguments**: positional (order matters), default (optional values), keyword (name=value)

### 🔤 Strings
- 🎯 **Indexing**: Access characters by position [0], [-1] for last
- ✂️ **slicing**: Extract parts [start:end:step], end is exclusive
- 💥 **split()**: Break string into list by separator
- 🧹 **strip()**: Remove whitespace from start/end
- 🔍 **find()**: Return index of substring or -1 if not found
- 🔄 **replace()**: Replace old substring with new one
- 🎨 **f-strings**: Format strings with variables using f"text {variable}"

## 🎯 Module 2: Core Python, Files

### 📋 Lists
- 🏗️ **Creation**: [1,2,3] or list(), ordered and mutable collection
- 🎯 **indexing**: Access elements by position [0], [-1] for last
- ✂️ **slicing**: Extract parts [start:end:step], creates new list
- ➕ **append()**: Add single element to end
- 🗑️ **pop()**: Remove and return element by index (last if no index)
- 📊 **sort()**: Arrange elements in ascending order in-place
- 🎨 **list comprehension**: [expression for item in iterable if condition]

### 🔒 Tuples
- 🛡️ **Immutable nature**: Cannot change after creation, use () or comma
- 📦 **tuple unpacking**: Assign tuple elements to variables: a,b = (1,2)

### 🗂️ Dictionaries
- 🔑 **Key-value structure**: {key: value} pairs, keys must be unique and immutable
- 🛡️ **get()**: Safe access dict.get(key, default) returns None if key missing
- 📋 **items()**: Returns key-value pairs as tuples for iteration

### 🎲 Sets
- 💎 **Definition & Characteristics**: Unordered collection of unique elements, no duplicates
- 🏗️ **Creation**: {1,2,3} or set(), empty set needs set() not {}
- ➕ **Adding elements**: add() for single, update() for multiple
- 🗑️ **Removing elements**: remove() (error if missing), discard() (no error)
- 🔍 **Membership test**: in and not in operators for checking existence
- 📏 **Length**: len() returns number of elements
- 🔄 **Iteration**: for loop to access each element
- 🤝 **Union**: | or union() combines sets with all unique elements
- 🎯 **Intersection**: & or intersection() returns common elements only
- ➖ **Difference**: - or difference() returns elements in first but not second
- ⚡ **Symmetric difference**: ^ returns elements in either set but not both
- 📊 **Subset/Superset**: issubset() and issuperset() check containment relationships
- 🚫 **Disjoint sets**: isdisjoint() returns True if no common elements
- 📋 **Copying sets**: copy() creates shallow copy of set

### 📁 File Handling
- 🔓 **open()**: Opens file with mode ('r' read, 'w' write, 'a' append)
- 📖 **read()**: Reads entire file content as string
- ✍️ **write()**: Writes string to file (overwrites in 'w' mode)
- ➕ **append()**: Adds content to end of file without overwriting
- 🛡️ **with statement**: Automatically closes file after use, best practice

---

## ⚡ Quick Reference Patterns

```python
# Essential syntax patterns
if condition: action
for i in range(n): action
while condition: action
def func(): return value
[x for x in list if condition]
{key: value for key, value in dict.items()}
with open("file.txt", "r") as f: content = f.read()
```

## ⚠️ Common Mistakes to Avoid
- 🚨 input() returns string - convert with int()/float()
- ⚖️ Use == for comparison, = for assignment  
- 🔒 Single tuple needs comma: (5,) not (5)
- 🎲 Empty set is set() not {}
- 📁 'w' mode overwrites file, 'a' mode appends

#python #cheatsheet #exam-prep #last-minute #quick-reference