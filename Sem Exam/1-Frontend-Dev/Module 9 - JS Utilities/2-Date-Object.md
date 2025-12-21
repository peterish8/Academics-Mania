# 📅 Date Object

## 🎯 **Working with Time**

> [!SUCCESS] **Definition**: Object to work with dates and times.
> Based on milliseconds since **Unix Epoch** (Jan 1, 1970).

---

## 🕰️ **Creating Dates**

```javascript
const now = new Date(); // Current date & time
const specific = new Date("2024-12-25"); // Specific string
const custom = new Date(2024, 11, 25); // Year, Month (0-11), Day
```
> [!WARNING] **The Month Trap**: Months are **0-indexed**!
> 0 = Jan, 11 = Dec.
> Days are 1-indexed. Wth JS? 🤷‍♂️

---

## 📥 **Getting Values (Getters)**

```javascript
const d = new Date();

d.getFullYear(); // 2024
d.getMonth();    // 0-11 (Current Month)
d.getDate();     // 1-31 (Day of Month)
d.getDay();      // 0-6 (Day of Week, 0=Sun)
d.getTime();     // Milliseconds since 1970 (Timestamp)
```

---

## 📤 **Setting Values (Setters)**

```javascript
d.setFullYear(2025);
d.setMonth(0); // January
```

---

## 🔦 **Displaying Dates**

```javascript
d.toDateString(); // "Wed Dec 25 2024"
d.toISOString();  // "2024-12-25T00:00:00.000Z" (Database standard)
d.toLocaleDateString(); // "12/25/2024" (Based on user PC)
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Months Lie**: 0 = January. 🤥
> - **Days Truth**: 1 = 1st of month.
> - **Weekdays**: 0 = Sunday (Sun starts the week).

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What number represents January in JavaScript dates?
> > [!SUCCESS]- Answer
> > **0**.

> [!QUESTION] **Q2**: What does `Date.now()` return?
> > [!SUCCESS]- Answer
> > The current timestamp in milliseconds since Jan 1, 1970.

> [!QUESTION] **Q3**: How do you create a date for Dec 25, 2024 using numbers?
> > [!SUCCESS]- Answer
> > `new Date(2024, 11, 25)`. Remember Month 11 is December!

> [!QUESTION] **Q4**: What day of the week is 0?
> > [!SUCCESS]- Answer
> > Sunday.

> [!QUESTION] **Q5**: Why use `toISOString()`?
> > [!SUCCESS]- Answer
> > It provides a standard, consistent format (YYYY-MM-DD...) useful for interacting with APIs and Databases.

---

Back to: [[Sem Exam/Frontend-Dev/Module 9 - JS Utilities/README|Module 9 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
