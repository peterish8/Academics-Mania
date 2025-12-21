# 🏗️ Dynamically Adding/Removing Elements

## 🎯 **Creating Content via JS**

> [!SUCCESS] **Goal**: Build HTML elements from scratch in JavaScript and put them on the page.
> Essential for To-Do lists, Feeds, etc.

---

## 🔨 **The 3-Step Process**

1.  **Create**: `document.createElement(tag)`
2.  **Modify**: Add text/classes.
3.  **Append**: Attach to a parent.

```javascript
// 1. Create
const newDiv = document.createElement('div');

// 2. Modify
newDiv.textContent = "I am new!";
newDiv.classList.add('box');

// 3. Append to Body (or any other container)
document.body.appendChild(newDiv);
```

---

## 🗑️ **Removing Elements**

- `element.remove()`: New & Easy.
- `parent.removeChild(child)`: Old school.

```javascript
newDiv.remove(); // Bye bye! 👋
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Create** = Make it in memory 🧠
> - **Append** = Put it on page 📄
> - **Remove** = Delete it 🗑️

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Does `createElement` automatically show the element on the screen?
> > [!SUCCESS]- Answer
> > No. It only creates it in memory. You must `appendChild` or `append` it to the DOM to make it visible.

> [!QUESTION] **Q2**: What is the difference between `appendChild` and `append`?
> > [!SUCCESS]- Answer
> > `appendChild` takes only one NODE. `append` can take multiple Nodes AND text strings (`Parent.append(div, "text")`).

> [!QUESTION] **Q3**: How do you remove an element named `box`?
> > [!SUCCESS]- Answer
> > `box.remove()`

> [!QUESTION] **Q4**: Can you move an existing element by appending it elsewhere?
> > [!SUCCESS]- Answer
> > Yes! An element can only exist in one place. If you `appendChild` an element that is already on the page, it gets **moved** to the new spot.

> [!QUESTION] **Q5**: How do create a `<li>` tag?
> > [!SUCCESS]- Answer
> > `document.createElement('li')`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 10 - DOM Events/README|Module 10 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
