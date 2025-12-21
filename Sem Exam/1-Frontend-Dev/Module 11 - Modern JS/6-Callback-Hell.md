# 🧶 Callback Hell & Readability

## 🎯 **The Problem**

> [!WARNING] **Pyramid of Doom**: Asynchronous operations that depend on each other (run strictly one after another).
> If you nested callbacks, code becomes unreadable triangle soup. 🍜

```javascript
// BAD CODE ❌
getData(function(a) {
    getMoreData(a, function(b) {
        getMoreData(b, function(c) {
            getMoreData(c, function(d) {
                console.log(d);
            });
        });
    });
});
```

---

## 💡 **The Solutions**

### **1. Modularize (Name your functions)**
> Extract functions instead of writing them inline.

### **2. Promises (ES6)**
> Flattens the callback chain. `then()` chaining.

### **3. Async/Await (ES8) 🌟**
> Write async code that looks synchronous. The goal!

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Triangle Shape** = DOOM ⚠️.
> - **Right-heavy code** = Bad code.
> - **Solution** = Flatten it (Promises/Async).

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What visual shape indicates Callback Hell?
> > [!SUCCESS]- Answer
> > A sideways pyramid or triangle (indentation growing to the right).

> [!QUESTION] **Q2**: Why is Callback Hell bad?
> > [!SUCCESS]- Answer
> > Hard to read, hard to debug, and error handling becomes complex (you handle errors in every single level).

> [!QUESTION] **Q3**: What feature replaced callbacks for async operations in 2015?
> > [!SUCCESS]- Answer
> > Promises.

> [!QUESTION] **Q4**: Does extracting functions solve the async problem?
> > [!SUCCESS]- Answer
> > No, it just makes the code cleaner. The logic is still callback-based. You usually need Promises to solve the control flow issue.

> [!QUESTION] **Q5**: Is `setTimeout` callback-based?
> > [!SUCCESS]- Answer
> > Yes, originally. But often wrapped in Promises in modern code.

---

Back to: [[Sem Exam/Frontend-Dev/Module 11 - Modern JS/README|Module 11 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
