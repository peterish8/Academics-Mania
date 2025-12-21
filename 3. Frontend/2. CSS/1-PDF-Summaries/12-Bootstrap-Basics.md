# 🅱️ Bootstrap Basics

## 🎯 What is Bootstrap?
Open-source front-end framework for responsive, mobile-first websites with pre-designed CSS, JavaScript, and components.

## 🚀 Integration
```html
<!-- CSS in <head> -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JS before </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
```

## 📦 Key Features
1. **Responsive Grid System** - 12-column layout with breakpoints
2. **Pre-styled Components** - Buttons, navbars, forms, modals, cards
3. **CSS Utilities** - Spacing, colors, typography, borders
4. **JavaScript Plugins** - Interactive components
5. **Mobile-First Approach** - Designed for all devices

## 🏗️ Core Components

### Containers
- `.container` → Fixed-width, responsive
- `.container-fluid` → Full-width always

### Typography
- `.h1` to `.h6` → Heading classes
- `.fw-bold`, `.fw-light` → Font weights
- `.text-center`, `.text-uppercase` → Text utilities

### Spacing
- `m-{size}` → Margin (0-5)
- `p-{size}` → Padding (0-5)
- `mt-3`, `px-4` → Specific sides

### Images
- `.img-fluid` → Responsive images
- `.rounded`, `.rounded-circle` → Shape utilities

### Colors
- `.text-primary`, `.text-success` → Text colors
- `.bg-primary`, `.bg-warning` → Background colors

### Grid System
```html
<div class="container">
  <div class="row">
    <div class="col-md-4">Column 1</div>
    <div class="col-md-8">Column 2</div>
  </div>
</div>
```

### Responsive Utilities
- `.d-none` → Hide element
- `.d-md-block` → Show on medium+ screens
- `.d-sm-none` → Hide on small screens