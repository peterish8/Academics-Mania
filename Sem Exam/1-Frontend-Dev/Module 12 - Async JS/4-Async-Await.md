# ⚡ Async / Await

## 🎯 **Modern Async Syntax (ES2017)**

> [!SUCCESS] **Goal**: Read Async code as if it were Synchronous.
> No more `.then()` chains! ⛓️➡️🚫

---

## 🛠️ **Syntax**

1.  **`async`**: Put in front of a function. It AUTOMATICALLY returns a Promise.
2.  **`await`**: Put in front of a Promise. It **Pauses** execution until the Promise resolves.

```javascript
// The Old Way (Promises)
function getData() {
    fetch('url')
        .then(res => res.json())
        .then(data => console.log(data));
}

// The New Way (Async/Await)
async function getData() {
    const res = await fetch('url'); // Pause here 🛑
    const data = await res.json();  // Pause here 🛑
    console.log(data);
}
```

---

## 🧠 **Rules of Engagement**

- You can ONLY use `await` inside an `async` function (or top-level modules).
- If the promise rejects, `await` throws an error (Handle with try/catch).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Async** = "I promise to return a value" 🤞
> - **Await** = "I will wait for you" ⏳
> - **Syntactic Sugar** = Same logic under the hood (Promises), just sweeter syntax 🍬.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What does an `async` function always return?
> > [!SUCCESS]- Answer
> > A **Promise**. (Even if you return `10`, it becomes `Promise.resolve(10)`).

> [!QUESTION] **Q2**: Can you use `await` in a regular function?
> > [!SUCCESS]- Answer
> > No. It causes a Syntax Error. Must be `async`.

> [!QUESTION] **Q3**: Does `await` block the main thread?
> > [!SUCCESS]- Answer
> > No! It yields control back to the Event Loop/Browser, allowing other scripts/events to run while waiting. It only "blocks" the code *inside* that specific async function.

> [!QUESTION] **Q4**: How do you handle errors in Async/Await?
> > [!SUCCESS]- Answer
> > Wrap the code in a `try...catch` block.

> [!QUESTION] **Q5**: Is `async/await` faster than `.then()`?
> > [!SUCCESS]- Answer
> > No. Performance is roughly the same. It's purely for readability.

---

Back to: [[Sem Exam/Frontend-Dev/Module 12 - Async JS/README|Module 12 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
