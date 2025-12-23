# 🎭 Polymorphism & Duck Typing

## 📌 1. Polymorphism
"Many forms". Different classes can be treated as instances of the same general class through the same interface.

```python
class Cat:
    def speak(self): print("Meow")

class Dog:
    def speak(self): print("Woof")

animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()  # Works for both, even though they are different classes
```

---

## 🦆 2. Duck Typing
"If it walks like a duck and quacks like a duck, it's a duck."
Python doesn't care about the type of object, only if it has the right method.

```python
class Car:
    def move(self): print("Drive")

class Boat:
    def move(self): print("Sail")

def start_journey(vehicle):
    vehicle.move() # Doesn't matter if it's Car or Boat

start_journey(Car())
```

---

## ➕ 3. Operator Overloading
Customizing how standard operators (`+`, `-`, `==`) behave with your objects.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define behavior for '+'
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, 1)
print(v1 + v2)  # Vector(3, 5)
```

---

## 🧠 Practice Exercises
1. **Currency**: Create a `Currency` class that can add two currency objects together (e.g., `$5 + $10 = $15`). Handle different currencies if you want a challenge!

---
> [[Sem Exam/3-Intro-to-Programming/Module 3 - OOP/README|🔙 Back to Module 3 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
