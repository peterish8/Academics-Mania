# 🎯 Advanced Selectors - My Style Notes

## 🎯 **What are Advanced Selectors?**

> [!INFO] **Definition**: Powerful tools to target specific elements precisely
> Like having **laser-guided styling** instead of shotgun approach!

**📍 Key Points:**
- Target elements based on states, relationships, positions
- Reduce need for extra classes and IDs
- Create interactive effects without JavaScript
- Essential for modern CSS development

**🎯 Use Cases:**
- Interactive hover effects
- Form styling and validation
- Navigation menu states
- Complex layout targeting

---

## 🎭 **Pseudo-classes for Interactions**

### **🖱️ :hover State**

> [!INFO] **Definition**: Styles applied when mouse cursor is over element
> Like elements **lighting up** when you point at them!

**📍 Key Points:**
- Triggered by mouse entering element area
- Removed when mouse leaves
- Works on any element, not just links
- Great for user feedback

**🎨 Visual:**
```css
button:hover {
    background: green;
    transform: scale(1.1);
}
```

**🎯 Use Cases:**
- Button hover effects
- Image zoom on hover
- Tooltip triggers
- Navigation menu highlights

---

### **👆 :active State**

> [!INFO] **Definition**: Styles applied while element is being clicked
> Like elements **reacting** to being pressed!

**📍 Key Points:**
- Active only during click/tap
- Very brief duration
- Provides immediate feedback
- Often combined with hover

**🎨 Visual:**
```css
button:active {
    transform: scale(0.95);
    background: darkgreen;
}
```

**🎯 Use Cases:**
- Button press animations
- Click feedback effects
- Touch interaction responses
- Game-like interactions

---

### **🎯 :focus State**

> [!INFO] **Definition**: Styles applied when element receives keyboard focus
> Like **highlighting** the active form field!

**📍 Key Points:**
- Triggered by Tab key or clicking
- Essential for accessibility
- Helps keyboard navigation
- Required for form usability

**🎨 Visual:**
```css
input:focus {
    border: 2px solid blue;
    outline: none;
    box-shadow: 0 0 5px blue;
}
```

**🎯 Use Cases:**
- Form field highlighting
- Keyboard navigation aids
- Accessibility improvements
- User input guidance

---

## 🔗 **Link States**

### **🔵 :link and :visited**

> [!INFO] **Definition**: Different styles for unvisited vs visited links
> Like **breadcrumbs** showing where you've been!

**📍 Key Points:**
- :link = never visited before
- :visited = already clicked/visited
- Browser remembers visited links
- Important for user navigation

**🎨 Visual:**
```css
a:link {
    color: blue;
    text-decoration: underline;
}

a:visited {
    color: purple;
    text-decoration: none;
}
```

**🎯 Use Cases:**
- Navigation breadcrumbs
- External link styling
- User journey tracking
- Reading progress indication

---

## 👶 **Child Position Selectors**

### **🥇 :first-child**

> [!INFO] **Definition**: Selects the first child element within a parent
> Like styling the **eldest sibling**!

**📍 Key Points:**
- Must be the very first child
- Ignores text nodes and comments
- Useful for list styling
- Common in navigation menus

**🎨 Visual:**
```css
li:first-child {
    color: red;
    font-weight: bold;
}
```

**🎯 Use Cases:**
- First menu item styling
- Article introduction paragraphs
- List item special treatment
- Header row in tables

---

### **🏁 :last-child**

> [!INFO] **Definition**: Selects the last child element within a parent
> Like styling the **youngest sibling**!

**📍 Key Points:**
- Must be the very last child
- Automatically updates if content changes
- Great for removing bottom margins
- Useful for footer styling

**🎨 Visual:**
```css
li:last-child {
    border-bottom: none;
    margin-bottom: 0;
}
```

**🎯 Use Cases:**
- Remove bottom borders from lists
- Last paragraph spacing
- Footer menu items
- Final form field styling

---

### **🔢 :nth-child(n)**

> [!INFO] **Definition**: Selects specific child by position number
> Like **picking specific kids** from a lineup!

**📍 Key Points:**
- n can be number, formula, or keyword
- Counting starts from 1 (not 0)
- Can use odd/even keywords
- Very flexible and powerful

**🎨 Visual:**
```css
li:nth-child(2) { color: orange; }     /* 2nd item */
li:nth-child(odd) { background: #f0f0f0; } /* 1st, 3rd, 5th... */
li:nth-child(even) { background: white; }   /* 2nd, 4th, 6th... */
li:nth-child(3n) { color: red; }       /* Every 3rd item */
```

