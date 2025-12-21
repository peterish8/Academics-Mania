# 🎢 Event Loop & Microtasks

## 🎯 **The Flow**

> [!SUCCESS] **Concept**: How JS manages Async code on a Single Thread.

JavaScript has:
1.  **Call Stack**: Runs Sync code. LIFO.
2.  **Web APIs**: Browser features (Timer, Fetch, DOM).
3.  **Callback Queue**: Waiting room for `setTimeout`.
4.  **Microtask Queue**: VIP Waiting room for `Promises`.
5.  **Event Loop**: The Gatekeeper.

---

## 🎡 **How it Works**

> **Rule**: The Event Loop checks: "Is the Stack empty?"
> YES -> Check Microtasks (VIPs) -> Check Callback Queue (Normals).

```javascript
console.log("1");

setTimeout(() => console.log("2"), 0); // Callback Queue

Promise.resolve().then(() => console.log("3")); // Microtask (VIP)

console.log("4");

// Order: 1, 4, 3, 2
```
> **Explanation**:
> 1. Sync `1` runs.
> 2. `Timeout` sent to Web API.
> 3. `Promise` sent to Microtask Queue.
> 4. Sync `4` runs.
> 5. Stack Empty! Event Loop checks VIPs -> Run `3`.
> 6. VIPs Empty! Event Loop checks Normals -> Run `2`.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Stack** = Currently Working.
> - **Microtasks** = VIP Pass 🎟️ (Promises). Front of line.
> - **Callback Queue** = General Admission 🎫 (Timers). Back of line.
> - **Event Loop** = The Bouncer 🦍.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What runs first: A Promise or a setTimeout?
> > [!SUCCESS]- Answer
> > **Promise** (Microtask Queue has higher priority).

> [!QUESTION] **Q2**: Can the Event Loop push a callback to the Stack if the Stack is busy?
> > [!SUCCESS]- Answer
> > No. The Stack must be completely empty (Idle) before the Event Loop moves items from Queues.

> [!QUESTION] **Q3**: What happens if you block the Call Stack (e.g. infinite loop)?
> > [!SUCCESS]- Answer
> > The Event Loop stops spinning, callbacks never run, and the browser freezes.

> [!QUESTION] **Q4**: Where do DOM events (clicks) go?
> > [!SUCCESS]- Answer
> > Callback Queue (Task Queue).

> [!QUESTION] **Q5**: Is `queueMicrotask()` a real function?
> > [!SUCCESS]- Answer
> > Yes! It allows you to manually schedule code for the Microtask queue.

---

Back to: [[Sem Exam/Frontend-Dev/Module 12 - Async JS/README|Module 12 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
