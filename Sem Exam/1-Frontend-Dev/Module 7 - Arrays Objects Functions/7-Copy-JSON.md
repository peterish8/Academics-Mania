# 🐑 Shallow vs Deep Copy & JSON

## 🎯 **Why Copy?**

> [!SUCCESS] **Goal**: To create a duplicate of an object that can be modified WITHOUT affecting the original.

---

## 🌊 **1. Shallow Copy**

> Copies the top-level properties. Nested objects are still **Shared References!** ⚠️
> **Methods**: `Object.assign()`, `Spread Operator (...)`.

```javascript
const original = { name: "A", details: { age: 20 } };
const shallow = { ...original };

shallow.name = "B"; // Safe (Top level)
shallow.details.age = 30; // UNSAFE! Changes original too! 😱
```

---

## 🤿 **2. Deep Copy (The JSON Hack)**

> Copies **Everything**, removing all references.
> **Method**: `JSON.parse(JSON.stringify(obj))`

```javascript
const deep = JSON.parse(JSON.stringify(original));
deep.details.age = 99; // Safe! Original is untouched. 🛡️
```

**Limitations**:
- Removes Functions (Methods).
- Removes `undefined` values.
- Converts Dates to Strings.

---

## 🛠️ **Modern Deep Copy**

> `structuredClone(obj)` (New browser feature!)

```javascript
const distinct = structuredClone(original); // The best way nowadays!
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Shallow** = Skin Deep (Top layer only) 🧴
> - **Deep** = All the way down (Total clone) 🐑
> - **JSON** = The quick & dirty cloner (Lost functions) ⚡

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Does the Spread operator `...` create a deep copy?
> > [!SUCCESS]- Answer
> > No, it creates a **Shallow Copy**. Nested objects remain referenced.

> [!QUESTION] **Q2**: What happens to functions when you use `JSON.stringify()`?
> > [!SUCCESS]- Answer
> > They are stripped out/removed entirely from the resulting string.

> [!QUESTION] **Q3**: What is the modern built-in function for deep cloning?
> > [!SUCCESS]- Answer
> > `structuredClone()`.

> [!QUESTION] **Q4**: If an object has no nested objects, is a shallow copy enough?
> > [!SUCCESS]- Answer
> > Yes. If it's only one level deep (flat), shallow copy works perfectly as a full detached copy.

> [!QUESTION] **Q5**: How do you clone an array?
> > [!SUCCESS]- Answer
> > `const clone = [...originalArray];`

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
