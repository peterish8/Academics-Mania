# 📄 Sample Paper - FDB Model Paper

> [!INFO] **Instructions**
> - Try to answer first before clicking the "Show Answer" toggle.
> - Focus on the **Explanation** and **Keywords** to build strong concepts.

---

## **Section A: Multiple Choice Questions**

### 1. Which HTML element is used to emphasize text semantically?
**Options:**
a) `<b>`
b) `<strong>`
c) `<mark>`
d) `<i>`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `<strong>`
> **Explanation:**  
> - `<strong>`: Indicates strong importance/seriousness (Semantic).
> - `<b>`: Makes text bold but has no semantic meaning (Stylistic).
> - `<i>`: Italics (Stylistic).
> - `<mark>`: Highlights text.
> **Keywords:** Semantic, Strong Importance, Bold vs Strong.

---

### 2. Which tag groups navigation-related links?
**Options:**
a) `<menu>`
b) `<nav>`
c) `<header>`
d) `<aside>`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `<nav>`
> **Explanation:**  
> The `<nav>` tag is specifically designed to wrap major navigation blocks (links to other pages or parts of the same page).
> **Keywords:** Navigation, Links, Semantic Tag.

---

### 3. Which input field allows users to select multiple lines of text?
**Options:**
a) `text`
b) `textarea`
c) `email`
d) `password`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `textarea`
> **Explanation:**  
> - `<input type="text">` is for a single line.
> - `<textarea>` is a defined element for multi-line text input (comments, reviews).
> **Keywords:** Multi-line, Input, Textarea.

---

### 4. Which CSS unit scales based on the root element?
**Options:**
a) `em`
b) `%`
c) `rem`
d) `px`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `rem`
> **Explanation:**  
> - `rem` stands for **Root EM**. It is relative to the `<html>` (root) font-size.
> - `em` is relative to the **parent** element's font size.
> **Keywords:** Relative Units, Root Element, Scaling.

---

### 5. Which property controls the stacking order of elements?
**Options:**
a) `float`
b) `overflow`
c) `z-index`
d) `visibility`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `z-index`
> **Explanation:**  
> `z-index` determines which element sits on top of others along the Z-axis (depth). It only works on positioned elements (`relative`, `absolute`, `fixed`, `sticky`).
> **Keywords:** Stacking Context, Z-axis, Overlap.

---

### 6. Which layout system arranges elements in rows and columns simultaneously?
**Options:**
a) Flexbox
b) Float
c) Grid
d) Inline-block

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) Grid
> **Explanation:**  
> - **CSS Grid** is a 2-dimensional system (Rows AND Columns).
> - **Flexbox** is a 1-dimensional system (Rows OR Columns).
> **Keywords:** 2D Layout, Rows & Columns, Grid System.

---

### 7. Which JavaScript keyword prevents reassignment?
**Options:**
a) `var`
b) `let`
c) `const`
d) `static`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `const`
> **Explanation:**  
> Variables declared with `const` cannot be reassigned to a new value. Note: If the value is an object/array, its properties/contents CAN still be modified (mutation).
> **Keywords:** Constants, Reassignment, Immutability.

---

### 8. Which method converts a JavaScript object into a JSON string?
**Options:**
a) `JSON.parse()`
b) `stringify()`
c) `JSON.stringify()`
d) `toJSON()`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `JSON.stringify()`
> **Explanation:**  
> - `JSON.stringify()`: Object -> String (Sending data).
> - `JSON.parse()`: String -> Object (Receiving data).
> **Keywords:** Serialization, Object to String, API Data.

---

### 9. What is the output of: `typeof null`
**Options:**
a) `null`
b) `object`
c) `undefined`
d) `number`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `object`
> **Explanation:**  
> This is a famous bug in JavaScript from its early days. `null` is a primitive value, but `typeof null` incorrectly returns `'object'`.
> **Keywords:** JS Bug, Primitives, Typeof Operator.

---

