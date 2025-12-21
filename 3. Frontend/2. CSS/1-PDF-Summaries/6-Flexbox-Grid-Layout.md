# 🔧 Flexbox & Grid Layout

## 🎯 Flexbox Basics
- `display: flex` → activates flexbox
- **Main Axis** → primary direction (row/column)
- **Cross Axis** → perpendicular to main axis

## 🎛️ Flexbox Properties

### Container Properties
- `justify-content` → aligns along main axis
  - `flex-start`, `center`, `flex-end`, `space-between`, `space-around`
- `align-items` → aligns along cross axis
  - `flex-start`, `center`, `flex-end`, `stretch`, `baseline`
- `flex-direction` → main axis direction
  - `row`, `row-reverse`, `column`, `column-reverse`
- `flex-wrap` → wrapping behavior
  - `nowrap`, `wrap`, `wrap-reverse`
- `align-content` → aligns multiple lines

### Item Properties
- `order` → controls item order (default: 0)
- `flex-grow` → ability to grow (default: 0)
- `flex-shrink` → ability to shrink (default: 1)
- `flex-basis` → initial size before grow/shrink

## 🏗️ CSS Grid Basics
- `display: grid` → activates grid
- `grid-template-columns` → defines column sizes
- `grid-template-rows` → defines row sizes
- `gap` → space between grid items

### Grid Units
- `px` → fixed pixels
- `fr` → fraction of available space
- `1fr 1fr 1fr` → 3 equal columns