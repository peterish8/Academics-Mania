# 🔗 Value vs Reference

## 🎯 **The Concept**

> [!SUCCESS] **Analogy**:
> **Value**: I give you a **Photocopy** of my notes. If you draw on it, my notes stay clean. 📄
> **Reference**: I give you the **Google Doc Link** to my notes. If you edit it, my notes change too! 🔗

---

## 🧱 **Passed by Value (Primitives)**

> Strings, Numbers, Booleans.
> Stored in Stack. Completely independent copies.

```javascript
let a = 10;
let b = a;
b = 20;

console.log(a); // 10 (Safe!)
```

---

## 🔗 **Passed by Reference (Objects/Arrays)**

> Objects, Arrays.
> Stored in Heap. Variables hold the **Address**, not the data.

```javascript
let arr1 = [1, 2];
let arr2 = arr1; // Copies pointer, NOT data!

arr2.push(3);

console.log(arr1); // [1, 2, 3] (Changed! 😱)
```

---

## ⚖️ **Comparing References**

> Objects are only equal if they are the SAME instance.

```javascript
const obj1 = { val: 1 };
const obj2 = { val: 1 };

console.log(obj1 === obj2); // FALSE! (Different memory addresses)
console.log(obj1 === obj1); // TRUE
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Primitives** = Safe Copies.
> - **Objects** = Shared Links.
> - **Equality** checks the Address, not the Content!

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Do arrays compare by value or reference?
> > [!SUCCESS]- Answer
> > Reference. `[1] === [1]` is false because they are two different arrays in memory.

> [!QUESTION] **Q2**: If I pass an object into a function and modify it, does the original object change?
> > [!SUCCESS]- Answer
> > Yes! Because you passed the reference (address).

> [!QUESTION] **Q3**: How can you check if two objects contain the same data?
> > [!SUCCESS]- Answer
> > You have to manually compare their properties or convert to JSON string: `JSON.stringify(a) === JSON.stringify(b)`.

> [!QUESTION] **Q4**: Are variables holding objects actually holding the object data?
> > [!SUCCESS]- Answer
> > No, they hold a **Pointer** (memory address) to where the data is stored in the Heap.

> [!QUESTION] **Q5**: Is `null` a reference type?
> > [!SUCCESS]- Answer
> > No, it's a primitive.

---

Back to: [[Sem Exam/Frontend-Dev/Module 7 - Arrays Objects Functions/README|Module 7 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
