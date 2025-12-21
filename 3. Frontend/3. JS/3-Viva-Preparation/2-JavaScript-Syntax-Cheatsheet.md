
## 📊 Arrays & Array Methods

### Array Creation
```javascript
let arr1 = [];                    // Empty array
let arr2 = [1, 2, 3];            // Array literal ---> [1, 2, 3]
let arr3 = new Array(5);         // Array with 5 empty slots
let arr4 = Array.of(1, 2, 3);    // [1, 2, 3]
```

### Mutating Array Methods
```javascript
/*
--- 1. Mutating Methods (Change the Original Array) ---
*/

// --- push() ---
// Adds one or more elements to the end
let pets = ["dog", "cat"];
// pets is: ["dog", "cat"]
let newLength = pets.push("hamster", "fish");
// newLength is: 4
// pets is: ["dog", "cat", "hamster", "fish"]

// --- pop() ---
// Removes the last element
let colors = ["red", "green", "blue"];
// colors is: ["red", "green", "blue"]
let removedColor = colors.pop();
// removedColor is: "blue"
// colors is: ["red", "green"]

// --- shift() ---
// Removes the first element
let tools = ["hammer", "saw", "drill"];
// tools is: ["hammer", "saw", "drill"]
let removedTool = tools.shift();
// removedTool is: "hammer"
// tools is: ["saw", "drill"]

// --- unshift() ---
// Adds one or more elements to the start
let numbers = [10, 20];
// numbers is: [10, 20]
let newLength2 = numbers.unshift(0, 5);
// newLength2 is: 4
// numbers is: [0, 5, 10, 20]

// --- splice() ---
// Adds, removes, or replaces elements
let letters = ["a", "b", "c", "d", "e"];
// letters is: ["a", "b", "c", "d", "e"]
let removedLetters = letters.splice(1, 2); // Removes "b", "c"
// removedLetters is: ["b", "c"]
// letters is: ["a", "d", "e"]

let moreLetters = ["x", "y", "z"];
// moreLetters is: ["x", "y", "z"]
moreLetters.splice(1, 0, "a", "b"); // Adds "a", "b" at index 1
// moreLetters is: ["x", "a", "b", "y", "z"]

let vehicles = ["car", "bus", "bike"];
// vehicles is: ["car", "bus", "bike"]
vehicles.splice(0, 1, "truck"); // Replaces "car" with "truck"
// vehicles is: ["truck", "bus", "bike"]

// --- sort() ---
// Sorts the elements
let names = ["Zoe", "Adam", "Eve", "Bob"];
// names is: ["Zoe", "Adam", "Eve", "Bob"]
names.sort();
// names is: ["Adam", "Bob", "Eve", "Zoe"]

let scores = [100, 5, 25];
// scores is: [100, 5, 25]
scores.sort((a, b) => a - b); // Correct numeric sort
// scores is: [5, 25, 100]

// --- reverse() ---
// Reverses the order of elements
let countdown = [1, 2, 3, 4, 5];
// countdown is: [1, 2, 3, 4, 5]
countdown.reverse();
// countdown is: [5, 4, 3, 2, 1]

/*
--- 2. Non-Mutating Methods (Create New Arrays/Values) ---
*/

// --- concat() ---
// Joins two or more arrays
let arr1 = ["a", "b"];
// arr1 is: ["a", "b"]
let arr2 = ["c", "d"];
// arr2 is: ["c", "d"]
let combined = arr1.concat(arr2);
// combined is: ["a", "b", "c", "d"]
// arr1 is still: ["a", "b"]

// --- slice() ---
// Copies a portion of an array
let animals = ["ant", "bison", "camel", "duck", "elephant"];
// animals is: ["ant", "bison", "camel", "duck", "elephant"]
let middle = animals.slice(1, 4); // Start at index 1, end before index 4
// middle is: ["bison", "camel", "duck"]
// animals is still: ["ant", "bison", "camel", "duck", "elephant"]

// --- map() ---
// Creates a new array by transforming every element
let prices = [10, 20, 30];
// prices is: [10, 20, 30]
let withTax = prices.map(price => price * 1.1);
// withTax is: [11, 22, 33]
// prices is still: [10, 20, 30]

// --- filter() ---
// Creates a new array with elements that pass a test
let allNumbers = [1, 5, 10, 15, 20];
// allNumbers is: [1, 5, 10, 15, 20]
let over10 = allNumbers.filter(num => num > 10);
// over10 is: [15, 20]
// allNumbers is still: [1, 5, 10, 15, 20]

// --- find() ---
// Returns the first element that passes a test
let users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 35 }
];
// users is: (array of objects)
let userBob = users.find(user => user.name === "Bob");
// userBob is: { name: "Bob", age: 30 }
// users is still: (array of objects)

// --- includes() ---
// Checks if an array contains a certain value
let pantry = ["flour", "sugar", "eggs"];
// pantry is: ["flour", "sugar", "eggs"]
let hasSugar = pantry.includes("sugar");
// hasSugar is: true
let hasMilk = pantry.includes("milk");
// hasMilk is: false

// --- join() ---
// Joins all elements into a string
let words = ["Hello", "World"];
// words is: ["Hello", "World"]
let sentence = words.join(" ");
// sentence is: "Hello World"
// words is still: ["Hello", "World"]

// --- reduce() ---
// Reduces the array to a single value
let costs = [10.50, 5.00, 20.00];
// costs is: [10.50, 5.00, 20.00]
let total = costs.reduce((sum, currentCost) => sum + currentCost, 0);
// total is: 35.5
// costs is still: [10.50, 5.00, 20.00]
```

