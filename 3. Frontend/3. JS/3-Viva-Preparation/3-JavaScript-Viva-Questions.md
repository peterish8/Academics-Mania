# 🎯 JavaScript Viva Questions & Answers - Frontend Development Basics

## 📊 Arrays & Array Methods

### Q1: What's the difference between `slice()` and `splice()`?
**Answer:** 
- `slice(start, end)`: Non-mutating, returns new array from start to end-1
- `splice(start, deleteCount, ...items)`: Mutating, removes/adds elements, returns removed elements
```javascript
let arr = [1, 2, 3, 4, 5];
arr.slice(1, 3);    // [2, 3] - original unchanged
arr.splice(1, 2);   // [2, 3] - original becomes [1, 4, 5]
```

### Q2: What will this code output?
```javascript
let arr = [1, 2, 3];
console.log(arr.push(4));
console.log(arr.pop());
console.log(arr);
```
**Answer:**
- `4` - push() returns new length
- `4` - pop() returns removed element
- `[1, 2, 3]` - final array state

### Q3: How do you remove the first element from an array?
**Answer:** Use `shift()` method
```javascript
let arr = [1, 2, 3];
let first = arr.shift();  // Returns 1, arr becomes [2, 3]
```

### Q4: What's the difference between `push()` and `concat()`?
**Answer:**
- `push()`: Mutates original array, adds elements to end, returns new length
- `concat()`: Returns new array, doesn't mutate original, merges arrays
```javascript
let arr1 = [1, 2];
arr1.push(3);              // arr1 becomes [1, 2, 3], returns 3
let arr2 = arr1.concat(4); // arr2 is [1, 2, 3, 4], arr1 unchanged
```

### Q5: How do you add elements to the beginning of an array?
**Answer:** Use `unshift()` method
```javascript
let arr = [2, 3];
arr.unshift(1);     // arr becomes [1, 2, 3], returns 3 (new length)
```

### Q6: What will this code output?
```javascript
let arr = [1, 2, 3, 4, 5];
let result = arr.splice(2, 1, 'a', 'b');
console.log(result);
console.log(arr);
```
**Answer:**
- `[3]` - splice returns array of removed elements
- `[1, 2, 'a', 'b', 4, 5]` - original array after modification

---

## 🔧 Normal Functions

### Q1: What is function hoisting? Give an example.
**Answer:** Function declarations are moved to the top of their scope during compilation.
```javascript
console.log(greet("John"));  // Works! Outputs: "Hello, John"

function greet(name) {
    return `Hello, ${name}`;
}
```

### Q2: What's the difference between function declaration and function expression?
**Answer:**
```javascript
// Function Declaration - Hoisted completely
function declared() { return "declared"; }

// Function Expression - Variable hoisted, function not
var expressed = function() { return "expressed"; };

console.log(declared());   // Works
console.log(expressed());  // TypeError if called before assignment
```

### Q3: What will this code output?
```javascript
function test() {
    console.log(arguments.length);
    console.log(arguments[0]);
}
test(1, 2, 3);
```
**Answer:**
- `3` - Number of arguments passed
- `1` - First argument value

### Q4: How do you create a function with default parameters?
**Answer:**
```javascript
function greet(name = "World", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}
greet();           // "Hello, World!"
greet("John");     // "Hello, John!"
```

### Q5: What is the `arguments` object?
**Answer:** Array-like object containing all arguments passed to a function
```javascript
function sum() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}
sum(1, 2, 3, 4);  // 10
```

### Q6: Can you call a function before declaring it? Why?
**Answer:** Yes, for function declarations due to hoisting. No, for function expressions.
```javascript
// This works
console.log(declared());  // "Hello"
function declared() { return "Hello"; }

// This doesn't work
console.log(expressed()); // TypeError
var expressed = function() { return "Hello"; };
```

---

## ➡️ Arrow Functions

