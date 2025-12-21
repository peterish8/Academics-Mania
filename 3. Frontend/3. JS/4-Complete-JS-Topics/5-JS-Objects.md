# 🏗️ JS Objects

## 📖 Definition
Objects are collections of key-value pairs that represent entities with properties and methods. They are fundamental data structures in JavaScript for organizing and manipulating data.

## 🎯 Object Creation

### Object Literal (Most Common)
```javascript
// Basic object literal
const person = {
    name: "John",
    age: 30,
    city: "New York"
};

// Object with methods
const calculator = {
    result: 0,
    add: function(x) {
        this.result += x;
        return this;
    },
    multiply: function(x) {
        this.result *= x;
        return this;
    },
    getValue: function() {
        return this.result;
    }
};

// ES6 method shorthand
const user = {
    name: "Jane",
    age: 25,
    
    // Method shorthand (no function keyword)
    greet() {
        return `Hello, I'm ${this.name}`;
    },
    
    getAge() {
        return this.age;
    }
};
```

### Empty Object
```javascript
// Create empty object
const emptyObj1 = {};
const emptyObj2 = new Object();

// Add properties later
emptyObj1.name = "John";
emptyObj1.age = 30;
```

### Computed Property Names (ES6)
```javascript
const propertyName = "dynamicKey";
const value = "dynamicValue";

const obj = {
    staticKey: "static value",
    [propertyName]: value,                    // Dynamic key
    [`${propertyName}_2`]: "another value",   // Computed key
    [Date.now()]: "timestamp key"            // Expression as key
};

console.log(obj);
// {
//   staticKey: "static value",
//   dynamicKey: "dynamicValue",
//   dynamicKey_2: "another value",
//   1234567890: "timestamp key"
// }
```

## 🔍 Property Access

### Dot Notation
```javascript
const person = {
    name: "John",
    age: 30,
    address: {
        street: "123 Main St",
        city: "New York"
    }
};

// Reading properties
console.log(person.name);           // "John"
console.log(person.address.city);   // "New York"

// Setting properties
person.age = 31;
person.email = "john@example.com";  // Add new property
```

### Bracket Notation
```javascript
const person = {
    "first name": "John",    // Property with space
    "last-name": "Doe",      // Property with hyphen
    age: 30
};

// Reading with bracket notation
console.log(person["first name"]);  // "John"
console.log(person["last-name"]);   // "Doe"

// Dynamic property access
const prop = "age";
console.log(person[prop]);          // 30

// Computed property access
const prefix = "first";
console.log(person[prefix + " name"]); // "John"
```

### Optional Chaining (ES2020)
```javascript
const user = {
    name: "John",
    address: {
        street: "123 Main St"
        // city property is missing
    }
};

// Without optional chaining (can throw error)
// console.log(user.address.city.toUpperCase()); // TypeError

// With optional chaining (safe)
console.log(user.address?.city?.toUpperCase()); // undefined
console.log(user.contact?.phone);               // undefined
console.log(user.getName?.());                  // undefined (method doesn't exist)
```

## 🔧 Object Properties

### Property Descriptors
```javascript
const obj = {};

// Define property with descriptor
Object.defineProperty(obj, "name", {
    value: "John",
    writable: true,      // Can be changed
    enumerable: true,    // Shows up in for...in loops
    configurable: true   // Can be deleted or reconfigured
});

// Define multiple properties
Object.defineProperties(obj, {
    age: {
        value: 30,
        writable: false    // Read-only property
    },
    email: {
        value: "john@example.com",
        enumerable: false  // Won't show in Object.keys()
    }
});

// Get property descriptor
const descriptor = Object.getOwnPropertyDescriptor(obj, "name");
console.log(descriptor);
// {value: "John", writable: true, enumerable: true, configurable: true}
```

### Getters and Setters
```javascript
const person = {
    firstName: "John",
    lastName: "Doe",
    
    // Getter - computed property
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },
    
    // Setter - validate and set
    set fullName(value) {
        const parts = value.split(" ");
        this.firstName = parts[0] || "";
        this.lastName = parts[1] || "";
    },
    
    get initials() {
        return `${this.firstName[0]}${this.lastName[0]}`;
    }
};

console.log(person.fullName);  // "John Doe" (getter called)
person.fullName = "Jane Smith"; // Setter called
console.log(person.firstName); // "Jane"
console.log(person.initials);  // "JS"
```

## 🔍 Object Methods

### Property Enumeration
```javascript
const obj = {a: 1, b: 2, c: 3};

