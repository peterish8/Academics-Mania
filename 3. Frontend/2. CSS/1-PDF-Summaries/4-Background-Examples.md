# 📝 Background Examples - Summary

## 🎨 **Background Property Examples**

### **1. background-color**
```css
div {
    background-color: lightblue;
}
```
```html
<div>This has a light blue background.</div>
```

### **2. background-image**
```css
div {
    background-image: url("background.jpg");
}
```
```html
<div>Background image applied here.</div>
```

### **3. background-repeat**
```css
div {
    background-image: url("pattern.png");
    background-repeat: repeat-x;
}
```
- `repeat` - both directions (default)
- `repeat-x` - horizontal only
- `repeat-y` - vertical only
- `no-repeat` - no repetition

### **4. background-size**
```css
div {
    background-image: url("wall.jpg");
    background-size: cover;
}
```
- `auto` - original size (default)
- `cover` - covers entire element
- `contain` - fits inside element
- `100px 200px` - custom size

### **5. background-position**
```css
div {
    background-image: url("flower.png");
    background-repeat: no-repeat;
    background-position: right bottom;
}
```

**3 Ways to Define Position:**

**1. Length Units (px)**
```css
background-position: 50px 30px;
```
- First value: horizontal (x-axis)
- Second value: vertical (y-axis)

**2. Percentages**
```css
background-position: 50% 25%;
```

**3. Keywords**
```css
background-position: left top;      /* default */
background-position: left center;
background-position: left bottom;
background-position: center top;
background-position: center center; /* exact middle */
background-position: center bottom;
background-position: right top;
background-position: right center;
background-position: right bottom;
```

---

## 🎨 **Complete Example**
```css
.container {
    background-color: rgb(255, 0, 0);
    background-image: url("./bg.jpg");
    background-repeat: no-repeat;
    background-position: 40px 150px;
    background-size: contain;
    background-attachment: scroll;
    background-clip: text;
    background-origin: content-box;
}
```