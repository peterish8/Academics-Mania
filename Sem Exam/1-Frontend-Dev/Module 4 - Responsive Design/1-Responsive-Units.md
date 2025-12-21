# 📏 Responsive Units

## 🎯 **Why Units Matter**

> [!SUCCESS] **The Goal**: Avoid hard-coded sizes.
> Instead of saying "This box is 500px wide", say "This box is half the screen".

---

## 📊 **Absolute vs Relative Units**

### **1. Absolute Units (Fixed)**
- **px (Pixels)**: Takes up exactly that many dots on the screen.
    - **Pros**: Precise.
    - **Cons**: Does NOT scale. Bad for responsiveness. **Avoid using for container widths.**

### **2. Relative Units (Flexible) 🌟**
- **% (Percentage)**: Relative to the **Parent**.
    - `width: 50%` = Half of parent width.
- **vw / vh (Viewport Units)**: Relative to the **Window/Screen**.
    - `100vw` = 100% of Screen Width.
    - `100vh` = 100% of Screen Height (Perfect for Hero Sections!).
- **rem (Root EM)**: Relative to the HTML root font size (usually 16px).
    - `2rem` = 32px (16 * 2). **Best for Fonts/Padding**.
- **em**: Relative to the **Parent's Font Size**.
    - Can compound (cascade) and get messy. Use sparingly.

---

## 📐 **The `rem` vs `em` Debate**

> [!TIP] **Verdict**: Use `rem` for almost everything (font-size, padding, margin). It's predictable because it always looks at the Root (`html`).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **PX** = **P**ermanent e**X**act size (Rigid) 🧊
> - **VW** = **V**iewport **W**idth (Screen width) ↔️
> - **VH** = **V**iewport **H**eight (Screen height) ↕️
> - **REM** = **R**oot **EM** (Global font size) 🌳

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Which unit represents 1% of the viewport width?
> > [!SUCCESS]- Answer
> > `1vw`

> [!QUESTION] **Q2**: Why is `px` generally bad for container layouts?
> > [!SUCCESS]- Answer
> > It is fixed. On a small mobile screen, a `width: 800px` container will cause a horizontal scrollbar (breaking the layout).

> [!QUESTION] **Q3**: If the root font-size is 20px, how big is `2rem`?
> > [!SUCCESS]- Answer
> > **40px** (2 * 20px).

> [!QUESTION] **Q4**: Use a unit to make a section take up the full height of the screen.
> > [!SUCCESS]- Answer
> > `height: 100vh;`

> [!QUESTION] **Q5**: What is the difference between % and vw?
> > [!SUCCESS]- Answer
> > `%` is based on the **parent element**. `vw` is based on the **browser window**.

---

Back to: [[Sem Exam/Frontend-Dev/Module 4 - Responsive Design/README|Module 4 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
