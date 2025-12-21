# 🏗️ Hoisting

## 🎯 **What is Hoisting?**

> [!SUCCESS] **Definition**: JavaScript moves declarations to the top of their scope during the "Creation Phase".
> Allows you to use functions/variables *before* they are written in code.

---

## 📜 **Variable Hoisting**

### **`var`**
> Hoisted and initialized with `undefined`.
```javascript
console.log(a); // undefined (Valid! No error)
var a = 5;
```

### **`let` / `const`**
> Hoisted BUT uninitialized. In the **Temporal Dead Zone (TDZ)**.
```javascript
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 10;
```

---

## 🔨 **Function Hoisting**

### **Function Declarations**
> Hoisted fully! (Can call anywhere).
```javascript
hello(); // Works! "Hi"

function hello() {
    console.log("Hi");
}
```

### **Function Expressions (Arrow/Variables)**
> Treated like variables.
```javascript
greet(); // Error! greet is not a function (it's undefined)
var greet = () => console.log("Hi");
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Declarations** float to the top 🎈.
> - **Variables** leave their values behind (bring only the name).
> - **TDZ** = The danger zone for `let/const` ☠️.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What value does a hoisted `var` have?
> > [!SUCCESS]- Answer
> > `undefined`

> [!QUESTION] **Q2**: Why can't you access let/const before declaration?
> > [!SUCCESS]- Answer
> > They are in the **Temporal Dead Zone (TDZ)** until the code execution reaches their declaration line.

> [!QUESTION] **Q3**: Are Function Expressions hoisted?
> > [!SUCCESS]- Answer
> > No. Only the variable declaration (var) is hoisted, not the function definition assigned to it.

> [!QUESTION] **Q4**: Is Hoisting good practice?
> > [!SUCCESS]- Answer
> > Generally, **No**. Reliance on hoisting makes code confusing. Always declare variables/functions at the top or before usage.

> [!QUESTION] **Q5**: Does hoisting actually move code lines?
> > [!SUCCESS]- Answer
> > No. It's a mental model. Physically properties are set up in memory during the compile phase, but the code stays in place.

---

Back to: [[Sem Exam/Frontend-Dev/Module 11 - Modern JS/README|Module 11 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
