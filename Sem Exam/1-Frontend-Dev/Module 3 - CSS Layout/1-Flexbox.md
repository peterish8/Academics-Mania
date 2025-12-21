# 💪 CSS Flexbox

## 🎯 **What is Flexbox?**

> [!SUCCESS] **Definition**: The Flexible Box Layout Module.
> Designed for **1-Dimensional** layouts (Row OR Column). Use it for alignment and distributing space.

---

## 🏗️ **The Architecture**

1.  **Flex Container** (Parent): `display: flex;`
2.  **Flex Items** (Children): The direct children inside.

```css
.container {
    display: flex; /* Activates Flexbox context */
}
```

---

## 🧭 **Parent Properties (Container)**

### **1. flex-direction (Axis)**
> Controls the direction of the Main Axis.
- `row` (Default): Left to Right.
- `column`: Top to Bottom.
- `row-reverse`: Right to Left.
- `column-reverse`: Bottom to Top.

### **2. justify-content (Main Axis Alignment)**
> Moves items along the main axis (usually Horizontal).
- `flex-start` (Default): Start of line.
- `flex-end`: End of line.
- `center`: Dead center.
- `space-between`: Max space between items (Edges touch sides).
- `space-around`: Equal space around items.

### **3. align-items (Cross Axis Alignment)**
> Moves items along the cross axis (usually Vertical).
- `stretch` (Default): Stretches to fill height.
- `flex-start`: Top.
- `flex-end`: Bottom.
- `center`: Middle (Vertical Centering!).

### **4. flex-wrap**
> Default: `nowrap` (Squeezes items).
> `wrap`: Items drop to next line if no space.

---

## 🧒 **Child Properties (Items)**

### **1. flex-grow**
> Controls how much the item grows to fill empty space.
> `0` (Default) = Don't grow.
> `1` = Grow evenly.

### **2. align-self**
> Overrides `align-items` for a SINGLE item.

```css
.item-2 {
    align-self: flex-end; /* This one drops to bottom */
}
```

---

## 🎯 **The Holy Grail: Centering a Div**

> [!TIP] **Memorize This!** Use on 90% of layouts.

```css
.parent {
    display: flex;
    justify-content: center; /* Horrorzontal */
    align-items: center;     /* Vertical */
    height: 100vh;           /* Full screen height */
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Justify** = Main Axis (Usually Left/Right) ↔️
> - **Align** = Cross Axis (Usually Top/Bottom) ↕️
> - **Space-Between** = Push to edges (Walls) 🧱
> - **Display: Flex** = Activates superpowers ⚡

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the default `flex-direction`?
> > [!SUCCESS]- Answer
> > `row` (Left to Right).

> [!QUESTION] **Q2**: Which property handles vertical alignment in a default row?
> > [!SUCCESS]- Answer
> > `align-items`.

> [!QUESTION] **Q3**: How do you make items go to the next line if they don't fit?
> > [!SUCCESS]- Answer
> > `flex-wrap: wrap;`

> [!QUESTION] **Q4**: Explain `justify-content: space-between`.
> > [!SUCCESS]- Answer
> > It pushes the first item to the start and the last item to the end, with equal spacing between the items in the middle.

> [!QUESTION] **Q5**: What does `flex: 1` do on a child?
> > [!SUCCESS]- Answer
> > It allows the item to grow and fill available empty space evenly.

---

Back to: [[Sem Exam/Frontend-Dev/Module 3 - CSS Layout/README|Module 3 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
