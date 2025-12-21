# 🎨 Basic User Interface Animations

## 🎯 **Micro-Interactions**

> [!SUCCESS] **Definition**: Small, subtle animations that provide feedback.
> "I clicked this", "This is loading", "Pay attention here".

---

## 🔄 **The Loading Spinner (Classic)**

> Created using a border and rotation.

```css
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.loader {
    width: 50px;
    height: 50px;
    border: 5px solid #ccc; /* Light grey ring */
    border-top: 5px solid blue; /* Colored segment */
    border-radius: 50%; /* Circle */
    animation: spin 1s linear infinite; /* Spin forever */
}
```

---

## 🖱️ **Button Press Effect**

> Mimic a real button being pressed down.

```css
.btn {
    transition: transform 0.1s;
}

.btn:active {
    transform: scale(0.95); /* Shrinks slightly */
}
```

---

## 👁️ **Pulse Attention Grabber**

> Make a notification badge breathe.

```css
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); } /* Grow */
    100% { transform: scale(1); }
}

.badge {
    animation: pulse 2s infinite;
}
```

---

## 💡 **Performance Tip**

> [!WARNING] **Don't Animate layout properties!**
> Avoid animating `width`, `height`, `top`, `left`. They cause "Reflow" (laggy).
> **DO Animate**: `transform` (scale, rotate, translate) and `opacity`. They use the GPU (Hardware Acceleration). 🚀

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Why use `transform` instead of `width` for animations?
> > [!SUCCESS]- Answer
> > `transform` is handled by the GPU (Graphics Card), making it smoother (60fps) and avoiding heavy browser layout recalculations.

> [!QUESTION] **Q2**: How do you create a perfect circle?
> > [!SUCCESS]- Answer
> > `border-radius: 50%;` (assuming width = height).

> [!QUESTION] **Q3**: What pseudo-class triggers when a user CLICKS a button?
> > [!SUCCESS]- Answer
> > `:active`

> [!QUESTION] **Q4**: How do you make an animation constant speed (no acceleration)?
> > [!SUCCESS]- Answer
> > Use the `linear` timing function.

> [!QUESTION] **Q5**: Can you pause an animation on hover?
> > [!SUCCESS]- Answer
> > Yes! `animation-play-state: paused;` inside a `:hover` rule.

---

Back to: [[Sem Exam/Frontend-Dev/Module 5 - CSS Animations/README|Module 5 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
