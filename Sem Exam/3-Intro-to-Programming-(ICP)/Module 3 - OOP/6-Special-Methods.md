# ✨ Special / Magic Methods

## 📌 1. Dunder Methods
Methods starting and ending with double underscores (`__`). They define internal behavior.

- `__init__(self)`: Constructor.
- `__str__(self)`: String representation (user-friendly).
- `__repr__(self)`: String representation (developer-focused, debugging).
- `__len__(self)`: Behavior for `len()`.
- `__eq__(self, other)`: Behavior for `==`.

---

## 🛠️ 2. Examples

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by Your Favorite Author"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title

b1 = Book("Python 101", 250)
b2 = Book("Python 101", 300)

print(b1)         # Calls __str__ -> 'Python 101' by Your Favorite Author
print(len(b1))    # Calls __len__ -> 250
print(b1 == b2)   # Calls __eq__ -> True
```

---

## 🧠 Practice Exercises
1. **Deck of Cards**: Implement a class `Card` containing a suit and value. Implement `__str__` to print "Ace of Spades" and `__eq__` to compare values.

---
> [[Sem Exam/3-Intro-to-Programming/Module 3 - OOP/README|🔙 Back to Module 3 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
