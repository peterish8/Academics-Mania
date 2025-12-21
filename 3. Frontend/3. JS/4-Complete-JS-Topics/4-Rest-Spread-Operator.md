# 🔄 Rest & Spread Operator

## 📖 Definition
The rest and spread operators both use the same syntax (`...`) but serve opposite purposes. Rest collects multiple elements into an array, while spread expands arrays or objects into individual elements.

## 🔄 Rest Operator (Collect)

### Function Parameters
```javascript
// Collect all arguments into an array
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3));         // 6
console.log(sum(1, 2, 3, 4, 5));   // 15

// Mix regular parameters with rest
function greet(greeting, ...names) {
    return `${greeting} ${names.join(", ")}!`;
}

console.log(greet("Hello", "John", "Jane", "Bob")); // "Hello John, Jane, Bob!"
```

### Array Destructuring
```javascript
const numbers = [1, 2, 3, 4, 5];

// Rest in destructuring - collect remaining elements
const [first, second, ...rest] = numbers;
console.log(first);  // 1
console.log(second); // 2
console.log(rest);   // [3, 4, 5]

// Skip elements
const [a, , c, ...others] = numbers;
console.log(a);      // 1
console.log(c);      // 3
console.log(others); // [4, 5]
```

### Object Destructuring
```javascript
const user = {
    name: "John",
    age: 30,
    email: "john@example.com",
    city: "New York",
    country: "USA"
};

// Rest in object destructuring - collect remaining properties
const {name, age, ...otherInfo} = user;
console.log(name);      // "John"
console.log(age);       // 30
console.log(otherInfo); // {email: "john@example.com", city: "New York", country: "USA"}

// Rename while destructuring
const {name: userName, ...details} = user;
console.log(userName); // "John"
console.log(details);  // {age: 30, email: "john@example.com", city: "New York", country: "USA"}
```

## 📤 Spread Operator (Expand)

### Array Spread
```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Combine arrays
const combined = [...arr1, ...arr2];
console.log(combined); // [1, 2, 3, 4, 5, 6]

// Add elements while spreading
const extended = [0, ...arr1, 3.5, ...arr2, 7];
console.log(extended); // [0, 1, 2, 3, 3.5, 4, 5, 6, 7]

// Copy array (shallow copy)
const copy = [...arr1];
console.log(copy); // [1, 2, 3]

// Convert string to array
const letters = [..."hello"];
console.log(letters); // ["h", "e", "l", "l", "o"]
```

### Object Spread
```javascript
const obj1 = {a: 1, b: 2};
const obj2 = {c: 3, d: 4};

// Combine objects
const combined = {...obj1, ...obj2};
console.log(combined); // {a: 1, b: 2, c: 3, d: 4}

// Override properties
const updated = {...obj1, b: 20, e: 5};
console.log(updated); // {a: 1, b: 20, e: 5}

// Copy object (shallow copy)
const copy = {...obj1};
console.log(copy); // {a: 1, b: 2}

// Add properties while spreading
const extended = {
    id: 1,
    ...obj1,
    timestamp: Date.now()
};
```

### Function Calls
```javascript
function multiply(a, b, c) {
    return a * b * c;
}

const numbers = [2, 3, 4];

// Spread array as function arguments
const result = multiply(...numbers);
console.log(result); // 24

// Mix spread with regular arguments
const result2 = multiply(1, ...numbers.slice(1));
console.log(result2); // 12 (1 * 3 * 4)

// Find max/min in array
const nums = [1, 5, 3, 9, 2];
const max = Math.max(...nums);
const min = Math.min(...nums);
console.log(max); // 9
console.log(min); // 1
```

## 🎯 Practical Examples

### Array Manipulation
```javascript
// Remove duplicates
const numbers = [1, 2, 2, 3, 3, 4, 5];
const unique = [...new Set(numbers)];
console.log(unique); // [1, 2, 3, 4, 5]

// Flatten array (one level)
const nested = [[1, 2], [3, 4], [5, 6]];
const flattened = [].concat(...nested);
console.log(flattened); // [1, 2, 3, 4, 5, 6]

// Insert elements at specific position
const original = [1, 2, 5, 6];
const toInsert = [3, 4];
const position = 2;
const result = [
    ...original.slice(0, position),
    ...toInsert,
    ...original.slice(position)
];
console.log(result); // [1, 2, 3, 4, 5, 6]
```

### Object Manipulation
```javascript
// Update nested object properties
const user = {
    name: "John",
    address: {
        street: "123 Main St",
        city: "New York"
    }
};

const updatedUser = {
    ...user,
    address: {
        ...user.address,
        city: "Boston"
    }
};

// Conditional properties
const includeEmail = true;
const userWithConditionalEmail = {
    name: "John",
    age: 30,
    ...(includeEmail && {email: "john@example.com"})
};

// Remove properties (using destructuring + rest)
const {password, ...userWithoutPassword} = {
    name: "John",
    email: "john@example.com",
    password: "secret123"
};
console.log(userWithoutPassword); // {name: "John", email: "john@example.com"}
```

### Function Utilities
```javascript
// Create flexible logger function
function log(level, ...messages) {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${level.toUpperCase()}:`, ...messages);
}

log("info", "User logged in", {userId: 123});
log("error", "Database connection failed", "Retrying...");

// Curry function with rest parameters
const curry = (fn, ...args1) => (...args2) => fn(...args1, ...args2);

