# 🧮 Math Object & Common Methods

## 🎯 **The Math Object**

> [!SUCCESS] **Definition**: A built-in object that has properties and methods for mathematical constants and functions.
> It's not a constructor (you can't write `new Math()`). Static usage only.

---

## 🔢 **Rounding Methods**

- `Math.round(4.6)`: Standard rounding (**5**).
- `Math.ceil(4.1)`: Round **UP** (**5**). "Ceiling" 🏠
- `Math.floor(4.9)`: Round **DOWN** (**4**). "Floor" ⬇️
- `Math.trunc(4.9)`: Removes decimal part (**4**).

---

## 🎲 **Random Numbers**

> `Math.random()` returns a float between **0 (inclusive)** and **1 (exclusive)**.
> e.g., 0.1234, 0.9999.

**Formula: Random Integer between min and max**
```javascript
// Random number between 1 and 10
const random = Math.floor(Math.random() * 10) + 1;
```

---

## 📏 **Other Useful Methods**

- `Math.max(1, 2, 3)`: Returns largest (**3**).
- `Math.min(1, 2, 3)`: Returns smallest (**1**).
- `Math.abs(-5)`: Absolute value (**5**).
- `Math.pow(2, 3)`: Power (**8**). (Same as `2**3`).
- `Math.sqrt(16)`: Square Root (**4**).
- `Math.PI`: Constant (**3.14159...**).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Ceil** = Ceiling (Up) ☝️
> - **Floor** = Floor (Down) 👇
> - **Random** = 0 to 0.999... (Never hits 1!)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What does `Math.floor(5.99)` return?
> > [!SUCCESS]- Answer
> > **5**. It always rounds down.

> [!QUESTION] **Q2**: How do you get the largest number from an array `arr`?
> > [!SUCCESS]- Answer
> > `Math.max(...arr)` using the spread operator.

> [!QUESTION] **Q3**: Does `Math.random()` ever return 1?
> > [!SUCCESS]- Answer
> > No. It is exclusive of 1.

> [!QUESTION] **Q4**: How to get the absolute (positive) version of a negative number?
> > [!SUCCESS]- Answer
> > `Math.abs(-10)`.

> [!QUESTION] **Q5**: What is the value of `Math.PI` roughly?
> > [!SUCCESS]- Answer
> > 3.14159...

---

Back to: [[Sem Exam/Frontend-Dev/Module 9 - JS Utilities/README|Module 9 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
