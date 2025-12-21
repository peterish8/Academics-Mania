# 🎭 Pseudo-classes & Pseudo-elements

## 🎯 **What's the Difference?**

| Feature | Pseudo-class (`:`) | Pseudo-element (`::`) |
|---------|--------------------|-----------------------|
| **Symbol**| Single Colon `:` | Double Colon `::` |
| **Logic** | Selects a **STATE** of an element | Selects a **PART** of an element |
| **Example**| `a:hover` (When hovered) | `p::first-line` (First line of text) |

---

## 🖱️ **Common Pseudo-classes (`:`)**

> Styles that apply only when an element is in a specific **state**.

### **1. Link States (LVHA Rule)**
> Order matters! **L**ove **V**isits **H**ate **A**ngry.
1. `:link` (Unvisited)
2. `:visited` (Visited)
3. `:hover` (Mouse over - User Favorite! ✨)
4. `:active` (Clicked down)

```css
a:hover {
    color: red;
    text-decoration: underline;
}
```

### **2. Form States**
- `:focus`: When clicked/typed in (CRITICAL for accessibility!).
- `:checked`: For checkboxes/radios.
- `:disabled`: When input is disabled.
```css
input:focus {
    border-color: blue;
    outline: none; /* Replace default outline with border for aesthetics */
}
```

### **3. Structural Pseudo-classes**
> Select based on position in parent.
- `:first-child`: First element.
- `:last-child`: Last element.
- `:nth-child(n)`: The n-th element. (`odd`, `even`, `3`).

```css
/* Zebra striping for tables */
tr:nth-child(even) {
    background-color: #f2f2f2;
}
```

---

## 👻 **Common Pseudo-elements (`::`)**

> Creates "fake" elements or selects parts of text.

### **1. `::before` and `::after` (The Magic Makers 🪄)**
> Inserts content BEFORE or AFTER the element's content.
> **Must have `content: ""` property!**

```css
.required::after {
    content: " *";
    color: red;
}
```
> **Result**: Name *

### **2. Text Parts**
- `::first-letter`: Magazine drop-cap style.
- `::first-line`: Only the first line.
- `::selection`: When user highlights text.

```css
/* Change highlight color */
::selection {
    background-color: yellow;
    color: black;
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Class** (`:`) = Describes a **State** (Happy, Sad, Hovered)
> - **Element** (`::`) = Describes a **Piece** (An arm, a leg, a first-line)
> - **Before/After** = Needs **Content**! (Empty string `""` is fine)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the correct order for link pseudo-classes?
> > [!SUCCESS]- Answer
> > **LVHA**: :link, :visited, :hover, :active.

> [!QUESTION] **Q2**: Which property is MANDATORY for `::before` and `::after` to work?
> > [!SUCCESS]- Answer
> > `content`. Even if it's empty (`content: "";`), it must be defined.

> [!QUESTION] **Q3**: How do you select every OTHER row in a table?
> > [!SUCCESS]- Answer
> > `tr:nth-child(even)` or `tr:nth-child(odd)`.

> [!QUESTION] **Q4**: Should you use `:` or `::` for pseudo-elements like `after`?
> > [!SUCCESS]- Answer
> > Standard is `::after` (Double colon). Single colon works in old browsers for legacy reasons, but double is syntactically correct for elements.

> [!QUESTION] **Q5**: What does `:focus` do?
> > [!SUCCESS]- Answer
> > It applies styles when an element (input, link, button) is selected via click or Tab key navigation.

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
