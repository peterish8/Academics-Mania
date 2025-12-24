# 5️⃣ Constructors and Destructors

> [!INFO] **Definition: Constructor (`__init__`)**
> A special method that runs automatically when an object is created. It is used to initialize object attributes.

> [!INFO] **Definition: Destructor (`__del__`)**
> A special method that runs when an object is destroyed or garbage collected. Used for cleanup.

---

### Default Constructor

> **Goal**: Constructor with no parameters (except self).

```python
class Car:
    def __init__(self):  # Default constructor
        self.brand = "Unknown"
        print("Car created!")

# TEST
car = Car()  # "Car created!" printed
print(car.brand)  # Unknown
```

---

### Parameterized Constructor

> **Goal**: Constructor that accepts parameters to initialize object.

```python
class Student:
    def __init__(self, name, age):  # Parameterized
        self.name = name
        self.age = age

# TEST
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
print(s1.name, s1.age)  # Alice 20
print(s2.name, s2.age)  # Bob 22
```

---

### Constructor with Default Values

> **Goal**: Make some parameters optional.

```python
class Employee:
    def __init__(self, name, salary=50000):  # Default value
        self.name = name
        self.salary = salary

# TEST
e1 = Employee("John")           # Uses default salary
e2 = Employee("Jane", 75000)    # Custom salary
print(e1.salary)  # 50000
print(e2.salary)  # 75000
```

---

### Constructor Overloading (Python Way)

> **Note**: Python doesn't support multiple constructors. Use default arguments or *args.

```python
class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# TEST - "Overloaded" behavior
r1 = Rectangle()         # Uses defaults: 1x1
r2 = Rectangle(5)        # 5x1
r3 = Rectangle(5, 3)     # 5x3
print(r1.area(), r2.area(), r3.area())  # 1, 5, 15
```

---

## 📌 Destructor (__del__)

> **Definition**: Special method called when object is about to be destroyed (garbage collected).

```python
class File:
    def __init__(self, name):
        self.name = name
        print(f"File {name} opened")
    
    def __del__(self):  # Destructor
        print(f"File {self.name} closed")

# TEST
f = File("data.txt")   # "File data.txt opened"
del f                   # "File data.txt closed"
```

---

## 📊 Summary

| Type | Syntax | Purpose |
|------|--------|---------|
| **Default Constructor** | `def __init__(self):` | Initialize with fixed values |
| **Parameterized** | `def __init__(self, params):` | Initialize with custom values |
| **With Defaults** | `def __init__(self, p1, p2=val):` | Make params optional |
| **Destructor** | `def __del__(self):` | Cleanup when object is deleted |

---

## 🧠 Key Points
- **`__init__`** runs automatically on `ClassName()`
- **`__del__`** runs when `del object` or garbage collected
- Use default arguments for "overloading" effect
- Destructor is rarely needed (Python handles memory)

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is a Constructor?
>> [!SUCCESS]- Answer
>> Special method `__init__` that runs **automatically when object is created**.

> [!QUESTION] Q2: Default vs Parameterized Constructor?
>> [!SUCCESS]- Answer
>> **Default** = No parameters. **Parameterized** = Accepts parameters.

> [!QUESTION] Q3: What is `__del__`?
>> [!SUCCESS]- Answer
>> **Destructor** - called when object is deleted or garbage collected.

> [!QUESTION] Q4: Does Python support Constructor Overloading?
>> [!SUCCESS]- Answer
>> **No** - use default arguments instead.

> [!QUESTION] Q5: When does `__init__` run?
>> [!SUCCESS]- Answer
>> Automatically when you write `obj = ClassName()`.

---

[[4-Types-of-Inheritance|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[6-File-Handling|Next →]]
