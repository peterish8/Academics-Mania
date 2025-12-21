# 🚀 JavaScript Introduction, Variables & Data Types

## 🎯 What is JavaScript?
High-level, interpreted programming language for interactive web pages.

### Key Features
- **Lightweight** → Efficient and fast for web use
- **Dynamically Typed** → No type declarations needed
- **Multi-Paradigm** → Supports procedural, functional, and OOP
- **Runs Everywhere** → Browser (client-side) + Node.js (server-side)

## 🌐 Role in Web Development
- **HTML** → Structure (headings, paragraphs, buttons)
- **CSS** → Presentation (colors, fonts, layouts)  
- **JavaScript** → Behavior (interactions, validations, animations)

## 📝 Adding JS to HTML
1. **Internal Script**: `<script>console.log("Hello");</script>`
2. **External Script**: `<script src="app.js"></script>` (Recommended)
3. **Inline Script**: `<button onclick="alert('Hi')">Click</button>`

## 🔧 Console & Debugging
- `console.log()` → Print messages
- `console.error()` → Error messages
- `console.warn()` → Warning messages
- Browser DevTools → Inspect → Console tab

## 📦 Variables
Container for storing data.

### Declaration Methods
- `var` → Old way, function-scoped, hoisted
- `let` → Modern, block-scoped, allows reassignment
- `const` → Block-scoped, cannot be reassigned

### Scope Types
- **Global Scope** → Accessible anywhere
- **Block Scope** → Exists inside `{}` (let/const only)

### Hoisting
JavaScript moves declarations to top of scope:
- `var` → Hoisted with `undefined` value
- `let`/`const` → Hoisted but in Temporal Dead Zone

## 🎨 Data Types

### Primitive Types
- **String** → `"Hello"`, `'World'`
- **Number** → `25`, `99.99`
- **Boolean** → `true`, `false`
- **Undefined** → Variable declared but not assigned
- **Null** → Intentional empty value
- **BigInt** → Very large numbers (`123n`)

### Non-Primitive Types
- **Objects** → `{name: "Bob", age: 30}`
- **Arrays** → `["apple", "banana", "cherry"]`
- **Functions** → `function greet() {}`

## 🔍 typeof Operator
```javascript
typeof "hello"     // "string"
typeof 42          // "number"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object" (JavaScript quirk)
typeof {}          // "object"
typeof []          // "object"
typeof function(){} // "function"
```