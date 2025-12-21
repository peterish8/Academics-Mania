# 🚦 Sync vs Async Programming

## 🎯 **Synchronous (Sync)**

> [!SUCCESS] **Concept**: Code executes line by line.
> **Blocking**: The next line CANNOT start until the current line finishes.
> "Single-lane traffic." 🚗🚗🚗

```javascript
console.log("Start");
alert("Blocking!"); // User must click OK.
console.log("End"); // Waits... forever until click.
```

---

## ⏳ **Asynchronous (Async)**

> [!SUCCESS] **Concept**: Code starts a task and moves on immediately.
> **Non-Blocking**: "I'll get back to you when this is done."
> "Multi-lane traffic." 🛣️

```javascript
console.log("Start");

setTimeout(() => {
    console.log("Middle (2s later)");
}, 2000);

console.log("End"); // Runs immediately!

// Output: Start, End, Middle.
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Sync** = Telephone Call ☎️ (Must hold line).
> - **Async** = Text Message 💬 (Send and do other stuff).

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Is JavaScript synchronous or asynchronous by nature?
> > [!SUCCESS]- Answer
> > Synchronous (Single-threaded). But it uses Web APIs (like setTimeout) to achieve asynchronous behavior.

> [!QUESTION] **Q2**: What is a "Blocking" operation?
> > [!SUCCESS]- Answer
> > An operation that stops the execution of further code until it completes (like `alert` or a heavy loop).

> [!QUESTION] **Q3**: Why is Async important for web requests?
> > [!SUCCESS]- Answer
> > If web requests were synchronous, the entire browser would freeze (unresponsive) while waiting for the server to reply.

> [!QUESTION] **Q4**: Does `setTimeout` guarantee exact timing?
> > [!SUCCESS]- Answer
> > No. It guarantees a **minimum** delay, but depends on the Event Loop being free.

> [!QUESTION] **Q5**: In the example above, why does "End" print before "Middle"?
> > [!SUCCESS]- Answer
> > Because `setTimeout` is async. JS hands it off and continues to the next line ("End") immediately. The callback runs later.

---

Back to: [[Sem Exam/Frontend-Dev/Module 12 - Async JS/README|Module 12 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
