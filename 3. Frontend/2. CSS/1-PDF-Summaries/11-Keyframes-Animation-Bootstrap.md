# 🎬 CSS Keyframes, Animation & Bootstrap

## 🎯 CSS Animations with @keyframes
More control than transitions - define multiple animation states.

### Basic Syntax
```css
@keyframes animationName {
  from { /* starting state */ }
  to { /* ending state */ }
}

.element {
  animation: animationName duration timing-function iteration-count delay;
}
```

### Animation Examples

#### Fade-In Effect
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade-in { animation: fadeIn 2s forwards; }
```

#### Slide-In Box
```css
@keyframes slideIn {
  from { transform: translateX(-200px); }
  to { transform: translateX(0); }
}
.slide-box { animation: slideIn 2s ease-out forwards; }
```

#### Bouncing Ball
```css
@keyframes bounce {
  0%, 100% { top: 0; }
  50% { top: 150px; }
}
.ball { animation: bounce 1s ease-in-out infinite; }
```

## 🅱️ Bootstrap Introduction
Popular front-end framework for responsive, mobile-first websites.

### Key Features
1. **Responsive Grid System** - 12-column layout (col-, col-sm-, col-md-, col-lg-)
2. **Pre-styled Components** - Buttons, navbars, forms, modals, cards
3. **CSS Utilities** - Spacing, colors, typography, borders, flexbox
4. **JavaScript Plugins** - Tooltips, modals, carousels, accordions
5. **Mobile-First Approach** - Designed for all devices

### Getting Started
📖 **Documentation**: https://getbootstrap.com/docs/5.0/getting-started/introduction/

## 💡 Key Concepts
- **@keyframes** define animation steps
- **Animation properties** control timing and behavior
- **Bootstrap** accelerates development with pre-built components
- **Mobile-first** responsive design philosophy