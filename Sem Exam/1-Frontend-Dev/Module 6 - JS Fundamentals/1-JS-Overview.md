# 📜 JavaScript Overview & Execution

## 🎯 **What is JavaScript?**

> [!SUCCESS] **Definition**: A lightweight, interpreted programming language that powers the dynamic behavior of websites.
> It can update content, control multimedia, animate images, and much more.

---

## 🏃 **How JS Runs in the Browser**

1.  **HTML Parsing**: Browser reads HTML.
2.  **Script Tag**: Browser sees `<script src="app.js"></script>`.
3.  **Fetch & Execute**: Browser pauses HTML rendering, downloads JS, and runs it (unless `defer` or `async` is used).
4.  **V8 Engine**: Chrome uses the **V8 Engine** to compile JS into machine code.

---

## 🔗 **Adding JS to HTML**

### **1. Internal (Script Tag)**
```html
<script>
  console.log("Hello!");
</script>
```

### **2. External (Recommended)**
```html
<script src="script.js"></script>
```

> [!TIP] **Where to put it?**
> Put `<script>` at the **bottom of `<body>`** OR in `<head>` with the `defer` attribute.
> This ensures HTML loads BEFORE JavaScript runs.

```html
<head>
  <script src="script.js" defer></script> 
</head>
```
> **defer**: "Wait until HTML is done parsing, then run."

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **ECMAScript (ES)** = The Official Name/Standard 📘
> - **JavaScript (JS)** = The Implementation 🛠️
> - **V8** = The Engine (like a car engine) that drives Chrome 🏎️

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What tag is used to include JavaScript?
> > [!SUCCESS]- Answer
> > `<script>`

> [!QUESTION] **Q2**: Why put scripts at the bottom of the body?
> > [!SUCCESS]- Answer
> > To allow the HTML content to load and display first, preventing the user from seeing a blank white screen while a heavy script loads.

> [!QUESTION] **Q3**: What does the `defer` attribute do?
> > [!SUCCESS]- Answer
> > It tells the browser to download the script in the background but ONLY execute it after the HTML parsing is complete.

> [!QUESTION] **Q4**: Is JavaScript the same as Java?
> > [!SUCCESS]- Answer
> > **NO!** "Java is to JavaScript as Car is to Carpet". They are completely different languages.

> [!QUESTION] **Q5**: What is the Console?
> > [!SUCCESS]- Answer
> > A developer tool in the browser used to output messages (`console.log`) and debug errors.

---

Back to: [[Sem Exam/Frontend-Dev/Module 6 - JS Fundamentals/README|Module 6 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
