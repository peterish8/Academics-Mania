# 📄 JSON & Higher-Order Functions Mastery

## 📄 JSON (JavaScript Object Notation) Deep Dive

### 🎯 What is JSON?
**Definition**: A lightweight, text-based data interchange format that's easy for humans to read and write, and easy for machines to parse and generate.

**Key Characteristics**:
- **Language-independent** → Works with any programming language
- **Text-based** → Pure string format
- **Structured** → Organized key-value pairs
- **Lightweight** → Minimal syntax overhead

### 🎨 JSON vs JavaScript Object

| Feature | JavaScript Object | JSON |
|---------|------------------|------|
| **Keys** | Can be unquoted | Must be double-quoted |
| **Values** | Any JS type | String, Number, Boolean, null, Object, Array |
| **Functions** | ✅ Allowed | ❌ Not allowed |
| **undefined** | ✅ Allowed | ❌ Not allowed |
| **Comments** | ✅ Allowed | ❌ Not allowed |
| **Trailing commas** | ✅ Allowed | ❌ Not allowed |

```javascript
// JavaScript Object
const jsObject = {
  name: "Alice",           // Unquoted key
  age: 25,
  isActive: true,
  greet: function() {      // Function (not JSON-compatible)
    return "Hello";
  },
  data: undefined          // undefined (not JSON-compatible)
};

// JSON String
const jsonString = `{
  "name": "Alice",         
  "age": 25,
  "isActive": true,
  "hobbies": ["reading", "coding"]
}`;
```

---

## 🔄 JSON Methods Mastery

### 📤 JSON.stringify() - Object to String

#### Basic Usage
```javascript
const user = {
  name: "Alice",
  age: 25,
  hobbies: ["reading", "coding"],
  address: {
    city: "New York",
    country: "USA"
  }
};

const jsonString = JSON.stringify(user);
console.log(jsonString);
// '{"name":"Alice","age":25,"hobbies":["reading","coding"],"address":{"city":"New York","country":"USA"}}'

console.log(typeof jsonString); // "string"
```

#### Advanced stringify() Options
```javascript
const data = {
  name: "Alice",
  age: 25,
  password: "secret123",
  createdAt: new Date()
};

// Pretty printing with indentation
const prettyJson = JSON.stringify(data, null, 2);
console.log(prettyJson);
/*
{
  "name": "Alice",
  "age": 25,
  "password": "secret123",
  "createdAt": "2024-01-15T10:30:00.000Z"
}
*/

// Filtering properties (replacer function)
const filteredJson = JSON.stringify(data, (key, value) => {
  if (key === "password") return undefined; // Exclude password
  return value;
});

// Filtering with array
const selectedJson = JSON.stringify(data, ["name", "age"]);
console.log(selectedJson); // '{"name":"Alice","age":25}'
```

### 📥 JSON.parse() - String to Object

#### Basic Usage
```javascript
const jsonString = '{"name":"Bob","age":30,"isActive":true}';
const obj = JSON.parse(jsonString);

console.log(obj);        // {name: "Bob", age: 30, isActive: true}
console.log(obj.name);   // "Bob"
console.log(typeof obj); // "object"
```

#### Error Handling
```javascript
function safeJsonParse(jsonString) {
  try {
    return JSON.parse(jsonString);
  } catch (error) {
    console.error("Invalid JSON:", error.message);
    return null;
  }
}

// Valid JSON
const validResult = safeJsonParse('{"name":"Alice"}');
console.log(validResult); // {name: "Alice"}

// Invalid JSON
const invalidResult = safeJsonParse('{name:"Alice"}'); // Missing quotes
console.log(invalidResult); // null
```

#### Reviver Function
```javascript
const jsonWithDates = '{"name":"Alice","birthDate":"2024-01-15T10:30:00.000Z"}';

const parsed = JSON.parse(jsonWithDates, (key, value) => {
  // Convert date strings back to Date objects
  if (key === "birthDate") {
    return new Date(value);
  }
  return value;
});

console.log(parsed.birthDate instanceof Date); // true
```

---

## 🌐 JSON Use Cases Deep Dive

### 1️⃣ API Communication

#### Sending Data to Server
```javascript
const userData = {
  name: "Alice",
  email: "alice@example.com",
  preferences: {
    theme: "dark",
    notifications: true
  }
};

// POST request with JSON data
fetch("https://api.example.com/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(userData) // Convert to JSON string
})
.then(response => response.json()) // Parse JSON response
.then(data => console.log("User created:", data))
.catch(error => console.error("Error:", error));
```

