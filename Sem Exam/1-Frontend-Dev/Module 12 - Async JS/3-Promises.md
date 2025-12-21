# 🤞 Promises & Chaining

## 🎯 **What is a Promise?**

> [!SUCCESS] **Definition**: An object representing the **eventual completion (or failure)** of an async operation.
> A "Receipt" for a future value. 🧾

---

## 🚥 **3 States**

1.  **Pending**: Work in progress... ⏳
2.  **Resolved (Fulfilled)**: Success! Data received. ✅
3.  **Rejected**: Failed! Error occurred. ❌

---

## 🛠️ **Creating a Promise**

```javascript
const myPromise = new Promise((resolve, reject) => {
    let success = true;
    if (success) {
        resolve("Good Job!");
    } else {
        reject("Oops!");
    }
});
```

---

## 🔗 **Consuming Promises (then/catch)**

> [!INFO] **Chaining**: `.then()` returns a NEW promise, allowing chains.

```javascript
myPromise
    .then(data => {
        console.log(data); // "Good Job!"
        return data + " Round 2";
    })
    .then(newData => {
        console.log(newData); // "Good Job! Round 2"
    })
    .catch(error => {
        console.log("Error:", error);
    })
    .finally(() => {
        console.log("I run no matter what.");
    });
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Resolve** = Success ✅
> - **Reject** = Fail ❌
> - **Then** = What's next? ➡️
> - **Catch** = Safety Net 🕸️

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What state is a promise in initially?
> > [!SUCCESS]- Answer
> > `Pending`.

> [!QUESTION] **Q2**: Can a promise change from Resolved back to Pending?
> > [!SUCCESS]- Answer
> > No. Promises are immutable once settled. They resolve/reject ONLY once.

> [!QUESTION] **Q3**: What does `.finally()` do?
> > [!SUCCESS]- Answer
> > Executes code regardless of the result (Success or Failure). Good for cleanup (hiding loaders).

> [!QUESTION] **Q4**: How do you run multiple promises in parallel?
> > [!SUCCESS]- Answer
> > `Promise.all([p1, p2, p3])`.

> [!QUESTION] **Q5**: If you throw an error inside `.then()`, where is it caught?
> > [!SUCCESS]- Answer
> > In the next `.catch()` block down the chain.

---

Back to: [[Sem Exam/Frontend-Dev/Module 12 - Async JS/README|Module 12 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
