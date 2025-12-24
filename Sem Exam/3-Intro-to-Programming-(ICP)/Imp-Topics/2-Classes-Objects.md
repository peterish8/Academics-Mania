# 2️⃣ Classes and Objects

> [!INFO] **Definition: Class**
> A blueprint or template that defines the structure (attributes) and behavior (methods) of objects.

> [!INFO] **Definition: Object**
> An instance of a class with actual values stored in memory. Each object is a separate entity.

```python
# Class = Blueprint
class Car:
    pass

# Object = Instance
my_car = Car()
```

---

## 📌 Class Variables vs Instance Variables

| Type | Belongs To | Shared? |
|------|------------|---------|
| **Class Variable** | Class itself | Yes, all objects share it |
| **Instance Variable** | Each object | No, unique to each object |

```python
class Student:
    school = "ABC School"  # Class variable (shared)
    
    def __init__(self, name):
        self.name = name   # Instance variable (unique)

# TEST
s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school, s2.school)  # Same: ABC School, ABC School
print(s1.name, s2.name)      # Different: Alice, Bob
```

---

## 📌 Methods

### Instance Method
> **Goal**: Method that operates on instance data using `self`.

```python
class Calculator:
    def __init__(self, value):
        self.value = value
    
    def add(self, num):       # Instance method
        return self.value + num

calc = Calculator(10)
print(calc.add(5))  # 15
```

### Constructor (__init__)
> **Goal**: Special method called automatically when object is created. Initializes attributes.

```python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

p = Person("John", 25)  # __init__ called automatically
print(p.name, p.age)
```

### The `self` Keyword
> **Definition**: Reference to the current instance. Used to access instance variables and methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name      # self.name = instance variable
    
    def bark(self):
        print(f"{self.name} says Woof!")  # self refers to current object

dog = Dog("Buddy")
dog.bark()  # Buddy says Woof!
```

---

## 📌 Object Operations

### Creating Objects
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create objects
book1 = Book("Python 101", "John")
book2 = Book("Java Basics", "Jane")
```

### Accessing Data Members
```python
print(book1.title)   # Python 101
print(book1.author)  # John
```

### Modifying Object Properties
```python
book1.title = "Advanced Python"  # Modify
print(book1.title)  # Advanced Python
```

---

## 🧠 Key Points
- **Class** = Blueprint, **Object** = Instance
- **Class Variable** = Shared, **Instance Variable** = Unique
- **`__init__`** = Constructor (runs on object creation)
- **`self`** = Reference to current object

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is a Class?
>> [!SUCCESS]- Answer
>> A **blueprint/template** for creating objects.

> [!QUESTION] Q2: What is an Object?
>> [!SUCCESS]- Answer
>> An **instance** of a class with actual values.

> [!QUESTION] Q3: Difference between Class Variable and Instance Variable?
>> [!SUCCESS]- Answer
>> Class Variable = **Shared** by all objects. Instance Variable = **Unique** to each object.

> [!QUESTION] Q4: What is `self`?
>> [!SUCCESS]- Answer
>> Reference to the **current object** being used.

> [!QUESTION] Q5: What does `__init__` do?
>> [!SUCCESS]- Answer
>> **Constructor** - runs automatically when object is created to initialize attributes.

---

[[1-OOPS-Fundamentals|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[3-Four-Pillars-OOPS|Next →]]
