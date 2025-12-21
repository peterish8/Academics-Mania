## 📚 Table of Contents
1. [Arrays & Array Methods](#arrays--array-methods)
2. [Normal Functions](#normal-functions)
3. [Arrow Functions](#arrow-functions)
4. [Rest & Spread Operator](#rest--spread-operator)
5. [JS Objects](#js-objects)
6. [Factory Functions](#factory-functions)
7. [Constructor Functions](#constructor-functions)
8. [Object & Object Methods](#object--object-methods)
9. [Value vs Reference](#value-vs-reference)
10. [Shallow vs Deep Copy](#shallow-vs-deep-copy)
11. [JSON Methods](#json-methods)
12. [JS Loops](#js-loops)

---

## 📊 Arrays & Array Methods

### 📖 Definition
Arrays are ordered collections of elements that can store multiple values in a single variable.

### 🎯 Key Methods
**Mutating:** push(), pop(), shift(), unshift(), splice(), sort(), reverse()
**Non-Mutating:** slice(), concat(), join(), indexOf(), includes()

### 💡 Mnemonics
**"PPSS"** - Push, Pop, Shift, unShift (basic array operations)
**"SCJI"** - Slice, Concat, Join, IndexOf (non-mutating methods)

### ✅ Do's
- Use push() to add elements to end
- Use slice() for copying arrays without mutation
- Use splice() for adding/removing elements at specific positions
- Check array length before accessing elements

### ❌ Don'ts
- Don't confuse slice() with splice()
- Don't modify arrays while iterating over them
- Don't use delete operator on array elements (creates holes)

### 🔧 Tips & Tricks
- splice() changes original array, slice() doesn't
- push() returns new length, pop() returns removed element
- Use spread operator [...arr] for quick array copying
- Array indices start from 0

### 🎯 Use Cases
- Storing lists of data (users, products, etc.)
- Managing dynamic collections
- Implementing stacks and queues
- Data manipulation and filtering

---

## 🔧 Normal Functions

### 📖 Definition
Traditional JavaScript functions declared using the `function` keyword with their own execution context.

### 🎯 Key Concepts
**Declaration:** function name() {}
**Expression:** const name = function() {}
**Hoisting:** Function declarations are fully hoisted

### 💡 Mnemonics
**"DEH"** - Declaration, Expression, Hoisting (function types)

### ✅ Do's
- Use function declarations for main functions
- Use descriptive function names
- Keep functions small and focused
- Return values explicitly

### ❌ Don'ts
- Don't create functions inside loops
- Don't rely on hoisting behavior
- Don't use too many parameters (use objects instead)

### 🔧 Tips & Tricks
- Functions have their own `this` context
- Can be called before declaration (hoisting)
- `arguments` object available inside functions
- Can be used as constructors with `new`

### 🎯 Use Cases
- Event handlers
- Reusable code blocks
- Constructor functions
- Callback functions

---

## ➡️ Arrow Functions

### 📖 Definition
ES6 syntax for writing functions with shorter syntax and lexical `this` binding.

### 🎯 Key Concepts
**Syntax:** () => {}
**Lexical this:** Inherits `this` from enclosing scope
**No hoisting:** Must be declared before use

### 💡 Mnemonics
**"SLN"** - Shorter syntax, Lexical this, No hoisting

### ✅ Do's
- Use for short, simple functions
- Use for callbacks and array methods
- Use when you need lexical `this` binding
- Use implicit return for single expressions

### ❌ Don'ts
- Don't use as constructor functions
- Don't use when you need `arguments` object
- Don't use for object methods (loses `this` context)

### 🔧 Tips & Tricks
- Parentheses optional for single parameter
- Curly braces optional for single expression
- No `this`, `arguments`, `super` binding
- Cannot be used with `new` keyword

### 🎯 Use Cases
- Array method callbacks (map, filter, reduce)
- Event handlers in React
- Short utility functions
- Functional programming patterns

---

## 🔄 Rest & Spread Operator

### 📖 Definition
Three dots (...) used to collect (rest) or expand (spread) elements.

### 🎯 Key Concepts
**Rest:** Collects multiple elements into array
**Spread:** Expands array/object elements
**Same syntax:** Context determines behavior

### 💡 Mnemonics
**"CES"** - Collect (rest), Expand (spread), Same syntax

### ✅ Do's
- Use rest for variable number of parameters
- Use spread for array/object copying
- Use spread for function arguments
- Use rest in destructuring

### ❌ Don'ts
- Don't confuse rest with spread
- Don't use rest parameter in middle of parameters
- Don't spread non-iterable objects

### 🔧 Tips & Tricks
- Rest must be last parameter in functions
- Spread creates shallow copies
- Works with both arrays and objects
- Can be used in destructuring assignments

### 🎯 Use Cases
- Function parameters with variable arguments
- Array/object cloning
- Merging arrays/objects
- Converting NodeList to Array

---

## 🏗️ JS Objects

### 📖 Definition
Objects are collections of key-value pairs that represent real-world entities.

### 🎯 Key Concepts
**Properties:** Key-value pairs
**Methods:** Functions as object properties
**Dynamic:** Can add/remove properties at runtime

### 💡 Mnemonics
**"PMD"** - Properties, Methods, Dynamic

### ✅ Do's
- Use object literals for simple objects
- Use dot notation for known properties
- Use bracket notation for dynamic properties
- Group related data and functions

### ❌ Don'ts
- Don't use reserved keywords as property names
- Don't modify Object.prototype
- Don't use objects as arrays

### 🔧 Tips & Tricks
- Objects are passed by reference
- Property names are strings (or Symbols)
- Can use computed property names
- `this` refers to the calling object

### 🎯 Use Cases
- Data modeling
- Configuration objects
- Namespacing
- API response handling

---

## 🏭 Factory Functions

### 📖 Definition
Functions that return new objects without using the `new` keyword.

### 🎯 Key Concepts
**Returns object:** Always returns new object
**No new keyword:** Called like regular function
**Closure:** Can create private variables

### 💡 Mnemonics
**"RNC"** - Returns object, No new, Closure

### ✅ Do's
- Use for creating multiple similar objects
- Use for encapsulation and privacy
- Return object literals
- Use parameters for customization

### ❌ Don'ts
- Don't forget to return the object
- Don't use `this` keyword inside
- Don't make them too complex

### 🔧 Tips & Tricks
- Can create private variables using closures
- More flexible than constructor functions
- Can return different object types
- No prototype chain by default

### 🎯 Use Cases
- Creating objects with private data
- Object creation without `new`
- Functional programming patterns
- Module pattern implementation

---

## 🏗️ Constructor Functions

### 📖 Definition
Functions used with `new` keyword to create objects with shared prototype.

### 🎯 Key Concepts
**New keyword:** Must use `new` to create instances
**This binding:** `this` refers to new object
**Prototype:** Shared methods via prototype

### 💡 Mnemonics
**"NTP"** - New keyword, This binding, Prototype

### ✅ Do's
- Start function name with capital letter
- Use `this` to set properties
- Add methods to prototype
- Always use with `new` keyword

### ❌ Don'ts
- Don't forget `new` keyword
- Don't add methods inside constructor
- Don't return values explicitly

### 🔧 Tips & Tricks
- Creates prototype chain automatically
- `instanceof` works with constructor functions
- Can check with `new.target`
- More memory efficient than factory functions

### 🎯 Use Cases
- Creating multiple instances of same type
- Implementing inheritance
- Building class-like structures
- Framework/library development

---

## 🔧 Object & Object Methods

### 📖 Definition
Built-in methods for working with objects and their properties.

### 🎯 Key Methods
**Object.keys():** Returns array of property names
**Object.values():** Returns array of property values
**Object.entries():** Returns array of [key, value] pairs
**Object.assign():** Copies properties between objects

### 💡 Mnemonics
**"KVEA"** - Keys, Values, Entries, Assign

### ✅ Do's
- Use Object.keys() to iterate over properties
- Use Object.assign() for shallow copying
- Use hasOwnProperty() to check own properties
- Use Object.create() for prototype-based inheritance

### ❌ Don'ts
- Don't use for...in without hasOwnProperty() check
- Don't modify objects during iteration
- Don't confuse Object.assign() with deep copying

### 🔧 Tips & Tricks
- Object.assign() performs shallow copy
- Object.keys() only returns enumerable properties
- Use Object.freeze() to make objects immutable
- Object.create(null) creates object without prototype

### 🎯 Use Cases
- Object property manipulation
- Converting objects to arrays
- Merging configuration objects
- Creating object copies

---

## 📊 Value vs Reference

### 📖 Definition
How JavaScript handles different data types in memory and assignment.

### 🎯 Key Concepts
**Primitives:** Passed by value (copy)
**Objects:** Passed by reference (memory address)
**Mutation:** Objects can be changed through references

### 💡 Mnemonics
**"POR"** - Primitives by value, Objects by Reference

### ✅ Do's
- Understand primitive vs reference types
- Use spread operator for shallow copying
- Be careful when modifying object parameters
- Use const for object references

### ❌ Don'ts
- Don't assume object assignment creates copies
- Don't modify objects passed as parameters
- Don't confuse reference equality with value equality

### 🔧 Tips & Tricks
- Primitives: Number, String, Boolean, null, undefined
- Objects: Arrays, Functions, Objects, Dates
- === compares references for objects
- Changing object properties affects all references

### 🎯 Use Cases
- Understanding function parameter behavior
- Avoiding unintended mutations
- Implementing proper copying strategies
- Memory management optimization

---

## 📋 Shallow vs Deep Copy

### 📖 Definition
Different levels of copying objects and their nested properties.

### 🎯 Key Concepts
**Shallow Copy:** Copies first level only
**Deep Copy:** Copies all nested levels
**Reference sharing:** Shallow copies share nested object references

### 💡 Mnemonics
**"SDR"** - Shallow (first level), Deep (all levels), Reference sharing

### ✅ Do's
- Use spread operator for shallow copying
- Use JSON methods for simple deep copying
- Understand when each type is needed
- Use libraries like Lodash for complex deep copying

### ❌ Don'ts
- Don't use JSON methods for objects with functions
- Don't assume spread operator creates deep copies
- Don't modify nested objects in shallow copies

### 🔧 Tips & Tricks
- Spread operator: {...obj} or [...arr]
- JSON method: JSON.parse(JSON.stringify(obj))
- JSON method limitations: functions, dates, undefined
- Libraries provide robust deep copy solutions

### 🎯 Use Cases
- Preventing unintended mutations
- State management in applications
- Creating independent object copies
- Data transformation without side effects

---

## 📋 JSON Methods

### 📖 Definition
JavaScript Object Notation methods for converting between objects and strings.

### 🎯 Key Methods
**JSON.stringify():** Object to JSON string
**JSON.parse():** JSON string to object
**Error handling:** Use try-catch for parsing

### 💡 Mnemonics
**"SPE"** - Stringify, Parse, Error handling

### ✅ Do's
- Use for data serialization
- Handle parsing errors with try-catch
- Understand JSON limitations
- Use for simple deep copying

### ❌ Don'ts
- Don't stringify functions or undefined
- Don't parse untrusted JSON without validation
- Don't rely on JSON for complex object copying

### 🔧 Tips & Tricks
- JSON.stringify() omits functions and undefined
- Dates become strings when stringified
- Can use replacer function in stringify()
- Can use reviver function in parse()

### 🎯 Use Cases
- API data exchange
- Local storage data persistence
- Configuration file handling
- Simple object deep copying

---

## 🔄 JS Loops

### 📖 Definition
Control structures for repeating code execution based on conditions.

### 🎯 Key Types
**for loop:** Counter-based iteration
**while loop:** Condition-based iteration
**do-while loop:** Execute at least once

### 💡 Mnemonics
**"FWD"** - For, While, Do-while

### ✅ Do's
- Use for loop for known iterations
- Use while loop for unknown iterations
- Use do-while when you need at least one execution
- Always ensure loop termination conditions

### ❌ Don'ts
- Don't create infinite loops
- Don't modify loop counter inside loop body
- Don't use loops when array methods are better

### 🔧 Tips & Tricks
- for loop has three parts: init, condition, increment
- while loop checks condition before execution
- do-while checks condition after execution
- Use break and continue for flow control

### 🎯 Use Cases
- Array iteration
- Counting operations
- Conditional repetition
- Game loops and animations

---

## 🎯 Quick Study Tips

### 🧠 Memory Techniques
1. **Practice coding daily** - Build muscle memory
2. **Use browser console** - Test concepts immediately
3. **Create small projects** - Apply multiple concepts together
4. **Explain concepts aloud** - Teaching reinforces learning

### ⏰ Last-Minute Preparation
1. Review array method differences (mutating vs non-mutating)
2. Practice function syntax variations
3. Understand object creation patterns
4. Know value vs reference behavior

### 🔍 Common Pitfalls to Avoid
- Confusing slice() with splice()
- Forgetting `new` keyword with constructors
- Assuming spread creates deep copies
- Not handling JSON parsing errors

---

*💡 Focus on understanding concepts and their practical applications rather than just memorizing syntax!*