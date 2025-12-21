# 🛠️ Built-in HOF Methods

## 🎯 **Array Magic Methods**

> [!SUCCESS] **Goal**: Transform, filter, and analyze arrays without using loop boilerplate.
> Cleaner, shorter, and easier to read! ✨

Suppose we have:
```javascript
const users = [
    { name: "Alice", age: 25, active: true },
    { name: "Bob", age: 30, active: false },
    { name: "Charlie", age: 35, active: true }
];
```

---

## 🗺️ **1. map()**

> **Purpose**: Transform each item. Returns a **NEW Array** of same length.
> "Give me a list of just names."

```javascript
const names = users.map(user => user.name);
// ["Alice", "Bob", "Charlie"]
```

---

## 🔍 **2. filter()**

> **Purpose**: Select items that match a condition. Returns a **NEW Array** (can be smaller).
> "Give me active users."

```javascript
const activeUsers = users.filter(user => user.active);
// [{Alice...}, {Charlie...}]
```

---

## 💊 **3. reduce()**

> **Purpose**: Condense array to a **Single Value** (Sum, Average, Object).
> "Give me the total age."

```javascript
// acc = Accumulator (Running total)
// curr = Current Item
const totalAge = users.reduce((acc, curr) => acc + curr.age, 0);
// 90
```
> **Note**: The `0` at the end is the initial value of `acc`.

---

## 🔎 **4. find()**

> **Purpose**: Returns the **FIRST** item that matches. Returns **Item** or `undefined`.
> "Find Bob."

```javascript
const bob = users.find(user => user.name === "Bob");
// { name: "Bob"... }
```

---

## ✅ **5. some() & every()**

> Return **Boolean** (`true`/`false`).

- `some()`: At least one matches?
- `every()`: Do ALL match?

```javascript
const hasMinors = users.some(user => user.age < 18); // false
const allAdults = users.every(user => user.age >= 18); // true
```

---

## 🔄 **6. forEach()**

> **Purpose**: Run a function for each item. Returns **undefined**.
> Use for side effects (logging, saving to DB). **Cannot return a value**.

```javascript
users.forEach(user => console.log(user.name));
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Map** = Morph 🐛→🦋 (Same count, different shape)
> - **Filter** = Sieve 🍝 (Less items)
> - **Reduce** = Snowball ☃️ (Rolls into one)
> - **Find** = Detective 🕵️‍♂️ (Finds the one)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Does `map` modify the original array?
> > [!SUCCESS]- Answer
> > No! It returns a new array.

> [!QUESTION] **Q2**: What does `find` return if no item matches?
> > [!SUCCESS]- Answer
> > `undefined`.

> [!QUESTION] **Q3**: Can you break out of a `forEach` loop?
> > [!SUCCESS]- Answer
> > No! You cannot use `break` or `continue`. Use a regular `for...of` loop if you need to stop early.

> [!QUESTION] **Q4**: What is the second argument in `reduce(callback, initialValue)`?
> > [!SUCCESS]- Answer
> > The `initialValue` for the accumulator. If omitted, it uses the first array element.

> [!QUESTION] **Q5**: Which method checks if ALL elements satisfy a condition?
> > [!SUCCESS]- Answer
> > `every()`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 8 - HOF Callbacks/README|Module 8 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
