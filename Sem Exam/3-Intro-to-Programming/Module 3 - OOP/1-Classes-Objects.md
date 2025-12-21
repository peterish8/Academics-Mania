# 🏗️ Classes & Objects

## 📌 1. Definitions
- **Class**: A blueprint or template for creating objects.
- **Object**: An instance of a class.

---

## 🛠️ 2. Creating a Class
`__init__` is the constructor method, called automatically when creating a new object. `self` refers to the current instance.

```python
class Dog:
    # Class Attribute (Shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance Attributes (Unique to each instance)
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Creating Objects (Instantiation)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)    # Buddy
print(dog1.bark())  # Buddy says Woof!
print(dog1.species) # Canis familiaris
```

---

## 🧠 Practice Exercises
1. **Car Class**: Create a `Car` class with attributes `make`, `model`, `year` and a method `drive()` that prints "Vroom!".
2. **Student Class**: Create a `Student` class with `name` and `grades` (list). Add a method to calculate the average grade.

---
> [[Sem Exam/3-Intro-to-Programming/Module 3 - OOP/README|🔙 Back to Module 3 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
