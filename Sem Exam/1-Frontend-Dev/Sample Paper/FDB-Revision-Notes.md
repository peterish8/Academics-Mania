# ⚡ Last-Minute Revision Notes: Frontend Development

> [!TIP] **Quick Scan Mode**
> Read this 1 hour before the exam to refresh memory hooks and keywords.

---

## 🏗️ HTML Essentials
- **Semantics**: Use `<strong>` (meaning) over `<b>` (style). Use `<nav>`, `<header>`, `<article>` for structure.
- **Block vs Inline**:
  - **Block**: New line, 100% width (`div`, `p`, `h1-h6`).
  - **Inline**: Same line, content width (`span`, `a`, `img`).
- **Inputs**: `<textarea>` for multi-line, `type="email"` for validation.
- **Attributes**: `id` (Unique, ONE per page), `class` (Reusable).

---

## 🎨 CSS Foundations
- **Box Model (C-P-B-M)**:
  1.  **Content** (Inside)
  2.  **Padding** (Space inside border)
  3.  **Border** (Line)
  4.  **Margin** (Space outside border)
- **Units**:
  - `px`: Absolute.
  - `em`: Relative to **Parent**.
  - `rem`: Relative to **Root (HTML)**.
  - `vw/vh`: Viewport width/height.
- **Positioning**:
  - `static`: Default.
  - `relative`: Offset from original spot.
  - `absolute`: Removed from flow, relative to nearest positioned ancestor.
  - `fixed`: Stuck to viewport (scrolls with you).
  - `sticky`: Toggles relative/fixed based on scroll.
- **Display**:
  - `none`: Removes element (No space).
  - `hidden`: Hides element (Keeps space).

---

## 📐 Layout Systems
| Feature | Flexbox (1D) | Grid (2D) |
| :--- | :--- | :--- |
| **Axis** | Row **OR** Column | Row **AND** Column |
| **Alignment** | Content-first | Layout-first |
| **Main Prop** | `justify-content` | `grid-template-columns` |
| **Cross Prop** | `align-items` | `align-content` |

---

## 📜 JavaScript Core
- **Variables**:
  - `var`: Function scope, Hoisted (avoid).
  - `let`: Block scope, Reassignable.
  - `const`: Block scope, **Immutable binding** (Reference can change).
- **Data Types**:
  - **Primitives**: String, Number, Boolean, Null, Undefined, Symbol.
  - **Reference**: Objects, Arrays, Functions.
  - *Bug*: `typeof null === 'object'`.
- **Coercion**:
  - Implicit (`"5" + 5 = "55"`).
  - Explicit (`parseInt("5")`).
  - **Advice**: Always use `===` (Strict Equality).

---

## ⚙️ Advanced Concepts
- **Execution Context**:
  - **GEC** (Global) + **FEC** (Function).
  - **Call Stack**: LIFO structure handling execution.
- **Hoisting**: Var/Functions moved to top. `let/const` in Temporal Dead Zone (TDZ).
- **Event Bubbling**: Event flows **Inner Target ➡ Outer Parent**.
- **Promises**:
  - States: `Pending` ➡ `Resolved` (Success) OR `Rejected` (Error).
  - Use `.then()` or `async/await` to handle.

---

## 📦 Array Power-Methods
- `map()`: Transforms **all** elements (Returns new array).
- `filter()`: Selects **some** elements (Returns new array).
- `reduce()`: Accumulates to **one** value.
- `some()`: True if **any** match.
- `every()`: True if **all** match.

---

## 🖱️ DOM Snippets
```javascript
// Quick Selection
const btn = document.querySelector('#btn');

// Changing Style
btn.style.backgroundColor = 'red';

// Event Listener
btn.addEventListener('click', () => {
  console.log('Clicked!');
});

// Create & Append
const li = document.createElement('li');
li.textContent = 'New Item';
document.ul.appendChild(li);
```
