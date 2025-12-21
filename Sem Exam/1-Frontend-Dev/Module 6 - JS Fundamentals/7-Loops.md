# 🔄 Loops

## 🎯 **Repeating Actions**

> [!SUCCESS] **Concept**: Execute a block of code multiple times.
> "Do this 10 times." 🔁

---

## 1️⃣ **The `for` Loop**

> Standard loop. Control everything manually.
> `for (initialization; condition; update)`

```javascript
for (let i = 0; i < 5; i++) {
    console.log("Count:", i);
}
```

---

## 2️⃣ **The `while` Loop**

> Runs as long as condition is true.
> **Warning**: Can cause Infinite Loops if you forget to update! ⚠️

```javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++; // Don't forget this!
}
```

---

## 3️⃣ **Modern Loops (Cleaner!) 🌟**

### **For...Of (Arrays)**
> Best for iterating over arrays.

```javascript
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}
```

### **For...In (Objects)**
> Best for iterating over object keys.

```javascript
const user = { name: "John", age: 30 };
for (const key in user) {
    console.log(key, user[key]);
}
```

---

## 🛑 **Break & Continue**

- `break`: Stops the loop completely.
- `continue`: Skips current iteration and jumps to the next one.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **OF** = Arrays (Values) 📦
> - **IN** = Objects (Keys/Index) 🔑
> - **While** = "While you wait" (Condition based) ⏳

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Which loop is best for iterating over an Array's values?
> > [!SUCCESS]- Answer
> > `for...of`.

> [!QUESTION] **Q2**: What loop is best for iterating over an Object's properties?
> > [!SUCCESS]- Answer
> > `for...in`.

> [!QUESTION] **Q3**: What does the `continue` keyword do?
> > [!SUCCESS]- Answer
> > Skips the rest of the code in the current iteration and moves to the next iteration.

> [!QUESTION] **Q4**: How do you create an infinite loop?
> > [!SUCCESS]- Answer
> > `while(true) { ... }` or `for(;;) { ... }`. (Usually a bad idea without a break statement!).

> [!QUESTION] **Q5**: What happens if `i` starts at 0, the condition is `i < 3`, and `i` increments by 1?
> > [!SUCCESS]- Answer
> > The loop runs for values 0, 1, 2 (Total 3 times).

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
