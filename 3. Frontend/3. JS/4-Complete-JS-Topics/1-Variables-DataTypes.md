# 🔢 Variables & Data Types

## 📖 Definition
Variables are containers that store data values. JavaScript has dynamic typing, meaning variables can hold different data types without explicit declaration.

## 🎯 Variable Declaration

### Modern JavaScript (ES6+)
```javascript
let name = "John";          // Mutable variable
const age = 25;             // Immutable variable
var city = "NYC";           // Avoid using var (function-scoped)
```

### Variable Naming Rules
- Must start with letter, underscore (_), or dollar sign ($)
- Can contain letters, numbers, underscores, dollar signs
- Cannot use reserved keywords
- Case-sensitive

## 📊 Data Types

### Primitive Types
```javascript
// Number
let integer = 42;
let decimal = 3.14;
let negative = -10;
let infinity = Infinity;
let notANumber = NaN;

// String
let singleQuote = 'Hello';
let doubleQuote = "World";
let templateLiteral = `Hello ${name}`;

// Boolean
let isActive = true;
let isComplete = false;

// Undefined
let notAssigned;            // undefined
let explicitUndefined = undefined;

// Null
let emptyValue = null;

// Symbol (ES6)
let uniqueId = Symbol('id');

// BigInt (ES2020)
let bigNumber = 123456789012345678901234567890n;
```

### Non-Primitive Types
```javascript
// Object
let person = {name: "John", age: 30};

// Array
let numbers = [1, 2, 3, 4, 5];

// Function
let greet = function() { return "Hello"; };
```

## 🔍 Type Checking

### typeof Operator
```javascript
typeof 42;                  // "number"
typeof "hello";             // "string"
typeof true;                // "boolean"
typeof undefined;           // "undefined"
typeof null;                // "object" (JavaScript quirk!)
typeof {};                  // "object"
typeof [];                  // "object"
typeof function(){};        // "function"
typeof Symbol('id');        // "symbol"
typeof 123n;                // "bigint"
```

### Advanced Type Checking
```javascript
// Check for array
Array.isArray([1, 2, 3]);              // true
Array.isArray({});                      // false

// Check for null specifically
value === null;                         // true for null only

// Check for NaN
Number.isNaN(NaN);                      // true
isNaN("hello");                         // true (converts to NaN)
Number.isNaN("hello");                  // false (no conversion)
```

## 🔄 Type Conversion

### Implicit Conversion (Coercion)
```javascript
// String conversion
"5" + 3;                    // "53" (number to string)
"Hello" + true;             // "Hellotrue"

// Number conversion
"5" - 3;                    // 2 (string to number)
"5" * "2";                  // 10
true + 1;                   // 2 (boolean to number)

// Boolean conversion
if ("hello") {}             // true (non-empty string)
if (0) {}                   // false (zero is falsy)
```

### Explicit Conversion
```javascript
// To String
String(123);                // "123"
(123).toString();           // "123"
123 + "";                   // "123"

// To Number
Number("123");              // 123
parseInt("123px");          // 123
parseFloat("123.45px");     // 123.45
+"123";                     // 123 (unary plus)

// To Boolean
Boolean(1);                 // true
Boolean(0);                 // false
!!1;                        // true (double negation)
```

## 🎯 Variable Scope

### Block Scope (let, const)
```javascript
{
    let blockScoped = "I'm in a block";
    const alsoBlockScoped = "Me too";
}
// console.log(blockScoped); // ReferenceError
```

### Function Scope (var)
```javascript
function example() {
    var functionScoped = "I'm function scoped";
    if (true) {
        var stillFunctionScoped = "Me too";
    }
    console.log(stillFunctionScoped); // Works!
}
```

### Global Scope
```javascript
var globalVar = "I'm global";
let globalLet = "I'm also global";
const globalConst = "Me three";

// Without declaration (avoid!)
implicitGlobal = "I'm accidentally global";
```

## 💡 Best Practices

### Variable Declaration
```javascript
// ✅ Good
const PI = 3.14159;                     // Use const for constants
let userName = "john_doe";              // Use let for variables that change
let isLoggedIn = false;                 // Descriptive names

// ❌ Avoid
var x = 5;                              // Unclear name, old syntax
let 2names = "invalid";                 // Invalid syntax
```

### Naming Conventions
```javascript
// ✅ Good
const MAX_USERS = 100;                  // Constants in UPPER_CASE
let firstName = "John";                 // camelCase for variables
let isActive = true;                    // Boolean with is/has prefix
let getUserData = function() {};        // Functions with verbs

// ❌ Avoid
let first_name = "John";                // snake_case (not JS convention)
let FirstName = "John";                 // PascalCase (for constructors)
```

## 🔧 Common Patterns

### Default Values
```javascript
// Using OR operator
let name = userName || "Guest";

// Using nullish coalescing (ES2020)
let name2 = userName ?? "Guest";        // Only null/undefined

// Function parameters
function greet(name = "World") {
    return `Hello, ${name}!`;
}
```

### Type Guards
```javascript
function processValue(value) {
    if (typeof value === "string") {
        return value.toUpperCase();
    }
    if (typeof value === "number") {
        return value * 2;
    }
    if (Array.isArray(value)) {
        return value.length;
    }
    return "Unknown type";
}
```

## 🚨 Common Pitfalls

### Truthy/Falsy Values
```javascript
// Falsy values (6 total)
false, 0, -0, 0n, "", null, undefined, NaN

// Everything else is truthy
if ([]) {}                  // true (empty array is truthy!)
if ({}) {}                  // true (empty object is truthy!)
if ("0") {}                 // true (string "0" is truthy!)
```

### Variable Hoisting
```javascript
console.log(hoistedVar);    // undefined (not ReferenceError)
var hoistedVar = "I'm hoisted";

// console.log(notHoisted); // ReferenceError
let notHoisted = "I'm not hoisted";
```

### Temporal Dead Zone
```javascript
console.log(typeof myLet);  // ReferenceError (TDZ)
let myLet = "Hello";

console.log(typeof myVar);  // "undefined" (hoisted)
var myVar = "Hello";
```

## 🎯 Practice Examples

### Type Checking Function
```javascript
function getType(value) {
    if (value === null) return "null";
    if (Array.isArray(value)) return "array";
    if (value instanceof Date) return "date";
    return typeof value;
}

console.log(getType(null));         // "null"
console.log(getType([]));           // "array"
console.log(getType(new Date()));   // "date"
```

### Safe Type Conversion
```javascript
function toNumber(value) {
    if (typeof value === "number") return value;
    if (typeof value === "string") {
        const num = Number(value);
        return isNaN(num) ? 0 : num;
    }
    return 0;
}

console.log(toNumber("123"));       // 123
console.log(toNumber("abc"));       // 0
console.log(toNumber(true));        // 0
```

---

*💡 Understanding variables and data types is fundamental to mastering JavaScript!*