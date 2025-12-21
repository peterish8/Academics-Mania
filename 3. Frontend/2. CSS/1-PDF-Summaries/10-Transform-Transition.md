# 🔄 CSS Transform & Transition

## 🎯 Transform Property
Visually manipulates elements without affecting layout flow.

### Basic Transform Functions
1. **`translate()`** → Move elements
   - `translateX(50px)` → move right
   - `translateY(-50px)` → move up
   - `translate(50px, 100px)` → move right + down

2. **`rotate()`** → Rotate elements
   - `rotate(45deg)` → clockwise rotation
   - `rotate(-30deg)` → counter-clockwise

3. **`scale()`** → Resize elements
   - `scale(1.5)` → 150% bigger
   - `scale(0.5)` → 50% smaller
   - `scale(1.5, 0.5)` → wider, shorter

4. **`skew()`** → Tilt elements
   - `skewX(20deg)` → horizontal tilt
   - `skewY(15deg)` → vertical tilt

5. **`matrix()`** → Advanced 2D transforms
   - `matrix(scaleX, skewY, skewX, scaleY, translateX, translateY)`

## 🌐 3D Transforms
- **`translate3d(x, y, z)`** → 3D movement
- **`scale3d(x, y, z)`** → 3D scaling
- **`rotate3d(x, y, z, angle)`** → 3D rotation
- **`matrix3d()`** → Advanced 3D transforms

### 3D Requirements
```css
.parent {
  perspective: 800px; /* Enables 3D view */
  transform-style: preserve-3d; /* Maintains depth */
}
```

## 💡 Key Points
- **No layout disruption** - transforms don't affect document flow
- **Hardware acceleration** - smooth performance
- **Combine functions** - `transform: translateX(50px) rotate(45deg) scale(1.2)`
- **3D needs perspective** - parent must have perspective property