### Non-Mutating Array Methods
```javascript
let numbers = [1, 2, 3, 4, 5];

// Extract portions
let slice = numbers.slice(1, 4);              // [2, 3, 4] (start, end)
let copy = numbers.slice();                   // Full copy

// Combine arrays
let combined = numbers.concat([6, 7]);        // [1, 2, 3, 4, 5, 6, 7]

// Convert to string
let joined = numbers.join("-");               // "1-2-3-4-5"

// Search methods
let index = numbers.indexOf(3);               // 2
let exists = numbers.includes(4);             // true
```

---

## 🔧 Normal Functions

### Function Declaration
```javascript

// Can be called before declaration (hoisting)
console.log(greet("John"));  // Works due to hoisting

function greet(name) {
    return `Hello, ${name}!`;
}
```

### Function Expression
```javascript
const greet = function(name) {
    return `Hello, ${name}!`;
};

// Cannot be called before declaration
```

### Function with Default Parameters
```javascript
function greet(name = "World") {
    return `Hello, ${name}!`;
}
```

### Function with Rest Parameters
```javascript
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}
sum(1, 2, 3, 4);  // 10
```

### Function Properties
```javascript
function example() {
    console.log(arguments.length);    // Number of arguments
    console.log(this);                // Context object
}
```

---

## ➡️ Arrow Functions

### Basic Syntax
```javascript
// Basic arrow function
const greet = (name) => {
    return `Hello, ${name}!`;
};

// Single parameter (parentheses optional)
const greet = name => {
    return `Hello, ${name}!`;
};

// Multiple parameters
const add = (a, b) => {
    return a + b;
};

// No parameters
const sayHello = () => {
    return "Hello!";
};
```

### Implicit Return
```javascript
// Single expression - implicit return
const add = (a, b) => a + b;
const greet = name => `Hello, ${name}!`;
const getUser = () => ({name: "John", age: 30});  // Return object
```

### Arrow Functions in Array Methods
```javascript
let numbers = [1, 2, 3, 4, 5];

let doubled = numbers.map(x => x * 2);
let evens = numbers.filter(x => x % 2 === 0);
let sum = numbers.reduce((acc, x) => acc + x, 0);
```

---

## 🔄 Rest & Spread Operator

### Rest Operator (Collect)
```javascript
// In function parameters
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

// In destructuring
let [first, ...rest] = [1, 2, 3, 4, 5];
// first = 1, rest = [2, 3, 4, 5]

let {name, ...otherProps} = {name: "John", age: 30, city: "NYC"};
// name = "John", otherProps = {age: 30, city: "NYC"}
```

