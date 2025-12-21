# 🧮 Specificity & Inheritance

## 🧬 **CSS Inheritance**

> [!SUCCESS] **Definition**: Some properties are passed down from parent to children.
> "Like father, like son!" 👨‍👦

**Inherited Properties** (Mostly text-related):
- `color`
- `font-family`
- `font-size`
- `text-align`
- `line-height`

**Non-Inherited Properties** (Box-model related):
- `width`, `height`
- `margin`, `padding`
- `border`

**Forcing Inheritance**:
```css
button {
    font-family: inherit; /* Forces button to use parent's font */
}
```

---

## ⚔️ **Specificity (The "War" of Styles)**

> [!WARNING] **The Conflict**: What happens if two rules target the SAME element?
> **The Browser calculates a score**. The highest score wins! 🏆

### **The Scoring System** 🔢

| Selector Type | Score (Weight) | Example |
|---------------|----------------|---------|
| **Inline Style** | 1000 | `style="color: red"` |
| **ID** Selector | 100 | `#navbar` |
| **Class**, Pseudo-class | 10 | `.btn`, `:hover` |
| **Tag** (Type) Selector | 1 | `div`, `h1` |
| **Universal** (*) | 0 | `*` |

**Example Calculation:**
```css
/* Rule A: Score 1 (Tag) */
h1 { color: red; }

/* Rule B: Score 10 (Class) */
.title { color: blue; }

/* Rule C: Score 100 (ID) */
#main-title { color: green; }
```
> If `<h1 id="main-title" class="title">` exists, it will be **GREEN** because ID (100) > Class (10) > Tag (1).

---

## 🔨 **Overriding Styles**

### **1. Increase Specificity**
Add more selectors to "outweigh" the old rule.
```css
div.content p { color: purple; } /* Score: 1+10+1 = 12 */
```

### **2. Order Matters (The Cascade)**
If specificity is **EQUAL**, the **LAST** rule written wins.
```css
h1 { color: red; }
h1 { color: blue; } /* Winner! */
```

### **3. The Nuclear Option: `!important` ☢️**
> Overrides EVERYTHING, even inline styles.
```css
p {
    color: red !important;
}
```
> **⚠️ Warning**: AVOID using this unless absolutely necessary. It makes debugging a nightmare because you can't override it easily later.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Inheritance**: Text styles flow down ⬇️. Box styles stay put ⏹️.
> - **Specificity**:
>   - **ID** = Heavy weight 🏋️‍♂️ (100)
>   - **Class** = Medium weight 🏃‍♂️ (10)
>   - **Tag** = Feather weight 🪶 (1)
> - **!important** = The "I don't care about rules" button 🚨

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Does `margin` inherit from parent to child?
> > [!SUCCESS]- Answer
> > No. Box model properties (margin, padding, border) do rarely inherit by default.

> [!QUESTION] **Q2**: Calculate the specificity score: `div#container .item`
> > [!SUCCESS]- Answer
> > **111** (1 Tag `div` + 100 ID `#container` + 10 Class `.item`).

> [!QUESTION] **Q3**: If you have `p { color: red !important; }` and `<p style="color: blue;">`, which color wins?
> > [!SUCCESS]- Answer
> > **Red**. `!important` overrides even inline styles (which usually have the highest specificity).

> [!QUESTION] **Q4**: Use `inherit` to fix a button font issue.
> > [!SUCCESS]- Answer
> > Buttons often ignore the body font. Use `button { font-family: inherit; }` to make them match the rest of the site.

> [!QUESTION] **Q5**: Which wins? `div p` (Score 2) or `.text` (Score 10)?
> > [!SUCCESS]- Answer
> > `.text` (Score 10) wins because 10 is greater than 2.

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
