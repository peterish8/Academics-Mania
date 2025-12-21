# 🔒 Closures

## 🎯 **What is a Closure?**

> [!SUCCESS] **Definition**: A function bundled together with references to its surrounding state (lexical environment).
> **Plain English**: A function that "remembers" variables from where it was created, even after that place is gone. 🧠

---

## 🛠️ **How it Works**

1.  Outer function runs and returns an Inner function.
2.  Outer function finishes (popped off stack).
3.  Inner function still works and can access Outer's variables!

```javascript
function createCounter() {
    let count = 0; // Private variable
    
    return function() {
        count++; // It "remembers" count!
        return count;
    };
}

const myCounter = createCounter();
console.log(myCounter()); // 1
console.log(myCounter()); // 2
```

---

## 🛡️ **Why use them?**

1.  **Data Privacy**: Mimics private variables (like private in Java/C++).
2.  **State Management**: Maintaining state in async functions.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Closure** = Function + Backpack 🎒 (Carries its variables with it).
> - **Private** = Variables are hidden inside the closure bubble.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What creates a closure?
> > [!SUCCESS]- Answer
> > Defining a function inside another function.

> [!QUESTION] **Q2**: Do closures cause memory leaks?
> > [!SUCCESS]- Answer
> > They can if not used carefully, because they keep variables in memory that usually would be garbage collected.

> [!QUESTION] **Q3**: Can I access the `count` variable directly in the example above?
> > [!SUCCESS]- Answer
> > No! It is effectively private. You can only modify it via the returned function.

> [!QUESTION] **Q4**: What is the "Backpack" analogy?
> > [!SUCCESS]- Answer
> > When a function is returned, it carries a "backpack" containing all the variables that were present when it was born.

> [!QUESTION] **Q5**: Are closures common in JS?
> > [!SUCCESS]- Answer
> > Extremely. Used in callbacks, event listeners, HOFs, and module patterns.

---

Back to: [[Sem Exam/Frontend-Dev/Module 11 - Modern JS/README|Module 11 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
