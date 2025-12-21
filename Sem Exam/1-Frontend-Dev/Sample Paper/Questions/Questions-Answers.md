# Important Questions & Answers

## 1. What is var, let and const? What is the difference between them?

In JavaScript, `var`, `let`, and `const` are used to declare variables but they behave differently.

### **var:**
*   **Scope:** Function-scoped, meaning it works inside the entire function.
*   **Reassignment:** It can be redeclared and reassigned, so its value can change any time.
*   **Hoisting:** It gets hoisted, so it is created before the code runs.

### **let:**
*   **Scope:** Block-scoped, which means it only works inside the block `{ }`.
*   **Reassignment:** It cannot be redeclared but can be reassigned.
*   **Safety:** This makes it safer to use in modern JS.

### **const:**
*   **Scope:** Block-scoped but its value **cannot be changed** after assigning.
*   **Reassignment:** We cannot redeclare or reassign a `const` variable.
*   **Note:** However, if `const` is an array or object, the internal values can still change.

### **Example:**
```javascript
var a = 10; 
let b = 20; 
const c = 30;
```
These three help control variable usage properly.

### **Comparison Table:**

| Feature | var | let | const |
| :--- | :--- | :--- | :--- |
| **Scope** | Function | Block | Block |
| **Hoisting** | Hoisted & Initialized | Hoisted but not initialized | Hoisted but not initialized |
| **Redeclaration** | Yes | No | No |
| **Reassignment** | Yes | Yes | No |

---

## 2. What are conditional statements in JS? Explain with example.

Conditional statements help JavaScript make decisions. 
They let the program run different code based on whether a condition is true or false.

**The main conditional statements are:**
*   `if`
*   `else`
*   `else if`
*   `switch`

*   The **`if`** statement checks a condition. If it is true, that block runs.
*   If not, the **`else`** part runs.
*   **`else if`** is used when there are multiple conditions.
*   **`switch`** is used when we want to compare one value with many cases.

### **Example:**
```javascript
let marks = 70;
if (marks >= 50) {
    console.log("Pass");
} else {
    console.log("Fail");
}
```
This shows how conditions decide the output. 
Conditional statements are important for controlling the flow of a program.

---

## 3. What are loops in JS? Explain with an example.

Loops are used in JavaScript to repeat a block of code multiple times without writing it again and again. 
They are useful when we want to do the same task many times, like printing numbers or going through an array.

**The main types of loops are:**
*   `for`
*   `while`
*   `do-while`
*   `for-of`
*   `for-in`

*   The **`for`** loop runs for a fixed number of times. 
*   The **`while`** loop runs as long as the condition is true. 
*   The **`do-while`** loop will run the code at least once before checking the condition.

### **Example:**
```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```
This displays numbers 1 to 5. 
Loops make programs shorter, easier to write, and more efficient.

---

## 4. What is a datatype? Explain types of datatypes.

A datatype tells JavaScript what kind of value a variable is storing.
It helps the program understand how the data should be used and what operations can be performed on it.

JavaScript datatypes are mainly divided into two categories:

### **Primitive Datatypes:**
*   **String:** Text values like `"hello"`
*   **Number:** Numeric values like `10`, `12.5`
*   **Boolean:** `true` or `false`
*   **Null:** Represents empty or no value
*   **Undefined:** Variable declared but no value assigned
*   **BigInt:** Very large numbers
*   **Symbol:** Unique values used for special purposes

### **Non-Primitive Datatype:**
*   **Object:** Collections of data (arrays, functions, objects)

### **Example:**
```javascript
let name = "John";      // String
let age = 20;           // Number
let isAdult = true;     // Boolean
let person = { name: "Ava", age: 22 }; // Object
```
Datatypes help JavaScript manage memory, perform operations correctly, and avoid errors in the program.

---

## 5. What are operators? Explain types of operators.

Operators are symbols used to perform operations on values and variables.
They help JavaScript perform calculations, comparisons, and logical decisions.

**Types of operators in JavaScript:**

### **Arithmetic Operators:**
*   `+` (Addition)
*   `-` (Subtraction)
*   `*` (Multiplication)
*   `/` (Division)
*   `%` (Modulus/Remainder)
*   `**` (Exponent)

### **Comparison Operators:**
*   `==` (Equal)
*   `===` (Strict equal)
*   `!=` (Not equal)
*   `>` (Greater than)
*   `<` (Less than)

### **Logical Operators:**
*   `&&` (Logical AND)
*   `||` (Logical OR)
*   `!` (Logical NOT)

### **Assignment Operators:**
*   `=` (Assigns value)
*   `+=` (Adds and assigns)
*   `-=` (Subtracts and assigns)

### **Unary Operators:**
*   `++` (Increment)
*   `--` (Decrement)

### **Example:**
```javascript
let a = 10;
let b = 5;

console.log(a + b);             // Arithmetic
console.log(a > b);             // Comparison
console.log(a == 10 && b == 5); // Logical
```
Operators help JavaScript perform calculations, compare values, and control the flow of code.
