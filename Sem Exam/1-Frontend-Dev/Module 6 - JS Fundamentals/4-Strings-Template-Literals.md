# 📝 Strings & Template Literals

## 🎯 **Working with Text**

> [!SUCCESS] **Definition**: A sequence of characters used to represent text.

---

## 🧵 **String Creating**

> You can use `'Single Quotes'`, `"Double Quotes"`, or `` `Backticks` ``.

```javascript
const name = "John"; // Standard
const job = 'Developer'; // Also Standard
```

---

## ✨ **Template Literals (Backticks)**

> The modern superpower for strings! Introduced in ES6.
> Allows **Embedded Variables** and **Multi-line Strings**.

```javascript
const age = 25;

// Old Way (Concatenation Hell 🤮)
const text = "Hello, my name is " + name + " and I am " + age + " years old.";

// New Way (Interpolation 😍)
const textNew = `Hello, my name is ${name} and I am ${age} years old.`;
```

**Multi-line Support:**
```javascript
const html = `
    <div>
        <h1>Title</h1>
        <p>Text</p>
    </div>
`;
```

---

## 🧰 **Common String Methods**

> Strings are immutable, so methods return a NEW string.

- `.length`: Property, returns character count.
- `.toUpperCase()` / `.toLowerCase()`: Change case.
- `.indexOf("text")`: Find position.
- `.includes("text")`: Returns `true`/`false`.
- `.slice(start, end)`: Cut a part out.
- `.split(" ")`: Convert to Array.
- `.replace("old", "new")`: Replace content.

```javascript
let text = "Hello World";
console.log(text.length); // 11
console.log(text.toUpperCase()); // "HELLO WORLD"
console.log(text.includes("World")); // true
console.log(text.split(" ")); // ["Hello", "World"]
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **${}** = The Interpolation Placeholder (Money stays inside curly braces 💰)
> - **Backticks** = The magic wand for multi-line and vars 🪄

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What characters wrap a Template Literal?
> > [!SUCCESS]- Answer
> > Backticks ( ` ).

> [!QUESTION] **Q2**: How do you insert a variable inside a template literal?
> > [!SUCCESS]- Answer
> > Using the syntax `${variableName}`.

> [!QUESTION] **Q3**: Does `.toUpperCase()` change the original string?
> > [!SUCCESS]- Answer
> > No. Strings are immutable. It returns a *new* string with the changes.

> [!QUESTION] **Q4**: How do you convert a string "a,b,c" into an array?
> > [!SUCCESS]- Answer
> > `string.split(",")`.

> [!QUESTION] **Q5**: What method checks if a string contains a specific word?
> > [!SUCCESS]- Answer
> > `.includes("word")`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