#### Receiving Data from Server
```javascript
// GET request expecting JSON response
async function fetchUserData(userId) {
  try {
    const response = await fetch(`https://api.example.com/users/${userId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const userData = await response.json(); // Parse JSON automatically
    return userData;
  } catch (error) {
    console.error("Failed to fetch user data:", error);
    return null;
  }
}

// Usage
fetchUserData(123).then(user => {
  if (user) {
    console.log(`Welcome, ${user.name}!`);
  }
});
```

### 2️⃣ localStorage Integration

#### Saving Complex Data
```javascript
const appSettings = {
  theme: "dark",
  language: "en",
  fontSize: 16,
  notifications: {
    email: true,
    push: false,
    sms: true
  },
  recentFiles: ["file1.txt", "file2.txt", "file3.txt"]
};

// Save to localStorage (must be string)
localStorage.setItem("appSettings", JSON.stringify(appSettings));

// Retrieve from localStorage
const savedSettings = localStorage.getItem("appSettings");
if (savedSettings) {
  const settings = JSON.parse(savedSettings);
  console.log("Loaded settings:", settings);
  
  // Apply settings to app
  document.body.className = settings.theme;
  document.documentElement.style.fontSize = settings.fontSize + "px";
}
```

#### Settings Manager Pattern
```javascript
class SettingsManager {
  constructor(key = "appSettings") {
    this.storageKey = key;
    this.defaultSettings = {
      theme: "light",
      language: "en",
      fontSize: 14
    };
  }
  
  load() {
    try {
      const saved = localStorage.getItem(this.storageKey);
      return saved ? JSON.parse(saved) : this.defaultSettings;
    } catch (error) {
      console.error("Failed to load settings:", error);
      return this.defaultSettings;
    }
  }
  
  save(settings) {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(settings));
      return true;
    } catch (error) {
      console.error("Failed to save settings:", error);
      return false;
    }
  }
  
  update(newSettings) {
    const current = this.load();
    const updated = { ...current, ...newSettings };
    return this.save(updated);
  }
}

// Usage
const settings = new SettingsManager();
settings.update({ theme: "dark", fontSize: 16 });
```

### 3️⃣ Configuration Files
```javascript
// config.json (external file)
{
  "apiUrl": "https://api.example.com",
  "timeout": 5000,
  "retryAttempts": 3,
  "features": {
    "darkMode": true,
    "notifications": false
  }
}

// Loading configuration
async function loadConfig() {
  try {
    const response = await fetch("./config.json");
    const config = await response.json();
    return config;
  } catch (error) {
    console.error("Failed to load config:", error);
    return null;
  }
}
```

---

## 🔄 Higher-Order Functions (HOF) Mastery

### 🎯 What Makes a Function "Higher-Order"?

**Definition**: A function that either:
1. **Takes another function as an argument** (callback)
2. **Returns a function** (function factory)

```javascript
// Example 1: Takes function as argument
function processArray(arr, callback) {
  return arr.map(callback);
}

// Example 2: Returns a function
function createMultiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

const double = createMultiplier(2);
console.log(double(5)); // 10
```

### 🎯 Why Higher-Order Functions Matter

#### Benefits
- **Code Reusability** → Same logic, different operations
- **Abstraction** → Hide complex implementation details
- **Composability** → Combine simple functions into complex ones
- **Functional Programming** → Declarative vs imperative style

#### Real-World Analogy
Think of HOFs like a **coffee machine**:
- The machine (HOF) stays the same
- You can insert different coffee pods (callback functions)
- Each pod produces different coffee (different results)

---

## 🛠️ Built-in Higher-Order Functions Deep Dive

### 1️⃣ forEach() - The Iterator

#### Basic Usage
```javascript
const numbers = [1, 2, 3, 4, 5];

// Traditional for loop
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] * 2);
}

// forEach (cleaner)
numbers.forEach(num => console.log(num * 2));

// With index and array parameters
numbers.forEach((num, index, array) => {
  console.log(`Index ${index}: ${num} (Array length: ${array.length})`);
});
```

#### Practical Applications
```javascript
// DOM manipulation
const buttons = document.querySelectorAll('.btn');
buttons.forEach(button => {
  button.addEventListener('click', handleClick);
});

