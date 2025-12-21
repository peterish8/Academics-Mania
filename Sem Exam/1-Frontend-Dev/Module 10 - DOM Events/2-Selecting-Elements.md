# 🎯 Selecting Elements

## 🎯 **Finding Elements**

> [!SUCCESS] **Goal**: Before you can change an element, you must find it in the DOM.

---

## 🏗️ **The Modern Way (Query Selectors)**

> Uses CSS syntax! (`.class`, `#id`, `tag`). **Recommended**. 🌟

### **1. `querySelector(selector)`**
> Returns the **FISRT** match only.

```javascript
const btn = document.querySelector('.btn'); // First button with class .btn
```

### **2. `querySelectorAll(selector)`**
> Returns **ALL** matches as a NodeList (Array-like).

```javascript
const allBtns = document.querySelectorAll('.btn');
allBtns.forEach(btn => console.log(btn));
```

---

## 🏛️ **The Old Way (Specific Methods)**

> Faster performance, but less flexible syntax.

- `getElementById('id')`: Returns one element. (No `#` needed).
- `getElementsByClassName('class')`: Returns HTMLCollection (Live list!).
- `getElementsByTagName('tag')`: Returns HTMLCollection.

```javascript
const title = document.getElementById('main-title');
```

---

## 🆚 **NodeList vs HTMLCollection**

- **NodeList** (`querySelectorAll`): Static (snapshot). Has `.forEach()`.
- **HTMLCollection** (`getElementsBy...`): Live (updates auto). No `.forEach()` (must convert to Array).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **querySelector** = Just like CSS 🎨 (Easy!)
> - **All** = List 📋 (Needs a loop)
> - **Id** = Unique ☝️ (Element, singular)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Can you use `.forEach` on the result of `getElementsByClassName`?
> > [!SUCCESS]- Answer
> > No! It returns an HTMLCollection. You must convert it `Array.from()` or spread `[...]` first. `querySelectorAll` DOES supportforEach.

> [!QUESTION] **Q2**: Which selector method uses CSS syntax like `.class` or `#id`?
> > [!SUCCESS]- Answer
> > `querySelector` and `querySelectorAll`.

> [!QUESTION] **Q3**: If `querySelector` finds multiple matches, which one is returned?
> > [!SUCCESS]- Answer
> > Only the **first** one found in the document order.

> [!QUESTION] **Q4**: Does `getElementById` need the hash symbol `#`?
> > [!SUCCESS]- Answer
> > No. You just pass the ID string name. `getElementById("title")`.

> [!QUESTION] **Q5**: What is returned if `querySelector` finds nothing?
> > [!SUCCESS]- Answer
> > `null`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 10 - DOM Events/README|Module 10 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
