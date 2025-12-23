# 3️⃣ Four Pillars of OOPS

---

## 📌 1. Encapsulation

> **Definition**: Bundling data (attributes) and methods together, restricting direct access to some components.

### Data Hiding & Access Modifiers

| Modifier | Syntax | Access |
|----------|--------|--------|
| **Public** | `name` | Anywhere |
| **Protected** | `_name` | Class + Subclasses |
| **Private** | `__name` | Class only |

```python
class BankAccount:
    def __init__(self, balance):
        self.owner = "John"       # Public
        self._bank = "ABC Bank"   # Protected
        self.__balance = balance  # Private
    
    def get_balance(self):        # Getter (controlled access)
        return self.__balance
    
    def deposit(self, amount):    # Setter
        self.__balance += amount

# TEST
acc = BankAccount(1000)
print(acc.owner)         # Works: John
print(acc._bank)         # Works but discouraged
# print(acc.__balance)   # Error! Private
print(acc.get_balance()) # Works: 1000
```

---

## 📌 2. Abstraction

> **Definition**: Hide complex implementation, show only essential features.

### Abstract Classes
> Use `abc` module to create abstract classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # No implementation
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):           # Must implement
        return self.l * self.w
    
    def perimeter(self):      # Must implement
        return 2 * (self.l + self.w)

# shape = Shape()  # Error! Can't instantiate abstract class
rect = Rectangle(5, 3)
print(rect.area())  # 15
```

---

## 📌 3. Inheritance

> **Definition**: A class (child) inherits attributes and methods from another class (parent).

### Base Class & Derived Class

```python
class Animal:           # Base/Parent class
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal speaks")

class Dog(Animal):      # Derived/Child class
    def speak(self):    # Override parent method
        print(f"{self.name} says Woof!")

# TEST
dog = Dog("Buddy")
dog.speak()  # Buddy says Woof!
```

---

## 📌 4. Polymorphism

> **Definition**: Same interface, different implementations. "Many forms."

### Method Overriding (Run-time Polymorphism)
> Child class provides different implementation of parent's method.

```python
class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):           # Override
        print("Penguin can't fly!")

# Same method name, different behavior
Bird().fly()     # Bird flies
Penguin().fly()  # Penguin can't fly!
```

### Method Overloading (Compile-time)
> Python doesn't support true overloading, but we can use default arguments.

```python
class Math:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c

m = Math()
print(m.add(2, 3))      # 5
print(m.add(2, 3, 4))   # 9
```

---

## 📊 Summary Table

| Pillar | Purpose | Example |
|--------|---------|---------|
| **Encapsulation** | Hide data, control access | Private variables |
| **Abstraction** | Hide complexity | Abstract classes |
| **Inheritance** | Reuse code | Parent → Child |
| **Polymorphism** | Same name, different behavior | Method overriding |

---

## 🧠 Key Points
- **Encapsulation**: `__private` hides data
- **Abstraction**: Use `@abstractmethod` decorator
- **Inheritance**: `class Child(Parent):`
- **Polymorphism**: Override methods in child class

---

[[2-Classes-Objects|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[4-Types-of-Inheritance|Next →]]
