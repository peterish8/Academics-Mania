# 🧬 Prototype, Inheritance & Object Methods

## 🔗 Prototype Inheritance

### What is Prototype?
Every object has hidden `[[Prototype]]` property linking to another object for inheritance.

### Prototype Chain
- **Date objects** → Date.prototype → Object.prototype
- **Array objects** → Array.prototype → Object.prototype
- **Custom objects** → Constructor.prototype → Object.prototype

### Adding to Prototype
```javascript
function Person(name) {
  this.name = name;
}
Person.prototype.sayHi = function() {
  console.log(`Hi, I'm ${this.name}`);
};

const p1 = new Person("Alice");
p1.sayHi(); // "Hi, I'm Alice"
```

### Object.create()
```javascript
const person = { greet() { console.log("Hello!"); } };
const student = Object.create(person);
student.name = "Alice";
student.greet(); // "Hello!" (inherited)
```

## 🔍 Enumerating Properties

### for...in Loop
Iterates over enumerable properties (including inherited).
```javascript
for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key, obj[key]); // Own properties only
  }
}
```

### Object Methods
- `Object.keys(obj)` → Array of own property names
- `Object.values(obj)` → Array of own property values  
- `Object.entries(obj)` → Array of [key, value] pairs
- `hasOwnProperty(prop)` → Check if property is own (not inherited)

### Object.assign()
Shallow merge objects.
```javascript
const merged = Object.assign({}, defaults, options);
// Copies properties from defaults and options to new object
```

## 🆚 Object.assign vs Spread
| Feature | Object.assign | Spread {...} |
|---------|---------------|--------------|
| Mutates target | Yes (if target provided) | No (always new object) |
| Syntax | `Object.assign(target, src)` | `{...obj1, ...obj2}` |
| Readability | Verbose | Clean and concise |

## 🏗️ Object Creation Patterns

### new Object() vs Object.create()
- `new Object()` → Creates with Object.prototype
- `Object.create(proto)` → Creates with custom prototype

### Nested Objects
```javascript
const user = {
  name: "Alice",
  address: {
    city: "Mumbai",
    coords: { lat: 19.07, lng: 72.88 }
  }
};

// Safe access with optional chaining
console.log(user.contact?.phone); // undefined (no error)
```