### Q1: What's the main difference between arrow functions and regular functions?
**Answer:** Arrow functions don't have their own `this`, `arguments`, or `super` binding.
```javascript
let obj = {
    name: "John",
    regular: function() { return this.name; },    // "John"
    arrow: () => { return this.name; }            // undefined (global this)
};
```

### Q2: When should you NOT use arrow functions?
**Answer:**
- As object methods (loses `this` context)
- As constructor functions (cannot use `new`)
- When you need `arguments` object
```javascript
let obj = {
    name: "John",
    greet: () => `Hello ${this.name}`  // Wrong! this is not obj
};
```

### Q3: What will this code output?
```javascript
const multiply = (a, b) => a * b;
const square = x => x * x;
const greet = () => "Hello";

console.log(multiply(3, 4));
console.log(square(5));
console.log(greet());
```
**Answer:**
- `12` - 3 * 4
- `25` - 5 * 5
- `"Hello"` - function call

### Q4: How do you return an object from an arrow function?
**Answer:** Wrap the object in parentheses for implicit return
```javascript
const createUser = (name, age) => ({name, age});
// OR with explicit return
const createUser2 = (name, age) => {
    return {name, age};
};
```

### Q5: What's the difference in `this` binding?
**Answer:**
```javascript
function RegularFunction() {
    this.name = "Regular";
    
    this.regularMethod = function() {
        return this.name;  // "Regular"
    };
    
    this.arrowMethod = () => {
        return this.name;  // "Regular" (lexical this)
    };
}

let obj = new RegularFunction();
let regular = obj.regularMethod;
let arrow = obj.arrowMethod;

regular();  // undefined (lost context)
arrow();    // "Regular" (preserved context)
```

### Q6: Can arrow functions be hoisted?
**Answer:** No, arrow functions are always expressions and follow variable hoisting rules.
```javascript
console.log(arrow());  // ReferenceError or TypeError
const arrow = () => "Hello";
```

---

## 🔄 Rest & Spread Operator

### Q1: What's the difference between rest and spread operators?
**Answer:**
- **Rest**: Collects multiple elements into an array (function parameters, destructuring)
- **Spread**: Expands array/object elements (function calls, array/object literals)
```javascript
// Rest - collects
function sum(...numbers) { }  // Collects arguments into array

// Spread - expands
sum(...[1, 2, 3]);           // Expands array into arguments
```

### Q2: What will this code output?
```javascript
function test(a, b, ...rest) {
    console.log(a);
    console.log(b);
    console.log(rest);
}
test(1, 2, 3, 4, 5);
```
**Answer:**
- `1` - first parameter
- `2` - second parameter
- `[3, 4, 5]` - rest parameters as array

### Q3: How do you copy an array using spread operator?
**Answer:**
```javascript
let original = [1, 2, 3];
let copy = [...original];        // Shallow copy
let extended = [...original, 4, 5]; // Copy and add elements
```

### Q4: What will this code output?
```javascript
let arr1 = [1, 2];
let arr2 = [3, 4];
let combined = [...arr1, ...arr2];
console.log(combined);
```
**Answer:** `[1, 2, 3, 4]` - Arrays are combined using spread

### Q5: How do you use rest in destructuring?
**Answer:**
```javascript
let [first, second, ...rest] = [1, 2, 3, 4, 5];
// first = 1, second = 2, rest = [3, 4, 5]

let {name, ...otherProps} = {name: "John", age: 30, city: "NYC"};
// name = "John", otherProps = {age: 30, city: "NYC"}
```

### Q6: Can you use rest parameter in the middle of function parameters?
**Answer:** No, rest parameter must be the last parameter.
```javascript
// Wrong
function wrong(a, ...rest, b) { }  // SyntaxError

// Correct
function correct(a, b, ...rest) { }
```

---

## 🏗️ JS Objects

