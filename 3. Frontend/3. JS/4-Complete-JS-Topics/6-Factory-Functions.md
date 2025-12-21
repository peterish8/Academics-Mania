# 🏭 Factory Functions

## 📖 Definition
Factory functions are regular functions that return new objects. They provide an alternative to constructor functions and classes for creating objects, offering more flexibility and avoiding the need for the `new` keyword.

## 🎯 Basic Factory Function

### Simple Factory
```javascript
// Basic factory function
function createPerson(name, age) {
    return {
        name: name,
        age: age,
        greet: function() {
            return `Hello, I'm ${this.name} and I'm ${this.age} years old`;
        }
    };
}

// Usage - no 'new' keyword needed
const person1 = createPerson("John", 30);
const person2 = createPerson("Jane", 25);

console.log(person1.greet()); // "Hello, I'm John and I'm 30 years old"
console.log(person2.greet()); // "Hello, I'm Jane and I'm 25 years old"
```

### ES6 Enhanced Factory
```javascript
// Using ES6 features
function createUser(name, email, role = "user") {
    return {
        // Property shorthand
        name,
        email,
        role,
        
        // Computed properties
        id: Math.random().toString(36).substr(2, 9),
        createdAt: new Date().toISOString(),
        
        // Method shorthand
        getInfo() {
            return `${this.name} (${this.role}) - ${this.email}`;
        },
        
        updateRole(newRole) {
            this.role = newRole;
            return this; // Method chaining
        },
        
        isAdmin() {
            return this.role === "admin";
        }
    };
}

const user = createUser("John", "john@example.com", "admin");
console.log(user.getInfo()); // "John (admin) - john@example.com"
console.log(user.isAdmin()); // true
```

## 🔒 Private Variables with Closures

### Basic Privacy
```javascript
function createCounter() {
    let count = 0; // Private variable
    
    return {
        // Public methods that have access to private variable
        increment() {
            count++;
            return count;
        },
        
        decrement() {
            count--;
            return count;
        },
        
        getCount() {
            return count;
        },
        
        reset() {
            count = 0;
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());  // 2

// Private variable is not accessible
console.log(counter.count); // undefined - truly private!
```

### Advanced Privacy Pattern
```javascript
function createBankAccount(initialBalance = 0) {
    let balance = initialBalance;
    let transactionHistory = [];
    
    // Private helper function
    function addTransaction(type, amount) {
        transactionHistory.push({
            type,
            amount,
            balance: balance,
            timestamp: new Date()
        });
    }
    
    return {
        deposit(amount) {
            if (amount <= 0) {
                throw new Error("Deposit amount must be positive");
            }
            balance += amount;
            addTransaction("deposit", amount);
            return balance;
        },
        
        withdraw(amount) {
            if (amount <= 0) {
                throw new Error("Withdrawal amount must be positive");
            }
            if (amount > balance) {
                throw new Error("Insufficient funds");
            }
            balance -= amount;
            addTransaction("withdrawal", amount);
            return balance;
        },
        
        getBalance() {
            return balance;
        },
        
        getTransactionHistory() {
            // Return copy to prevent external modification
            return [...transactionHistory];
        },
        
        getLastTransaction() {
            return transactionHistory[transactionHistory.length - 1] || null;
        }
    };
}

const account = createBankAccount(1000);
account.deposit(500);
account.withdraw(200);
console.log(account.getBalance()); // 1300
console.log(account.getTransactionHistory().length); // 2
```

## 🔧 Factory Function Patterns

### Configurable Factory
```javascript
function createApiClient(config = {}) {
    const {
        baseUrl = "https://api.example.com",
        timeout = 5000,
        retries = 3,
        apiKey = null
    } = config;
    
    // Private state
    let requestCount = 0;
    
    return {
        async get(endpoint, params = {}) {
            requestCount++;
            const url = new URL(endpoint, baseUrl);
            Object.keys(params).forEach(key => 
                url.searchParams.append(key, params[key])
            );
            
            const headers = {
                'Content-Type': 'application/json',
                ...(apiKey && { 'Authorization': `Bearer ${apiKey}` })
            };
            
            try {
                const response = await fetch(url, { 
                    method: 'GET', 
                    headers,
                    timeout 
                });
                return await response.json();
            } catch (error) {
                console.error(`Request failed: ${error.message}`);
                throw error;
            }
        },
        
        async post(endpoint, data) {
            requestCount++;
            const url = new URL(endpoint, baseUrl);
            
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    ...(apiKey && { 'Authorization': `Bearer ${apiKey}` })
                },
                body: JSON.stringify(data),
                timeout
            });
            
            return await response.json();
        },
        
        getRequestCount() {
            return requestCount;
        },
        
        getConfig() {
            return { baseUrl, timeout, retries };
        }
    };
}

const api = createApiClient({
    baseUrl: "https://jsonplaceholder.typicode.com",
    apiKey: "my-secret-key"
});
```

