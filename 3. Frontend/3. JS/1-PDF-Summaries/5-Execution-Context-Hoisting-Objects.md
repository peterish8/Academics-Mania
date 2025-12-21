# ⚙️ Execution Context, Hoisting & Objects

## 🔄 JavaScript Execution Context

### How JS Code Runs
1. **Global Execution Context** created first
2. **Two phases** for each execution context:
   - **Memory Creation Phase** → Allocate memory, assign `undefined`
   - **Code Execution Phase** → Execute line by line, assign values

### Call Stack
- Manages execution contexts
- **LIFO** (Last In, First Out) structure
- Global context at bottom, function contexts pushed/popped

## 🚁 Hoisting Deep Dive
Memory allocation happens before code execution.

### Variable Hoisting
```javascript
console.log(x); // undefined (not error)
var x = 10;

// let/const in Temporal Dead Zone
console.log(y); // ReferenceError
let y = 20;
```

### Function Hoisting
```javascript
// Function declarations fully hoisted
sayHi(); // Works!
function sayHi() { console.log("Hi"); }

// Function expressions not hoisted
sayBye(); // TypeError
var sayBye = function() { console.log("Bye"); };
```

## 🔧 String Methods
- `split('')` → Convert string to array
- `join(',')` → Convert array to string

## 📦 Rest Operator (...args)
Collects remaining arguments into array.
```javascript
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3, 4); // 10
```

## 🌟 Spread Operator (...)
Expands arrays/objects.
```javascript
// Arrays
let arr1 = [1, 2];
let arr2 = [3, 4];
let combined = [...arr1, ...arr2]; // [1, 2, 3, 4]

// Objects
let obj1 = {a: 1};
let obj2 = {b: 2};
let merged = {...obj1, ...obj2}; // {a: 1, b: 2}
```

## 🏗️ Objects Fundamentals

### Object Creation
```javascript
// Object literal (recommended)
const user = {
  name: "Alice",
  age: 30,
  greet() { return `Hi, I'm ${this.name}`; }
};

// Constructor
const car = new Object();
car.make = "Toyota";
```

### Property Access
- **Dot notation**: `obj.property`
- **Bracket notation**: `obj["property"]` or `obj[variable]`

### this Keyword
- **Object method**: `this` refers to the object
- **Arrow functions**: `this` from outer scope
- **Global scope**: `this` refers to window (browser)

### Adding/Updating/Deleting
```javascript
obj.newProp = "value";    // Add
obj.existingProp = "new"; // Update
delete obj.unwanted;      // Delete
```