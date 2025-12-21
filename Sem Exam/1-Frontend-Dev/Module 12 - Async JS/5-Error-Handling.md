# 🚨 Error Handling (Try / Catch)

## 🎯 **Managing Chaos**

> [!SUCCESS] **Goal**: When things break (network down, bad data), don't crash the app. Catch the error and show a nice message. 🛡️

---

## 🕸️ **Try / Catch Block**

> Wrap dangerous code in `try`. Handle failures in `catch`.

```javascript
async function getUser() {
    try {
        console.log("Fetching...");
        const res = await fetch('fake-url');
        const data = await res.json();
    } catch (error) {
        console.error("Oops! Something broke:", error.message);
        // Show UI error message here
    }
}
```

---

## 💣 **Throwing Custom Errors**

> You can manually trigger an error using `throw`.

```javascript
function checkAge(age) {
    if (age < 18) {
        throw new Error("Too young!"); // Stops execution immediately
    }
    return true;
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Try** = "Attempt this risky jump" 🤸
> - **Catch** = "Safety mat" 🧘 (Only runs if you fall)
> - **Throw** = "Abort Mission!" 🚀

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: If no error occurs in `try`, does `catch` run?
> > [!SUCCESS]- Answer
> > No. It is skipped completely.

> [!QUESTION] **Q2**: What object is passed to the `catch` block?
> > [!SUCCESS]- Answer
> > The Error object (usually containing `.message` and `.stack`).

> [!QUESTION] **Q3**: Can you nest try/catch blocks?
> > [!SUCCESS]- Answer
> > Yes, but it makes code messy. Bubbling errors up to a main handler is usually better.

> [!QUESTION] **Q4**: What keyword manually stops execution and creates an error?
> > [!SUCCESS]- Answer
> > `throw`.

> [!QUESTION] **Q5**: Does `catch` handle syntax errors?
> > [!SUCCESS]- Answer
> > No, because the code usually won't even parse/start running if there is a syntax error. It handles Runtime errors.

---

Back to: [[Sem Exam/Frontend-Dev/Module 12 - Async JS/README|Module 12 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
