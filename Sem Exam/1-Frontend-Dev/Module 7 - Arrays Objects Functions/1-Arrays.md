# 📦 Arrays & Common Methods

## 🎯 **What is an Array?**

> [!SUCCESS] **Definition**: An ordered list of values (can be mixed types).
> Zero-indexed (First item is 0).

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // Apple
```

---

## 🛠️ **Adding & Removing Items**

> [!TIP] **Stack & Queue methods**

1.  **push()**: Add to **End**. `arr.push('Mango')`
2.  **pop()**: Remove from **End**. `arr.pop()`
3.  **unshift()**: Add to **Start**. `arr.unshift('Grape')`
4.  **shift()**: Remove from **Start**. `arr.shift()`

---

## ✂️ **Modifying Arrays**

### **1. slice(start, end)**
> **Does NOT modify** original. Returns a copy of a portion.
> "Slice a piece of cake 🍰" (Original cake stays).

```javascript
let nums = [0, 1, 2, 3, 4];
let part = nums.slice(1, 3); // [1, 2] (End index is exclusive)
```

### **2. splice(start, count, items...)**
> **Modifies** original. Removes or replaces items.
> "Splice the wire 🔌" (Cuts the original).

```javascript
let nums = [0, 1, 2, 3];
nums.splice(1, 2); // Removes 2 items starting at index 1
// Result: [0, 3]
```

---

## 🔍 **Searching**

- `indexOf(value)`: Returns index or -1.
- `includes(value)`: Returns true/false.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Push/Pop** = End 🔚
> - **Shift/Unshift** = Start 🏁
> - **Slice** = Safe (Copy) 🍕
> - **Splice** = Surgery (Modifies) 🔪

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What method removes the last element of an array?
> > [!SUCCESS]- Answer
> > `pop()`

> [!QUESTION] **Q2**: What does `slice(1, 4)` return?
> > [!SUCCESS]- Answer
> > Elements from index 1 up to (but NOT including) index 4.

> [!QUESTION] **Q3**: Does `splice` modify the original array?
> > [!SUCCESS]- Answer
> > Yes, it is destructive.

> [!QUESTION] **Q4**: How do you add an element to the BEGINNING of an array?
> > [!SUCCESS]- Answer
> > `unshift(element)`

> [!QUESTION] **Q5**: What does `includes` return?
> > [!SUCCESS]- Answer
> > A boolean (`true` or `false`).

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
