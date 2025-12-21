# 📄 JSON & Higher-Order Functions

## 📄 JSON Use Cases

### 1. API Data Exchange
```javascript
fetch("https://api.example.com/users/1")
  .then(response => response.json()) // Parse JSON
  .then(data => console.log(data));
```

### 2. localStorage
```javascript
const settings = {theme: "dark", fontSize: 16};

// Save to localStorage
localStorage.setItem("appSettings", JSON.stringify(settings));

// Retrieve from localStorage
const saved = JSON.parse(localStorage.getItem("appSettings"));
console.log(saved); // {theme: "dark", fontSize: 16}
```

### Quick Summary
- `JSON.stringify(obj)` → Object to JSON string
- `JSON.parse(string)` → JSON string to object
- Used in APIs and localStorage

## 🔄 Higher-Order Functions (HOF)

### Definition
Functions that:
- Take another function as argument, OR
- Return another function

```javascript
function higherOrder(fn) {
  console.log("Calling callback...");
  fn(); // Execute passed function
}

higherOrder(() => console.log("I'm the callback!"));
```

## 🛠️ Built-in Higher-Order Functions

### 1. forEach()
Execute function for each element (no return).
```javascript
const nums = [1, 2, 3];
nums.forEach(n => console.log(n * 2)); // 2, 4, 6
```

### 2. map()
Transform each element, return new array.
```javascript
const nums = [1, 2, 3];
const squares = nums.map(n => n * n);
console.log(squares); // [1, 4, 9]
```

### 3. filter()
Select elements that pass condition.
```javascript
const nums = [5, 10, 15, 20];
const evens = nums.filter(n => n % 2 === 0);
console.log(evens); // [10, 20]
```

### 4. reduce()
Reduce array to single value.
```javascript
const nums = [1, 2, 3, 4];
const sum = nums.reduce((acc, curr) => acc + curr, 0);
console.log(sum); // 10
```

### 5. find()
Return first element that matches.
```javascript
const nums = [3, 7, 11, 15];
const firstOdd = nums.find(n => n % 2 !== 0);
console.log(firstOdd); // 3
```

### 6. some()
True if at least one element passes.
```javascript
const nums = [2, 4, 6, 9];
const hasOdd = nums.some(n => n % 2 !== 0);
console.log(hasOdd); // true
```

### 7. every()
True only if all elements pass.
```javascript
const nums = [2, 4, 6, 8];
const allEven = nums.every(n => n % 2 === 0);
console.log(allEven); // true
```

## 📋 HOF Quick Reference

| Method | Purpose | Returns |
|--------|---------|---------|
| `forEach` | Loop through array | `undefined` |
| `map` | Transform elements | New array |
| `filter` | Select elements | New array |
| `reduce` | Combine to single value | Single value |
| `find` | First match | Element or `undefined` |
| `some` | At least one passes | `boolean` |
| `every` | All must pass | `boolean` |

### Memory Tricks
- **forEach** → "For each element, do something"
- **map** → "Map each element to new value"
- **filter** → "Filter out unwanted elements"
- **reduce** → "Reduce many to one"
- **find** → "Find the first match"
- **some** → "Some elements pass"
- **every** → "Every element must pass"