### Mixin Factory Pattern
```javascript
// Mixins for common functionality
const canWalk = {
    walk() {
        return `${this.name} is walking`;
    }
};

const canFly = {
    fly() {
        return `${this.name} is flying`;
    }
};

const canSwim = {
    swim() {
        return `${this.name} is swimming`;
    }
};

// Factory that combines mixins
function createAnimal(name, abilities = []) {
    const animal = {
        name,
        energy: 100,
        
        rest() {
            this.energy = 100;
            return `${this.name} is resting`;
        },
        
        getEnergy() {
            return this.energy;
        }
    };
    
    // Add abilities based on array
    abilities.forEach(ability => {
        switch(ability) {
            case 'walk':
                Object.assign(animal, canWalk);
                break;
            case 'fly':
                Object.assign(animal, canFly);
                break;
            case 'swim':
                Object.assign(animal, canSwim);
                break;
        }
    });
    
    return animal;
}

const bird = createAnimal("Eagle", ["walk", "fly"]);
const fish = createAnimal("Shark", ["swim"]);
const duck = createAnimal("Duck", ["walk", "fly", "swim"]);

console.log(bird.fly());   // "Eagle is flying"
console.log(duck.swim());  // "Duck is swimming"
```

## 🎯 Method Chaining

### Fluent Interface
```javascript
function createQueryBuilder() {
    let query = {
        select: [],
        from: "",
        where: [],
        orderBy: [],
        limit: null
    };
    
    return {
        select(...fields) {
            query.select.push(...fields);
            return this; // Return this for chaining
        },
        
        from(table) {
            query.from = table;
            return this;
        },
        
        where(condition) {
            query.where.push(condition);
            return this;
        },
        
        orderBy(field, direction = "ASC") {
            query.orderBy.push(`${field} ${direction}`);
            return this;
        },
        
        limit(count) {
            query.limit = count;
            return this;
        },
        
        build() {
            let sql = `SELECT ${query.select.join(", ")} FROM ${query.from}`;
            
            if (query.where.length > 0) {
                sql += ` WHERE ${query.where.join(" AND ")}`;
            }
            
            if (query.orderBy.length > 0) {
                sql += ` ORDER BY ${query.orderBy.join(", ")}`;
            }
            
            if (query.limit) {
                sql += ` LIMIT ${query.limit}`;
            }
            
            return sql;
        },
        
        reset() {
            query = {
                select: [],
                from: "",
                where: [],
                orderBy: [],
                limit: null
            };
            return this;
        }
    };
}

const queryBuilder = createQueryBuilder();
const sql = queryBuilder
    .select("name", "email", "age")
    .from("users")
    .where("age > 18")
    .where("active = 1")
    .orderBy("name", "ASC")
    .limit(10)
    .build();

console.log(sql);
// "SELECT name, email, age FROM users WHERE age > 18 AND active = 1 ORDER BY name ASC LIMIT 10"
```

## 🔄 Factory with State Management

### State Machine Factory
```javascript
function createStateMachine(initialState, transitions) {
    let currentState = initialState;
    let history = [initialState];
    
    return {
        getCurrentState() {
            return currentState;
        },
        
        transition(action) {
            const possibleTransitions = transitions[currentState];
            
            if (!possibleTransitions || !possibleTransitions[action]) {
                throw new Error(`Invalid transition: ${action} from ${currentState}`);
            }
            
            const newState = possibleTransitions[action];
            history.push(newState);
            currentState = newState;
            
            return newState;
        },
        
        canTransition(action) {
            const possibleTransitions = transitions[currentState];
            return !!(possibleTransitions && possibleTransitions[action]);
        },
        
        getHistory() {
            return [...history];
        },
        
        getPossibleTransitions() {
            return Object.keys(transitions[currentState] || {});
        },
        
        reset() {
            currentState = initialState;
            history = [initialState];
        }
    };
}

// Traffic light state machine
const trafficLightTransitions = {
    red: { next: "green" },
    green: { next: "yellow" },
    yellow: { next: "red" }
};

const trafficLight = createStateMachine("red", trafficLightTransitions);

console.log(trafficLight.getCurrentState()); // "red"
trafficLight.transition("next"); // red -> green
console.log(trafficLight.getCurrentState()); // "green"
trafficLight.transition("next"); // green -> yellow
console.log(trafficLight.getHistory()); // ["red", "green", "yellow"]
```

