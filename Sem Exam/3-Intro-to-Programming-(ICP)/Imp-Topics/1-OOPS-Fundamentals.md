# 1️⃣ OOPS Fundamentals

> [!INFO] **Definition: Object-Oriented Programming (OOP)**
> A programming paradigm where code is organized around **objects** that contain both data (attributes) and methods (functions). It focuses on "what to do" rather than "how to do".

---

## 📌 Advantages of OOPS

| Advantage | Explanation |
|-----------|-------------|
| **Modularity** | Code organized into classes/objects |
| **Reusability** | Inheritance allows code reuse |
| **Data Hiding** | Encapsulation protects data |
| **Flexibility** | Polymorphism allows same interface, different behaviors |
| **Easy Maintenance** | Modular code is easier to fix |

---

## 📌 OOPS vs Procedural Programming

| Feature | OOPS | Procedural |
|---------|------|------------|
| **Focus** | Objects & Data | Functions & Logic |
| **Data** | Bundled with methods | Separate from functions |
| **Access** | Controlled (public/private) | Global, less control |
| **Reusability** | High (Inheritance) | Low (Copy-paste) |
| **Example** | Python, Java, C++ | C, Pascal |

---

## 💻 Quick Example

```python
# Procedural Style
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print(area)

# OOPS Style
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())
```

---

## 🧠 Key Points
- **OOPS** = Objects + Classes
- **4 Pillars**: Encapsulation, Abstraction, Inheritance, Polymorphism
- **Benefits**: Reusability, Modularity, Data Protection

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is OOP in one sentence?
>> [!SUCCESS]- Answer
>> Programming paradigm based on **objects** containing data and methods.

> [!QUESTION] Q2: Name the 4 pillars of OOPS?
>> [!SUCCESS]- Answer
>> Encapsulation, Abstraction, Inheritance, Polymorphism.

> [!QUESTION] Q3: Main advantage of OOPS over Procedural?
>> [!SUCCESS]- Answer
>> **Code Reusability** through inheritance and encapsulation.

> [!QUESTION] Q4: Give one example of OOP language?
>> [!SUCCESS]- Answer
>> Python, Java, C++, C#

> [!QUESTION] Q5: What is bundled together in an object?
>> [!SUCCESS]- Answer
>> **Data (attributes)** and **Code (methods)**.

---

[[0-Array-Problems|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[2-Classes-Objects|Next →]]
