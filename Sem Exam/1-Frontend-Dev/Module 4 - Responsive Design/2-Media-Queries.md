# 📶 Media Queries & Breakpoints

## 🎯 **What is a Media Query?**

> [!SUCCESS] **Definition**: A CSS rule that allows you to apply different styles based on device characteristics (mostly width).
> "IF screen is small, THEN make font smaller."

---

## ⚙️ **Syntax**

> [!INFO] **The Rule**: `@media (condition) { rules }`

```css
/* Default (Desktop/Global) Styles */
body {
    background-color: blue;
}

/* Screen is 600px wide OR LESS */
@media (max-width: 600px) {
    body {
        background-color: red;
    }
}
```

---

## 📱 **Common Breakpoints**

> Breakpoints are the specific widths where your layout "breaks" or changes.

| Device | Width Range | Breakpoint Example |
|--------|-------------|--------------------|
| **Phone** | Small (<600px) | `max-width: 600px` |
| **Tablet** | Medium (600-900px) | `max-width: 900px` |
| **Desktop**| Large (>900px) | `min-width: 900px` |

---

## 🏗️ **Strategic Approach**

> Don't target specific devices (iPhone 12 vs 13). Target **content breaking points**.
> If your text line gets too long, add a breakpoint.
> If your 3-column grid looks squished, drop to 1-column.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **@media** = The "Condition" Wrapper 🎁
> - **max-width** = "Up to this size" (Mobile adaptation) 📉
> - **min-width** = "From this size up" (Desktop adaptation) 📈

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What does `@media (max-width: 500px)` mean?
> > [!SUCCESS]- Answer
> > The styles inside will apply ONLY if the viewport is 500px wide or **narrower**.

> [!QUESTION] **Q2**: Should media queries go at the top or bottom of your CSS file?
> > [!SUCCESS]- Answer
> > **Bottom**. Because of the "Cascade", later rules override earlier ones. If you put them at the top, your default styles might overwrite them.

> [!QUESTION] **Q3**: Can you change font-size inside a media query?
> > [!SUCCESS]- Answer
> > Yes, you can change ANY css property (color, display, width, etc.).

> [!QUESTION] **Q4**: Essential meta tag required for media queries to work on phones?
> > [!SUCCESS]- Answer
> > `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

> [!QUESTION] **Q5**: What is a "Breakpoint"?
> > [!SUCCESS]- Answer
> > A specific screen width (pixel value) where the layout is programmed to change via a media query.

---

Back to: [[Sem Exam/Frontend-Dev/Module 4 - Responsive Design/README|Module 4 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
