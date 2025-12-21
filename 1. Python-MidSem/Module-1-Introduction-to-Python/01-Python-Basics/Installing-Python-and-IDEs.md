# Installing Python and IDEs

#module1 #python-basics #installation #setup

---

## What is Python?

Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used for web development, data science, automation, and more.

---

## Installing Python

### Windows Installation
1. Visit [python.org](https://python.org)
2. Download latest Python version (3.x)
3. Run installer
4. **Important**: Check "Add Python to PATH"
5. Click "Install Now"

### Verification
```python
# Open Command Prompt and type:
python --version
# or
python -V
```

> [!NOTE] **Python Version**
> Always use Python 3.x (3.8 or higher recommended). Python 2.x is deprecated.

---

## Popular IDEs and Editors

### 1. IDLE (Built-in)
- Comes with Python installation
- Simple interface
- Good for beginners
- Interactive shell available

### 2. PyCharm
- Professional IDE
- Code completion
- Debugging tools
- Project management

### 3. Visual Studio Code
- Lightweight editor
- Python extension available
- Integrated terminal
- Git integration

### 4. Jupyter Notebook
- Web-based interface
- Great for data science
- Interactive coding
- Markdown support

---

## Python Interactive Shell

```python
# Start Python shell
python

# Basic operations
>>> print("Hello, World!")
Hello, World!

>>> 2 + 3
5

>>> exit()  # or Ctrl+Z (Windows) / Ctrl+D (Mac/Linux)
```

---

## Running Python Files

### Method 1: Command Line
```python
# Save code in file.py
print("Hello from file!")

# Run from command prompt
python file.py
```

### Method 2: IDE
- Create new file with `.py` extension
- Write code
- Click Run button or press F5

---

## Important Points

> [!TIP] **Best Practices**
> - Always use meaningful file names
> - Save files with `.py` extension
> - Keep Python updated to latest version
> - Use virtual environments for projects

> [!WARNING] **Common Issues**
> - Forgetting to add Python to PATH
> - Using Python 2.x instead of 3.x
> - Not saving files with `.py` extension

---

## Related Topics
- [[Python-Syntax-Rules]] - Basic syntax rules
- [[Print-Function]] - Output in Python
- [[Variables]] - Storing data

---

## Quick Practice

1. Install Python on your system
2. Open IDLE and print your name
3. Create a `.py` file and run it from command line

**Next**: Learn about the [[Print-Function]] →