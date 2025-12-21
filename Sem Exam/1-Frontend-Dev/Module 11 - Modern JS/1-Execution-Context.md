# ⚙️ Execution Context & Call Stack

## 🎯 **Execution Context**

> [!SUCCESS] **Definition**: The environment where JavaScript code runs.

**Two Phases:**
1.  **Creation Phase**: Memory is allocated for variables and functions (Hoisting).
2.  **Execution Phase**: Code is executed line-by-line.

---

## 🥞 **The Call Stack**

> [!INFO] **Concept**: JS is **Single Threaded** (One thing at a time).
> It uses a Stack (LIFO - Last In, First Out) to manage function calls.

1.  `Global()` context pushed.
2.  `funcA()` called -> Pushed on top.
3.  `funcB()` called inside A -> Pushed on top.
4.  `funcB()` finishes -> Popped off.
5.  `funcA()` finishes -> Popped off.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Stack** = Stack of Plates 🍽️ (Put on top, take from top).
> - **Context** = The "Room" the code runs in.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Is JavaScript Multi-threaded?
> > [!SUCCESS]- Answer
> > No. It is **Single-threaded** (can only do one task at a time in the main thread).

> [!QUESTION] **Q2**: What happens if you call a function that calls itself recursively without end?
> > [!SUCCESS]- Answer
> > **Stack Overflow**. Use up all available stack memory and crash.

> [!QUESTION] **Q3**: What is the "Global Execution Context"?
> > [!SUCCESS]- Answer
> > The default context created when the script starts (The `window` object in browsers).

> [!QUESTION] **Q4**: Does the Creation phase happen before or after Execution?
> > [!SUCCESS]- Answer
> > Before. This is why Hoisting works.

> [!QUESTION] **Q5**: What data structure does the JS engine use to track function calls?
> > [!SUCCESS]- Answer
> > A Stack (Call Stack).

---

Back to: [[Sem Exam/Frontend-Dev/Module 11 - Modern JS/README|Module 11 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
