# 6️⃣ File Handling

> [!INFO] **Definition: File Handling**
> The process of performing operations on files such as creating, reading, writing, and appending data. Python uses built-in `open()` function.

---

## 📌 Opening & Closing Files

```python
# Method 1: Manual close
file = open("test.txt", "r")
content = file.read()
file.close()  # Must close!

# Method 2: With statement (auto-close) ✅ Recommended
with open("test.txt", "r") as file:
    content = file.read()
# Automatically closed after block
```

---

## 📌 File Modes

| Mode | Description | Creates if not exist? | Overwrites? |
|------|-------------|----------------------|-------------|
| **r** | Read only | ❌ Error | - |
| **w** | Write only | ✅ Yes | ✅ Yes |
| **a** | Append | ✅ Yes | ❌ No |
| **r+** | Read & Write | ❌ Error | ❌ No |
| **w+** | Write & Read | ✅ Yes | ✅ Yes |
| **a+** | Append & Read | ✅ Yes | ❌ No |

```python
# Read mode
with open("file.txt", "r") as f:
    pass

# Write mode (overwrites!)
with open("file.txt", "w") as f:
    pass

# Append mode (adds to end)
with open("file.txt", "a") as f:
    pass
```

---

## 📌 Reading Files

### read() - Read entire file
> **Goal**: Get all content as single string.

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

### readline() - Read one line
> **Goal**: Read file line by line.

```python
with open("data.txt", "r") as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
    print(line1, line2)
```

### readlines() - Read all lines as list
> **Goal**: Get list where each element is a line.

```python
with open("data.txt", "r") as f:
    lines = f.readlines()  # ['line1\n', 'line2\n', ...]
    for line in lines:
        print(line.strip())  # Remove \n
```

---

## 📌 Writing Files

### write() - Write string
> **Goal**: Write text to file.

```python
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line")
```

### writelines() - Write list of strings
> **Goal**: Write multiple lines from list.

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

---

## 💻 Complete Example

```python
# Writing to file
with open("students.txt", "w") as f:
    f.write("Alice, 85\n")
    f.write("Bob, 90\n")
    f.write("Charlie, 78\n")

# Reading from file
with open("students.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(", ")
        print(f"{name} scored {score}")
```

---

## 📊 Methods Summary

| Method | Input/Output | Usage |
|--------|--------------|-------|
| **read()** | Returns string | Full file content |
| **readline()** | Returns string | One line at a time |
| **readlines()** | Returns list | All lines as list |
| **write()** | Takes string | Write text |
| **writelines()** | Takes list | Write multiple strings |

---

## 🧠 Key Points
- Always use `with` statement (auto-closes file)
- **"r"** = read, **"w"** = write (overwrites!), **"a"** = append
- `readline()` for line-by-line, `read()` for all at once
- Don't forget `\n` for new lines in write!

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: Best way to open a file?
>> [!SUCCESS]- Answer
>> Using `with` statement: `with open("file.txt", "r") as f:`

> [!QUESTION] Q2: What does mode "w" do?
>> [!SUCCESS]- Answer
>> Opens for **writing** and **overwrites** existing content.

> [!QUESTION] Q3: Difference between read() and readlines()?
>> [!SUCCESS]- Answer
>> `read()` = **single string**. `readlines()` = **list of lines**.

> [!QUESTION] Q4: How to add content without overwriting?
>> [!SUCCESS]- Answer
>> Use **append mode**: `open("file.txt", "a")`

> [!QUESTION] Q5: Why use `with` statement?
>> [!SUCCESS]- Answer
>> **Auto-closes** the file even if error occurs.

---

[[5-Constructors-Destructors|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[7-Exception-Handling|Next →]]
