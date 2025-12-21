# 🎩 Higher-Order Functions

## 🎯 **What is a HOF?**

> [!SUCCESS] **Definition**: A function that does at least one of these:
> 1. Takes one or more functions as arguments (Parameters). 📥
> 2. Returns a function as its result. 📤

---

## 🛠️ **Example 1: Taking a Function**

> Common in array methods and event handling.

```javascript
// 'map' is the HOF. It takes 'double' as an argument.
const nums = [1, 2, 3];
const double = x => x * 2;

const result = nums.map(double); 
```

---

## 🏭 **Example 2: Returning a Function**

> Creates specialized functions (Closures).

```javascript
function multiplier(factor) {
    // Returns a NEW function
    return function(x) {
        return x * factor;
    };
}

const double = multiplier(2);
const triple = multiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **HOF** = The Manager 👔 (Delegates work to callbacks)
> - **Callback** = The Employee 👷 (Does the actual work)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Is `console.log` a Higher-Order Function?
> > [!SUCCESS]- Answer
> > No. It takes data strings/objects, not functions, and returns undefined.

> [!QUESTION] **Q2**: Is `addEventListener` a HOF?
> > [!SUCCESS]- Answer
> > Yes! It takes a callback function as its second argument.

> [!QUESTION] **Q3**: Why are HOFs useful?
> > [!SUCCESS]- Answer
> > They allow abstraction. You can write generic logic (like "process this list") and pass specific behavior (like "multiply by 2") later.

> [!QUESTION] **Q4**: What do we call a function returned by another function that remembers its scope?
> > [!SUCCESS]- Answer
> > A **Closure**.

> [!QUESTION] **Q5**: Write a HOF `repeat` that runs a function `n` times.
> > [!SUCCESS]- Answer
> > ```javascript
> > function repeat(n, action) {
> >   for (let i = 0; i < n; i++) action(i);
> > }
> > ```

---

Back to: [[Sem Exam/Frontend-Dev/Module 8 - HOF Callbacks/README|Module 8 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
