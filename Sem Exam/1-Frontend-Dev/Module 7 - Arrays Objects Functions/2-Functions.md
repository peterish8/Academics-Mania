# 🔨 Function Types: Normal vs Arrow

## 🎯 **What are Functions?**

> [!SUCCESS] **Definition**: Reusable blocks of code.
> "Write once, run many times."

---

## 📜 **1. Function Declaration (Normal)**

> Traditional way. Hoisted (Can be called BEFORE it's defined).

```javascript
// Valid
sayHello(); 

function sayHello() {
    console.log("Hello!");
}
```

---

## 🏹 **2. Arrow Functions (ES6)**

> Modern syntax. **NOT Hoisted**. Has no `this` context (useful for callbacks).

```javascript
// Basic
const add = (a, b) => {
    return a + b;
};

// Implicit Return (One liner magic) ✨
const multiply = (a, b) => a * b;

// One Argument (No parenthesis needed)
const greet = name => console.log(`Hi ${name}`);
```

---

## 🆚 **Comparison**

| Feature | Declaration | Arrow Function |
|---------|-------------|----------------|
| **Syntax** | Verbose | Concise |
| **Hoisting** | Yes (Run before define) | No (Define first!) |
| **`this`** | Dynamic (Caller context) | Static (Parent context) |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Declaration** = Old School (Reliable, Hoisted) 👴
> - **Arrow** = New School (Short, Modern, No `this` pain) 🏹

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Can you omit the `return` keyword in Arrow Functions?
> > [!SUCCESS]- Answer
> > Yes, but ONLY if the code block is a single expression on one line (without curly braces).

> [!QUESTION] **Q2**: Are Arrow Functions hoisted?
> > [!SUCCESS]- Answer
> > No. You must define them before calling them.

> [!QUESTION] **Q3**: How do arrow functions handle `this`?
> > [!SUCCESS]- Answer
> > They do not have their own `this`. They inherit `this` from the surrounding scope (lexical scoping).

> [!QUESTION] **Q4**: Can you use Arrow Functions as Constructors (with `new`)?
> > [!SUCCESS]- Answer
> > No! Doing so throws an Error.

> [!QUESTION] **Q5**: Rewrite `function(a) { return a + 1; }` as an arrow function.
> > [!SUCCESS]- Answer
> > `a => a + 1`

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
