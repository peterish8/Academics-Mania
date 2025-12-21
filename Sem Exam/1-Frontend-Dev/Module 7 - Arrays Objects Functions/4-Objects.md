# 🧶 Objects: Properties & Methods

## 🎯 **What is an Object?**

> [!SUCCESS] **Definition**: A collection of key-value pairs.
> Describes a real-world entity (e.g., a User, a Car).

```javascript
const car = {
    brand: "Tesla",      // Property
    model: "Model 3",
    start: function() {  // Method
        console.log("Vroom!");
    }
};
```

---

## 🔑 **Accessing Properties**

### **1. Dot Notation (`.`)**
> Standard & cleanest.
> `car.brand`

### **2. Bracket Notation (`[]`)**
> Use when key is dynamic (variable) or has spaces.
> `car["model"]`
> `car[myVariable]`

---

## 🛠️ **Methods**

> A function stored inside an object.

```javascript
const user = {
    name: "John",
    greet() { // Shorthand syntax
        console.log("Hi!");
    }
};
user.greet();
```

---

## 🗑️ **Deleting Properties**

> To remove a key-value pair completely.
> `delete user.name;`

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Dot** for known keys.
> - **Bracket** for weird keys (spaces) or variables. 🧐
> - **Method** = Function inside Object.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: How do you access a property named "full name" (with a space)?
> > [!SUCCESS]- Answer
> > Bracket notation: `obj["full name"]`. Dot notation `obj.full name` would error.

> [!QUESTION] **Q2**: What keyword removes a property from an object?
> > [!SUCCESS]- Answer
> > `delete`.

> [!QUESTION] **Q3**: How do you check if a key exists in an object?
> > [!SUCCESS]- Answer
> > `'key' in object` OR `object.hasOwnProperty('key')`.

> [!QUESTION] **Q4**: Can keys be numbers?
> > [!SUCCESS]- Answer
> > Yes, but they are converted to strings internally. Use bracket notation to access them: `obj[1]`.

> [!QUESTION] **Q5**: What happens if you access a property that doesn't exist?
> > [!SUCCESS]- Answer
> > It returns `undefined`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
