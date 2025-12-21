# 📐 CSS Units, Responsive Images & Media Queries

## 📏 CSS Units

### Absolute Units
- **`px`** → Fixed pixels, never changes

### Relative Units
- **`%`** → Relative to parent element
- **`vw`** → 1% of viewport width
- **`vh`** → 1% of viewport height  
- **`rem`** → Relative to root font size (html)
- **`em`** → Relative to parent font size

## 🖼️ Responsive Images

### Max/Min Properties
```css
img {
  max-width: 100%;  /* Never overflow container */
  max-height: 100%; /* Scale down proportionally */
}

img {
  min-width: 200px;  /* Never smaller than 200px */
  min-height: 150px; /* Never shorter than 150px */
}
```

## 📱 Media Queries

### Responsive Breakpoints
```css
/* Mobile */
@media screen and (max-width: 600px) {
  /* Mobile styles */
}

/* Tablet */
@media screen and (min-width: 601px) and (max-width: 1024px) {
  /* Tablet styles */
}

/* Desktop */
@media screen and (min-width: 1025px) {
  /* Desktop styles */
}
```

## 🎯 Key Concepts
- **Absolute units** → Fixed size
- **Relative units** → Adapt to context
- **Responsive images** → Scale with container
- **Media queries** → Different styles for different screens