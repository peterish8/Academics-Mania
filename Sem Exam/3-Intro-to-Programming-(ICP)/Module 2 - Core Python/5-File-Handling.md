# 📄 File Handling

## 📌 1. Opening Files
The `open()` function is the key.
`file = open('filename', 'mode')`

**Modes**:
- `'r'`: Read (default). Error if file doesn't exist.
- `'w'`: Write. Creates file or truncates (empties) existing file.
- `'a'`: Append. Creates file if missing, adds to end.
- `'r+'`: Read and Write.

---

## 🛡️ 2. The `with` Statement (Context Manager)
Always use `with` to ensure the file closes automatically, even if errors occur.

```python
# Writing
with open('example.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is Python.")

# Reading
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```

---

## 📖 3. Reading Methods
- `read()`: Reads entire file as one string.
- `readline()`: Reads one line at a time.
- `readlines()`: Reads all lines into a list.

```python
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Process line by line efficiency
```

---

## 🧠 Practice Exercises
1. **Log Writer**: Write a script that asks the user for a message and appends it to `log.txt` with a timestamp.
2. **File Stats**: Read a text file and count the number of lines, words, and characters.
3. **Copy File**: Create a program that copies the content of `source.txt` to `destination.txt`.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
