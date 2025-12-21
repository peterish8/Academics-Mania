# 📝 CSS Introduction & Basics - Summary

## 🎨 **What is CSS?**
- **CSS** = Cascading Style Sheets
- Introduced in 1994 by Håkon Wium Lie
- **Purpose**: Style web pages and reuse styles

---

## 🏗️ **CSS Structure**
```css
selector {
    property: value;
}
```
- **Selector** - Chooses elements (p, .class, #id)
- **Property** - What to change (color, font-size)
- **Value** - Setting for the property

**Example:**
```css
p {
    color: blue;
    font-size: 16px;
}
```

---

## 📍 **Types of CSS**

### **Inline CSS**
```html
<p style="color:red; font-size:18px;">Inline CSS</p>
```

### **Internal CSS**
```html
<head>
    <style>
        p { color: green; }
    </style>
</head>
```

### **External CSS**
```html
<link rel="stylesheet" href="styles.css">
```
```css
/* styles.css */
p {
    color: purple;
    font-size: 18px;
}
```

---

## 🎯 **CSS Selectors**

### **Basic Selectors**
```css
p { color: blue; }                    /* Tag */
.red-text { color: red; }             /* Class */
#main-heading { font-size: 24px; }    /* ID */
* { margin: 0; padding: 0; }          /* Universal */
```

### **Attribute Selectors**
```css
input[type] { border: 2px solid red; }
input[type="password"] { background: yellow; }
input[placeholder] { font-weight: bold; }
```

---

## 🎨 **Colors & Fonts**

### **Colors**
```css
h1 { color: red; }              /* Named */
h2 { color: #00ff00; }          /* Hex */
h3 { color: rgb(0, 0, 255); }   /* RGB */
```

### **Fonts**
```css
p {
    font-family: Arial, sans-serif;
    font-size: 18px;
    font-style: italic;
    font-weight: bold;
}
```

---

## 📦 **CSS Box Model**
- **Content** - Text/Image inside
- **Padding** - Space between content & border
- **Border** - Surrounds padding/content
- **Margin** - Space outside element

```css
.box {
    width: 200px;
    height: 200px;
    padding: 15px;
    border: 2px solid red;
    margin-top: 100px;
}
```

---

## 🎭 **Pseudo-classes**
```css
button:hover { background-color: green; }
button:active { background-color: darkgreen; }
```