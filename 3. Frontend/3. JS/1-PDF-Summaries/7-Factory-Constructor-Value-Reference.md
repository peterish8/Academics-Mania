# 🏭 Factory Functions, Constructors & Memory

## 🏭 Factory Functions
Normal functions that return objects.
```javascript
function createPerson(name, age) {
  return {
    name: name,
    age: age,
    greet() { console.log(`Hello, I'm ${this.name}`); }
  };
}

const person1 = createPerson("Alice", 25);
```
**Pros**: Simple, flexible  
**Cons**: Each object has own copy of methods

## 🏗️ Constructor Functions
Used with `new` keyword, conventionally capitalized.
```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function() {
  console.log(`Hi, I'm ${this.name}`);
};

const p1 = new Person("Alice", 25);
```

### new Keyword Process
1. Creates new empty object
2. Sets prototype to constructor's prototype
3. Binds `this` to new object
4. Returns object automatically

## 📊 Value vs Reference

### Primitives (By Value)
```javascript
let a = 10;
let b = a;    // b gets copy of value
b = 20;
console.log(a); // 10 (unchanged)
```

### Objects (By Reference)
```javascript
let obj1 = {name: "Alice"};
let obj2 = obj1;  // obj2 gets reference
obj2.name = "Bob";
console.log(obj1.name); // "Bob" (changed!)
```

## 📋 Shallow vs Deep Copy

### Shallow Copy
Copies first level only, nested objects shared.
```javascript
let obj = {name: "Alice", address: {city: "Paris"}};
let shallow = {...obj};
shallow.address.city = "London";
console.log(obj.address.city); // "London" (affected!)
```

### Deep Copy
```javascript
// Using structuredClone (modern)
let deep1 = structuredClone(obj);

// Using JSON (limited)
let deep2 = JSON.parse(JSON.stringify(obj));

// Custom recursive function
function deepClone(obj) {
  if (obj === null || typeof obj !== "object") return obj;
  let copy = Array.isArray(obj) ? [] : {};
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      copy[key] = deepClone(obj[key]);
    }
  }
  return copy;
}
```

## 📄 JSON Methods

### JSON.stringify()
Object → JSON string
```javascript
const user = {name: "Alice", age: 25};
const jsonString = JSON.stringify(user);
// '{"name":"Alice","age":25}'
```

### JSON.parse()
JSON string → Object
```javascript
const jsonData = '{"name":"Bob","age":30}';
const obj = JSON.parse(jsonData);
// {name: "Bob", age: 30}
```

### Common Use Cases
- **API communication** → Send/receive data
- **localStorage** → Store objects as strings

## 🔄 Callback Functions
Functions passed as arguments to other functions.
```javascript
function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

function sayBye() {
  console.log("Goodbye!");
}

greet("Alice", sayBye);
// Output: "Hello Alice", "Goodbye!"
```