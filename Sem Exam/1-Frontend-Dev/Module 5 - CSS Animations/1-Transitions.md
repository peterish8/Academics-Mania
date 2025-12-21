# 🔄 Transitions

## 🎯 **What are Transitions?**

> [!SUCCESS] **Definition**: Allows you to change property values smoothly over a given duration.
> Turning a "Snap" into a "Glide". ⛸️

---

## 🧩 **Syntax**

> `transition: property duration timing-function delay;`

```css
.button {
    background-color: blue;
    /* Watch the background-color change over 0.3s */
    transition: background-color 0.3s ease-in-out;
}

.button:hover {
    background-color: red; /* Trigger */
}
```

---

## ⏱️ **Timing Functions (The Feel)**

- `linear`: Constant speed (Robot). 🤖
- `ease` (Default): Slow start, fast middle, slow end (Natural). 🌿
- `ease-in`: Slow start. 🚀
- `ease-out`: Slow end (Braking). 🛑
- `cubic-bezier(n,n,n,n)`: Custom curve.

---

## 🎨 **Multiple Transitions**

> Comma-separated allow different speeds for different properties.

```css
transition: width 2s, height 4s;
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **State A** → **State B** (Needs a trigger like `:hover` to work).
> - **Ease** = Natural feel.
> - **Linear** = Robotic feel.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What CSS property is required for a transition to work?
> > [!SUCCESS]- Answer
> > You need two states (e.g., normal and `:hover`) and the `transition` property defined on the element.

> [!QUESTION] **Q2**: Which timing function represents a constant speed?
> > [!SUCCESS]- Answer
> > `linear`.

> [!QUESTION] **Q3**: Can you transition `display: none` to `display: block`?
> > [!SUCCESS]- Answer
> > **No**. Display is a discrete property (it's either there or not). You cannot animate it. Use `opacity` or `visibility` instead.

> [!QUESTION] **Q4**: What does the delay value do?
> > [!SUCCESS]- Answer
> > It waits for the specified time before STARTING the animation.

> [!QUESTION] **Q5**: Where should you put the `transition` property?
> > [!SUCCESS]- Answer
> > On the **Base Element** (e.g., `.box`), NOT on the hover state (`.box:hover`). If you put it on hover, it will transition "in" but snap back instantly when you mouse out.

---

Back to: [[Sem Exam/Frontend-Dev/Module 5 - CSS Animations/README|Module 5 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
