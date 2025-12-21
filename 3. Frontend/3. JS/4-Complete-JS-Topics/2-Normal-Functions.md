# 🔧 Normal Functions

## 📖 Definition
Normal functions are traditional JavaScript functions declared using the `function` keyword. They have their own execution context, can be hoisted, and have access to the `arguments` object.

## 🎯 Function Declaration

### Basic Syntax
```javascript
function functionName(parameters) {
    // Function body
    return value; // Optional
}

// Example
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("John")); // "Hello, John!"
```

### Function with Multiple Parameters
```javascript
function add(a, b) {
    return a + b;
}

function calculateArea(length, width) {
    return length * width;
}

function displayInfo(name, age, city) {
    console.log(`Name: ${name}, Age: ${age}, City: ${city}`);
}
```

## 🔄 Function Expression

### Anonymous Function Expression
```javascript
const greet = function(name) {
    return `Hello, ${name}!`;
};

// Must be called after declaration
console.log(greet("Jane")); // "Hello, Jane!"
```

### Named Function Expression
```javascript
const factorial = function fact(n) {
    if (n <= 1) return 1;
    return n * fact(n - 1); // Can reference itself by name
};

console.log(factorial(5)); // 120
```

## 🎯 Function Parameters

### Default Parameters (ES6)
```javascript
function greet(name = "World", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

console.log(greet());              // "Hello, World!"
console.log(greet("John"));        // "Hello, John!"
console.log(greet("Jane", "Hi"));  // "Hi, Jane!"
```

### Rest Parameters
```javascript
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3));         // 6
console.log(sum(1, 2, 3, 4, 5));   // 15

function introduce(name, ...hobbies) {
    console.log(`Hi, I'm ${name}`);
    console.log(`My hobbies are: ${hobbies.join(", ")}`);
}

introduce("John", "reading", "coding", "gaming");
```

### Arguments Object (Legacy)
```javascript
function oldSum() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}

console.log(oldSum(1, 2, 3, 4)); // 10

// Arguments is array-like but not a real array
function showArguments() {
    console.log(typeof arguments);        // "object"
    console.log(Array.isArray(arguments)); // false
    console.log(arguments.length);        // Number of arguments
}
```

## 🔍 Function Hoisting

### Declaration Hoisting
```javascript
// This works due to hoisting
console.log(sayHello("John")); // "Hello, John!"

function sayHello(name) {
    return `Hello, ${name}!`;
}

// Function declarations are fully hoisted
```

### Expression Hoisting
```javascript
// This doesn't work
console.log(sayGoodbye("John")); // TypeError: sayGoodbye is not a function

var sayGoodbye = function(name) {
    return `Goodbye, ${name}!`;
};

// Only variable declaration is hoisted, not the function assignment
```

## 🎯 Return Values

### Explicit Return
```javascript
function multiply(a, b) {
    return a * b; // Explicit return
}

function getUser() {
    return {
        name: "John",
        age: 30,
        email: "john@example.com"
    };
}
```

### Implicit Return (undefined)
```javascript
function logMessage(message) {
    console.log(message);
    // No return statement = returns undefined
}

let result = logMessage("Hello"); // result is undefined
```

### Early Return
```javascript
function divide(a, b) {
    if (b === 0) {
        return "Cannot divide by zero";
    }
    return a / b;
}

function processUser(user) {
    if (!user) return "No user provided";
    if (!user.name) return "User name required";
    if (!user.email) return "User email required";
    
    // Process valid user
    return `Processing user: ${user.name}`;
}
```

## 🔧 Function Scope and Context

### Local Scope
```javascript
function example() {
    let localVar = "I'm local";
    var functionScoped = "I'm function scoped";
    
    if (true) {
        let blockScoped = "I'm block scoped";
        var stillFunctionScoped = "Still function scoped";
    }
    
    console.log(localVar);              // Works
    console.log(functionScoped);        // Works
    console.log(stillFunctionScoped);   // Works
    // console.log(blockScoped);        // ReferenceError
}
```

### this Context
```javascript
function regularFunction() {
    console.log(this); // Depends on how function is called
}

const obj = {
    name: "John",
    greet: function() {
        console.log(`Hello, I'm ${this.name}`); // this refers to obj
    },
    
    nested: function() {
        function inner() {
            console.log(this); // this is global object (or undefined in strict mode)
        }
        inner();
    }
};

obj.greet(); // "Hello, I'm John"
```

## 🎯 Higher-Order Functions

### Functions as Parameters
```javascript
function processArray(arr, callback) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(callback(arr[i]));
    }
    return result;
}

function double(x) {
    return x * 2;
}

function square(x) {
    return x * x;
}

const numbers = [1, 2, 3, 4, 5];
console.log(processArray(numbers, double)); // [2, 4, 6, 8, 10]
console.log(processArray(numbers, square)); // [1, 4, 9, 16, 25]
```

### Functions Returning Functions
```javascript
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5));  // 10
console.log(triple(4));  // 12

