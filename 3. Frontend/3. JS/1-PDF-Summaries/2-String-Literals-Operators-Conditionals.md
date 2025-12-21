# 📝 String Literals, Operators & Conditionals

## 🎯 Strings & Template Literals

### String Declaration
- **Single quotes**: `'Hello'`
- **Double quotes**: `"World"`
- **Backticks**: `` `Template Literal` ``

### String Properties & Methods
- `length` → Number of characters
- `toUpperCase()` / `toLowerCase()` → Change case
- `slice(start, end)` → Extract part of string
- `includes()` → Check if substring exists
- `trim()` → Remove whitespace

### String Concatenation
```javascript
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName; // "John Doe"
```

### Template Literals
```javascript
let name = "Alice";
let age = 25;
console.log(`Hello, my name is ${name} and I am ${age} years old.`);
// Multi-line strings
let msg = `Line 1
Line 2
Line 3`;
```

## 🔧 Operators

### 1. Arithmetic Operators
- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division
- `%` → Remainder (modulo)

### 2. Assignment Operators
- `=` → Assign
- `+=` → Add and assign
- `-=` → Subtract and assign
- `*=` → Multiply and assign
- `/=` → Divide and assign

### 3. Comparison Operators
- `==` → Equal value (loose)
- `===` → Equal value and type (strict)
- `!=` → Not equal (loose)
- `!==` → Not equal value or type (strict)
- `>`, `<`, `>=`, `<=` → Comparison

### 4. Logical Operators
- `&&` → AND (both conditions true)
- `||` → OR (at least one condition true)
- `!` → NOT (opposite of condition)

### 5. Unary Operators
- `++` → Increment
- `--` → Decrement
- `typeof` → Get data type

### 6. Ternary Operator
```javascript
let result = (condition) ? "if true" : "if false";
let grade = (marks >= 50) ? "Pass" : "Fail";
```

## 🎯 Conditional Statements

### 1. if Statement
```javascript
if (age >= 18) {
  console.log("You can vote");
}
```

### 2. if-else Statement
```javascript
if (num % 2 === 0) {
  console.log("Even");
} else {
  console.log("Odd");
}
```

### 3. if-else if Ladder
```javascript
if (marks >= 90) {
  console.log("Grade A+");
} else if (marks >= 75) {
  console.log("Grade A");
} else if (marks >= 50) {
  console.log("Grade B");
} else {
  console.log("Grade C");
}
```

### 4. Switch Statement
```javascript
switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  default:
    console.log("Weekend");
}
```

### 5. Short-circuiting
```javascript
// && executes right side only if left is true
// something llike to check a condition
isLoggedIn && console.log("Welcome!"); 


// || executes right side only if left is false
// something like to write a default msg 
let displayName = userName || "Guest";
```