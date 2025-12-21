# 🌟 Rest & Spread Operators

## 🎯 **The Three Dots (`...`)**

> [!SUCCESS] **Concept**: The behavior depends on WHERE you use it.
> **Spread**: Unpacks an array (Expands). 📤
> **Rest**: Packs items into an array (Collects). 📥

---

## 🍞 **Spread Operator (Expand)**

> Used in function calls or array definitions.
> "Take this bag of apples and spread them on the table."

### **1. Merging Arrays**
```javascript
const fruits = ["Apple", "Banana"];
const moreFruits = ["Cherry", ...fruits]; 
// Result: ["Cherry", "Apple", "Banana"]
```

### **2. Passing Arguments**
```javascript
const nums = [1, 2, 3];
Math.max(...nums); // Becomes Math.max(1, 2, 3)
```

---

## 🎒 **Rest Operator (Collect)**

> Used in function parameters.
> "Take all these loose items and put them into a BAG."

```javascript
function sum(...numbers) {
    // numbers is now an Array [1, 2, 3, 4]
    return numbers.reduce((a, b) => a + b);
}

sum(1, 2, 3, 4);
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Spread** = Outgoing (Unpacking) 📤
> - **Rest** = Incoming (Packing) 📥
> - Same symbol `...`, context decides the role.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: How do you copy an array using spread?
> > [!SUCCESS]- Answer
> > `const copy = [...original];`

> [!QUESTION] **Q2**: Can Rest parameters be used at the start of a function definition?
> > [!SUCCESS]- Answer
> > No. The Rest parameter must always be the **LAST** parameter. `function(a, ...rest)` is valid. `function(...rest, a)` is invalid.

> [!QUESTION] **Q3**: What happens if you use `...` on a string?
> > [!SUCCESS]- Answer
> > It spreads the string into characters: `[..."hello"]` becomes `['h', 'e', 'l', 'l', 'o']`.

> [!QUESTION] **Q4**: How do you merge two objects?
> > [!SUCCESS]- Answer
> > `const combined = { ...obj1, ...obj2 };`

> [!QUESTION] **Q5**: Is `Math.max(arr)` valid if arr is an array?
> > [!SUCCESS]- Answer
> > No, it returns NaN. You must spread it: `Math.max(...arr)`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
