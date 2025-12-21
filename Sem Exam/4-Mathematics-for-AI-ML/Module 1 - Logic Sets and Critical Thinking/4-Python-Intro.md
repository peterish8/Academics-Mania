# 🐍 Working with Python (Jupyter)

## 📌 1. Python for Math
Using Python sets and logic.
`Set` operations are built-in.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)  # {1, 2, 3, 4, 5, 6}

# Intersection
print(A & B)  # {3, 4}

# Difference
print(A - B)  # {1, 2}

# Cartesian Product (using itertools)
import itertools
product = list(itertools.product([1, 2], ['a', 'b']))
print(product) # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

## 📓 2. Jupyter Notebooks
- Interactive environment.
- Blocks of code (Cells).
- Shift + Enter to run.
- Markdown cells for notes.

---
> [[Sem Exam/4-Mathematics-for-AI-ML/Module 1 - Logic Sets and Critical Thinking/README|🔙 Back to Module 1 Overview]] | [[../Math-AI-ML-Hub|🏠 Back to Subject Hub]]