### 10. Which event fires when a user clicks an element?
**Options:**
a) `submit`
b) `hover`
c) `click`
d) `focus`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `click`
> **Explanation:**  
> - `click`: Mouse click or tap.
> - `submit`: Form submission.
> - `focus`: Input field active.
> **Keywords:** Mouse Events, Interaction.

---

### 11. Which CSS property hides an element but preserves layout space?
**Options:**
a) `display: none`
b) `opacity: 0`
c) `visibility: hidden`
d) `overflow: hidden`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `visibility: hidden`
> **Explanation:**  
> - `visibility: hidden`: Hides element, but it **still takes up space**.
> - `display: none`: Hides element and **removes it** from the layout flow (no space).
> **Keywords:** Layout Space, Hiding Elements, Visibility vs Display.

---

### 12. Which array method checks if at least one element matches a condition?
**Options:**
a) `every()`
b) `map()`
c) `some()`
d) `filter()`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `some()`
> **Explanation:**  
> - `some()`: Returns true if **ANY** element passes.
> - `every()`: Returns true if **ALL** elements pass.
> - `filter()`: Returns a new array.
> **Keywords:** Array Methods, Logic Check, Some vs Every.

---

### 13. Which selector targets all `<p>` elements inside a `<section>`?
**Options:**
a) `section + p`
b) `section.p`
c) `section > p`
d) `section p`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** d) `section p`
> **Explanation:**  
> - `section p`: Descendant selector (Any `p` inside `section`, however deep).
> - `section > p`: Child selector (Only direct children).
> - `section + p`: Adjacent sibling (Immediately after).
> **Keywords:** Descendant Selector, Space Combinator, CSS Specificity.

---

### 14. Which HTML attribute uniquely identifies an element?
**Options:**
a) `class`
b) `name`
c) `id`
d) `key`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `id`
> **Explanation:**  
> An `id` MUST be unique across the entire page. Classes can be reused on multiple elements.
> **Keywords:** Unique Identifier, Selection, Styling.

---

### 15. Which loop is best suited when the number of iterations is unknown?
**Options:**
a) `for`
b) `while`
c) `forEach`
d) `map`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `while`
> **Explanation:**  
> - `while`: Runs *while* a condition is true (unpredictable/unknown count).
> - `for`: Best when you know the start and end points (known count).
> **Keywords:** Control Flow, Condition-based Looping.

---

### 16. Which CSS rule defines animation stages?
**Options:**
a) `@media`
b) `@keyframes`
c) `@animate`
d) `@frames`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `@keyframes`
> **Explanation:**  
> `@keyframes` allows you to define the styles at specific points (0%, 50%, 100%) of the animation cycle.
> **Keywords:** CSS Animations, Keyframes, Stages.

---

### 17. What does `Array.isArray([])` return?
**Options:**
a) `false`
b) `true`
c) `undefined`
d) `error`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `true`
> **Explanation:**  
> Because `typeof []` returns `'object'` which leads to true, 
> `Array.isArray()` is the reliable standard method to check if a value is strictly an array which returns false in this case.
> **Keywords:** Type Checking, Array Validation.

---

### 18. Which object provides date and time functionality?
**Options:**
a) `Time`
b) `Clock`
c) `Date`
d) `Math`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `Date`
> **Explanation:**  
> The `Date` object is used to work with dates and times (e.g., `new Date()`).
> **Keywords:** JS Built-ins, Date Object.

---

### 19. Which Bootstrap class centers text horizontally?
**Options:**
a) `center-text`
b) `align-center`
c) `text-center`
d) `text-align`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** c) `text-center`
> **Explanation:**  
> In Bootstrap utility classes, `text-center` applies `text-align: center`.
> **Keywords:** Bootstrap, Utility Classes, Text Alignment.

---

