# 🍔 Responsive Navigation

## 🎯 **The Hamburger Menu**

> [!SUCCESS] **Concept**:
> **Desktop**: Links visible in a horizontal row.
> **Mobile**: Links hidden behind a button (☰). Clicking opens a drawer.

---

## 🛠️ **Logic (No JS version for CSS Exam)**

> You can use the "Checkbox Hack" or `:target` to do this with Pure CSS, but usually, simple JS is used. For this module, we focus on the **CSS Layout** change.

### **The CSS Strategy:**

```css
/* 1. Mobile Styles (Default) */
.nav-links {
    display: none; /* Hidden by default */
    flex-direction: column;
}

.hamburger {
    display: block; /* Show button */
}

/* 2. Desktop Styles (Enhancement) */
@media (min-width: 768px) {
    .nav-links {
        display: flex; /* Visible Row */
        flex-direction: row;
    }
    
    .hamburger {
        display: none; /* Hide button */
    }
}
```

---

## 🖱️ **The "Checkbox Hack" (Pure CSS Toggle)**

> [!TIP] **Advanced Trick**: Toggle menu without JavaScript using a hidden checkbox!

1.  **Input**: Hidden Checkbox.
2.  **Label**: The Hamburger Icon (connected to checkbox).
3.  **Selector**: `input:checked ~ .menu`.

```css
#toggle:checked ~ .nav-links {
    display: flex; /* Show menu when checked */
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Mobile**: Column Layout + Toggle Button.
> - **Desktop**: Row Layout + Hidden Button.
> - **Transition**: Use `display` or `transform` to show/hide.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What CSS property changes the nav from vertical to horizontal?
> > [!SUCCESS]- Answer
> > `flex-direction` (column to row).

> [!QUESTION] **Q2**: Why do we hide the hamburger icon on desktop?
> > [!SUCCESS]- Answer
> > Because there is enough screen space to show the links directly; the menu button is unnecessary.

> [!QUESTION] **Q3**: What is the "Checkbox Hack"?
> > [!SUCCESS]- Answer
> > A technique using a hidden checkbox and the sibling selector (`~`) to toggle CSS styles (like showing a menu) when the label is clicked.

> [!QUESTION] **Q4**: For accessibility, what attribute should a hamburger button have?
> > [!SUCCESS]- Answer
> > `aria-label="Toggle navigation"` or `aria-expanded="false/true"` to tell screen readers what the button does.

> [!QUESTION] **Q5**: If using Flexbox, how do you stack links on mobile?
> > [!SUCCESS]- Answer
> > `flex-direction: column;`

---

Back to: [[Sem Exam/Frontend-Dev/Module 4 - Responsive Design/README|Module 4 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
