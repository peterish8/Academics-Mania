# 🧪 CSS Variables (Custom Properties)

## 🎯 **What are CSS Variables?**

> [!SUCCESS] **Definition**: Values defined once and reused throughout the document.
> The **DRY** (Don't Repeat Yourself) principle for CSS! ♻️

**Why use them?**
- Change a color in ONE place, and it updates everywhere.
- Essential for **Dark Mode** functionality.
- Makes code readable (`var(--main-color)` vs `#0056b3`).

---

## ⚙️ **Syntax**

### **1. 1. Declaration (Defining)**
> Variables are usually defined in the `:root` pseudo-class (global scope).
> **Must start with two dashes (`--`)**.

```css
:root {
    --primary-color: #007bff;
    --text-dark: #333333;
    --spacing-md: 16px;
}
```

### **2. Usage (Consuming)**
> Use the `var()` function to retrieve the value.

```css
button {
    background-color: var(--primary-color);
    padding: var(--spacing-md);
    color: white;
}

h1 {
    color: var(--text-dark);
}
```

---

## 🌗 **Use Case: Dark Mode**

> [!TIP] **How it works**: You just change the variable values!

```css
:root {
    --bg-color: white;
    --text-color: black;
}

/* When body has class="dark" */
body.dark {
    --bg-color: #121212;
    --text-color: white;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
}
```

---

## 🛡️ **Fallbacks**

> You can provide a backup value if the variable isn't found.
```css
color: var(--brand-color, blue); 
/* Uses blue if --brand-color is undefined */
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **--** = Custom CSS Property (like a private variable)
> - **:root** = The global container (like global variables in JS) 🌍
> - **var()** = The fetcher function 🐕

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What characters must CSS variable names start with?
> > [!SUCCESS]- Answer
> > Two hyphens: `--` (e.g., `--my-var`).

> [!QUESTION] **Q2**: Where is the best place to define global variables?
> > [!SUCCESS]- Answer
> > In the `:root` selector, which matches the highest-level element (usually `<html>`), making the variables available everywhere.

> [!QUESTION] **Q3**: How do you use a variable named `--main-color`?
> > [!SUCCESS]- Answer
> > `color: var(--main-color);`

> [!QUESTION] **Q4**: Variable values are case-sensitive. True or False?
> > [!SUCCESS]- Answer
> > **True**. `--Main-Color` and `--main-color` are different variables.

> [!QUESTION] **Q5**: Can JavaScript interact with CSS variables?
> > [!SUCCESS]- Answer
> > Yes! JavaScript can read and set CSS variables dynamically, which is great for theming (e.g., dynamic color pickers).

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
