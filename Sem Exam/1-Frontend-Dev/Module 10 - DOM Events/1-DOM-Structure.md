# 🌳 DOM Structure & Hierarchy

## 🎯 **What is the DOM?**

> [!SUCCESS] **Definition**: Document Object Model.
> The browser converts your HTML code into a **Tree of Objects** that JavaScript can interact with.

---

## 🌲 **The Tree Structure**

- **Window**: The browser tab (Global parent).
  - **Document**: The web page.
    - **html** (Root)
      - **head**
      - **body**
        - **div**
          - **h1**
          - **p**

> Every tag, text, and attribute is a **Node** in this tree.

---

## 🪜 **Navigating the Tree**

You can walk up and down the tree relative to a selected element.

- `parentElement`: Go up ⬆️
- `children`: Go down (all kids) ⬇️
- `firstElementChild`: First kid 👶
- `nextElementSibling`: Next neighbor ➡️
- `previousElementSibling`: Previous neighbor ⬅️

```javascript
const box = document.querySelector('.box');
const parent = box.parentElement;
const nextBox = box.nextElementSibling;
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **DOM** = The Bridge between JS and HTML 🌉
> - **Tree** = Upside down (Root at top) 🌲
> - **Node** = Every single piece (Element, Text, Comment) 🍂

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the root object of the browser/DOM?
> > [!SUCCESS]- Answer
> > The `window` object. (The `document` is just a property of the window).

> [!QUESTION] **Q2**: What property accesses the direct children of an element?
> > [!SUCCESS]- Answer
> > `.children` (returns an HTMLCollection).

> [!QUESTION] **Q3**: Does `.children` include text nodes (whitespace)?
> > [!SUCCESS]- Answer
> > No. `.children` only refers to Element nodes (tags). `.childNodes` includes text/whitespace.

> [!QUESTION] **Q4**: How do you select the `<body>` tag in JS?
> > [!SUCCESS]- Answer
> > `document.body`

> [!QUESTION] **Q5**: What is the difference between `parentElement` and `parentNode`?
> > [!SUCCESS]- Answer
> > They are almost identical. `parentElement` returns null if the parent is not an element (rare), but usually safe to use either.

---

Back to: [[Sem Exam/Frontend-Dev/Module 10 - DOM Events/README|Module 10 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
