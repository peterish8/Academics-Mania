# 📢 Event Propagation (Bubbling & Capturing)

## 🎯 **What is Propagation?**

> [!SUCCESS] **Concept**: When you click an element (like a button), you are ALSO clicking its parent (div), and the body, and the html tag.
> Propagation is the order in which these events fire. 🌊

---

## 🫧 **1. Bubbling (Default)**

> Events start at the **Target** and bubble **UP** to ancestors.
> `Button` → `Div` → `Body` → `HTML`

```javascript
div.addEventListener('click', () => console.log('Div clicked'));
btn.addEventListener('click', () => console.log('Btn clicked'));

// Click Button output:
// "Btn clicked"
// "Div clicked" (Bubbled up!)
```

---

## 🥅 **2. Capturing (Trickling)**

> Events start at the **Top** and go **DOWN** to target.
> `HTML` → `Body` → `Div` → `Button`
> Usually disabled by default. Enable with `{capture: true}`.

---

## 🛑 **Stopping Propagation**

> "Don't tell my parents!" 🤫
> Prevents the event from reaching ancestors.

```javascript
btn.addEventListener('click', (e) => {
    e.stopPropagation(); // Stop bubbling!
    console.log("Only Button clicked");
});
```

---

## ⚡ **Event Delegation**

> [!TIP] **Pro Pattern**: Instead of adding 100 listeners to 100 buttons, add **1 listener** to the parent container and check `e.target`.

```javascript
/* HTML: <ul id="list"> <li>A</li> <li>B</li> </ul> */

document.getElementById('list').addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        console.log("List item clicked:", e.target.textContent);
    }
});
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Bubbling** = Bubbles go UP 🧼 (Default).
> - **Capturing** = Falling DOWN ⤵️.
> - **Delegation** = Manager handles complaints for all employees 👔.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the default propagation phase in browsers?
> > [!SUCCESS]- Answer
> > **Bubbling**.

> [!QUESTION] **Q2**: Which method stops the event from bubbling up?
> > [!SUCCESS]- Answer
> > `e.stopPropagation()`.

> [!QUESTION] **Q3**: What is `e.target` vs `e.currentTarget`?
> > [!SUCCESS]- Answer
> > `e.target` is the element that was actually CLICKED. `e.currentTarget` is the element that owns the event listener (the one currently handling it).

> [!QUESTION] **Q4**: Why is Event Delegation better for performance?
> > [!SUCCESS]- Answer
> > It uses fewer event listeners (less memory) and handles dynamically added elements automatically.

> [!QUESTION] **Q5**: How do you enable Capturing phase?
> > [!SUCCESS]- Answer
> > Pass `true` or `{capture: true}` as the third argument to `addEventListener`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 11 - Modern JS/README|Module 11 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
