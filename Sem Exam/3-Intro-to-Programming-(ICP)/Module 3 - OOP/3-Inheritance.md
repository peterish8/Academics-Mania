# 👨‍👦 Inheritance

## 📌 1. Basic Inheritance
A child class inherits attributes and methods from a parent class.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Woof!")  # Method Overriding
```

---

## 🛠️ 2. `super()`
Used to call methods from the parent class, especially `__init__`.

```python
class Bird:
    def __init__(self, name):
        self.name = name

class Penguin(Bird):
    def __init__(self, name, can_swim=True):
        super().__init__(name)  # Initialize parent values
        self.can_swim = can_swim
```

---

## 🌳 3. Types of Inheritance
- **Single**: A -> B
- **Multiple**: A, B -> C (Child inherits from multiple parents)
- **Multilevel**: A -> B -> C

```python
# Multiple Inheritance
class Flyer:
    def fly(self): print("Flying")

class Swimmer:
    def swim(self): print("Swimming")

class Duck(Flyer, Swimmer):
    pass
```

---

## 🧠 Practice Exercises
1. **Shape Hierarchy**: Create a base class `Shape` with `calculate_area()`. Create child classes `Rectangle` and `Circle` that override this method.

---
> [[Sem Exam/3-Intro-to-Programming/Module 3 - OOP/README|🔙 Back to Module 3 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
