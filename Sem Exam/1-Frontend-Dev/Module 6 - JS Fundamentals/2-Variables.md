# 📦 Variables: var, let, const

## 🎯 **What is a Variable?**

> [!SUCCESS] **Definition**: A "Box" to store data.
> You give the box a name, and put a value inside it.

---

## 🆚 **The Three Keywords**

| Feature | `var` (Old) 👴 | `let` (New) 🧒 | `const` (New) 🔒 |
|---------|----------------|----------------|------------------|
| **Scope** | Function Scope | Block Scope `{}` | Block Scope `{}` |
| **Update?** | Yes | Yes | **No** |
| **Redeclare?**| Yes | No | No |
| **Use Case**| Legacy code | Changing values | Constant values |

### **1. `var` (Legacy - AVOID)**
- Can be redeclared (bad!).
- Leaks out of blocks (loops/if statements).
- **Hoisted** (moved to top) with `undefined`.

### **2. `let` (The Standard Variable)**
- Use when the value **will change** (e.g., counters, loops).
- Scoped to the block `{}`.

### **3. `const` (The Constant)**
- Use when the value **will NOT change**.
- Must be assigned immediately.
- **Note**: Objects declared with const CAN differ (you can change properties, just not the whole object).

---

## 🛡️ **Block Scope vs Function Scope**

```javascript
// Function Scope (var)
function test() {
    if (true) {
        var x = 10;
    }
    console.log(x); // Works! Prints 10 (Leaked out of 'if')
}

// Block Scope (let/const)
function test2() {
    if (true) {
        let y = 10;
    }
    console.log(y); // ERROR! y is not defined (Stayed inside 'if')
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **var** = **Var**ey loose containment 🗑️
> - **let** = **Let** it change 🔄
> - **const** = **Const**ant 🧱
> - **Rule**: Default to `const`. Use `let` only if you need to reassign. Never use `var`.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Can you reassign a `const` variable?
> > [!SUCCESS]- Answer
> > No. `const x = 10; x = 20;` will throw a TypeError.

> [!QUESTION] **Q2**: What happens if you try to redeclare a `let` variable in the same scope?
> > [!SUCCESS]- Answer
> > SyntaxError: Identifier has already been declared.

> [!QUESTION] **Q3**: Does `var` respect the `{}` block of an if-statement?
> > [!SUCCESS]- Answer
> > No. `var` is function-scoped, so it "leaks" out of if-blocks and loops. `let` and `const` are block-scoped.

> [!QUESTION] **Q4**: Can you mutate the *contents* of a `const` array?
> > [!SUCCESS]- Answer
> > Yes! `const` prevents reassignment of the variable reference, but not the contents of the object/array. `const arr = []; arr.push(1)` is valid.

> [!QUESTION] **Q5**: What is the default value of a variable declared with `let` but not assigned?
> > [!SUCCESS]- Answer
> > `undefined`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
