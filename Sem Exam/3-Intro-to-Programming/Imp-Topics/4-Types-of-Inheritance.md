# 4️⃣ Types of Inheritance

---

## 📌 1. Single Inheritance

> **Definition**: One child inherits from one parent.

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

Back to: [[Imp-Topics-Hub|ICP Topics Hub]]
