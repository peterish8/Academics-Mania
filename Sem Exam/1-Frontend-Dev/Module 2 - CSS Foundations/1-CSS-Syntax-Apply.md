# 🎨 CSS Syntax & How to Apply Styles

## 🎯 **What is CSS?**

> [!SUCCESS] **Definition**: CSS = Cascading Style Sheets
> If HTML is the skeleton 🦴, CSS is the skin, clothes, and makeup! 💅

**📍 Key Points:**
- Controls **colors, fonts, layout, and spacing**.
- "Cascading" means rules fall down from top to bottom (and last rule wins usually).
- Separation of content (HTML) and presentation (CSS).

---

## 🧰 **CSS Syntax**

> [!INFO] **Formula**: Selector + { Property: Value; }

```css
/* Selector */
h1 {
    color: blue;        /* Declaration */
    font-size: 20px;    /* Property: Value; */
}
```
- **Selector**: What HTML element to style (`h1`).
- **Property**: What aspect to change (`color`).
- **Value**: What to change it to (`blue`).
- **Must end with a semicolon (;)**!

---

## 3️⃣ **Ways to Apply CSS**

### **1. Inline CSS (Not Recommended)**
> Written directly inside the HTML tag using the `style` attribute.
```html
<h1 style="color: red; font-size: 30px;">Hello</h1>
```
- **Pros**: Quick fix, overrides everything.
- **Cons**: Messy code, hard to maintain, no reusability.

### **2. Internal CSS**
> Written inside the `<head>` of the HTML file using the `<style>` tag.
```html
<head>
    <style>
        h1 {
            color: green;
        }
    </style>
</head>
```
- **Pros**: Good for single-page sites.
- **Cons**: Can't share styles across multiple pages.

### **3. External CSS (Best Practice! 🌟)**
> Written in a separate `.css` file and linked in the HTML.

**In `index.html`:**
```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

**In `style.css`:**
```css
h1 {
    color: blue;
}
```
- **Pros**: Keeps HTML clean, one file styles the WHOLE website, caching benefits.

---

## 🧪 **Browser Defaults (User Agent Styles)**

> [!INFO] **Note**: Every browser (Chrome, Firefox) has its own default styles.
> e.g., Browsers add default margin to `<body>` and `<h1>`.

**CSS Reset**: Many developers use a "Reset" to strip these defaults.
```css
/* Simple Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Inline** = **In** the line (Bad) 🛑
> - **Internal** = **In** the head (Okay) ⚠️
> - **External** = **Ex**tra file (Excellent) ✅

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the correct syntax for a CSS comment?
> > [!SUCCESS]- Answer
> > `/* This is a comment */`

> [!QUESTION] **Q2**: Which HTML tag is used to define internal CSS?
> > [!SUCCESS]- Answer
> > The `<style>` tag, placed inside the `<head>`.

> [!QUESTION] **Q3**: What is the HTML tag to link an external CSS file?
> > [!SUCCESS]- Answer
> > `<link rel="stylesheet" href="style.css">`

> [!QUESTION] **Q4**: Why is External CSS preferred over Inline CSS?
> > [!SUCCESS]- Answer
> > External CSS separates content from design, allows reusing styles across multiple pages (maintainability), and allows the browser to cache the CSS file (performance).

> [!QUESTION] **Q5**: What character must follow every CSS property declaration?
> > [!SUCCESS]- Answer
> > A semicolon `;`. e.g., `color: red;`

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
