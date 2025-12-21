# 🔗 Advanced Selectors (Combinators)

## 🎯 **What are Combinators?**

> [!SUCCESS] **Definition**: Symbols that explain the **relationship** between two selectors.
> "Select THIS only if it is inside/next to THAT."

---

## 🧩 **The 4 Combinators**

### **1. Descendant Selector (Space)**
> Selects ALL matching elements inside.
> **Symbol**: Space (` `)

```css
div p {
    color: blue;
}
```
> Selects **ALL** `<p>` tags inside `<div>`, no matter how deep (grandchildren included).

### **2. Child Selector (Greater Than)**
> Selects only **DIRECT** children.
> **Symbol**: `>`

```css
div > p {
    color: red;
}
```
> Selects only `<p>` tags that are **directly** inside `<div>`. Grandchildren are ignored.

### **3. Adjacent Sibling Selector (Plus)**
> Selects the **IMMEDIATELY** following element.
> **Symbol**: `+`

```css
h1 + p {
    font-weight: bold;
}
```
> Selects the `<p>` ONLY if it comes **right after** an `<h1>`.

### **4. General Sibling Selector (Tilde)**
> Selects **ALL** following siblings.
> **Symbol**: `~`

```css
h1 ~ p {
    color: green;
}
```
> Selects ALL `<p>` tags that come after `<h1>`, as long as they share the same parent.

---

## 🏷️ **Attribute Selectors**

> Select elements based on their attributes (href, src, type, etc.).

```css
/* Exact match */
input[type="text"] { ... }

/* Contains word */
[title~="flower"] { ... }

/* Starts with (e.g., https) */
a[href^="https"] { color: green; }

/* Ends with (e.g., .pdf) */
a[href$=".pdf"] { color: red; }
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Space** = Family Tree (Everyone inside) 🌳
> - **>** = Direct Kids Only 👶
> - **+** = Next Door Neighbor (Immediate) 🏠
> - **~** = All Younger Siblings (General) 👯‍♂️

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Which selector targets all `<p>` tags inside a `<div>`, even grandchildren?
> > [!SUCCESS]- Answer
> > Descendant selector: `div p` (Space).

> [!QUESTION] **Q2**: What does `ul > li` select?
> > [!SUCCESS]- Answer
> > Only the `<li>` elements that are **direct children** of the `<ul>`. It won't affect nested lists deeper down.

> [!QUESTION] **Q3**: How do you select all external links (starting with https)?
> > [!SUCCESS]- Answer
> > Attribute selector: `a[href^="https"]`.

> [!QUESTION] **Q4**: What does the `+` combinator do?
> > [!SUCCESS]- Answer
> > It selects an element that is placed **immediately after** the specified element.

> [!QUESTION] **Q5**: How do you style an Input only if it has `type="submit"`?
> > [!SUCCESS]- Answer
> > `input[type="submit"] { ... }`

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