### Q1: What are the different ways to create objects in JavaScript?
**Answer:**
```javascript
// Object literal
let obj1 = {name: "John", age: 30};

// Constructor function
function Person(name) { this.name = name; }
let obj2 = new Person("John");

// Object.create()
let obj3 = Object.create({name: "John"});

// Class (ES6)
class User { constructor(name) { this.name = name; } }
let obj4 = new User("John");
```

### Q2: What will this code output?
```javascript
let obj = {
    name: "John",
    greet: function() {
        return `Hello, ${this.name}`;
    }
};

let greetFunc = obj.greet;
console.log(obj.greet());
console.log(greetFunc());
```
**Answer:**
- `"Hello, John"` - Method called on object, `this` refers to obj
- `"Hello, undefined"` - Function called without context, `this` is global/undefined

### Q3: How do you add a property to an object dynamically?
**Answer:**
```javascript
let obj = {};
let propertyName = "dynamicProp";

// Bracket notation
obj[propertyName] = "value";

// Or directly
obj["anotherProp"] = "another value";

// Computed property names (ES6)
let obj2 = {
    [propertyName]: "value"
};
```

### Q4: What's the difference between dot notation and bracket notation?
**Answer:**
- **Dot notation**: For known property names, cleaner syntax
- **Bracket notation**: For dynamic properties, properties with spaces/special chars
```javascript
let obj = {"first name": "John", age: 30};

obj.age;              // Works - known property
obj["first name"];    // Required - space in property name

let prop = "age";
obj[prop];            // Dynamic access
```

### Q5: How do you check if a property exists in an object?
**Answer:**
```javascript
let obj = {name: "John", age: 30};

// hasOwnProperty (own properties only)
obj.hasOwnProperty("name");     // true

// in operator (own + inherited)
"name" in obj;                  // true

// undefined check
obj.name !== undefined;         // true

// Object.hasOwn() (modern)
Object.hasOwn(obj, "name");     // true
```

### Q6: What will this code output?
```javascript
let obj = {a: 1};
obj.b = obj;
console.log(obj.b.a);
console.log(obj.b.b.a);
```
**Answer:**
- `1` - obj.b refers to obj, so obj.b.a is obj.a
- `1` - obj.b.b refers to obj again, so obj.b.b.a is obj.a

---

## 🏭 Factory Functions

### Q1: What is a factory function and how is it different from a constructor?
**Answer:** Factory function returns objects without using `new` keyword.
```javascript
// Factory function
function createPerson(name, age) {
    return {
        name: name,
        age: age,
        greet() { return `Hello, I'm ${this.name}`; }
    };
}

// Constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}

let person1 = createPerson("John", 30);    // No 'new'
let person2 = new Person("Jane", 25);      // Requires 'new'
```

### Q2: How do you create private variables in factory functions?
**Answer:** Use closures to create private variables.
```javascript
function createCounter() {
    let count = 0;  // Private variable
    
    return {
        increment() { return ++count; },
        decrement() { return --count; },
        getCount() { return count; }
        // count is not directly accessible
    };
}

let counter = createCounter();
counter.increment();  // 1
// counter.count is undefined (private)
```

### Q3: What will this code output?
```javascript
function createUser(name) {
    return {
        name: name,
        getName: function() {
            return this.name;
        }
    };
}

let user1 = createUser("John");
let user2 = createUser("Jane");
console.log(user1.getName());
console.log(user2.getName());
console.log(user1.getName === user2.getName);
```
**Answer:**
- `"John"` - user1's name
- `"Jane"` - user2's name  
- `false` - Each object has its own method instance

### Q4: What are the advantages of factory functions?
**Answer:**
- No need for `new` keyword
- Can return different object types
- Easy to create private variables with closures
- More flexible than constructor functions
- Can use arrow functions

### Q5: How do you optimize factory functions for memory?
**Answer:** Share methods through prototypes or external functions.
```javascript
// Shared methods object
const personMethods = {
    greet() { return `Hello, I'm ${this.name}`; }
};

