# ➕ Operators & Expressions

## 🎯 **Doing Math & Logic**

> [!SUCCESS] **Concept**: Operators perform actions on values.

---

## 🔢 **Arithmetic Operators**

- `+` (Add), `-` (Subtract), `*` (Multiply), `/` (Divide)
- `%` (**Modulus**): Remainder of division.
- `**` (**Exponentiation**): Power of.
- `++` (Increment), `--` (Decrement).

```javascript
10 % 3; // Returns 1 (3 goes into 10 three times, 1 left over)
2 ** 3; // Returns 8 (2 * 2 * 2)
```

---

## ⚖️ **Comparison Operators**

> Return `true` or `false`.

| Operator  | Meaning                         | Example               |
| --------- | ------------------------------- | --------------------- |
| `==`      | Equal (Value only)              | `5 == "5"` (true) ⚠️  |
| `===`     | **Strict Equal** (Value + Type) | `5 === "5"` (false) ✅ |
| `!=`      | Not Equal                       | `5 != "5"` (false)    |
| `!==`     | **Strict Not Equal**            | `5 !== "5"` (true)    |
| `>` / `<` | Greater / Less than             |                       |

> [!TIP] **Rule**: ALWAYS use `===` and `!==`. Never trust type coercion.

---

## 🧠 **Logical Operators**

> Combining boolean values.

- `&&` (**AND**): Both must be true.
- `||` (**OR**): At least one must be true.
- `!` (**NOT**): Inverts value.

```javascript
true && false; // false
true || false; // true
!true; // false
```

---

## 🛠️ **Ternary Operator (The One-Liner IF)**

> Syntax: `condition ? valueIfTrue : valueIfFalse`

```javascript
let age = 20;
let status = age >= 18 ? "Adult" : "Minor";
```

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the result of `10 % 4`?
> > [!SUCCESS]- Answer
> > **2**. (4 goes into 10 twice, leaving a remainder of 2).

> [!QUESTION] **Q2**: Why is `===` better than `==`?
> > [!SUCCESS]- Answer
> > `===` checks both **Value** AND **Type**. `==` attempts to convert types (Type Coercion), which leads to bugs (e.g., `0 == false` is true).

> [!QUESTION] **Q3**: What does `!` do?
> > [!SUCCESS]- Answer
> > It inverts a boolean. `!true` becomes `false`.

> [!QUESTION] **Q4**: Rewrite this as a ternary: `if(x > 10) y = 'big'; else y = 'small';`
> > [!SUCCESS]- Answer
> > `y = x > 10 ? 'big' : 'small';`

> [!QUESTION] **Q5**: What is `"5" + 5` in JavaScript?
> > [!SUCCESS]- Answer
> > `"55"` (String concatenation). One of JS's quirks!

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
