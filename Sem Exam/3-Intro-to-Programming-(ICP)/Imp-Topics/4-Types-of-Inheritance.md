# 4️⃣ Types of Inheritance

> [!INFO] **Definition: Inheritance**
> The ability of a child class to acquire properties and methods from a parent class. Python supports 5 types of inheritance.

---

## 📌 1. Single Inheritance

> One child inherits from one parent.

```
    Parent
       ↓
    Child
```

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# TEST
dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Own method
```

---

## 📌 2. Multiple Inheritance

> **Definition**: One child inherits from multiple parents.

```
  Parent1    Parent2
      ↘      ↙
       Child
```

```python
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):  # Multiple parents
    def skill3(self):
        print("Coding")

# TEST
c = Child()
c.skill1()  # From Father
c.skill2()  # From Mother
c.skill3()  # Own
```

---

## 📌 3. Multilevel Inheritance

> **Definition**: Chain of inheritance (grandparent → parent → child).

```
  Grandparent
       ↓
    Parent
       ↓
    Child
```

```python
class Grandparent:
    def func1(self):
        print("Grandparent")

class Parent(Grandparent):
    def func2(self):
        print("Parent")

class Child(Parent):
    def func3(self):
        print("Child")

# TEST
c = Child()
c.func1()  # From Grandparent
c.func2()  # From Parent
c.func3()  # Own
```

---

## 📌 4. Hierarchical Inheritance

> **Definition**: Multiple children inherit from one parent.

```
       Parent
      /      \
  Child1   Child2
```

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# TEST
Dog().speak()  # Inherited
Cat().speak()  # Inherited
```

---

## 📌 5. Hybrid Inheritance

> **Definition**: Combination of multiple inheritance types.

```python
class A:
    def funcA(self):
        print("A")

class B(A):
    def funcB(self):
        print("B")

class C(A):
    def funcC(self):
        print("C")

class D(B, C):  # Multiple + Hierarchical
    def funcD(self):
        print("D")

# TEST
d = D()
d.funcA()  # From A
d.funcB()  # From B
d.funcC()  # From C
d.funcD()  # Own
```

---

## 📊 Summary Table

| Type | Structure | Example |
|------|-----------|---------|
| **Single** | A → B | Dog inherits Animal |
| **Multiple** | A, B → C | Child inherits Father, Mother |
| **Multilevel** | A → B → C | Grandparent → Parent → Child |
| **Hierarchical** | A → B, C | Dog, Cat inherit Animal |
| **Hybrid** | Mix of above | Complex family tree |

---

## 🧠 Key Points
- Python supports all types of inheritance
- **MRO** (Method Resolution Order) resolves conflicts in multiple inheritance
- Use `super()` to call parent methods

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is Single Inheritance?
>> [!SUCCESS]- Answer
>> One child class inherits from **one parent class**.

> [!QUESTION] Q2: How to do Multiple Inheritance in Python?
>> [!SUCCESS]- Answer
>> `class Child(Parent1, Parent2):`

> [!QUESTION] Q3: What is Multilevel Inheritance?
>> [!SUCCESS]- Answer
>> **Chain**: Grandparent → Parent → Child

> [!QUESTION] Q4: What is Hierarchical Inheritance?
>> [!SUCCESS]- Answer
>> **Multiple children** inherit from **one parent**.

> [!QUESTION] Q5: What is MRO?
>> [!SUCCESS]- Answer
>> **Method Resolution Order** - order in which Python looks for methods in inheritance hierarchy.

---

[[3-Four-Pillars-OOPS|← Previous]] | [[Imp-Topics-Hub|🏠 Hub]] | [[5-Constructors-Destructors|Next →]]