function createPerson(name, age) {
    let person = Object.create(personMethods);
    person.name = name;
    person.age = age;
    return person;
}
```

### Q6: What will this factory function return?
```javascript
function createCalculator() {
    let result = 0;
    
    return {
        add(x) { result += x; return this; },
        multiply(x) { result *= x; return this; },
        getResult() { return result; }
    };
}

let calc = createCalculator();
console.log(calc.add(5).multiply(2).getResult());
```
**Answer:** `10` - Method chaining: 0 + 5 = 5, then 5 * 2 = 10

---

## 🏗️ Constructor Functions

### Q1: What happens when you call a constructor function without `new`?
**Answer:** `this` refers to global object, properties are set on global object.
```javascript
function Person(name) {
    this.name = name;
}

let person1 = new Person("John");    // Correct - creates new object
let person2 = Person("Jane");        // Wrong - this refers to global
console.log(window.name);            // "Jane" (in browser)
```

### Q2: How do you add methods to constructor functions efficiently?
**Answer:** Add methods to the prototype to share them among all instances.
```javascript
function Person(name) {
    this.name = name;
}

// Efficient - shared method
Person.prototype.greet = function() {
    return `Hello, I'm ${this.name}`;
};

// Inefficient - each instance gets own copy
function Person2(name) {
    this.name = name;
    this.greet = function() {
        return `Hello, I'm ${this.name}`;
    };
}
```

### Q3: What will this code output?
```javascript
function Car(make, model) {
    this.make = make;
    this.model = model;
}

Car.prototype.getInfo = function() {
    return `${this.make} ${this.model}`;
};

let car1 = new Car("Toyota", "Camry");
let car2 = new Car("Honda", "Civic");

console.log(car1.getInfo());
console.log(car1.getInfo === car2.getInfo);
```
**Answer:**
- `"Toyota Camry"` - car1's info
- `true` - Both instances share the same prototype method

### Q4: How do you check if an object was created by a specific constructor?
**Answer:** Use `instanceof` operator or check `constructor` property.
```javascript
function Person(name) { this.name = name; }
let john = new Person("John");

console.log(john instanceof Person);        // true
console.log(john.constructor === Person);   // true
```

### Q5: What is the difference between `__proto__` and `prototype`?
**Answer:**
- `prototype`: Property of constructor functions, defines what instances will inherit
- `__proto__`: Property of objects, points to the prototype they inherit from
```javascript
function Person() {}
let john = new Person();

Person.prototype.greet = function() { return "Hello"; };
console.log(john.__proto__ === Person.prototype);  // true
```

### Q6: What will this code output?
```javascript
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    return `${this.name} makes a sound`;
};

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

let dog = new Dog("Buddy", "Golden Retriever");
console.log(dog.speak());
console.log(dog instanceof Dog);
console.log(dog instanceof Animal);
```
**Answer:**
- `"Buddy makes a sound"` - Inherited method from Animal
- `true` - dog is instance of Dog
- `true` - dog is also instance of Animal (inheritance)

---

## 🔧 Object & Object Methods

### Q1: What's the difference between `Object.keys()`, `Object.values()`, and `Object.entries()`?
**Answer:**
```javascript
let obj = {a: 1, b: 2, c: 3};

Object.keys(obj);     // ["a", "b", "c"] - property names
Object.values(obj);   // [1, 2, 3] - property values  
Object.entries(obj);  // [["a", 1], ["b", 2], ["c", 3]] - key-value pairs
```

### Q2: What will this code output?
```javascript
let obj = {a: 1, b: 2};
let copy = Object.assign({c: 3}, obj);
obj.a = 10;
console.log(copy);
```
**Answer:** `{c: 3, a: 1, b: 2}` - Object.assign creates shallow copy, original change doesn't affect copy

### Q3: What's the difference between `hasOwnProperty()` and `in` operator?
**Answer:**
- `hasOwnProperty()`: Checks only object's own properties
- `in`: Checks both own and inherited properties
```javascript
let obj = {a: 1};
console.log(obj.hasOwnProperty('toString'));  // false
console.log('toString' in obj);               // true (inherited)
```

### Q4: How do you make an object immutable?
**Answer:**
```javascript
let obj = {a: 1, b: 2};

