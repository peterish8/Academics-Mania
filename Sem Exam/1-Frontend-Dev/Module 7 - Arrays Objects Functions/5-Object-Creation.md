# 🏗️ Object Creation Patterns

## 🎯 **Why Patterns?**

> [!SUCCESS] **Goal**: If you need to create 100 User objects, you don't want to type `{...}` 100 times.
> Use a "Blueprint" function instead! 📐

---

## 🏭 **1. Factory Functions**

> A normal function that returns an object.
> **Pros**: Simple, no `this` confusion.
> **Cons**: Creates copies of methods (memory heavy).

```javascript
function createPerson(name) {
    return {
        name: name,
        greet() { console.log("Hi"); }
    };
}

const p1 = createPerson("Alice");
```

---

## 👷 **2. Constructor Functions**

> Uses `this` and `new` keyword.
> **Convention**: Capitalize name (`Person`).
> **Pros**: Memory efficient (if using Prototypes).

```javascript
function Person(name) {
    this.name = name;
    this.greet = function() { console.log("Hi"); };
}

const p2 = new Person("Bob");
```

> [!WARNING] **Crucial**: You MUST use `new`. If you forget it, `this` refers to the global window, causing nasty bugs! 🐛

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Factory** = Returns a product (Object) 🏭
> - **Constructor** = Builds with `this` (Blueprint) 👷‍♂️
> - **New** = The Magic Trigger 🪄

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What happens if you call a Constructor function without `new`?
> > [!SUCCESS]- Answer
> > It runs as a regular function. `this` becomes undefined (in strict mode) or global window, and it returns undefined instead of an object.

> [!QUESTION] **Q2**: Which pattern usually starts with a Capital Letter?
> > [!SUCCESS]- Answer
> > Constructor Functions (e.g., `function User()`).

> [!QUESTION] **Q3**: Can Arrow Functions be used as Constructors?
> > [!SUCCESS]- Answer
> > No, they crash because they don't have their own `this`.

> [!QUESTION] **Q4**: How does a Factory function return the object?
> > [!SUCCESS]- Answer
> > Explicitly using the `return {...}` statement.

> [!QUESTION] **Q5**: Which keyword allows Constructor functions to instantiate a new object?
> > [!SUCCESS]- Answer
> > `new`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