## 💡 Advantages of Factory Functions

### Flexibility
```javascript
// Factory can return different object types
function createShape(type, ...args) {
    switch(type) {
        case "circle":
            return createCircle(args[0]); // radius
        case "rectangle":
            return createRectangle(args[0], args[1]); // width, height
        case "triangle":
            return createTriangle(args[0], args[1], args[2]); // sides
        default:
            throw new Error(`Unknown shape type: ${type}`);
    }
}

function createCircle(radius) {
    return {
        type: "circle",
        radius,
        area() {
            return Math.PI * this.radius ** 2;
        },
        perimeter() {
            return 2 * Math.PI * this.radius;
        }
    };
}

function createRectangle(width, height) {
    return {
        type: "rectangle",
        width,
        height,
        area() {
            return this.width * this.height;
        },
        perimeter() {
            return 2 * (this.width + this.height);
        }
    };
}

const circle = createShape("circle", 5);
const rectangle = createShape("rectangle", 4, 6);

console.log(circle.area());     // 78.54
console.log(rectangle.area());  // 24
```

### No `new` Keyword Issues
```javascript
// Factory functions work with or without 'new'
function createUser(name) {
    return {
        name,
        greet() {
            return `Hello, ${this.name}`;
        }
    };
}

// Both work the same way
const user1 = createUser("John");
const user2 = new createUser("Jane"); // Works but unnecessary

console.log(user1.greet()); // "Hello, John"
console.log(user2.greet()); // "Hello, Jane"
```

## 🚨 Disadvantages and Considerations

### Memory Usage
```javascript
// Each instance gets its own copy of methods
function createPerson(name) {
    return {
        name,
        // This method is recreated for each instance
        greet() {
            return `Hello, ${this.name}`;
        }
    };
}

const person1 = createPerson("John");
const person2 = createPerson("Jane");

// These are different function objects
console.log(person1.greet === person2.greet); // false

// Solution: Share methods via prototype or external object
const personMethods = {
    greet() {
        return `Hello, ${this.name}`;
    }
};

function createPersonOptimized(name) {
    const person = Object.create(personMethods);
    person.name = name;
    return person;
}

const optimized1 = createPersonOptimized("John");
const optimized2 = createPersonOptimized("Jane");

console.log(optimized1.greet === optimized2.greet); // true (shared method)
```

### instanceof Issues
```javascript
function createUser(name) {
    return { name };
}

const user = createUser("John");

// instanceof doesn't work with factory functions
console.log(user instanceof createUser); // false

// Solution: Use custom type checking
function createUserWithType(name) {
    return {
        name,
        type: "User",
        isUser: true
    };
}

function isUser(obj) {
    return obj && obj.type === "User" && obj.isUser === true;
}

const typedUser = createUserWithType("John");
console.log(isUser(typedUser)); // true
```

## 💡 Best Practices

### When to Use Factory Functions
```javascript
// ✅ Good use cases:
// 1. Need private variables
// 2. Want to avoid 'new' keyword
// 3. Need flexible object creation
// 4. Want to return different object types
// 5. Need complex initialization logic

// ✅ Example: Complex initialization
function createDatabaseConnection(config) {
    // Complex setup logic
    const connection = establishConnection(config);
    const cache = new Map();
    
    return {
        async query(sql, params) {
            const cacheKey = `${sql}:${JSON.stringify(params)}`;
            if (cache.has(cacheKey)) {
                return cache.get(cacheKey);
            }
            
            const result = await connection.execute(sql, params);
            cache.set(cacheKey, result);
            return result;
        },
        
        clearCache() {
            cache.clear();
        },
        
        close() {
            connection.close();
        }
    };
}
```

### Naming Conventions
```javascript
// ✅ Use descriptive names starting with 'create'
function createUser(name, email) { /* ... */ }
function createApiClient(config) { /* ... */ }
function createValidator(rules) { /* ... */ }

// ✅ Or use factory suffix
function userFactory(name, email) { /* ... */ }
function apiClientFactory(config) { /* ... */ }

// ❌ Avoid constructor-like names
function User(name, email) { /* Looks like constructor */ }
```

---

*💡 Factory functions provide a flexible, powerful way to create objects with encapsulation and privacy!*