// Prevent adding/removing properties
Object.seal(obj);

// Prevent all modifications
Object.freeze(obj);

// Check if frozen/sealed
Object.isFrozen(obj);   // true
Object.isSealed(obj);   // true
```

### Q5: What will this code output?
```javascript
let obj1 = {a: 1, b: {c: 2}};
let obj2 = Object.assign({}, obj1);
obj1.b.c = 10;
console.log(obj2.b.c);
```
**Answer:** `10` - Object.assign does shallow copy, nested objects are still referenced

### Q6: How do you iterate over object properties?
**Answer:**
```javascript
let obj = {a: 1, b: 2, c: 3};

// for...in loop
for (let key in obj) {
    console.log(key, obj[key]);
}

// Object.keys() with forEach
Object.keys(obj).forEach(key => {
    console.log(key, obj[key]);
});

// Object.entries() with for...of
for (let [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
```

---

## 📊 Value vs Reference

### Q1: Explain the difference between pass by value and pass by reference.
**Answer:**
- **Primitives** (number, string, boolean, null, undefined): Passed by value (copied)
- **Objects** (arrays, objects, functions): Passed by reference (memory address)
```javascript
let a = 5;
let b = a;      // b gets copy of value
a = 10;         // a changes, b remains 5

let obj1 = {x: 1};
let obj2 = obj1;  // obj2 gets reference to same object
obj1.x = 2;       // Both obj1.x and obj2.x are now 2
```

### Q2: What will this code output?
```javascript
function modifyValues(num, obj) {
    num = 100;
    obj.value = 100;
}

let number = 5;
let object = {value: 5};

modifyValues(number, object);
console.log(number);
console.log(object.value);
```
**Answer:**
- `5` - Primitive value unchanged (passed by value)
- `100` - Object property changed (passed by reference)

### Q3: How do you avoid reference issues when working with objects?
**Answer:** Create copies of objects before modifying them.
```javascript
let original = {a: 1, b: 2};

// Shallow copy
let copy1 = {...original};
let copy2 = Object.assign({}, original);

// Deep copy (for nested objects)
let copy3 = JSON.parse(JSON.stringify(original));
```

### Q4: What will this code output?
```javascript
let arr1 = [1, 2, 3];
let arr2 = arr1;
let arr3 = [...arr1];

arr1.push(4);
console.log(arr2);
console.log(arr3);
```
**Answer:**
- `[1, 2, 3, 4]` - arr2 references same array as arr1
- `[1, 2, 3]` - arr3 is a copy, unaffected by changes to arr1

### Q5: Why does this comparison return false?
```javascript
console.log([1, 2, 3] === [1, 2, 3]);  // false
console.log({a: 1} === {a: 1});        // false
```
**Answer:** Objects are compared by reference, not by value. Each object literal creates a new object in memory.

### Q6: What will this code output?
```javascript
function updateArray(arr) {
    arr = [1, 2, 3];  // Reassignment
    return arr;
}

let myArray = [4, 5, 6];
let result = updateArray(myArray);
console.log(myArray);
console.log(result);
```
**Answer:**
- `[4, 5, 6]` - Original array unchanged (reassignment doesn't affect original reference)
- `[1, 2, 3]` - New array returned by function

---

## 📋 Shallow vs Deep Copy

### Q1: What's the difference between shallow copy and deep copy?
**Answer:**
- **Shallow copy**: Copies first level properties only, nested objects are still referenced
- **Deep copy**: Copies all levels, creates completely independent copy
```javascript
let original = {a: 1, b: {c: 2}};

// Shallow copy
let shallow = {...original};
shallow.b.c = 10;  // Changes original.b.c too!

// Deep copy
let deep = JSON.parse(JSON.stringify(original));
deep.b.c = 20;     // Doesn't affect original
```

### Q2: What are the limitations of using JSON methods for deep copying?
**Answer:**
- Functions are omitted
- `undefined` values are omitted
- `Date` objects become strings
- `NaN` and `Infinity` become `null`
- Circular references cause errors
```javascript
let obj = {
    func: function() {},     // Lost
    date: new Date(),        // Becomes string
    undef: undefined,        // Lost
    nan: NaN                 // Becomes null
};
```

### Q3: What will this code output?
```javascript
let original = {
    name: "John",
    address: {
        city: "NYC",
        country: "USA"
    }
};

let copy = {...original};
copy.address.city = "LA";

console.log(original.address.city);
console.log(copy.address.city);
```
**Answer:**
- `"LA"` - Shallow copy shares nested object reference
- `"LA"` - Same nested object modified

### Q4: How do you create a proper deep copy function?
**Answer:**
```javascript
function deepCopy(obj) {
    if (obj === null || typeof obj !== "object") return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof Array) return obj.map(item => deepCopy(item));
    
    let copied = {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            copied[key] = deepCopy(obj[key]);
        }
    }
    return copied;
}
```

### Q5: What will this code output?
```javascript
let arr1 = [[1, 2], [3, 4]];
let arr2 = [...arr1];
arr1[0][0] = 99;