**🎯 Use Cases:**
- Zebra striping in tables
- Grid layout patterns
- Alternating card colors
- Complex list styling

---

## 🔗 **Combinators (Relationships)**

### **👨‍👩‍👧‍👦 Descendant Selector (space)**

> [!INFO] **Definition**: Selects elements nested anywhere inside another element
> Like styling **all family members** in a household!

**📍 Key Points:**
- Uses space between selectors
- Selects nested elements at any level
- Most commonly used combinator
- Can chain multiple levels

**🎨 Visual:**
```css
div p {
    color: red;
}

<div>
    <p>This is red</p>        ← Selected
    <section>
        <p>This is also red</p> ← Also selected
    </section>
</div>
```

**🎯 Use Cases:**
- Style all paragraphs in articles
- Format text within containers
- Theme entire sections
- Nested component styling

---

### **👨‍👦 Child Selector (>)**

> [!INFO] **Definition**: Selects only direct children, not grandchildren
> Like styling **only your kids**, not grandkids!

**📍 Key Points:**
- Uses greater-than (>) symbol
- Only selects immediate children
- More specific than descendant
- Prevents deep nesting issues

**🎨 Visual:**
```css
div > p {
    color: blue;
}

<div>
    <p>This is blue</p>         ← Selected (direct child)
    <section>
        <p>This is not blue</p> ← Not selected (grandchild)
    </section>
</div>
```

**🎯 Use Cases:**
- Navigation menu direct items
- Card component direct children
- Layout container immediate elements
- Preventing style inheritance

---

### **👫 Adjacent Sibling (+)**

> [!INFO] **Definition**: Selects element immediately following another
> Like styling the **next sibling** in line!

**📍 Key Points:**
- Uses plus (+) symbol
- Only selects the very next sibling
- Both elements must have same parent
- Useful for sequential styling

**🎨 Visual:**
```css
h2 + p {
    color: green;
    font-weight: bold;
}

<h2>Heading</h2>
<p>This paragraph is green</p>    ← Selected
<p>This paragraph is normal</p>   ← Not selected
```

**🎯 Use Cases:**
- First paragraph after headings
- Form labels and inputs
- Sequential content styling
- Article introduction paragraphs

---

### **👥 General Sibling (~)**

> [!INFO] **Definition**: Selects all siblings that come after an element
> Like styling **all younger siblings**!

**📍 Key Points:**
- Uses tilde (~) symbol
- Selects all following siblings
- Elements must share same parent
- More flexible than adjacent

**🎨 Visual:**
```css
h2 ~ p {
    color: orange;
}

<h2>Heading</h2>
<p>This is orange</p>     ← Selected
<div>Some content</div>
<p>This is also orange</p> ← Also selected
```

**🎯 Use Cases:**
- All paragraphs after headings
- Related content styling
- Section-based formatting
- Content group styling

---

## 🎨 **CSS Variables**

> [!INFO] **Definition**: Custom properties that store reusable values
> Like **design tokens** for consistent styling!

**📍 Key Points:**
- Defined with double dashes (--name)
- Used with var() function
- Can be scoped to elements
- Great for theming and consistency

**🎨 Visual:**
```css
:root {
    --main-color: #3498db;
    --padding: 10px;
    --border-radius: 5px;
}

.button {
    background: var(--main-color);
    padding: var(--padding);
    border-radius: var(--border-radius);
}
```

**🎯 Use Cases:**
- Design system colors
- Consistent spacing values
- Theme switching
- Component libraries
- Brand color management

---

## 🧠 **Memory Tricks**

> [!NOTE] **Pseudo-class Memory** 🎭
> - **:hover** = Mouse **hovers** over
> - **:active** = Currently **active** (being clicked)
> - **:focus** = Has keyboard **focus**
> - **:first-child** = **First** kid in family
> - **:last-child** = **Last** kid in family

> [!TIP] **Combinator Memory** 🔗
> - **Space** = Family tree (any descendant)
> - **>** = Direct parent-child only
> - **+** = Next door neighbor (adjacent)
> - **~** = All neighbors after (general sibling)

> [!SUCCESS] **CSS Variables** 🎨
> - **Define**: `--name: value;` (double dash)
> - **Use**: `var(--name)` (var function)
> - **Scope**: `:root` for global, element for local

Back to: [[README CSS]]