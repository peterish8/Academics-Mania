# ✏️ Updating Text & HTML Content

## 🎯 **Modifying Content**

> [!SUCCESS] **Goal**: Change the text inside an element.

---

## 🆚 **The Big Three Properties**

### **1. `textContent` (Best for Text) 🌟**
> Returns/Sets the raw text. **Ignores all CSS styles** (shows hidden text).
> **Use Case**: Changing text safely (prevents XSS attacks). Fast & Efficient.

```javascript
element.textContent = "New <b>Text</b>"; 
// Result: "New <b>Text</b>" (Literal tags shown)
```

### **2. `innerHTML` (Best for HTML)**
> Parses HTML tags.
> **Use Case**: Adding bold text or simplified rendering.
> **Warning**: Dangerous if user input is used (Security risk). ⚠️

```javascript
element.innerHTML = "New <b>Text</b>";
// Result: "New Text" (Bolded)
```

### **3. `innerText` (Older)**
> "What the user sees". Aware of CSS styling (e.g., won't show hidden text).
> Slower (triggers reflow). Avoid if `textContent` works.

---

## 🎨 **Updating Styles**

> Access the `.style` object.
> **Note**: Properties use camelCase (e.g., `backgroundColor` not `background-color`).

```javascript
const box = document.querySelector('.box');
box.style.backgroundColor = "red";
box.style.fontSize = "20px";
```

### **Better Way: ClassList**
> Add/Remove classes instead of inline styles!

```javascript
box.classList.add('highlight');
box.classList.remove('hidden');
box.classList.toggle('active'); // On/Off switch
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Text** = Plain words 📝 (`textContent`)
> - **HTML** = Formatting allowed 🏗️ (`innerHTML`)
> - **Styles** = CamelCase 🐪 (`backgroundColor`)
> - **ClassList** = Cleaner CSS management 🧼

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What happens if you put `<script>` tags inside `innerHTML`?
> > [!SUCCESS]- Answer
> > Modern browsers usually block it, but it's the main vector for XSS (Cross-Site Scripting) attacks if used with `img onError` and other tricks. Always sanitize!

> [!QUESTION] **Q2**: Which property respects CSS `display: none` and returns empty string for hidden elements?
> > [!SUCCESS]- Answer
> > `innerText`. (`textContent` returns the text even if hidden).

> [!QUESTION] **Q3**: How do you toggle a class named "dark-mode" on the body?
> > [!SUCCESS]- Answer
> > `document.body.classList.toggle('dark-mode')`.

> [!QUESTION] **Q4**: How do you write `margin-left` in JavaScript style object?
> > [!SUCCESS]- Answer
> > `marginLeft` (camelCase).

> [!QUESTION] **Q5**: Why is `element.style.color = 'red'` often bad practice?
> > [!SUCCESS]- Answer
> > It adds an **inline style**, which has high specificity and is hard to maintain. It's better to add a CSS class.

---

Back to: [[Sem Exam/Frontend-Dev/Module 10 - DOM Events/README|Module 10 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