console.log(arr2[0][0]);
```
**Answer:** `99` - Spread operator creates shallow copy, nested arrays are still referenced

### Q6: Which method creates a deep copy?
```javascript
let obj = {a: 1, b: {c: 2}};

// Option A
let copy1 = {...obj};

// Option B  
let copy2 = Object.assign({}, obj);

// Option C
let copy3 = JSON.parse(JSON.stringify(obj));
```
**Answer:** Option C - JSON methods create deep copy (with limitations)

---

## 📋 JSON Methods

### Q1: What will `JSON.stringify()` do with these values?
```javascript
let obj = {
    func: function() { return "hello"; },
    undef: undefined,
    num: 42,
    str: "hello",
    date: new Date(),
    nan: NaN,
    inf: Infinity
};
console.log(JSON.stringify(obj));
```
**Answer:** `{"num":42,"str":"hello","date":"2023-...","nan":null,"inf":null}`
- Functions and undefined are omitted
- Dates become ISO strings
- NaN and Infinity become null

### Q2: How do you handle JSON parsing errors?
**Answer:**
```javascript
function safeJsonParse(jsonString) {
    try {
        return JSON.parse(jsonString);
    } catch (error) {
        console.error("Invalid JSON:", error.message);
        return null;
    }
}

// Usage
let result = safeJsonParse('{"name": "John"}');  // Works
let invalid = safeJsonParse('{name: "John"}');   // Returns null
```

### Q3: What will this code output?
```javascript
let obj = {a: 1, b: 2, c: 3};
let jsonString = JSON.stringify(obj, ['a', 'c']);
console.log(jsonString);
```
**Answer:** `{"a":1,"c":3}` - Second parameter acts as filter, only includes specified keys

### Q4: How do you pretty-print JSON?
**Answer:**
```javascript
let obj = {name: "John", age: 30, city: "NYC"};

// Pretty print with 2 spaces
let formatted = JSON.stringify(obj, null, 2);
/*
{
  "name": "John",
  "age": 30,
  "city": "NYC"
}
*/
```

### Q5: What will this code output?
```javascript
let circular = {name: "John"};
circular.self = circular;

try {
    JSON.stringify(circular);
} catch (error) {
    console.log(error.message);
}
```
**Answer:** `"Converting circular structure to JSON"` - JSON.stringify can't handle circular references

### Q6: How do you use replacer and reviver functions?
**Answer:**
```javascript
let obj = {name: "John", age: 30, password: "secret"};

// Replacer function - exclude password
let json = JSON.stringify(obj, (key, value) => {
    return key === "password" ? undefined : value;
});

