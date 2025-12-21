# 📊 Arrays & Functions Deep Dive

## 💬 User Input with prompt()

### 🎯 What is prompt()?
**Definition**: A built-in browser method that displays a dialog box for user input.

**Syntax**: `prompt(message, defaultValue)`

### 📝 How prompt() Works
```javascript
// Basic usage
let name = prompt("What's your name?");
console.log("Hello, " + name);

// With default value
let age = prompt("How old are you?", "25");

// Handle cancellation
let city = prompt("Which city are you from?");
if (city === null) {
  console.log("User cancelled");
} else if (city === "") {
  console.log("User entered empty string");
} else {
  console.log("User lives in " + city);
}
```

### 🎯 Important Notes
- **Returns string** → Always converts input to string
- **Returns null** → If user clicks Cancel
- **Returns empty string** → If user clicks OK without typing
- **Blocks execution** → Page freezes until user responds

### 🔄 Type Conversion with prompt()
```javascript
// Convert to number
let ageString = prompt("Enter your age:");
let ageNumber = Number(ageString);
// or
let ageNumber2 = parseInt(ageString);

// Validate numeric input
let score = prompt("Enter your score:");
if (isNaN(score) || score === "") {
  console.log("Invalid number");
} else {
  console.log("Your score is: " + score);
}
```

**Memory Trick**: "prompt() = Prompts user, returns string or null"

---

## 📋 Arrays Mastery

### 🎯 What is an Array?
**Definition**: A special type of object that stores multiple values in an ordered sequence, accessed by numeric indices starting from 0.

**Real-world analogy**: Like a numbered list or a row of mailboxes, each with an address (index).

### 🏗️ Array Creation Methods

#### 1️⃣ Array Literal (Recommended)
```javascript
let fruits = ["apple", "banana", "cherry"];
let numbers = [1, 2, 3, 4, 5];
let mixed = ["hello", 42, true, null, {name: "Alice"}];
let empty = [];
```

#### 2️⃣ Array Constructor
```javascript
// Create with initial values
let colors = new Array("red", "green", "blue");

// Create empty array with specific length
let emptyArray = new Array(5); // [empty × 5]

// ⚠️ Gotcha: Single number creates empty array of that length
let confusing = new Array(3);    // [empty × 3]
let notConfusing = [3];          // [3]
```

#### 3️⃣ Dynamic Array Building
```javascript
let dynamicArray = [];
dynamicArray[0] = "first";
dynamicArray[1] = "second";
dynamicArray[5] = "sixth"; // Creates sparse array [empty × 3]

console.log(dynamicArray); // ["first", "second", empty × 3, "sixth"]
console.log(dynamicArray.length); // 6
```

### 📏 Array Length Property
```javascript
let items = ["a", "b", "c", "d"];
console.log(items.length); // 4

// Length is writable!
items.length = 2;
console.log(items); // ["a", "b"] (truncated!)

items.length = 5;
console.log(items); // ["a", "b", empty × 3] (extended with empty slots)
```

---

## 🛠️ Array Methods Deep Dive

### 1️⃣ Adding/Removing Elements

#### End Operations (push/pop)
```javascript
let stack = [1, 2, 3];

// Add to end
stack.push(4);           // [1, 2, 3, 4] - returns new length (4)
stack.push(5, 6, 7);     // [1, 2, 3, 4, 5, 6, 7] - can add multiple

// Remove from end
let last = stack.pop();  // Returns 7, array becomes [1, 2, 3, 4, 5, 6]
console.log(last);       // 7
```

#### Beginning Operations (unshift/shift)
```javascript
let queue = [2, 3, 4];

// Add to beginning
queue.unshift(1);        // [1, 2, 3, 4] - returns new length (4)
queue.unshift(-1, 0);    // [-1, 0, 1, 2, 3, 4] - can add multiple

// Remove from beginning
let first = queue.shift(); // Returns -1, array becomes [0, 1, 2, 3, 4]
console.log(first);        // -1
```

**Memory Trick**: 
- "push/pop = end operations (like a stack)"
- "unshift/shift = beginning operations (like a queue)"

### 2️⃣ Advanced Array Manipulation

#### splice() - The Swiss Army Knife
```javascript
let arr = ["a", "b", "c", "d", "e"];

// Remove elements
let removed = arr.splice(1, 2); // Remove 2 elements starting at index 1
console.log(removed);           // ["b", "c"]
console.log(arr);              // ["a", "d", "e"]

// Insert elements
arr.splice(1, 0, "x", "y");    // Insert at index 1, remove 0
console.log(arr);              // ["a", "x", "y", "d", "e"]

// Replace elements
arr.splice(1, 2, "z");         // Replace 2 elements with 1
console.log(arr);              // ["a", "z", "d", "e"]
```

