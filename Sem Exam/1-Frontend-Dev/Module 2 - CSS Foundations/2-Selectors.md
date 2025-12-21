# 🎯 CSS Selectors

## 🎯 **What are Selectors?**

> [!SUCCESS] **Definition**: Patterns used to select the HTML element(s) you want to style.
> How you tell CSS **"Hey, style THIS thing!"** 👉

---

## 🔍 **Basic Selectors**

### **1. Universal Selector (`*`)**
> Selects **EVERYTHING** on the page.
```css
* {
    margin: 0;
    padding: 0;
}
```
- **Use Case**: Commonly used for CSS resets.
- **Tip**: Heavy on performance if overused (unlikely on small sites).

### **2. Tag (Type) Selector**
> Selects all elements of a specific HTML tag.
```css
p {
    color: gray;
}
```
- **Effect**: Styles ALL `<p>` tags on the page.

### **3. Class Selector (`.`)**
> Selects elements with a specific `class` attribute.
> **Prefix**: Dot (`.`)
```css
.btn {
    background-color: blue;
}
```
```html
<button class="btn">Click me</button>
<a class="btn">Link button</a>
```
- **Key Point**: Reusable! Many elements can have the same class.

### **4. ID Selector (`#`)**
> Selects a SINGLE element with a specific `id` attribute.
> **Prefix**: Hash (`#`)
```css
#navbar {
    height: 50px;
}
```
```html
<nav id="navbar">...</nav>
```
- **Key Point**: Unique! Only ONE element per page should have this ID.

### **5. Grouping Selector (`,`)**
> Apply the same style to multiple selectors.
```css
h1, h2, h3 {
    font-family: Arial;
    color: darkblue;
}
```

---

## 🏆 **Class vs ID**

| Feature | Class (`.`) | ID (`#`) |
|---------|-------------|----------|
| **Symbol** | Dot `.` | Hash `#` |
| **Quantity**| Multiple elements | **Unique** (One only) |
| **Reuse** | Reusable everywhere | Use once per page |
| **Priority**| Medium | High (overrides class) |

> [!TIP] **Best Practice**: Use **Classes** for styling (99% of the time). Use **IDs** for JavaScript hooks or specific anchors.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **ID** = Identity Card 🪪 (Only you have your ID number) → `#`
> - **Class** = Classroom 🏫 (Many students in one class) → `.`
> - **Universal** = Universe 🌌 (Everything) → `*`

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Which selector matches the element `<div class="card">`?
> > [!SUCCESS]- Answer
> > `.card`

> [!QUESTION] **Q2**: Can you start a class name with a number (e.g., `.1st-item`)?
> > [!SUCCESS]- Answer
> > No! CSS class and ID names cannot start with a number. They must start with a letter, underscore, or hyphen.

> [!QUESTION] **Q3**: How do you select multiple elements (like h1 and p) to give them the same color?
> > [!SUCCESS]- Answer
> > Use a comma `,` to group them: `h1, p { color: red; }`

> [!QUESTION] **Q4**: Which has higher priority: Class selector or ID selector?
> > [!SUCCESS]- Answer
> > The **ID selector (#)** has higher priority (specificity) and will override styles defined by a class.

> [!QUESTION] **Q5**: What does the selector `p.intro` target?
> > [!SUCCESS]- Answer
> > It targets only `<p>` elements that ALSO have the class `intro`. It will NOT target a `<div>` with the class `intro`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
