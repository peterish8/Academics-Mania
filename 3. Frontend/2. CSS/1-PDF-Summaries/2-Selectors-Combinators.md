# 📝 Selectors & Combinators - Summary

## 🎯 **Why CSS Selectors?**
- Target specific elements
- Apply styles consistently
- Provide flexibility in styling

---

## 🔍 **General Selectors**

### **Universal Selector**
```css
* { margin: 0; padding: 0; }
```

### **Element Selector**
```css
p { color: blue; }
```

### **Class Selector**
```css
.highlight { background: yellow; }
```

### **ID Selector**
```css
#header { font-size: 24px; }
```

---

## 🎭 **Pseudo-selectors**

### **Interaction States**
```css
button:hover { background: green; }
button:active { transform: scale(0.95); }
input:focus { border: 2px solid blue; }
```

### **Link States**
```css
a:link { color: blue; }
a:visited { color: purple; }
```

### **Child Selectors**
```css
li:first-child { color: red; }
li:last-child { color: green; }
li:nth-child(2) { color: orange; }
li:nth-last-child(1) { color: pink; }
```

---

## 🔗 **Combinators**

### **Descendant Selector (space)**
```css
div p { color: red; }  /* All p inside div */
```

### **Child Selector (>)**
```css
div > p { color: blue; }  /* Direct child only */
```

### **Adjacent Sibling (+)**
```css
h2 + p { color: green; }  /* Immediately next sibling */
```

### **General Sibling (~)**
```css
h2 ~ p { color: orange; }  /* All siblings after */
```

---

## 🎨 **CSS Variables**
```css
:root {
    --main-color: #3498db;
    --padding: 10px;
}

h1 {
    color: var(--main-color);
    padding: var(--padding);
}
```