#### slice() - Non-destructive Copy
```javascript
let original = ["a", "b", "c", "d", "e"];

let copy1 = original.slice();      // ["a", "b", "c", "d", "e"] (full copy)
let copy2 = original.slice(1, 4);  // ["b", "c", "d"] (from index 1 to 3)
let copy3 = original.slice(-3);    // ["c", "d", "e"] (last 3 elements)
let copy4 = original.slice(-3, -1); // ["c", "d"] (negative indices)

console.log(original); // ["a", "b", "c", "d", "e"] (unchanged!)
```

**Key Difference**: 
- **splice()** → Modifies original array, returns removed elements
- **slice()** → Creates new array, original unchanged

### 3️⃣ Array Combination

#### concat() - Merge Arrays
```javascript
let arr1 = [1, 2];
let arr2 = [3, 4];
let arr3 = [5, 6];

// Combine multiple arrays
let combined = arr1.concat(arr2, arr3);
console.log(combined); // [1, 2, 3, 4, 5, 6]

// Add individual elements
let withExtras = arr1.concat(arr2, 7, 8, [9, 10]);
console.log(withExtras); // [1, 2, 3, 4, 7, 8, 9, 10]

// Original arrays unchanged
console.log(arr1); // [1, 2]
```

#### Modern Alternative: Spread Operator
```javascript
let arr1 = [1, 2];
let arr2 = [3, 4];
let arr3 = [5, 6];

// More flexible and readable
let combined = [...arr1, ...arr2, ...arr3];
let withExtras = [...arr1, ...arr2, 7, 8, ...arr3];
```

### 4️⃣ Array Searching

#### indexOf() and lastIndexOf()
```javascript
let fruits = ["apple", "banana", "apple", "cherry", "apple"];

console.log(fruits.indexOf("apple"));     // 0 (first occurrence)
console.log(fruits.lastIndexOf("apple")); // 4 (last occurrence)
console.log(fruits.indexOf("grape"));     // -1 (not found)

// Start searching from specific index
console.log(fruits.indexOf("apple", 1));  // 2 (first occurrence after index 1)
```

#### includes() - Boolean Check
```javascript
let numbers = [1, 2, 3, 4, 5];

console.log(numbers.includes(3));    // true
console.log(numbers.includes(6));    // false
console.log(numbers.includes(3, 3)); // false (start searching from index 3)

// Works with NaN (unlike indexOf)
let withNaN = [1, NaN, 3];
console.log(withNaN.includes(NaN));  // true
console.log(withNaN.indexOf(NaN));   // -1
```

### 🎯 Array Method Patterns
```javascript
// Method chaining
let result = [1, 2, 3, 4, 5]
  .slice(1, 4)    // [2, 3, 4]
  .concat([6, 7]) // [2, 3, 4, 6, 7]
  .reverse();     // [7, 6, 4, 3, 2]

// Check if array is empty
function isEmpty(arr) {
  return arr.length === 0;
}

// Safe array access
function safeGet(arr, index) {
  return index >= 0 && index < arr.length ? arr[index] : undefined;
}
```

---

## 🔧 Functions Mastery

### 🎯 What is a Function?
**Definition**: A reusable block of code that performs a specific task, can accept inputs (parameters), and can return outputs.

**Real-world analogy**: Like a recipe or a machine - you give it ingredients (parameters), it processes them, and gives you a result (return value).

### 🏗️ Function Declaration Deep Dive

```javascript
function calculateArea(length, width) {
  let area = length * width;
  return area;
}

// Function anatomy:
// - function keyword
// - function name (calculateArea)
// - parameters in parentheses (length, width)
// - function body in curly braces
// - return statement (optional)
```

#### 🚁 Hoisting with Function Declarations
```javascript
// This works! Function declarations are fully hoisted
console.log(sayHello("Alice")); // "Hello, Alice!"

function sayHello(name) {
  return `Hello, ${name}!`;
}

// JavaScript sees it as:
// function sayHello(name) { return `Hello, ${name}!`; }
// console.log(sayHello("Alice"));
```

### 🎯 Function Expression Deep Dive

```javascript
// Anonymous function expression
const multiply = function(a, b) {
  return a * b;
};

// Named function expression (better for debugging)
const divide = function divideNumbers(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
};

console.log(multiply(4, 5)); // 20
console.log(divide(10, 2));  // 5
```

#### ⚠️ No Hoisting with Function Expressions
```javascript
// This throws an error!
console.log(add(2, 3)); // TypeError: add is not a function

var add = function(a, b) {
  return a + b;
};

// JavaScript sees it as:
// var add; // undefined
// console.log(add(2, 3)); // Error: undefined is not a function
// add = function(a, b) { return a + b; };
```

### 🏹 Arrow Functions Mastery

#### Basic Syntax Evolution
```javascript
// Traditional function
function square(x) {
  return x * x;
}

// Function expression
const square2 = function(x) {
  return x * x;
};

// Arrow function (full syntax)
const square3 = (x) => {
  return x * x;
};

// Arrow function (concise)
const square4 = x => x * x;
```

