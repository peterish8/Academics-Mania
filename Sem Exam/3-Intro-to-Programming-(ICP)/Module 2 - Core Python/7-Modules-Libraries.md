# 📦 Modules & Libraries

## 📌 1. standard Library
Python comes with "batteries included". You can `import` powerful built-in modules.

```python
import math
import random
import datetime

print(math.sqrt(16))      # 4.0
print(random.randint(1, 10)) # Random number 1-10

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d")) # Current date
```

### **Import Variations**
```python
from math import pi, sqrt   # Import specific items
import numpy as np          # Alias for brevity
```

---

## 🛠️ 2. User-Defined Modules
You can save your code in a `.py` file (e.g., `my_utils.py`) and import it elsewhere.

**my_utils.py**:
```python
def add(a, b):
    return a + b
```

**main.py**:
```python
import my_utils

print(my_utils.add(5, 10))
```

---

## 📦 3. External Packages (pip)
Use `pip` to install packages from PyPI (Python Package Index).

**Terminal Commands**:
```bash
pip install requests    # Install a package
pip install pandas      # Install pandas
pip list                # List installed packages
```

---

## 🧠 Practice Exercises
1. **Dice Simulator**: Create a module `dice.py` with a function `roll(sides)` that returns a random number. Import and use it in `main.py`.
2. **Days Until Birthday**: Use the `datetime` module to calculate and print how many days remain until your next birthday.

---
> [[Sem Exam/3-Intro-to-Programming/Module 2 - Core Python/README|🔙 Back to Module 2 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
