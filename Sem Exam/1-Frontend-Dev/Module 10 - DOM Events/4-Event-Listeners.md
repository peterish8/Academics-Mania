# 👂 Event Listeners

## 🎯 **Listening for Actions**

> [!SUCCESS] **Definition**: Waiting for the user to do something (Click, Type, Submit).
> "When X happens, Run Y."

---

## 🎧 **addEventListener**

> The standard way to attach events.
> `element.addEventListener(event, callback)`

```javascript
const btn = document.querySelector('button');

btn.addEventListener('click', () => {
    console.log("Button clicked!");
});
```

---

## 🖱️ **Common Events**

- **Mouse**: `click`, `dblclick`, `mouseenter`, `mouseleave`.
- **Keyboard**: `keydown`, `keyup`, `keypress`.
- **Form**: `submit`, `input`, `change`.
- **Window**: `resize`, `scroll`, `load`.

---

## 🧠 **The Event Object (`e`)**

> The callback function receives an argument describing *what happened*.

```javascript
btn.addEventListener('click', (e) => {
    console.log(e.target); // The element clicked
    console.log(e.type);   // "click"
});
```

### **Prevent Default**
> Stops the browser's normal behavior (e.g., stopping a form from reloading the page).

```javascript
form.addEventListener('submit', (e) => {
    e.preventDefault(); // Stop reload! 🛑
    console.log("Form submitted!");
});
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **add...** = Subscribe 📨
> - **e** = The Receipt (Details of the event) 🧾
> - **preventDefault** = Stop! 🛑 (Essential for SPA logic)

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What method attaches an event handler?
> > [!SUCCESS]- Answer
> > `addEventListener()`.

> [!QUESTION] **Q2**: Why do we need `e.preventDefault()` on form submissions?
> > [!SUCCESS]- Answer
> > Because by default, forms send data to a server and **reload the page**. In modern JS apps, we want to handle data via JS without reloading.

> [!QUESTION] **Q3**: Which event fires every time you type a character in an input field?
> > [!SUCCESS]- Answer
> > The **`input`** event fires every time the value of an input field changes, such as on each key press, paste, or delete.  
The **`change`** event fires only when the user finishes typing and **moves out of the input field by clicking outside or pressing the Tab key**.

> [!QUESTION] **Q4**: How do you detect which key was pressed?
> > [!SUCCESS]- Answer
> > Use the event object: `e.key` (e.g., "Enter") or `e.code` (e.g., "KeyA").

> [!QUESTION] **Q5**: Can you remove an event listener?
> > [!SUCCESS]- Answer
> > Yes, using `removeEventListener(type, functionName)`. Note: You must pass the SAME named function (not an anonymous arrow function) to remove it.

---

Back to: [[Sem Exam/Frontend-Dev/Module 10 - DOM Events/README|Module 10 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
