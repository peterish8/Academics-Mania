# 🔒 Methods & Encapsulation

## 📌 1. Types of Methods
- **Instance Method**: Regular method, takes `self`. Accesses instance data.
- **Class Method**: Takes `cls`. Can't access unique instance data, but can access class variables.
- **Static Method**: Takes neither `self` nor `cls`. Just a regular function inside a class namespace.

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # Instance Method
    def area(self):
        return self.pi * (self.radius ** 2)

    # Class Method (Good for factory methods)
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # Static Method (Helper)
    @staticmethod
    def is_valid_radius(r):
        return r > 0
```

---

## 🛡️ 2. Encapsulation (Private & Protected)
Hiding internal state to prevent direct modification.

- `_var`: Protected (convention only, "please don't touch").
- `__var`: Private (name mangled, harder to access).

### **Getters and Setters (@property)**
Use decorators to control access.

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary  # Private

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative!")
        else:
            self.__salary = value

emp = Employee(50000)
emp.salary = 60000  # Uses setter
print(emp.salary)   # Uses getter
```

---

## 🧠 Practice Exercises
1. **BankAccount**: Create a class with a private balance. Allow deposits and withdrawals (only if funds exist) via methods. Use `@property` for seeing the balance.

---
> [[Sem Exam/3-Intro-to-Programming/Module 3 - OOP/README|🔙 Back to Module 3 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
