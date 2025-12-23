# 📝 ICP (Intro to Programming) - Important Topics Hub

> [!WARNING] **Exam Focus!** These are the important topics to cover for ICP exam!

> [!INFO] **Progress Tracker**
> 
> ```dataviewjs
> const tasks = dv.current().file.tasks;
> const completed = tasks.filter(t => t.completed).length;
> const total = tasks.length;
> const percent = total === 0 ? 0 : Math.round((completed / total) * 100);
> 
> dv.paragraph(`**Status:** ${completed}/${total} Topics Completed (**${percent}%**)`);
> dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease;"></div></div>`);
> ```

---

## 📋 Topics Checklist

### 0️⃣ Array Problems
- [ ] Second Largest Element (One Pass)
- [ ] Largest & Second Largest (Array Traversal)
→ [[0-Array-Problems|📖 Read Notes]]

---

### 1️⃣ OOPS Fundamentals
- [ ] Definition of OOP (Object-Oriented Programming)
- [ ] Advantages of OOPS
- [ ] OOPS vs Procedural Programming
→ [[1-OOPS-Fundamentals|📖 Read Notes]]

---

### 2️⃣ Classes and Objects
- [ ] Definition of Class & Object
- [ ] Class Variables vs Instance Variables
- [ ] Instance Methods & Constructor (__init__)
- [ ] self keyword
- [ ] Creating & Accessing Objects
→ [[2-Classes-Objects|📖 Read Notes]]

---

### 3️⃣ Four Pillars of OOPS
- [ ] Encapsulation (Data Hiding, Access Modifiers)
- [ ] Abstraction (Abstract Classes)
- [ ] Inheritance (Base & Derived Class)
- [ ] Polymorphism (Overloading & Overriding)
→ [[3-Four-Pillars-OOPS|📖 Read Notes]]

---

### 4️⃣ Types of Inheritance
- [ ] Single Inheritance
- [ ] Multiple Inheritance
- [ ] Multilevel Inheritance
- [ ] Hierarchical Inheritance
- [ ] Hybrid Inheritance
→ [[4-Types-of-Inheritance|📖 Read Notes]]

---

### 5️⃣ Constructors and Destructors
- [ ] Default Constructor
- [ ] Parameterized Constructor
- [ ] Constructor Overloading
- [ ] Destructor (__del__)
→ [[5-Constructors-Destructors|📖 Read Notes]]

---

### 6️⃣ File Handling
- [ ] Opening & Closing Files
- [ ] File Modes (r, w, a, r+, w+, a+)
- [ ] read(), readline(), readlines()
- [ ] write(), writelines()
→ [[6-File-Handling|📖 Read Notes]]

---

### 7️⃣ Exception Handling
- [ ] Errors vs Exceptions
- [ ] try, except, else, finally
- [ ] Multiple except blocks
- [ ] User-Defined Exceptions (raise)
→ [[7-Exception-Handling|📖 Read Notes]]

---

### 8️⃣ List
- [ ] List Basics (Mutable, Indexed)
- [ ] CRUD Operations
- [ ] Methods: append, insert, extend, remove, pop, sort, reverse
→ [[8-List|📖 Read Notes]]

---

### 9️⃣ Tuple
- [ ] Tuple Basics (Immutable)
- [ ] Packing & Unpacking
- [ ] Methods: count, index
→ [[9-Tuple|📖 Read Notes]]

---

### 🔟 Dictionary
- [ ] Key-Value Concept (Mutable)
- [ ] CRUD Operations
- [ ] Methods: keys, values, items, get, update, pop
→ [[10-Dictionary|📖 Read Notes]]

---

### 1️⃣1️⃣ Set
- [ ] Set Basics (Unique, Unordered)
- [ ] Set Operations (Union, Intersection, Difference)
- [ ] Methods: add, remove, discard, pop
→ [[11-Set|📖 Read Notes]]

---

## 🚀 Study Order (By Priority)

| Time | Topic | 
|------|-------|
| 25 min | 🔴 Four Pillars of OOPS |
| 20 min | 🔴 Classes and Objects |
| 15 min | 🔴 Exception Handling |
| 15 min | 🔴 File Handling |
| 20 min | 🟡 Types of Inheritance |
| 15 min | 🟡 List, Tuple, Dict, Set |
| 10 min | 🟢 Array Problems |

---

Good luck! 🍀