### 20. Which JavaScript function converts a string into an integer?
**Options:**
a) `Number()`
b) `parseInt()`
c) `toInt()`
d) `parse()`

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:** b) `parseInt()`
> **Explanation:**  
> - `parseInt("10.5")` -> `10` (Parses until it hits non-digits, returns Integer).
> - `Number()` is also valid but returns floats if present (`10.5`). The question specifically asks for *Integer*.
> **Keywords:** Type Conversion, Parsing, Integers.

---

## **Section B: Short Answer Questions**

### 1. Explain the difference between inline and block-level elements.

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> - **Block-level**:
>   - Always starts on a new line.
>   - Takes up the full width available (100%).
>   - Examples: `<div>`, `<p>`, `<h1>`, `<section>`.
> - **Inline-level**:
>   - Does NOT start on a new line.
>   - Takes up only as much width as necessary (content width).
>   - Examples: `<span>`, `<a>`, `<img>`, `<b>`.
> **Keywords:** Full-width vs Content-width, New Line Behavior.

### 2. Describe the CSS box model with a neat explanation.

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> Every HTML element is essentially a box consisting of 4 layers (from inside out):
> 1.  **Content**: The actual text or image.
> 2.  **Padding**: Transparent space *inside* the border, around content.
> 3.  **Border**: A line wrapping the padding and content.
> 4.  **Margin**: Transparent space *outside* the border, separating it from neighbors.
> **Keywords:** C-P-B-M (Content, Padding, Border, Margin), Layout Structure.

### 3. What is event bubbling in JavaScript?

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> Event Bubbling is a mechanism where an event triggered on the **innermost** element (target) first runs its handler, and then "bubbles up" to trigger handlers on its **parent** elements, all the way to the `<html>` root.
> - *Example*: Clicking a `<button>` inside a `<div>` triggers the button's click event first, then the div's click event.
> **Keywords:** Propagation, Inner to Outer, Bubble Up.

### 4. Explain Flexbox main-axis and cross-axis.

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> - **Main-Axis**: The primary direction flex items are laid out.
>   - Defined by `flex-direction`. (e.g., `row` -> Horizontal, `column` -> Vertical).
>   - Aligned using `justify-content`.
> - **Cross-Axis**: Perpendicular to the main axis.
>   - Defined by the opposite of direction.
>   - Aligned using `align-items`.
> **Keywords:** Direction, Perpendicular, Justify vs Align.

### 5. What is type coercion in JavaScript?

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> Type Coercion is the automatic or implicit conversion of values from one data type to another (e.g. String to Number).
> - **Implicit**: JS does it automatically (e.g., `"5" + 5` -> `"55"`).
> - **Explicit**: You do it manually (e.g., `Number("5")`).
> - Use Strict Equality (triple equals) to avoid coercion bugs.
> **Keywords:** Implicit Conversion, Weak Typing, String vs Number.

---

## **Section C: Long Answer**

### 1. Explain JavaScript execution context and the call stack.

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> **Execution Context (EC)**: The environment where JS code is executed.
> 1.  **Global Execution Context (GEC)**: Created when the script starts. Has global `window` and `this`.
> 2.  **Function Execution Context (FEC)**: Created whenever a function is *invoked*.
> 
> **Call Stack**:
> - A LIFO (Last In, First Out) data structure that tracks Function Execution Contexts.
> - When a function calls, it's **Pushed** onto the stack.
> - When it returns, it's **Popped** off the stack.
> - If the stack is busy, the browser "freezes" (Single Threaded).
> **Keywords:** Environment, LIFO Stack, Global/Function Context, Single Threaded.

### 2. Compare Grid and Flexbox layouts. Use cases.

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> **Flexbox (1D Layout):**
> - **Structure**: Row OR Column.
> - **Focus**: Content-first (aligning items inside a container).
> - **Use Case**: Navigation bars, centering elements, linear lists of items.
> 
> **Grid (2D Layout):**
> - **Structure**: Rows AND Columns simultaneously.
> - **Focus**: Layout-first (defining the overall page structure).
> - **Use Case**: Complex photo galleries, full page layouts (Header/Sidebar/Main/Footer).
> **Keywords:** 1D vs 2D, Content vs Layout, Alignment vs Structure.