#### 🎯 Arrow Function Variations
```javascript
// No parameters
const greet = () => "Hello World!";

// One parameter (parentheses optional)
const double = x => x * 2;
const triple = (x) => x * 3; // Parentheses for clarity

// Multiple parameters
const add = (a, b) => a + b;
const fullName = (first, last) => `${first} ${last}`;

// Block body (need explicit return)
const complexCalc = (x, y) => {
  let temp = x * 2;
  let result = temp + y;
  return result;
};

// Returning objects (wrap in parentheses)
const createUser = (name, age) => ({
  name: name,
  age: age,
  isActive: true
});
```

#### 🎯 this Binding Differences
```javascript
const obj = {
  name: "Alice",
  
  // Regular function - 'this' refers to obj
  regularMethod: function() {
    console.log(`Regular: ${this.name}`); // "Regular: Alice"
  },
  
  // Arrow function - 'this' from outer scope
  arrowMethod: () => {
    console.log(`Arrow: ${this.name}`); // "Arrow: undefined"
  },
  
  // Nested example
  nestedExample: function() {
    console.log(`Outer: ${this.name}`); // "Outer: Alice"
    
    // Regular function loses 'this' context
    setTimeout(function() {
      console.log(`Timeout regular: ${this.name}`); // "Timeout regular: undefined"
    }, 100);
    
    // Arrow function preserves 'this' context
    setTimeout(() => {
      console.log(`Timeout arrow: ${this.name}`); // "Timeout arrow: Alice"
    }, 200);
  }
};
```

### 📥📤 Parameters & Return Values

#### 🎯 Parameter Handling
```javascript
// Default parameters
function greet(name = "Guest", greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

console.log(greet());                    // "Hello, Guest!"
console.log(greet("Alice"));             // "Hello, Alice!"
console.log(greet("Bob", "Hi"));         // "Hi, Bob!"

// Rest parameters (...args)
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // 15

// Mixed parameters
function introduce(name, age, ...hobbies) {
  console.log(`I'm ${name}, ${age} years old`);
  console.log(`My hobbies: ${hobbies.join(", ")}`);
}

introduce("Alice", 25, "reading", "coding", "hiking");
```

#### 🔄 Return Value Patterns
```javascript
// Early return (guard clauses)
function divide(a, b) {
  if (b === 0) {
    return "Cannot divide by zero";
  }
  return a / b;
}

// Multiple return points
function getGrade(score) {
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

// Returning objects
function createPoint(x, y) {
  return {
    x: x,
    y: y,
    distance: Math.sqrt(x * x + y * y)
  };
}

// Returning functions (higher-order functions)
function createMultiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);
console.log(double(5)); // 10
console.log(triple(4)); // 12
```

### 🔄 Function as First-Class Citizens

#### Functions as Arguments (Callbacks)
```javascript
function processArray(arr, callback) {
  let result = [];
  for (let item of arr) {
    result.push(callback(item));
  }
  return result;
}

// Using with different callbacks
let numbers = [1, 2, 3, 4, 5];

let doubled = processArray(numbers, x => x * 2);
let squared = processArray(numbers, x => x * x);
let strings = processArray(numbers, x => `Number: ${x}`);

console.log(doubled); // [2, 4, 6, 8, 10]
console.log(squared); // [1, 4, 9, 16, 25]
console.log(strings); // ["Number: 1", "Number: 2", ...]
```

#### Functions as Return Values
```javascript
function createValidator(minLength) {
  return function(input) {
    return input.length >= minLength;
  };
}

const validatePassword = createValidator(8);
const validateUsername = createValidator(3);

console.log(validatePassword("12345"));    // false
console.log(validatePassword("12345678")); // true
console.log(validateUsername("ab"));       // false
console.log(validateUsername("abc"));      // true
```

---

## 🎯 Practical Patterns & Best Practices

### ✅ Array Best Practices
1. **Use meaningful names** → `users` not `arr`
2. **Check array length** before accessing elements
3. **Use appropriate methods** → `slice()` for copying, `splice()` for modifying
4. **Consider performance** → `push()` is faster than `unshift()`

### ✅ Function Best Practices
1. **Single responsibility** → One function, one task
2. **Pure functions** → Same input = same output, no side effects
3. **Meaningful names** → `calculateTax()` not `calc()`
4. **Keep functions small** → Easier to test and debug

### 🧠 Memory Tricks
- **Arrays** = "Ordered lists with numbered slots"
- **push/pop** = "Stack operations (end)"
- **shift/unshift** = "Queue operations (beginning)"
- **Function declaration** = "Hoisted and named"
- **Function expression** = "Not hoisted, can be anonymous"
- **Arrow functions** = "Concise syntax, lexical this"

**Master Memory Trick**: "Arrays store data, Functions process data - together they power JavaScript applications"