# 📝 Lists & Tables - Summary

## 📋 **Lists**

### **Ordered List (ol)**
```html
<ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</ol>
```

**Types:** `type="1|A|a|I|i"`
**Attributes:** `reversed`, `start="number"`

### **Unordered List (ul)**
```html
<ul>
    <li>Milk</li>
    <li>Bread</li>
    <li>Eggs</li>
</ul>
```

**Styles:** disc, circle, square, none

### **Nested Lists**
```html
<ul>
    <li>Fruits
        <ul>
            <li>Apple</li>
            <li>Banana</li>
        </ul>
    </li>
</ul>
```

---

## 📊 **Tables**

### **Basic Structure**
```html
<table border="1">
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>25</td>
        </tr>
    </tbody>
</table>
```

### **Table Elements**
- `<table>` - Container
- `<tr>` - Table row
- `<td>` - Table data
- `<th>` - Table header
- `<thead>` - Header section
- `<tbody>` - Body section
- `<tfoot>` - Footer section

### **Cell Merging**
- `colspan="2"` - Span 2 columns
- `rowspan="2"` - Span 2 rows

### **Attributes**
- `border="1"` - Add borders
- `width="100%"` - Table width
- `cellpadding` - Space inside cells