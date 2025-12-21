# PDF 13: File Handling in Python - Quick Summary

## 🎯 File Handling Essentials

### Basic Process
1. **Open** file using `open()`
2. **Read/Write** operations
3. **Close** file using `close()` or `with` statement

### Best Practice: with Statement
```python
with open("file.txt", "r") as f:
    content = f.read()
# File automatically closed
```

## 🔥 File Opening Modes

| Mode | Purpose | Cursor | File Required? | Behavior |
|------|---------|--------|----------------|----------|
| `'r'` | Read only | Start | Must exist | Default mode |
| `'w'` | Write only | Start | Creates new | **Overwrites** existing |
| `'a'` | Append only | End | Creates new | Adds to end |
| `'r+'` | Read + Write | Start | Must exist | Can read & write |
| `'w+'` | Write + Read | Start | Creates new | Overwrites, then read |
| `'a+'` | Append + Read | End | Creates new | Append + read anywhere |
| `'x'` | Exclusive create | Start | Must NOT exist | Fails if exists |

### Binary Modes
Add `'b'` to any mode: `'rb'`, `'wb'`, `'ab'`, etc. for images, videos, PDFs.

## ⚡ Reading Methods

```python
# Assume file.txt contains: "Hello\nWorld\nPython\n"

with open("file.txt", "r") as f:
    # Read entire file
    content = f.read()          # "Hello\nWorld\nPython\n"
    
    # Read specific characters
    first_5 = f.read(5)         # "Hello"
    
    # Read one line
    line1 = f.readline()        # "Hello\n"
    
    # Read all lines into list
    lines = f.readlines()       # ['Hello\n', 'World\n', 'Python\n']
```

## 🔥 Writing Methods

```python
# Write single string
with open("file.txt", "w") as f:
    f.write("Hello Python\n")

# Write multiple lines
with open("file.txt", "w") as f:
    f.writelines(["Line1\n", "Line2\n", "Line3\n"])
```

## 🎯 Cursor Control Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `tell()` | Get cursor position | `pos = f.tell()` |
| `seek(offset, whence)` | Move cursor | `f.seek(0)` (to start) |
| `truncate(size)` | Cut file to size | `f.truncate(10)` |
| `flush()` | Force write to disk | `f.flush()` |

### seek() Parameters
- `whence=0`: From start (default)
- `whence=1`: From current position  
- `whence=2`: From end

```python
with open("file.txt", "r") as f:
    f.seek(0)        # Move to start
    f.seek(5)        # Move to position 5
    print(f.tell())  # Show current position
```

## 🔥 Common Exam Patterns

### 1. Read and Process Lines
```python
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())  # Remove \n
```

### 2. Count Words/Lines
```python
with open("file.txt", "r") as f:
    lines = f.readlines()
    word_count = sum(len(line.split()) for line in lines)
    line_count = len(lines)
```

### 3. Append to Existing File
```python
with open("file.txt", "a") as f:
    f.write("\nNew line added")
```

### 4. Read and Write (r+ mode)
```python
with open("file.txt", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write("Modified: " + content)
```

### 5. Write and Read Back (w+ mode)
```python
with open("file.txt", "w+") as f:
    f.write("Hello World")
    f.seek(0)           # Move cursor to start
    content = f.read()  # Read what we wrote
```

## ⚠️ Key Points

### Mode Behaviors
- **'w' mode**: **OVERWRITES** entire file (data lost!)
- **'a' mode**: Always writes at end, safe for existing data
- **'r+' mode**: File must exist, cursor at start
- **'x' mode**: Fails if file already exists (safe creation)

### Common Mistakes
- Forgetting to close files (use `with` statement)
- Using 'w' when you meant 'a' (data loss!)
- Not moving cursor with `seek()` in '+' modes
- Trying to read from write-only modes

### File Existence
```python
import os
if os.path.exists("file.txt"):
    # File exists
    pass
```

## 🎯 Quick Examples

```python
# Safe file reading
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")

# Create file if not exists
with open("file.txt", "a") as f:
    f.write("Data\n")

# Binary file handling
with open("image.jpg", "rb") as f:
    data = f.read()
```

---
*Previous: [[PDF-12-Sets-Quick-Summary]]*

#file-handling #python #files #io-operations #exam-prep