const add = (a, b, c) => a + b + c;
const addFive = curry(add, 5);
const result = addFive(3, 2); // 10

// Pipe function composition
const pipe = (...functions) => (value) => 
    functions.reduce((acc, fn) => fn(acc), value);

const addOne = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

const transform = pipe(addOne, double, square);
console.log(transform(3)); // ((3 + 1) * 2)² = 64
```

## 🔧 Advanced Patterns

### Dynamic Object Creation
```javascript
// Create object with dynamic keys
function createConfig(env, ...features) {
    const baseConfig = {
        environment: env,
        timestamp: Date.now()
    };
    
    const featureConfig = features.reduce((config, feature) => ({
        ...config,
        [feature]: true
    }), {});
    
    return {
        ...baseConfig,
        features: featureConfig
    };
}

const config = createConfig("production", "auth", "logging", "caching");
console.log(config);
// {
//   environment: "production",
//   timestamp: 1234567890,
//   features: {auth: true, logging: true, caching: true}
// }
```

### Array Processing Chains
```javascript
// Process arrays with spread in method chains
const numbers = [1, 2, 3, 4, 5];

const result = numbers
    .map(x => x * 2)                    // [2, 4, 6, 8, 10]
    .filter(x => x > 5)                 // [6, 8, 10]
    .reduce((acc, x) => [...acc, x, x], []); // [6, 6, 8, 8, 10, 10]

// Merge multiple arrays with processing
const arrays = [[1, 2], [3, 4], [5, 6]];
const processed = arrays
    .map(arr => arr.map(x => x * 2))    // [[2, 4], [6, 8], [10, 12]]
    .reduce((acc, arr) => [...acc, ...arr], []); // [2, 4, 6, 8, 10, 12]
```

### State Management Patterns
```javascript
// Immutable state updates
const initialState = {
    users: [],
    loading: false,
    error: null
};

// Add user
const addUser = (state, user) => ({
    ...state,
    users: [...state.users, user]
});

// Update user
const updateUser = (state, userId, updates) => ({
    ...state,
    users: state.users.map(user => 
        user.id === userId ? {...user, ...updates} : user
    )
});

// Remove user
const removeUser = (state, userId) => ({
    ...state,
    users: state.users.filter(user => user.id !== userId)
});

// Toggle loading
const setLoading = (state, loading) => ({
    ...state,
    loading
});
```

## 💡 Best Practices

### When to Use Rest
```javascript
// ✅ Variable number of function arguments
function createTeam(captain, ...members) {
    return {
        captain,
        members,
        size: members.length + 1
    };
}

// ✅ Extracting remaining properties
const {id, ...userDetails} = user;

// ✅ Collecting array elements
const [head, ...tail] = array;
```

### When to Use Spread
```javascript
// ✅ Copying arrays/objects
const copy = [...original];
const objCopy = {...original};

// ✅ Combining arrays/objects
const combined = [...arr1, ...arr2];
const merged = {...obj1, ...obj2};

// ✅ Converting iterables to arrays
const chars = [..."hello"];
const args = [...arguments];

// ✅ Function calls with array arguments
Math.max(...numbers);
```

### Performance Considerations
```javascript
// ✅ Efficient for small to medium arrays/objects
const small = [...smallArray];

// ⚠️ Be careful with large datasets
const large = [...veryLargeArray]; // Can be memory intensive

// ✅ Use alternatives for large datasets
const largeCopy = Array.from(veryLargeArray);
const largeSlice = veryLargeArray.slice();
```

## 🚨 Common Pitfalls

### Shallow Copy Limitation
```javascript
const original = {
    name: "John",
    hobbies: ["reading", "coding"]
};

// ❌ Shallow copy - nested arrays/objects are still referenced
const copy = {...original};
copy.hobbies.push("gaming");
console.log(original.hobbies); // ["reading", "coding", "gaming"] - Original affected!

// ✅ Deep copy for nested structures
const deepCopy = {
    ...original,
    hobbies: [...original.hobbies]
};
```

### Rest Parameter Position
```javascript
// ❌ Rest parameter must be last
function wrong(a, ...rest, b) {} // SyntaxError

// ✅ Rest parameter at the end
function correct(a, b, ...rest) {}

// ❌ Multiple rest parameters
function invalid(...rest1, ...rest2) {} // SyntaxError

// ✅ Only one rest parameter allowed
function valid(...args) {}
```

### Object Property Order
```javascript
const base = {a: 1, b: 2};
const override = {b: 20, c: 3};

// Order matters in object spread
const result1 = {...base, ...override}; // {a: 1, b: 20, c: 3}
const result2 = {...override, ...base}; // {b: 2, c: 3, a: 1}

// Explicit override
const result3 = {...base, b: 30}; // {a: 1, b: 30}
```

### Performance with Large Objects
```javascript
// ❌ Inefficient for frequent updates on large objects
let largeState = {...veryLargeObject};
for (let i = 0; i < 1000; i++) {
    largeState = {...largeState, [`key${i}`]: i}; // Creates new object each time
}

// ✅ Better approach for multiple updates
const updates = {};
for (let i = 0; i < 1000; i++) {
    updates[`key${i}`] = i;
}
largeState = {...largeState, ...updates}; // Single object creation
```

---

*💡 Master rest and spread operators to write more concise and functional JavaScript code!*