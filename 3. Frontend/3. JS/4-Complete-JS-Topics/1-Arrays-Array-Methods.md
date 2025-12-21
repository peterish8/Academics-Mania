# 📊 Arrays & Array Methods

## 📖 Definition
Arrays are ordered collections of elements that can store multiple values in a single variable. They are zero-indexed and can hold any data type.

## 🎯 Array Creation
```javascript
// Array literal (most common)
let fruits = ["apple", "banana", "orange"];
let numbers = [1, 2, 3, 4, 5];
let mixed = [1, "hello", true, null];

// Array constructor
let arr1 = new Array();           // Empty array
let arr2 = new Array(5);          // Array with 5 empty slots
let arr3 = new Array(1, 2, 3);    // [1, 2, 3]

// Array.of() - creates array from arguments
let arr4 = Array.of(1, 2, 3);     // [1, 2, 3]
let arr5 = Array.of(5);           // [5] (not empty array with 5 slots)

// Array.from() - creates array from iterable
let arr6 = Array.from("hello");   // ["h", "e", "l", "l", "o"]
let arr7 = Array.from([1, 2, 3], x => x * 2); // [2, 4, 6]
```

## 🔧 Mutating Array Methods (Change Original Array)

### Adding Elements
```javascript
let fruits = ["apple", "banana"];

// push() - add to end, returns new length
let newLength = fruits.push("orange");        // Returns 3
console.log(fruits); // ["apple", "banana", "orange"]

// unshift() - add to beginning, returns new length
fruits.unshift("grape");                      // Returns 4
console.log(fruits); // ["grape", "apple", "banana", "orange"]

// splice() - add/remove at any position
fruits.splice(2, 0, "mango", "kiwi");        // At index 2, remove 0, add items
console.log(fruits); // ["grape", "apple", "mango", "kiwi", "banana", "orange"]
```

### Removing Elements
```javascript
let fruits = ["apple", "banana", "orange"];

// pop() - remove from end, returns removed element
let last = fruits.pop();                      // Returns "orange"
console.log(fruits); // ["apple", "banana"]

// shift() - remove from beginning, returns removed element
let first = fruits.shift();                   // Returns "apple"
console.log(fruits); // ["banana"]

// splice() - remove from any position
let removed = fruits.splice(1, 2);            // Remove 2 elements starting at index 1
console.log(removed); // ["banana", "orange"]
```

### Modifying Arrays
```javascript
let numbers = [3, 1, 4, 1, 5];

// sort() - sorts in place, returns sorted array
numbers.sort();                               // [1, 1, 3, 4, 5]
numbers.sort((a, b) => b - a);               // [5, 4, 3, 1, 1] (descending)

// reverse() - reverses in place, returns reversed array
numbers.reverse();                            // [1, 1, 3, 4, 5]

// fill() - fills with static value
numbers.fill(0);                              // [0, 0, 0, 0, 0]
numbers.fill(7, 2, 4);                       // [0, 0, 7, 7, 0] (start, end)
```

## 🔍 Non-Mutating Array Methods (Return New Array)

### Extracting Elements
```javascript
let numbers = [1, 2, 3, 4, 5];

// slice() - extract portion, returns new array
let portion = numbers.slice(1, 4);           // [2, 3, 4] (start, end)
let copy = numbers.slice();                  // [1, 2, 3, 4, 5] (full copy)
let lastTwo = numbers.slice(-2);             // [4, 5] (negative indices)

// concat() - merge arrays, returns new array
let moreNumbers = [6, 7, 8];
let combined = numbers.concat(moreNumbers);   // [1, 2, 3, 4, 5, 6, 7, 8]
let multiConcat = numbers.concat(6, [7, 8]); // [1, 2, 3, 4, 5, 6, 7, 8]
```

### Converting to String
```javascript
let fruits = ["apple", "banana", "orange"];

// join() - creates string from array elements
let str1 = fruits.join();                    // "apple,banana,orange"
let str2 = fruits.join(" - ");               // "apple - banana - orange"
let str3 = fruits.join("");                  // "applebananaorange"

// toString() - converts to comma-separated string
let str4 = fruits.toString();                // "apple,banana,orange"
```

## 🔍 Search Methods

### Finding Elements
```javascript
let numbers = [1, 2, 3, 4, 5, 3];

// indexOf() - first occurrence index, -1 if not found
let index1 = numbers.indexOf(3);             // 2
let index2 = numbers.indexOf(6);             // -1

// lastIndexOf() - last occurrence index
let lastIndex = numbers.lastIndexOf(3);      // 5

// includes() - boolean check for existence
let exists = numbers.includes(4);            // true
let notExists = numbers.includes(6);         // false

// find() - first element matching condition
let found = numbers.find(x => x > 3);        // 4
let notFound = numbers.find(x => x > 10);    // undefined

// findIndex() - index of first matching element
let foundIndex = numbers.findIndex(x => x > 3); // 3
let notFoundIndex = numbers.findIndex(x => x > 10); // -1
```

## 🔄 Higher-Order Array Methods

