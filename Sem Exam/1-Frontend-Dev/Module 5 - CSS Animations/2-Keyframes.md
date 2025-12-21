# 🎬 Keyframes & Animation Workflow

## 🎯 **What are Keyframes?**

> [!SUCCESS] **Definition**: A way to define animation "stages" or "waypoints".
> Allows complex animations without user interaction (unlike Transitions).

---

## 🛠️ **Defining the Animation (@keyframes)**

> You give it a name and define styles at various percentages.

```css
@keyframes slide-in {
    0% {
        transform: translateX(-100%); /* Start off-screen left */
        opacity: 0;
    }
    50% {
        opacity: 0.5;
    }
    100% {
        transform: translateX(0); /* End at normal position */
        opacity: 1;
    }
}
```

---

## 🏃 **Running the Animation**

> Use the `animation` property to call your keyframes.

```css
.box {
    /* name duration timing delay iteration direction fill-mode */
    animation: slide-in 2s ease-out 1s infinite alternate forwards;
}
```

### **Breakdown of Properties:**
1.  **name**: Match the `@keyframes` name.
2.  **duration**: How long one cycle takes (e.g., `2s`).
3.  **iteration-count**: How many times? (`1`, `3`, `infinite`).
4.  **direction**:
    - `normal`: 0% → 100%.
    - `reverse`: 100% → 0%.
    - `alternate`: 0% → 100% → 0% (Yo-yo effect).
5.  **fill-mode**:
    - `forwards`: Stay at the 100% style after finishing.
    - `backwards`: Revert to 0%.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **@keyframes** = The Script 📜
> - **animation** = The Actor 🎭
> - **forwards** = "Don't snap back!" 🚫
> - **infinite** = Loop forever ♾️

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What symbol is used to define keyframes?
> > [!SUCCESS]- Answer
> > The `@` symbol (`@keyframes`).

> [!QUESTION] **Q2**: Can you use `from` and `to` instead of percentages?
> > [!SUCCESS]- Answer
> > Yes! `from` = `0%` and `to` = `100%`.

> [!QUESTION] **Q3**: How do you make an animation run exactly 3 times?
> > [!SUCCESS]- Answer
> > Set `animation-iteration-count: 3;`.

> [!QUESTION] **Q4**: What does the `alternate` direction do?
> > [!SUCCESS]- Answer
> > Plays the animation forwards, then backwards, then forwards... creating a smooth loop.

> [!QUESTION] **Q5**: What property stops the element from resetting to its original state after animation?
> > [!SUCCESS]- Answer
> > `animation-fill-mode: forwards;`

---

Back to: [[Sem Exam/Frontend-Dev/Module 5 - CSS Animations/README|Module 5 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
