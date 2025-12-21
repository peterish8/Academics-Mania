# 🎨 Flexbox & Grid Portfolio Task

## 🏗️ Complete Portfolio Layout Example

### 📋 Structure Overview
- **Header** → Flexbox (title left, nav right)
- **Profile Card** → Flexbox (image + text horizontal)
- **Gallery** → Grid (3-column project showcase)
- **Footer** → Flexbox (centered content)

## 🎯 Key Techniques Used

### Header Layout
```css
.header {
  display: flex;
  justify-content: space-between; /* title left, nav right */
  align-items: center;
}
```

### Profile Card Layout
```css
.profile-card {
  display: flex;
  align-items: center;
  gap: 15px; /* space between image and text */
}
```

### Gallery Grid
```css
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
  gap: 10px;
}
```

### Footer Layout
```css
.footer {
  display: flex;
  justify-content: center; /* centered text */
}
```

## 💡 Layout Patterns
- **Flexbox** → 1D layouts (header, profile, footer)
- **Grid** → 2D layouts (project gallery)
- **Gap property** → consistent spacing
- **justify-content** → horizontal alignment
- **align-items** → vertical alignment