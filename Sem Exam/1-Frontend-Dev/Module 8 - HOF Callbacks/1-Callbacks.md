# 🤙 Callback Concepts

## 🎯 **What is a Callback?**

> [!SUCCESS] **Definition**: A function passed as an argument to another function.
> "Don't call me, I'll call you." 📞

**Why?**
- To run code **AFTER** something finishes (e.g., download complete).
- To make a function generic (reusable).

---

## ⚙️ **How it Works**

1.  Create a function (`myCallback`).
2.  Pass it **without parenthesis** to another function.
3.  The other function executes it later.

```javascript
function greet(name) {
    console.log(`Hello ${name}`);
}

function processInput(callback) {
    const name = "Alice";
    callback(name); // Executing the callback here!
}

processInput(greet); // Pass 'greet', don't run 'greet()'
```

---

## 🔄 **Synchronous vs Asynchronous Callbacks**

- **Sync**: Runs immediately (e.g., Array methods).
- **Async**: Runs later (e.g., `setTimeout`, API calls).

```javascript
// Async Example
setTimeout(() => {
    console.log("I ran after 2 seconds!");
}, 2000);
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Callback** = The Guest 🙋‍♂️
> - **HOF** = The Host 🏠
> - **No ()** = When passing, drop the parenthesis! Passing references, not results.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Why don't we use parenthesis when passing a callback? e.g., `func(callback)` vs `func(callback())`?
> > [!SUCCESS]- Answer
> > `callback()` executes immediately and passes the RESULT. `callback` passes the function definition itself so it can be run later.

> [!QUESTION] **Q2**: Is `setTimeout` synchronous or asynchronous?
> > [!SUCCESS]- Answer
> > Asynchronous. It schedules code to run later.

> [!QUESTION] **Q3**: Can a callback accept arguments?
> > [!SUCCESS]- Answer
> > Yes! The Higher-Order function calls the callback and can pass data into it (like the `name` example above).

> [!QUESTION] **Q4**: What is Callback Hell?
> > [!SUCCESS]- Answer
> > Nested callbacks inside callbacks (triangle shape code), making it hard to read and debug.

> [!QUESTION] **Q5**: Is an event listener (like `click`) a callback?
> > [!SUCCESS]- Answer
> > Yes! `btn.addEventListener('click', myFunction)` uses `myFunction` as a callback to run when the click happens.

---

Back to: [[Sem Exam/Frontend-Dev/Module 8 - HOF Callbacks/README|Module 8 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