### Transformation Methods
```javascript
let numbers = [1, 2, 3, 4, 5];

// map() - transform each element, returns new array
let doubled = numbers.map(x => x * 2);       // [2, 4, 6, 8, 10]
let strings = numbers.map(x => `Number: ${x}`); // ["Number: 1", "Number: 2", ...]

// filter() - select elements, returns new array
let evens = numbers.filter(x => x % 2 === 0); // [2, 4]
let greaterThan2 = numbers.filter(x => x > 2); // [3, 4, 5]

// reduce() - accumulate to single value
let sum = numbers.reduce((acc, x) => acc + x, 0); // 15
let product = numbers.reduce((acc, x) => acc * x, 1); // 120
let max = numbers.reduce((acc, x) => Math.max(acc, x)); // 5

// reduceRight() - reduce from right to left
let rightSum = numbers.reduceRight((acc, x) => acc + x, 0); // 15
```

### Iteration Methods
```javascript
let fruits = ["apple", "banana", "orange"];

// forEach() - execute function for each element, returns undefined
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});

// some() - test if any element matches condition
let hasLongName = fruits.some(fruit => fruit.length > 5); // true

// every() - test if all elements match condition
let allStrings = fruits.every(fruit => typeof fruit === "string"); // true
```

## 📊 Array Properties and Methods

### Length Property
```javascript
let arr = [1, 2, 3, 4, 5];

console.log(arr.length);                     // 5

// Changing length
arr.length = 3;                              // Truncates to [1, 2, 3]
arr.length = 5;                              // Extends with empty slots [1, 2, 3, , ,]

// Adding elements beyond length
arr[10] = "hello";                           // Creates sparse array
console.log(arr.length);                     // 11
```

### Static Methods
```javascript
// Array.isArray() - check if value is array
Array.isArray([1, 2, 3]);                   // true
Array.isArray("hello");                      // false

// Array.from() - create array from iterable
Array.from("hello");                         // ["h", "e", "l", "l", "o"]
Array.from({length: 3}, (_, i) => i);       // [0, 1, 2]

// Array.of() - create array from arguments
Array.of(1, 2, 3);                          // [1, 2, 3]
```

## 🎯 Advanced Array Techniques

### Flattening Arrays
```javascript
let nested = [1, [2, 3], [4, [5, 6]]];

// flat() - flatten one level
let flattened1 = nested.flat();              // [1, 2, 3, 4, [5, 6]]

// flat(depth) - flatten to specific depth
let flattened2 = nested.flat(2);             // [1, 2, 3, 4, 5, 6]

// flatMap() - map then flatten
let numbers = [1, 2, 3];
let doubled = numbers.flatMap(x => [x, x * 2]); // [1, 2, 2, 4, 3, 6]
```

### Array Destructuring
```javascript
let arr = [1, 2, 3, 4, 5];

// Basic destructuring
let [first, second] = arr;                   // first = 1, second = 2

// Skip elements
let [a, , c] = arr;                          // a = 1, c = 3

// Rest pattern
let [head, ...tail] = arr;                   // head = 1, tail = [2, 3, 4, 5]

// Default values
let [x, y, z = 0] = [1, 2];                 // x = 1, y = 2, z = 0
```

### Copying Arrays
```javascript
let original = [1, 2, 3];

// Spread operator (shallow copy)
let copy1 = [...original];

// Array.from()
let copy2 = Array.from(original);

// slice()
let copy3 = original.slice();

// concat()
let copy4 = [].concat(original);
```

## 💡 Best Practices

### Choosing the Right Method
```javascript
// ✅ Use map() for transformation
let doubled = numbers.map(x => x * 2);

// ✅ Use filter() for selection
let evens = numbers.filter(x => x % 2 === 0);

// ✅ Use find() for single element
let firstEven = numbers.find(x => x % 2 === 0);

// ✅ Use includes() for existence check
let hasThree = numbers.includes(3);

// ❌ Don't use forEach() when you need a return value
let doubled = [];
numbers.forEach(x => doubled.push(x * 2)); // Use map() instead
```

### Performance Considerations
```javascript
// ✅ Use appropriate method for task
let found = arr.find(x => x.id === targetId);     // Stops at first match

// ❌ Don't use filter() when you need only one element
let found = arr.filter(x => x.id === targetId)[0]; // Checks all elements

// ✅ Use for...of for simple iteration
for (let item of arr) {
    console.log(item);
}

// ❌ Don't use forEach() for simple logging
arr.forEach(item => console.log(item));
```

## 🚨 Common Pitfalls

### Mutating vs Non-Mutating
```javascript
let arr = [1, 2, 3];

// Mutating methods
arr.push(4);        // arr becomes [1, 2, 3, 4]
arr.sort();         // arr becomes [1, 2, 3, 4]

// Non-mutating methods
let newArr = arr.concat([5, 6]); // arr stays [1, 2, 3, 4], newArr is [1, 2, 3, 4, 5, 6]
let sliced = arr.slice(1, 3);    // arr unchanged, sliced is [2, 3]
```

### Array Holes
```javascript
let sparse = [1, , , 4];        // Array with holes
console.log(sparse.length);     // 4
console.log(sparse[1]);         // undefined

// Some methods skip holes
sparse.forEach(x => console.log(x)); // Only logs 1 and 4

// Others don't
sparse.map(x => x * 2);         // [2, NaN, NaN, 8]
```

---

*💡 Master array methods to become proficient in JavaScript data manipulation!*