// Practical example: Event handler factory
function createClickHandler(message) {
    return function(event) {
        console.log(`${message}: Button clicked!`);
        console.log("Event:", event.type);
    };
}
```

## 🔄 Closures

### Basic Closure
```javascript
function outerFunction(x) {
    // Outer function's variable
    
    function innerFunction(y) {
        // Inner function has access to outer function's variables
        return x + y;
    }
    
    return innerFunction;
}

const addFive = outerFunction(5);
console.log(addFive(3)); // 8 (5 + 3)
```

### Practical Closure Example
```javascript
function createCounter() {
    let count = 0;
    
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

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());  // 2
console.log(counter.decrement()); // 1
```

## 🎯 Function Methods

### call() Method
```javascript
function greet(greeting, punctuation) {
    return `${greeting}, ${this.name}${punctuation}`;
}

const person = { name: "John" };

// call() - invoke function with specific this context
const result = greet.call(person, "Hello", "!");
console.log(result); // "Hello, John!"
```

### apply() Method
```javascript
function introduce(greeting, ...hobbies) {
    console.log(`${greeting}, I'm ${this.name}`);
    console.log(`My hobbies: ${hobbies.join(", ")}`);
}

const person = { name: "Jane" };

// apply() - similar to call() but takes array of arguments
introduce.apply(person, ["Hi", "reading", "coding", "traveling"]);
```

### bind() Method
```javascript
function greet() {
    return `Hello, ${this.name}!`;
}

const person = { name: "Bob" };

// bind() - creates new function with bound this context
const boundGreet = greet.bind(person);
console.log(boundGreet()); // "Hello, Bob!"

// Partial application with bind
function multiply(a, b) {
    return a * b;
}

const double = multiply.bind(null, 2);
console.log(double(5)); // 10 (2 * 5)
```

## 🎯 Recursive Functions

### Basic Recursion
```javascript
function factorial(n) {
    // Base case
    if (n <= 1) {
        return 1;
    }
    // Recursive case
    return n * factorial(n - 1);
}

console.log(factorial(5)); // 120

function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(6)); // 8
```

### Tail Recursion (Optimized)
```javascript
function factorialTail(n, accumulator = 1) {
    if (n <= 1) {
        return accumulator;
    }
    return factorialTail(n - 1, n * accumulator);
}

console.log(factorialTail(5)); // 120
```

## 💡 Best Practices

### Function Naming
```javascript
// ✅ Good - Descriptive names
function calculateTotalPrice(items, taxRate) {
    return items.reduce((total, item) => total + item.price, 0) * (1 + taxRate);
}

function isValidEmail(email) {
    return email.includes("@") && email.includes(".");
}

// ❌ Avoid - Unclear names
function calc(x, y) {
    return x + y;
}

function check(str) {
    return str.length > 0;
}
```

### Single Responsibility
```javascript
// ✅ Good - Each function has one responsibility
function validateUser(user) {
    return user && user.name && user.email;
}

function formatUserName(name) {
    return name.trim().toLowerCase();
}

function saveUser(user) {
    // Save user to database
}

// ❌ Avoid - Function doing too many things
function processUser(user) {
    // Validation
    if (!user || !user.name || !user.email) return false;
    
    // Formatting
    user.name = user.name.trim().toLowerCase();
    
    // Saving
    // Save to database...
    
    // Logging
    console.log("User processed");
}
```

### Pure Functions
```javascript
// ✅ Good - Pure function (no side effects)
function add(a, b) {
    return a + b;
}

function getFullName(firstName, lastName) {
    return `${firstName} ${lastName}`;
}

// ❌ Avoid - Impure function (side effects)
let counter = 0;
function incrementCounter() {
    counter++; // Modifies external state
    return counter;
}
```

## 🚨 Common Pitfalls

### Hoisting Confusion
```javascript
// This works but is confusing
console.log(hoistedFunction()); // "I'm hoisted!"

function hoistedFunction() {
    return "I'm hoisted!";
}

// This doesn't work
console.log(notHoisted()); // TypeError

var notHoisted = function() {
    return "I'm not hoisted!";
};
```

### this Context Loss
```javascript
const obj = {
    name: "John",
    greet: function() {
        return `Hello, ${this.name}!`;
    }
};

const greetFunc = obj.greet;
console.log(greetFunc()); // "Hello, undefined!" - lost context

// Solution: bind the context
const boundGreet = obj.greet.bind(obj);
console.log(boundGreet()); // "Hello, John!"
```

### Closure Memory Leaks
```javascript
// Potential memory leak
function createHandler() {
    const largeData = new Array(1000000).fill("data");
    
    return function() {
        // Even if we don't use largeData, it's kept in memory
        console.log("Handler called");
    };
}

// Better: Only close over what you need
function createHandler() {
    const largeData = new Array(1000000).fill("data");
    const neededValue = largeData[0];
    
    return function() {
        console.log("Handler called with:", neededValue);
        // largeData can be garbage collected
    };
}
```

---

*💡 Master normal functions to build a solid foundation for JavaScript programming!*