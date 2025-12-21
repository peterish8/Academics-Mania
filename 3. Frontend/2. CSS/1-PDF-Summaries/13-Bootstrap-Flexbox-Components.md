# 🔧 Bootstrap Flexbox & Components

## 🎯 Bootstrap Flexbox Utilities

### Enable Flexbox
- `.d-flex` → `display: flex`
- `.d-inline-flex` → `display: inline-flex`

### Direction
- `.flex-row` → Horizontal (default)
- `.flex-column` → Vertical
- `.flex-row-reverse` → Horizontal reversed

### Justify Content (Main Axis)
- `.justify-content-start` → Left align
- `.justify-content-center` → Center align
- `.justify-content-end` → Right align
- `.justify-content-between` → Space between
- `.justify-content-around` → Space around
- `.justify-content-evenly` → Even spacing

### Align Items (Cross Axis)
- `.align-items-start` → Top align
- `.align-items-center` → Center align
- `.align-items-end` → Bottom align
- `.align-items-stretch` → Fill height
- `.align-items-baseline` → Text baseline

### Flex Properties
- `.flex-grow-1` → Grow to fill space
- `.flex-shrink-0` → Don't shrink
- `.flex-wrap` → Allow wrapping
- `.flex-nowrap` → No wrapping

### Individual Item Control
- `.align-self-start` → Individual alignment
- `.order-1` → Change visual order

## 🎨 Key Bootstrap Components

### Cards
```html
<div class="card">
  <div class="card-body">
    <h5 class="card-title">Title</h5>
    <p class="card-text">Content</p>
  </div>
</div>
```

### Navbar
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Brand</a>
    <div class="navbar-nav">
      <a class="nav-link" href="#">Home</a>
    </div>
  </div>
</nav>
```

### Buttons
- `.btn .btn-primary` → Primary button
- `.btn .btn-outline-success` → Outline button
- `.btn-sm`, `.btn-lg` → Size variants

### Forms
- `.form-control` → Input styling
- `.form-label` → Label styling
- `.mb-3` → Form group spacing

### Modal
- `data-bs-toggle="modal"` → Trigger modal
- `data-bs-target="#modalId"` → Target modal

## 💡 Layout Strategy
- **Grid System** → Page-level layout (rows & columns)
- **Flexbox Utilities** → Alignment & spacing within components