### Spread Operator (Expand)
```javascript
// With arrays
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combined = [...arr1, ...arr2];        // [1, 2, 3, 4, 5, 6]
let copy = [...arr1];                     // [1, 2, 3]

// With objects
let obj1 = {a: 1, b: 2};
let obj2 = {c: 3, d: 4};
let combined = {...obj1, ...obj2};        // {a: 1, b: 2, c: 3, d: 4}
let copy = {...obj1};                     // {a: 1, b: 2}

// In function calls
function sum(a, b, c) {
    return a + b + c;
}
let numbers = [1, 2, 3];
sum(...numbers);                          // Same as sum(1, 2, 3)
```

---

## 🏗️ JS Objects

### Object Creation
```javascript
// Object literal
let person = {
    name: "John",
    age: 30,
    greet: function() {
        return `Hello, I'm ${this.name}`;
    }
};

// Empty object
let obj = {};

// Adding properties
obj.name = "John";
obj["age"] = 30;
```

### Property Access
```javascript
let person = {name: "John", age: 30};

// Dot notation
person.name;                // "John"
person.age = 31;            // Set value

// Bracket notation
person["name"];             // "John"
person["age"] = 32;         // Set value

// Dynamic property access
let prop = "name";
person[prop];               // "John"
```

### Object Methods
```javascript
let person = {
    name: "John",
    age: 30,
    
    // Method shorthand (ES6)
    greet() {
        return `Hello, I'm ${this.name}`;
    },
    
    // Traditional method
    sayAge: function() {
        return `I'm ${this.age} years old`;
    }
};
```

---

## 🏭 Factory Functions

### Basic Factory Function
```javascript
function createPerson(name, age) {
    return {
        name: name,
        age: age,
        greet: function() {
            return `Hello, I'm ${this.name}`;
        }
    };
}

// Usage
let john = createPerson("John", 30);
let jane = createPerson("Jane", 25);
```

### Factory with Private Variables
```javascript
function createCounter() {
    let count = 0;  // Private variable
    
    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
}

let counter = createCounter();
counter.increment();  // 1
```

---

## 🏗️ Constructor Functions

### Basic Constructor
```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// Add methods to prototype
Person.prototype.greet = function() {
    return `Hello, I'm ${this.name}`;
};

// Usage
let john = new Person("John", 30);
let jane = new Person("Jane", 25);
```

### Constructor with Methods
```javascript
function Car(make, model) {
    this.make = make;
    this.model = model;
    this.isRunning = false;
}

Car.prototype.start = function() {
    this.isRunning = true;
    return `${this.make} ${this.model} started`;
};

Car.prototype.stop = function() {
    this.isRunning = false;
    return `${this.make} ${this.model} stopped`;
};
```

---

## 🔧 Object & Object Methods

### Built-in Object Methods
```javascript
let obj = {a: 1, b: 2, c: 3};

// Get keys, values, entries
Object.keys(obj);           // ["a", "b", "c"]
Object.values(obj);         // [1, 2, 3]
Object.entries(obj);        // [["a", 1], ["b", 2], ["c", 3]]

// Property checking
obj.hasOwnProperty("a");    // true
"a" in obj;                 // true

// Object manipulation
Object.assign({}, obj);     // Shallow copy
Object.freeze(obj);         // Make immutable
Object.seal(obj);           // Prevent adding/removing properties
```

### Object Creation Methods
```javascript
// Object.create()
let proto = {greet: function() { return "Hello"; }};
let obj = Object.create(proto);
obj.name = "John";

// Object.assign() - copying/merging
let target = {a: 1};
let source = {b: 2, c: 3};
Object.assign(target, source);  // target becomes {a: 1, b: 2, c: 3}
```

---

## 📊 Value vs Reference

### Primitive Types (Value)
```javascript
let a = 5;
let b = a;      // b gets copy of a's value
a = 10;         // a changes, b remains 5
console.log(b); // 5
```

### Reference Types (Reference)
```javascript
let obj1 = {name: "John"};
let obj2 = obj1;           // obj2 gets reference to same object
obj1.name = "Jane";        // Modify through obj1
console.log(obj2.name);    // "Jane" - obj2 sees the change

let arr1 = [1, 2, 3];
let arr2 = arr1;           // arr2 references same array
arr1.push(4);              // Modify through arr1
console.log(arr2);         // [1, 2, 3, 4] - arr2 sees the change
```

### Function Parameters
```javascript
function modifyPrimitive(x) {
    x = 100;               // Only changes local copy
}

