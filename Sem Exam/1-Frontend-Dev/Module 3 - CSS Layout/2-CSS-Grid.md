# ▦ CSS Grid

## 🎯 **What is CSS Grid?**

> [!SUCCESS] **Definition**: The **2-Dimensional** layout system.
> Handles **Rows** AND **Columns** at the same time. The most powerful layout tool in CSS. 🏗️

**Flexbox vs Grid**:
- **Flexbox**: Good for 1D (Navbars, lists).
- **Grid**: Good for 2D (Overall Page Layout, Photo Galleries).

---

## 🏗️ **Basic Syntax**

```css
.container {
    display: grid;
    /* Define Columns: 3 columns of equal width */
    grid-template-columns: 1fr 1fr 1fr; 
    /* Define Rows: 2 rows with fixed/auto height */
    grid-template-rows: 100px auto;
    /* Gap: Gutters between cells */
    gap: 10px;
}
```

---

## 📏 **The `fr` Unit**

> [!INFO] **Definition**: "Fraction". Represents a fraction of the available free space.
> `1fr 2fr` means the second column is twice as wide.

---

## 🗺️ **Grid Areas (The Visual Way)**

> Name your items and sketch the layout! 🎨

```css
.container {
    display: grid;
    grid-template-areas: 
        "header header header"
        "sidebar main main"
        "footer footer footer";
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

---

## ⚡ **Implicit vs Explicit Grid**

- **Explicit**: What you defined in `template-columns`.
- **Implicit**: New items automatically added (if you have more items than slots).
- Control auto rows: `grid-auto-rows: 100px;`

---

## 🔁 **Repeat Function**

> Save typing for repeating columns.

```css
/* Instead of 1fr 1fr 1fr 1fr */
grid-template-columns: repeat(4, 1fr);
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Grid** = Graph Paper 📉
> - **fr** = Share of the pie 🥧
> - **Gap** = Gutters (Space between cells) 🛣️
> - **Areas** = ASCII Art Layout (Visual naming) 🎨

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What CSS property turns on the Grid?
> > [!SUCCESS]- Answer
> > `display: grid;`

> [!QUESTION] **Q2**: What is the `fr` unit?
> > [!SUCCESS]- Answer
> > Fraction unit. It distributes available space proportionally (e.g., `1fr 1fr` is 50%-50%).

> [!QUESTION] **Q3**: How do you create a gap of 20px between all rows and columns?
> > [!SUCCESS]- Answer
> > `gap: 20px;`

> [!QUESTION] **Q4**: What function allows you to create 12 equal columns easily?
> > [!SUCCESS]- Answer
> > `repeat(12, 1fr)`

> [!QUESTION] **Q5**: Flexbox is 1D. What is Grid?
> > [!SUCCESS]- Answer
> > **2D** (Two-dimensional). It manages both columns and rows simultaneously.

---

Back to: [[Sem Exam/Frontend-Dev/Module 3 - CSS Layout/README|Module 3 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
