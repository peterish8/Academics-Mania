# 🧬 Data Types: Primitive & Reference

## 🎯 **The Two Categories**

> [!SUCCESS] **Concept**: How JavaScript stores data.
> **Primitives**: Stored directly in the stack (Simple).
> **Reference**: Stored in the heap, accessed via pointer (Complex).

---

## 🧱 **1. Primitive Types (7 Types)**
> Immutable (Cannot be changed, only replaced). Passed by **Value**.

1.  **String**: `"Hello"`
2.  **Number**: `123`, `5.5`
3.  **Boolean**: `true`, `false`
4.  **Undefined**: Variable declared but empty.
5.  **Null**: Intentionally empty.
6.  **Symbol**: Unique identifier (Advanced).
7.  **BigInt**: Huge numbers.

```javascript
let a = 10;
let b = a; // Copy value 10
a = 20;
console.log(b); // 10 (b didn't change!)
```

---

## 🔗 **2. Reference Types (Objects)**
> Mutable. Passed by **Reference** (Address).

1.  **Object**: `{ name: "John" }`
2.  **Array**: `[1, 2, 3]`
3.  **Function**

```javascript
let x = { name: "John" };
let y = x; // Copy address (pointer)
x.name = "Doe";
console.log(y.name); // "Doe" (y changed too! Both point to same room)
```

---

## ❓ **Typeof Operator**

> Check what data type something is.

```javascript
typeof "Hello" // "string"
typeof 42      // "number"
typeof true    // "boolean"
typeof undefined // "undefined"
typeof null    // "object" (Wait, what? A famous JS bug! 🐛)
typeof []      // "object"
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Primitives** = Photocopies 📄 (Changing original doesn't hurt copy)
> - **References** = Shared Google Doc 📝 (Anyone with link sees changes)
> - **NNSSBBU** = **N**ull, **N**umber, **S**tring, **S**ymbol, **B**oolean, **B**igInt, **U**ndefined.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What does `typeof null` return?
> > [!SUCCESS]- Answer
> > `"object"`. This is a historical bug in JavaScript that was never fixed to avoid breaking old websites.

> [!QUESTION] **Q2**: Is an Array a primitive type?
> > [!SUCCESS]- Answer
> > No, Arrays are Reference types (technically special Objects).

> [!QUESTION] **Q3**: What is the difference between `undefined` and `null`?
> > [!SUCCESS]- Answer
> > `undefined` means a variable has been declared but not assigned a value (JavaScript does this). `null` is an assignment value that means "no value" (Developers do this intentionally).

> [!QUESTION] **Q4**: If `let a = [1]; let b = a; b.push(2);`, what is `a`?
> > [!SUCCESS]- Answer
> > `[1, 2]`. Since arrays are reference types, `b` points to the same array as `a`.

> [!QUESTION] **Q5**: Are strings mutable in JavaScript?
> > [!SUCCESS]- Answer
> > No. Strings are primitive and immutable. modifying a string creates a NEW string. `str[0] = "X"` does nothing.

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
