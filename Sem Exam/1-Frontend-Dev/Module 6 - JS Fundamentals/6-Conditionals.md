# 🔀 Conditional Statements

## 🎯 **Making Decisions**

> [!SUCCESS] **Concept**: Running different code based on different conditions.
> "If it rains, take an umbrella." ☂️

---

## 🌲 **if / else if / else**

```javascript
let score = 85;

if (score >= 90) {
    console.log("A Grade");
} else if (score >= 80) {
    console.log("B Grade");
} else {
    console.log("Try Again");
}
```

---

## 🚦 **Switch Statement**

> Cleaner for checking **one variable** against **many specific values**.
> Use `break` to stop fall-through!

```javascript
let day = "Monday";

switch (day) {
    case "Monday":
        console.log("Start of week");
        break;
    case "Friday":
        console.log("Weekend coming!");
        break;
    default:
        console.log("Regular day");
}
```

---

## ✅ **Truthy & Falsy Values**

> JavaScript converts values to boolean in if-statements.

**Falsy Values (evaluate to false):**
- `false`
- `0`
- `""` (Empty string)
- `null`
- `undefined`
- `NaN` (Not a Number)

**Everything else is Truthy!** (including `"0"`, `[]`, `{}`).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Switch needs Breaks**: Without `break`, code "falls through" to the next case. 🧱
> - **Falsy 6**: Memorize the 6 falsy values. Everything else is true.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What happens if you forget `break` in a switch statement?
> > [!SUCCESS]- Answer
> > The code continues to execute the next case blocks regardless of whether they match (Fall-through behavior).

> [!QUESTION] **Q2**: Is an empty array `[]` truthy or falsy?
> > [!SUCCESS]- Answer
> > **Truthy**. Only the empty string `""` is falsy.

> [!QUESTION] **Q3**: What is the `default` keyword in a switch statement?
> > [!SUCCESS]- Answer
> > Like `else`, it runs if NO other cases match.

> [!QUESTION] **Q4**: How many `else` blocks can an if-statement have?
> > [!SUCCESS]- Answer
> > Only one (at the very end). But it can have multiple `else if` blocks.

> [!QUESTION] **Q5**: Is `NaN` (Not a Number) truthy or falsy?
> > [!SUCCESS]- Answer
> > **Falsy**.

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