// Data processing
const users = [{name: "Alice", age: 25}, {name: "Bob", age: 30}];
users.forEach(user => {
  console.log(`${user.name} is ${user.age} years old`);
});
```

**Key Point**: forEach() doesn't return anything (returns `undefined`)

### 2️⃣ map() - The Transformer

#### Basic Usage
```javascript
const numbers = [1, 2, 3, 4, 5];

// Transform each element
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// Original array unchanged
console.log(numbers); // [1, 2, 3, 4, 5]
```

#### Advanced Transformations
```javascript
const users = [
  {firstName: "Alice", lastName: "Johnson", age: 25},
  {firstName: "Bob", lastName: "Smith", age: 30},
  {firstName: "Carol", lastName: "Davis", age: 35}
];

// Extract full names
const fullNames = users.map(user => `${user.firstName} ${user.lastName}`);
console.log(fullNames); // ["Alice Johnson", "Bob Smith", "Carol Davis"]

// Create user cards (objects)
const userCards = users.map(user => ({
  id: user.firstName.toLowerCase(),
  displayName: user.firstName,
  isAdult: user.age >= 18
}));

// Chain with other methods
const adultNames = users
  .filter(user => user.age >= 30)
  .map(user => user.firstName);
console.log(adultNames); // ["Bob", "Carol"]
```

### 3️⃣ filter() - The Selector

#### Basic Usage
```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Select even numbers
const evens = numbers.filter(num => num % 2 === 0);
console.log(evens); // [2, 4, 6, 8, 10]

// Select numbers greater than 5
const greaterThanFive = numbers.filter(num => num > 5);
console.log(greaterThanFive); // [6, 7, 8, 9, 10]
```

#### Complex Filtering
```javascript
const products = [
  {name: "Laptop", price: 1000, category: "Electronics", inStock: true},
  {name: "Phone", price: 500, category: "Electronics", inStock: false},
  {name: "Book", price: 20, category: "Education", inStock: true},
  {name: "Headphones", price: 100, category: "Electronics", inStock: true}
];

// Multiple conditions
const availableElectronics = products.filter(product => 
  product.category === "Electronics" && 
  product.inStock && 
  product.price < 600
);

// Using helper functions
const isAffordable = product => product.price <= 100;
const isInStock = product => product.inStock;

const affordableInStock = products
  .filter(isAffordable)
  .filter(isInStock);
```

### 4️⃣ reduce() - The Accumulator

#### Basic Usage
```javascript
const numbers = [1, 2, 3, 4, 5];

// Sum all numbers
const sum = numbers.reduce((accumulator, current) => {
  return accumulator + current;
}, 0); // 0 is initial value

console.log(sum); // 15

// Shorter version
const sum2 = numbers.reduce((acc, curr) => acc + curr, 0);
```

#### Advanced reduce() Patterns
```javascript
const transactions = [
  {type: "income", amount: 1000},
  {type: "expense", amount: 200},
  {type: "income", amount: 500},
  {type: "expense", amount: 100}
];

// Calculate net balance
const balance = transactions.reduce((acc, transaction) => {
  return transaction.type === "income" 
    ? acc + transaction.amount 
    : acc - transaction.amount;
}, 0);

console.log(balance); // 1200

// Group by type
const grouped = transactions.reduce((acc, transaction) => {
  const type = transaction.type;
  if (!acc[type]) {
    acc[type] = [];
  }
  acc[type].push(transaction);
  return acc;
}, {});

// Count occurrences
const fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"];
const fruitCount = fruits.reduce((acc, fruit) => {
  acc[fruit] = (acc[fruit] || 0) + 1;
  return acc;
}, {});

console.log(fruitCount); // {apple: 3, banana: 2, cherry: 1}
```

### 5️⃣ find() - The Searcher

```javascript
const users = [
  {id: 1, name: "Alice", role: "admin"},
  {id: 2, name: "Bob", role: "user"},
  {id: 3, name: "Carol", role: "moderator"}
];

// Find first admin
const admin = users.find(user => user.role === "admin");
console.log(admin); // {id: 1, name: "Alice", role: "admin"}

// Find by ID
const userById = users.find(user => user.id === 2);
console.log(userById); // {id: 2, name: "Bob", role: "user"}

// Not found returns undefined
const notFound = users.find(user => user.role === "superuser");
console.log(notFound); // undefined
```

### 6️⃣ some() & every() - The Validators

#### some() - At Least One
```javascript
const numbers = [1, 3, 5, 8, 9];