// Get all enumerable property names
const keys = Object.keys(obj);
console.log(keys); // ["a", "b", "c"]

// Get all property values
const values = Object.values(obj);
console.log(values); // [1, 2, 3]

// Get key-value pairs
const entries = Object.entries(obj);
console.log(entries); // [["a", 1], ["b", 2], ["c", 3]]

// Convert entries back to object
const fromEntries = Object.fromEntries(entries);
console.log(fromEntries); // {a: 1, b: 2, c: 3}
```

### Property Checking
```javascript
const obj = {a: 1, b: 2};

// Check if property exists (own properties only)
console.log(obj.hasOwnProperty("a"));     // true
console.log(obj.hasOwnProperty("toString")); // false

// Modern alternative (ES2022)
console.log(Object.hasOwn(obj, "a"));     // true

// Check if property exists (including inherited)
console.log("a" in obj);                  // true
console.log("toString" in obj);           // true (inherited from Object.prototype)

// Check if property is enumerable
console.log(obj.propertyIsEnumerable("a")); // true
```

### Object Copying and Merging
```javascript
const obj1 = {a: 1, b: 2};
const obj2 = {c: 3, d: 4};
const obj3 = {b: 20, e: 5}; // Note: 'b' will override

// Object.assign() - shallow copy/merge
const merged = Object.assign({}, obj1, obj2, obj3);
console.log(merged); // {a: 1, b: 20, c: 3, d: 4, e: 5}

// Spread operator (ES6) - more common
const spreadMerged = {...obj1, ...obj2, ...obj3};
console.log(spreadMerged); // {a: 1, b: 20, c: 3, d: 4, e: 5}

// Clone object
const clone1 = Object.assign({}, obj1);
const clone2 = {...obj1};
```

## 🎯 Advanced Object Patterns

### Object Destructuring
```javascript
const user = {
    name: "John",
    age: 30,
    email: "john@example.com",
    address: {
        city: "New York",
        country: "USA"
    }
};

// Basic destructuring
const {name, age} = user;
console.log(name, age); // "John" 30

// Rename variables
const {name: userName, email: userEmail} = user;
console.log(userName); // "John"

// Default values
const {phone = "Not provided"} = user;
console.log(phone); // "Not provided"

// Nested destructuring
const {address: {city, country}} = user;
console.log(city, country); // "New York" "USA"

// Rest properties
const {name: n, ...otherProps} = user;
console.log(otherProps); // {age: 30, email: "john@example.com", address: {...}}
```

### Dynamic Property Manipulation
```javascript
const obj = {a: 1, b: 2, c: 3};

// Add properties conditionally
const shouldAddD = true;
const enhanced = {
    ...obj,
    ...(shouldAddD && {d: 4}),
    e: 5
};

// Remove properties
const {b, ...withoutB} = obj;
console.log(withoutB); // {a: 1, c: 3}

// Transform object properties
const doubled = Object.fromEntries(
    Object.entries(obj).map(([key, value]) => [key, value * 2])
);
console.log(doubled); // {a: 2, b: 4, c: 6}

// Filter object properties
const filtered = Object.fromEntries(
    Object.entries(obj).filter(([key, value]) => value > 1)
);
console.log(filtered); // {b: 2, c: 3}
```

### Object Factories
```javascript
// Factory function for creating similar objects
function createUser(name, age, role = "user") {
    return {
        name,
        age,
        role,
        id: Math.random().toString(36).substr(2, 9),
        createdAt: new Date(),
        
        greet() {
            return `Hello, I'm ${this.name}`;
        },
        
        getInfo() {
            return `${this.name} (${this.age}) - ${this.role}`;
        }
    };
}

const user1 = createUser("John", 30, "admin");
const user2 = createUser("Jane", 25);

console.log(user1.greet());    // "Hello, I'm John"
console.log(user2.getInfo());  // "Jane (25) - user"
```

## 🔒 Object Immutability

### Object.freeze()
```javascript
const obj = {a: 1, b: 2};

// Freeze object (prevent all modifications)
Object.freeze(obj);

obj.a = 10;        // Ignored in non-strict mode, throws in strict mode
obj.c = 3;         // Ignored
delete obj.b;      // Ignored

console.log(obj);  // {a: 1, b: 2} - unchanged

// Check if frozen
console.log(Object.isFrozen(obj)); // true
```

### Object.seal()
```javascript
const obj = {a: 1, b: 2};

// Seal object (prevent adding/removing properties, allow modification)
Object.seal(obj);