function modifyObject(obj) {
    obj.name = "Modified";  // Changes original object
}

let num = 5;
let person = {name: "John"};

modifyPrimitive(num);      // num remains 5
modifyObject(person);      // person.name becomes "Modified"
```

---

## 📋 Shallow vs Deep Copy

### Shallow Copy Methods
```javascript
let original = {a: 1, b: {c: 2}};

// Spread operator
let copy1 = {...original};

// Object.assign()
let copy2 = Object.assign({}, original);

// Array shallow copy
let arr = [1, 2, [3, 4]];
let arrCopy1 = [...arr];
let arrCopy2 = arr.slice();

// Note: Nested objects/arrays are still referenced
copy1.b.c = 99;            // Changes original.b.c too!
```

### Deep Copy Methods
```javascript
let original = {a: 1, b: {c: 2}, d: [3, 4]};

// JSON method (limitations: no functions, dates become strings)
let deepCopy = JSON.parse(JSON.stringify(original));

// Manual recursive function
function deepClone(obj) {
    if (obj === null || typeof obj !== "object") return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof Array) return obj.map(item => deepClone(item));
    
    let cloned = {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            cloned[key] = deepClone(obj[key]);
        }
    }
    return cloned;
}
```

---

## 📋 JSON Methods

### JSON.stringify()
```javascript
let obj = {name: "John", age: 30, active: true};

// Basic stringify
let jsonString = JSON.stringify(obj);
// '{"name":"John","age":30,"active":true}'

// With replacer function
let jsonString2 = JSON.stringify(obj, ["name", "age"]);  // Only include specified keys

// With space parameter (formatting)
let formatted = JSON.stringify(obj, null, 2);  // Pretty print with 2 spaces
```

### JSON.parse()
```javascript
let jsonString = '{"name":"John","age":30}';

// Basic parse
let obj = JSON.parse(jsonString);

// With error handling
try {
    let obj = JSON.parse(jsonString);
    console.log(obj);
} catch (error) {
    console.log("Invalid JSON:", error.message);
}

// With reviver function
let obj2 = JSON.parse(jsonString, (key, value) => {
    if (key === "age") return value + 1;  // Increment age by 1
    return value;
});
```

---

## 🔄 JS Loops

### For Loop
```javascript
// Basic for loop
for (let i = 0; i < 5; i++) {
    console.log(i);  // 0, 1, 2, 3, 4
}

// Loop through array
let arr = ["a", "b", "c"];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

// For...of loop (values)
for (let value of arr) {
    console.log(value);  // "a", "b", "c"
}

// For...in loop (keys/indices)
for (let index in arr) {
    console.log(index, arr[index]);  // 0 "a", 1 "b", 2 "c"
}
```

### While Loop
```javascript
// Basic while loop
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// While with condition
let numbers = [1, 2, 3, 4, 5];
let index = 0;
while (index < numbers.length) {
    console.log(numbers[index]);
    index++;
}
```

### Do-While Loop
```javascript
// Executes at least once
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);

// Useful for user input validation
let userInput;
do {
    userInput = prompt("Enter a number greater than 10:");
} while (userInput <= 10);
```

### Loop Control
```javascript
for (let i = 0; i < 10; i++) {
    if (i === 3) continue;    // Skip iteration when i is 3
    if (i === 7) break;       // Exit loop when i is 7
    console.log(i);           // Prints: 0, 1, 2, 4, 5, 6
}
```

---

## 💡 Quick Reference Patterns

### Common Array Operations
```javascript
let arr = [1, 2, 3, 4, 5];

// Check if array
Array.isArray(arr);                    // true

// Find element
arr.find(x => x > 3);                  // 4
arr.findIndex(x => x > 3);             // 3

// Transform array
arr.map(x => x * 2);                   // [2, 4, 6, 8, 10]
arr.filter(x => x % 2 === 0);          // [2, 4]
arr.reduce((sum, x) => sum + x, 0);    // 15
```

### Object Iteration
```javascript
let obj = {a: 1, b: 2, c: 3};

// Iterate over keys
for (let key in obj) {
    console.log(key, obj[key]);
}

// Iterate over entries
for (let [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
```