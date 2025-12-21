# 📊 Arrays & Functions Fundamentals

## 💬 prompt() Method
Displays dialog box for user input.
```javascript
let person = prompt("Enter your name", "Default Name");
if (person != null) {
  console.log("Hello " + person);
}
```

## 📋 Arrays

### What is an Array?
Special object to store multiple values in ordered sequence, accessed by index (starting from 0).

### Creating Arrays
```javascript
// Array literal (recommended)
let fruits = ["apple", "banana", "cherry"];

// Array constructor
let numbers = new Array(10, 20, 30);
let empty = new Array(5); // Creates array with 5 empty slots
```

### Array Property
- `length` → Total number of elements

### Common Array Methods

#### Adding/Removing Elements
- `push()` → Add to end
- `pop()` → Remove from end
- `unshift()` → Add to beginning
- `shift()` → Remove from beginning

#### Modifying Arrays
- `splice(start, deleteCount, item1, item2...)` → Add/remove at specific index
- `slice(start, end)` → Extract portion (doesn't change original)
- `concat()` → Merge arrays

#### Searching
- `indexOf()` → Find index of element (-1 if not found)
- `includes()` → Check if element exists (true/false)

### Array Examples
```javascript
let arr = [1, 2, 3];
arr.push(4);        // [1, 2, 3, 4]
arr.pop();          // [1, 2, 3]
arr.unshift(0);     // [0, 1, 2, 3]
arr.shift();        // [1, 2, 3]

let part = arr.slice(1, 3);  // [2, 3] (doesn't change arr)
arr.splice(1, 1, "x", "y");  // [1, "x", "y", 3]
```

## 🔧 Functions

### Function Declaration
```javascript
function greet(name) {
  return `Hello, ${name}`;
}
console.log(greet("Alice")); // "Hello, Alice"
```

**Key Points**:
- **Hoisted** → Can call before definition
- **Reusable** → Avoid code repetition
- **Named** → Better for debugging

### Function Expression
```javascript
const add = function(x, y) {
  return x + y;
};
console.log(add(5, 3)); // 8
```

**Key Points**:
- **Not hoisted** → Must define before calling
- **Can be anonymous**
- **Good for callbacks**

### Parameters & Return Values
```javascript
function multiply(a, b) {  // a, b are parameters
  return a * b;            // return value
}
let result = multiply(4, 5); // 4, 5 are arguments
```

### Arrow Functions
```javascript
// Regular function
function square(x) {
  return x * x;
}

// Arrow function
const squareArrow = (x) => x * x;

// Multiple parameters
const add = (a, b) => a + b;

// Block body (need explicit return)
const complex = (x) => {
  let result = x * 2;
  return result + 1;
};
```

### Key Differences: Arrow vs Regular
- **`this` binding** → Arrow functions inherit `this` from outer scope
- **Hoisting** → Arrow functions not hoisted
- **Implicit return** → Single expression returns automatically

### Function Examples
```javascript
// Function with default parameter
function greet(name = "Guest") {
  return `Hello, ${name}`;
}

// Function as callback
setTimeout(function() {
  console.log("Executed after 2 seconds");
}, 2000);

// Arrow function callback
numbers.map(n => n * 2);
```