obj.a = 10;        // Allowed
obj.c = 3;         // Ignored
delete obj.b;      // Ignored

console.log(obj);  // {a: 10, b: 2}

// Check if sealed
console.log(Object.isSealed(obj)); // true
```

### Object.preventExtensions()
```javascript
const obj = {a: 1, b: 2};

// Prevent adding new properties (allow modification and deletion)
Object.preventExtensions(obj);

obj.a = 10;        // Allowed
obj.c = 3;         // Ignored
delete obj.b;      // Allowed

console.log(obj);  // {a: 10}

// Check if extensible
console.log(Object.isExtensible(obj)); // false
```

## 🎯 this Context in Objects

### Method Context
```javascript
const person = {
    name: "John",
    
    greet: function() {
        return `Hello, I'm ${this.name}`;
    },
    
    // Arrow function - lexical this (not recommended for methods)
    arrowGreet: () => {
        return `Hello, I'm ${this.name}`; // 'this' is not person!
    },
    
    // Method shorthand
    introduce() {
        return `My name is ${this.name}`;
    }
};

console.log(person.greet());      // "Hello, I'm John"
console.log(person.arrowGreet()); // "Hello, I'm undefined"
console.log(person.introduce());  // "My name is John"
```

### Context Loss and Binding
```javascript
const person = {
    name: "John",
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

// Context loss when assigning method to variable
const greetFunc = person.greet;
console.log(greetFunc()); // "Hello, I'm undefined"

// Solutions:
// 1. bind()
const boundGreet = person.greet.bind(person);
console.log(boundGreet()); // "Hello, I'm John"

// 2. Arrow function wrapper
const wrappedGreet = () => person.greet();
console.log(wrappedGreet()); // "Hello, I'm John"

// 3. call() or apply()
console.log(greetFunc.call(person)); // "Hello, I'm John"
```

## 💡 Best Practices

### Object Design
```javascript
// ✅ Good - Clear, descriptive properties
const user = {
    id: 1,
    firstName: "John",
    lastName: "Doe",
    email: "john@example.com",
    isActive: true,
    
    getFullName() {
        return `${this.firstName} ${this.lastName}`;
    }
};

// ❌ Avoid - Unclear property names
const u = {
    i: 1,
    fn: "John",
    ln: "Doe",
    e: "john@example.com",
    a: true
};
```

### Method Definition
```javascript
// ✅ Good - Use method shorthand
const obj = {
    name: "John",
    
    greet() {
        return `Hello, ${this.name}`;
    }
};

// ❌ Avoid - Arrow functions for methods
const obj2 = {
    name: "John",
    
    greet: () => {
        return `Hello, ${this.name}`; // 'this' won't work as expected
    }
};

// ❌ Avoid - Function expressions (verbose)
const obj3 = {
    name: "John",
    
    greet: function() {
        return `Hello, ${this.name}`;
    }
};
```

### Property Access
```javascript
// ✅ Use dot notation when possible
obj.propertyName;

// ✅ Use bracket notation for dynamic access or special characters
obj[dynamicKey];
obj["property-with-hyphens"];
obj["property with spaces"];

// ✅ Use optional chaining for safe access
obj.nested?.property?.deepProperty;
```

## 🚨 Common Pitfalls

### Reference vs Value
```javascript
// Objects are passed by reference
const original = {a: 1, b: 2};
const reference = original;

reference.a = 10;
console.log(original.a); // 10 - Original is affected!

// Create actual copy
const copy = {...original};
copy.a = 20;
console.log(original.a); // 10 - Original not affected
```

### Property Existence Checking
```javascript
const obj = {a: 1, b: null, c: undefined};

// ❌ Unreliable checks
if (obj.b) {}           // false (null is falsy)
if (obj.c) {}           // false (undefined is falsy)
if (obj.d) {}           // false (doesn't exist)

// ✅ Proper existence checks
if ("b" in obj) {}                    // true
if (obj.hasOwnProperty("b")) {}       // true
if (Object.hasOwn(obj, "b")) {}       // true (modern)
if (obj.b !== undefined) {}           // false for undefined values
```

### this Binding Issues
```javascript
const obj = {
    name: "John",
    greet() {
        setTimeout(function() {
            console.log(this.name); // undefined - 'this' is global
        }, 1000);
    },
    
    greetCorrect() {
        setTimeout(() => {
            console.log(this.name); // "John" - arrow function preserves 'this'
        }, 1000);
    }
};
```

---

*💡 Objects are the foundation of JavaScript - master them to build complex applications!*