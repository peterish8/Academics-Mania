# 📝 Background Properties - Summary

## 🎨 **Background Properties**

### **1. background-color**
```css
div { background-color: red; }
```

### **2. background-image**
```css
div { background-image: url("image.png"); }
```

### **3. background-repeat**
```css
background-repeat: repeat;      /* default */
background-repeat: no-repeat;   /* once only */
background-repeat: repeat-x;    /* horizontal */
background-repeat: repeat-y;    /* vertical */
```

### **4. background-position**
**Keywords:**
```css
background-position: left top;
background-position: center center;
background-position: right bottom;
```

**Numeric values:**
```css
background-position: 50px 100px;
```

### **5. background-size**
```css
background-size: cover;     /* fills container */
background-size: contain;   /* fits inside */
background-size: 100px 200px; /* custom size */
```

### **6. background-attachment**
```css
background-attachment: scroll; /* default */
background-attachment: fixed;  /* stays fixed */
background-attachment: local;  /* scrolls with content */
```

### **7. background-clip**
```css
background-clip: border-box;  /* default */
background-clip: padding-box; /* covers padding */
background-clip: content-box; /* content only */
background-clip: text;        /* clipped to text */
```

### **8. background-origin**
```css
background-origin: border-box;  /* starts from border */
background-origin: padding-box; /* starts from padding */
background-origin: content-box; /* starts from content */
```

---

## 🔲 **Border Properties**

### **1. border-style**
```css
border-style: solid;   /* plain line */
border-style: dotted;  /* dotted line */
border-style: dashed;  /* dashed line */
border-style: double;  /* double lines */
border-style: none;    /* no border */
```

### **2. border-width**
```css
border-width: 5px;
```

### **3. border-color**
```css
border-color: red;
```

### **4. border-radius**
```css
border-radius: 10px;  /* rounded corners */
border-radius: 50%;   /* circle */
```

### **5. Individual Borders**
```css
border-top: 2px solid red;
border-left: 4px dashed blue;
```

### **6. Shorthand**
```css
border: 4px dotted green; /* width + style + color */
```