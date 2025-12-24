# 3️⃣ Four Pillars of OOPS

---

## 📌 1. Encapsulation

> [!INFO] **Definition: Encapsulation**
> Bundling data and methods together while hiding internal details from outside access. It protects data using access modifiers (public, protected, private).

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

> [!INFO] **Definition: Abstraction**
> Hiding complex implementation details and showing only the essential features to the user. It focuses on "what it does" not "how it does".

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

> [!INFO] **Definition: Inheritance**
> The ability of a child class to acquire properties and methods from a parent class, promoting code reusability.

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

> [!INFO] **Definition: Polymorphism**
> The ability for the same method name to have different behaviors in different classes. "Many forms" - same interface, different implementations.

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

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is Encapsulation?
>> [!SUCCESS]- Answer
>> Bundling data and methods together, **hiding internal details** using private variables.

> [!QUESTION] Q2: How to make a variable private in Python?
>> [!SUCCESS]- Answer
>> Use **double underscore prefix**: `__variable_name`

> [!QUESTION] Q3: What is the difference between Abstraction and Encapsulation?
>> [!SUCCESS]- Answer
>> **Abstraction** = Hide complexity (what). **Encapsulation** = Hide data (how).

> [!QUESTION] Q4: What is Polymorphism?
>> [!SUCCESS]- Answer
>> Same method name, **different implementations** in different classes.

> [!QUESTION] Q5: What is Method Overriding?
>> [!SUCCESS]- Answer
>> Child class provides **different implementation** of parent's method.

---

[[2-Classes-Objects|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[4-Types-of-Inheritance|Next →]]