// Reviver function - increment age
let parsed = JSON.parse(json, (key, value) => {
    return key === "age" ? value + 1 : value;
});
```

---

## 🔄 JS Loops

### Q1: What's the difference between `for`, `while`, and `do-while` loops?
**Answer:**
- `for`: Counter-based, known number of iterations
- `while`: Condition-based, may not execute at all
- `do-while`: Executes at least once, then checks condition
```javascript
for (let i = 0; i < 3; i++) { }      // Executes 3 times
while (false) { }                     // Never executes
do { } while (false);                 // Executes once
```

### Q2: What will this code output?
```javascript
for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
```
**Answer:** `0 1 2` - `let` creates block scope, each iteration has its own `i`

### Q3: What's the difference between `for...in` and `for...of`?
**Answer:**
- `for...in`: Iterates over enumerable property names (keys/indices)
- `for...of`: Iterates over iterable values
```javascript
let arr = ['a', 'b', 'c'];

for (let index in arr) {
    console.log(index);     // "0", "1", "2" (indices)
}

for (let value of arr) {
    console.log(value);     // "a", "b", "c" (values)
}
```

### Q4: What will this code output?
```javascript
let i = 0;
while (i < 3) {
    console.log(i);
    i++;
}
console.log("Final i:", i);
```
**Answer:**
- `0`
- `1` 
- `2`
- `"Final i: 3"`

### Q5: How do `break` and `continue` work in loops?
**Answer:**
- `break`: Exits the loop completely
- `continue`: Skips current iteration, continues with next
```javascript
for (let i = 0; i < 5; i++) {
    if (i === 2) continue;    // Skip when i is 2
    if (i === 4) break;       // Exit when i is 4
    console.log(i);           // Prints: 0, 1, 3
}
```

### Q6: What will this code output?
```javascript
let count = 0;
do {
    console.log("Count:", count);
    count++;
} while (count < 0);
```
**Answer:** `"Count: 0"` - do-while executes at least once even though condition is false

---

## 🎯 Bonus Tricky Questions

### Q1: What will this code output?
```javascript
let obj = {
    a: 1,
    b: function() { return this.a; },
    c: () => { return this.a; }
};

console.log(obj.b());
console.log(obj.c());
```
**Answer:**
- `1` - Regular function, `this` refers to obj
- `undefined` - Arrow function, `this` is lexically bound (global)

### Q2: What will this code output?
```javascript
function test() {
    return {
        a: 1
    };
}

function test2() {
    return
    {
        a: 1
    };
}

console.log(test());
console.log(test2());
```
**Answer:**
- `{a: 1}` - Object returned correctly
- `undefined` - Automatic semicolon insertion after `return`

### Q3: What will this code output?
```javascript
let a = [1, 2, 3];
let b = [1, 2, 3];
let c = a;

console.log(a == b);
console.log(a === b);
console.log(a == c);
console.log(a === c);
```
**Answer:**
- `false` - Different array objects
- `false` - Different array objects  
- `true` - Same reference
- `true` - Same reference

---

## 📚 Quick Study Tips

### 🧠 Memory Aids
- **Array methods**: "Mutating methods change original, non-mutating return new"
- **Functions**: "Declarations hoist completely, expressions don't"
- **Objects**: "Dot for known properties, brackets for dynamic"
- **Copying**: "Spread is shallow, JSON is deep (with limits)"

### ⚡ Common Gotchas
1. `slice()` vs `splice()` - one mutates, one doesn't
2. Arrow functions lose `this` context
3. Object assignment creates references, not copies
4. `for...in` gives keys, `for...of` gives values
5. JSON methods have limitations with functions and dates

### 🎯 Interview Success Tips
1. **Understand the difference** between similar concepts
2. **Practice with examples** - write and run code
3. **Know the limitations** of each method/approach
4. **Explain your reasoning** step by step
5. **Consider edge cases** in your answers

---

*💡 Master these fundamentals and you'll be well-prepared for any JavaScript frontend interview!*