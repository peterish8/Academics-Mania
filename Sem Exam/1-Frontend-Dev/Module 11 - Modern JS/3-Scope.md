# 🔭 Scope (Block, Function, Global)

## 🎯 **What is Scope?**

> [!SUCCESS] **Definition**: Determines where variables are accessible/visible.
> "Can I see variable X from here?" 👀

---

## 🌍 **1. Global Scope**

> Declared outside any function. Warning: Visible (and mutable) EVERYWHERE.

```javascript
let globalName = "I am Global";

function test() {
    console.log(globalName); // Works!
}
```

---

## 📦 **2. Function Scope (Local)**

> Variables declared inside a function are locked in there. `var`, `let`, and `const` all respect this.

```javascript
function secret() {
    let code = "123";
}
console.log(code); // ERROR: code is not defined
```

---

## 🧱 **3. Block Scope (New in ES6) 🌟**

> Variables declared inside `{ ... }` (if, for, while blocks).
> **Only `let` and `const` respect this!** `var` ignores it.

```javascript
if (true) {
    let blockSafe = "Hidden";
    var leaky = "I leaked out!";
}

console.log(leaky); // "I leaked out!" 😱
console.log(blockSafe); // ERROR (Correct behavior) ✅
```

---

## 🪜 **Scope Chain**

> If JS can't find a variable in the current scope, it looks UP to the parent.
> **Inner to Outer** direction only! (Outer cannot see Inner).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **let/const** = Block Respecters 🫡
> - **var** = The Rule Breaker 😈 (Ignores blocks)
> - **Chain** = Look Up ⬆️ (Never down)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What scope does `var` have?
> > [!SUCCESS]- Answer
> > Function Scope (or Global if outside function). It does NOT have Block scope.

> [!QUESTION] **Q2**: Can a child function access variables from its parent function?
> > [!SUCCESS]- Answer
> > Yes (Scope Chain / Lexical Scoping).

> [!QUESTION] **Q3**: Can a parent function access variables from its child function?
> > [!SUCCESS]- Answer
> > No. Scopes are private to the child.

> [!QUESTION] **Q4**: What happens if you declare a variable without any keyword (e.g., `x = 10`) inside a function?
> > [!SUCCESS]- Answer
> > It becomes an **Implicit Global** variable (BAD practice). In Strict Mode, this throws an error.

> [!QUESTION] **Q5**: Is `let` block scoped?
> > [!SUCCESS]- Answer
> > Yes.

---

Back to: [[Sem Exam/Frontend-Dev/Module 11 - Modern JS/README|Module 11 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