### 3. Explain JavaScript promises with an example.

> [!SUCCESS]- ✅ Click to Reveal Answer
> **Answer:**
> A **Promise** represents a value that may be available now, later, or never (Async operation). It has 3 states:
> 1.  **Pending**: Working...
> 2.  **Fulfilled (Resolved)**: Success.
> 3.  **Rejected**: Failure/Error.
> 
> **Example:**
> ```javascript
> const myPromise = new Promise((resolve, reject) => {
>     setTimeout(() => {
>         resolve("Success after 2 seconds!");
>     }, 2000);
> });
> 
> myPromise.then((message) => {
>     console.log(message);
> });
> ```
> **Keywords:** Async, Pending/Resolve/Reject, `.then()`, non-blocking.

---

## **Section D: Programming Questions**

### Q1. DOM Manipulation: Change Color

> [!SUCCESS]- ✅ Click to Reveal Solution
> **Solution:**
> ```html
> <button id="btn">Change Color</button>
> <p id="text">Hello World</p>
> 
> <script>
>     const btn = document.getElementById('btn');
>     const text = document.getElementById('text');
> 
>     btn.addEventListener('click', function() {
>         text.style.backgroundColor = "yellow";
>     });
> </script>
> ```
> **Explanation**:
> 1. Select elements using `getElementById`.
> 2. Attach `click` listener.
> 3. Use `.style` property to modify CSS.

### Q2. Array Processing (Odd, Triple, Sum)

> [!SUCCESS]- ✅ Click to Reveal Solution
> **Solution:**
> ```javascript
> const numbers = [1, 2, 3, 4, 5, 6, 7];
> 
> const result = numbers
>     .filter(num => num % 2 !== 0)  // Extract Odds: [1, 3, 5, 7]
>     .map(num => num * 3)           // Triple them: [3, 9, 15, 21]
>     .reduce((acc, curr) => acc + curr, 0); // Sum: 48
> 
> console.log(result);
> ```
> **Explanation**:
> - `filter`: Pick specific items.
> - `map`: Transform each item.
> - `reduce`: Aggregate/Sum items.

### Q3. Loop: neither 4 nor 6

> [!SUCCESS]- ✅ Click to Reveal Solution
> **Solution:**
> ```javascript
> let N = 20;
> 
> for (let i = 1; i <= N; i++) {
>     // Condition: NOT divisible by 4 AND NOT divisible by 6
>     if (i % 4 !== 0 && i % 6 !== 0) {
>         console.log(i);
>     }
> }
> ```
> **Explanation**:
> - Use `%` (Modulus) to check divisibility.
> - Use `&&` (AND operator) to ensure BOTH conditions are met.
> - `!== 0` means "does not have a remainder of 0", aka "is not divisible".

---

## **Section E: Debugging**

### Correct the code:
```javascript
let x = [1, 2];
let y = [3, 4, 5];
let z = [...x, ...y];
let total = x.length + y.length + z.length;
console.log(total); // Should print 10
```

> [!SUCCESS]- ✅ Click to Reveal Solution
> **Issue Analysis:**
> The original code snippet provided in the question:
> ```javascript
> let x = [1, 2];
> let y = [3, 4, 5];
> let z = [...x, ...y];
> let total = x.length + y.length + z.length;
> console.log(total);
> ```
> **Wait!** The code provided in the question **is actually correct** syntactically.
> - `x` length = 2
> - `y` length = 3
> - `z` length = 5 (Spread operator merges them)
> - `total` = 2 + 3 + 5 = **10**.
> 
> *If the question implied there was a bug, usually it's forgetting the spread operator `...` or confusing `length` property.*
> 
> **Corrected Concept**:
> The spread operator `...` properly expands the arrays. If the user had written `let z = [x, y]`, then `z` would be a nested array of length 2 (`[[1,2], [3,4,5]]`), which would be a logical bug.
> 
> **Final Output**: 10.
