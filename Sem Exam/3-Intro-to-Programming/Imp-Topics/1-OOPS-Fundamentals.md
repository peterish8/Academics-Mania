# 1️⃣ OOPS Fundamentals

---

## 📌 What is Object-Oriented Programming?

> **Definition**: A programming paradigm based on the concept of **objects** which contain data (attributes) and code (methods).

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

Back to: [[Imp-Topics-Hub|ICP Topics Hub]]
