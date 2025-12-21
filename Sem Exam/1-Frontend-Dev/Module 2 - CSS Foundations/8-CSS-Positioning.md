# 📌 CSS Positioning

## 🎯 **The `position` Property**

> [!SUCCESS] **Definition**: Controls how an element is placed in the document flow.
> Moving things around from their normal spots! 🚚

---

## 📍 **The 5 Position Values**

### **1. Static (Default)**
> The normal behavior. Elements stack one after another.
- `top`, `left`, `right`, `bottom`, `z-index` have **NO EFFECT**.

### **2. Relative**
> Positioned relative to **its normal self**.
- It creates a "ghost" space where it WAS.
- Perfect for nudge adjustments.
- **Key Use**: Acts as the anchor/parent for `absolute` children.
```css
.box {
    position: relative;
    top: 20px; /* Moves down 20px from where it SHOULD be */
    left: 10px;
}
```

### **3. Absolute (The Rebel 😎)**
> Removed from the normal flow. No space is left behind.
> Positioned relative to the **nearest positioned ancestor** (usually a `relative` parent).
> If no parent is positioned, it positions relative to the `<body>`.
```css
.child {
    position: absolute;
    top: 0;
    right: 0; /* Sticks to top-right corner of parent */
}
```

### **4. Fixed (The Glue 🧴)**
> Sticks to the **Viewport** (Browser Window).
> Stays in place when you scroll.
- **Use Case**: Sticky navbars, "Back to Top" buttons.
```css
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
}
```

### **5. Sticky (The Hybrid 🚗)**
> Toggles between `relative` and `fixed`.
> Acts like `relative` until you scroll past it, then becomes `fixed` (stuck).
- **Requirement**: Must have a `top` value (e.g., `top: 0`).
```css
.header {
    position: sticky;
    top: 0;
}
```

---

## 🥞 **Z-Index (The Stack)**

> [!INFO] **Definition**: Controls vertical stacking order (which element is on top).
> **Only works on positioned elements** (relative, absolute, fixed, sticky).

```css
.modal {
    z-index: 1000; /* High number = On top */
}
.background {
    z-index: -1; /* Low number = Behind */
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Relative** = Relative to **Self** 🧍
> - **Absolute** = Relative to **Parent** 👪 (if parent is relative)
> - **Fixed** = Relative to **Window** 🪟 (Scrolled)
> - **Sticky** = Scroll then **Stick** 🍯

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Which position value removes the element from the document flow completely (closing the gap)?
> > [!SUCCESS]- Answer
> > **Absolute** and **Fixed**.

> [!QUESTION] **Q2**: Why isn't my `z-index` working?
> > [!SUCCESS]- Answer
> > You probably forgot to set `position` (relative, absolute, etc.). `z-index` does nothing on `position: static` (default) elements.

> [!QUESTION] **Q3**: What is the "nearest positioned ancestor"?
> > [!SUCCESS]- Answer
> > When using `absolute`, the element looks up the tree for the first parent that has `position` set to anything OTHER than static. If none found, it uses `<body>`.

> [!QUESTION] **Q4**: How do you make a navbar stick to the top only AFTER scrolling to it?
> > [!SUCCESS]- Answer
> > Use `position: sticky; top: 0;`.

> [!QUESTION] **Q5**: Which position is default for all elements?
> > [!SUCCESS]- Answer
> > `static`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