// Check if any number is even
const hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven); // true (8 is even)

// Check if any user is admin
const users = [{role: "user"}, {role: "admin"}, {role: "user"}];
const hasAdmin = users.some(user => user.role === "admin");
console.log(hasAdmin); // true
```

#### every() - All Must Pass
```javascript
const numbers = [2, 4, 6, 8, 10];

// Check if all numbers are even
const allEven = numbers.every(num => num % 2 === 0);
console.log(allEven); // true

// Check if all users are adults
const users = [{age: 25}, {age: 30}, {age: 17}];
const allAdults = users.every(user => user.age >= 18);
console.log(allAdults); // false (17 < 18)
```

---

## 🎯 Method Chaining & Composition

### 🔗 Chaining Array Methods
```javascript
const sales = [
  {product: "Laptop", amount: 1000, month: "Jan"},
  {product: "Phone", amount: 500, month: "Jan"},
  {product: "Tablet", amount: 300, month: "Feb"},
  {product: "Laptop", amount: 1200, month: "Feb"},
  {product: "Phone", amount: 450, month: "Mar"}
];

// Complex data processing pipeline
const result = sales
  .filter(sale => sale.amount > 400)           // High-value sales only
  .map(sale => ({...sale, quarter: getQuarter(sale.month)})) // Add quarter
  .reduce((acc, sale) => {                     // Group by quarter
    const q = sale.quarter;
    acc[q] = (acc[q] || 0) + sale.amount;
    return acc;
  }, {});

function getQuarter(month) {
  const quarters = {
    Jan: "Q1", Feb: "Q1", Mar: "Q1",
    Apr: "Q2", May: "Q2", Jun: "Q2",
    Jul: "Q3", Aug: "Q3", Sep: "Q3",
    Oct: "Q4", Nov: "Q4", Dec: "Q4"
  };
  return quarters[month];
}
```

### 🏗️ Creating Custom Higher-Order Functions
```javascript
// Generic array processor
function processArray(array, ...operations) {
  return operations.reduce((result, operation) => {
    return result.map(operation);
  }, array);
}

// Usage
const numbers = [1, 2, 3, 4, 5];
const result = processArray(
  numbers,
  x => x * 2,      // Double
  x => x + 1,      // Add 1
  x => x ** 2      // Square
);
console.log(result); // [9, 25, 49, 81, 121]

// Conditional processor
function conditionalMap(array, condition, transform) {
  return array.map(item => condition(item) ? transform(item) : item);
}

// Double only even numbers
const mixed = [1, 2, 3, 4, 5, 6];
const result2 = conditionalMap(
  mixed,
  x => x % 2 === 0,  // Condition: is even
  x => x * 2         // Transform: double
);
console.log(result2); // [1, 4, 3, 8, 5, 12]
```

---

## 🧠 Best Practices & Performance

### ✅ When to Use Each Method

| Method | Use When | Returns |
|--------|----------|---------|
| `forEach` | Side effects (DOM, logging) | `undefined` |
| `map` | Transform every element | New array (same length) |
| `filter` | Select subset of elements | New array (≤ original length) |
| `reduce` | Combine into single value | Any type |
| `find` | Get first matching element | Element or `undefined` |
| `some` | Check if any match | `boolean` |
| `every` | Check if all match | `boolean` |

### ⚡ Performance Considerations
```javascript
// ❌ Inefficient: Multiple iterations
const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const result1 = data
  .filter(x => x > 3)
  .map(x => x * 2)
  .filter(x => x < 15);

// ✅ Efficient: Single iteration with reduce
const result2 = data.reduce((acc, x) => {
  if (x > 3) {
    const doubled = x * 2;
    if (doubled < 15) {
      acc.push(doubled);
    }
  }
  return acc;
}, []);

// ✅ Good balance: Readable and reasonably efficient
const result3 = data
  .filter(x => x > 3 && x * 2 < 15)  // Combined conditions
  .map(x => x * 2);
```

### 🧠 Memory Tricks
- **forEach** = "For each item, do something (no return)"
- **map** = "Map each item to something new"
- **filter** = "Filter out unwanted items"
- **reduce** = "Reduce many items to one result"
- **find** = "Find the first match"
- **some** = "Some items pass the test"
- **every** = "Every item must pass the test"

**Master Memory Trick**: "HOFs are like assembly lines - each function does one job well, and you can chain them together for complex processing"