# 🎨 Frontend Study Hub

> [!INFO] **Exam Preparation Hub**
> **Master Progress Tracker**
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

## 📝 **Sample Papers**
- [x] [[Sample Paper/FDB-Model-Paper|FDB Model Paper (Solved)]] 🎓
- [x] [[Sample Paper/samplepaper-2|Sample Paper 2 (Solved)]] 🎓
- [x] [[Sample Paper/FDB-Revision-Notes|⚡ Last-Minute Revision Notes]] 🚀

---

---

## 📚 **Checklist**

### **Module 1: HTML Essentials** 🏗️
- [x] [[Module 1 - HTML Essentials/README|Module Overview]]
- [x] [[Module 1 - HTML Essentials/1-HTML-Document-Structure|1. Doctype & Structure]]
- [x] [[Module 1 - HTML Essentials/2-Text-Elements|2. Headings & Paragraphs]]
- [x] [[Module 1 - HTML Essentials/3-Lists-Tables|3. Lists & Tables]]
- [x] [[Module 1 - HTML Essentials/4-Forms-Inputs|4. Forms & Input Types]]
- [x] [[Module 1 - HTML Essentials/5-Anchor-Navigation|5. Links & Navigation]]
- [x] [[Module 1 - HTML Essentials/6-Semantic-Elements|6. Semantic HTML]]
- [x] [[Module 1 - HTML Essentials/7-Meta-Tags-SEO|7. Meta Tags & SEO]]
- [x] [[Module 1 - HTML Essentials/8-Chrome-DevTools|8. Using Chrome DevTools]]

### **Module 2: CSS Foundations** 🎨
- [x] [[Module 2 - CSS Foundations/README|Module Overview]]
- [x] [[Module 2 - CSS Foundations/1-CSS-Syntax-Apply|1. Syntax & Include Methods]]
- [x] [[Module 2 - CSS Foundations/2-Selectors|2. Basic Selectors]]
- [x] [[Module 2 - CSS Foundations/3-Box-Model|3. The Box Model]]
- [x] [[Module 2 - CSS Foundations/4-Colors-Typography|4. Colors & Fonts]]
- [x] [[Module 2 - CSS Foundations/5-CSS-Variables|5. Variables (Custom Props)]]
- [ ] [[Module 2 - CSS Foundations/6-Pseudo-Classes-Elements|6. Pseudo-classes & Elements]]
- [ ] [[Module 2 - CSS Foundations/7-Specificity-Inheritance|7. Specificity & Inheritance]]
- [ ] [[Module 2 - CSS Foundations/8-CSS-Positioning|8. Positioning (Relative/Abs/Fixed)]]
- [ ] [[Module 2 - CSS Foundations/9-Advanced-Selectors|9. Combinators & Attr Selectors]]

### **Module 3: CSS Layout** 📐
- [x] [[Module 3 - CSS Layout/README|Module Overview]]
- [ ] [[Module 3 - CSS Layout/1-Flexbox|1. Flexbox System]]
- [ ] [[Module 3 - CSS Layout/2-CSS-Grid|2. CSS Grid]]

### **Module 4: Responsive Design** 📱
- [ ] [[Module 4 - Responsive Design/README|Module Overview]]
- [ ] [[Module 4 - Responsive Design/1-Responsive-Units|1. Units (rem, vh, vw)]]
- [x] [[Module 4 - Responsive Design/2-Media-Queries|2. Media Queries]]
- [ ] [[Module 4 - Responsive Design/3-Fluid-Layouts|3. Fluid Layouts & Images]]
- [ ] [[Module 4 - Responsive Design/4-Mobile-First|4. Mobile-First Strategy]]
- [ ] [[Module 4 - Responsive Design/5-Responsive-Navigation|5. Hamburger Menu Logic]]

### **Module 5: CSS Animations** ✨
- [ ] [[Module 5 - CSS Animations/README|Module Overview]]
- [ ] [[Module 5 - CSS Animations/1-Transitions|1. Transitions]]
- [x] [[Module 5 - CSS Animations/2-Keyframes|2. @keyframes Animations]]
- [ ] [[Module 5 - CSS Animations/3-UI-Animations|3. UI Micro-interactions]]

### **Module 6: JS Fundamentals** 📜
- [x] [[Module 6 - JS Fundamentals/README|Module Overview]]
- [x] [[Module 6 - JS Fundamentals/1-JS-Overview|1. Execution & Script Tags]]
- [x] [[Module 6 - JS Fundamentals/2-Variables|2. var vs let vs const]]
- [x] [[Module 6 - JS Fundamentals/3-Data-Types|3. Primitives vs References]]
- [x] [[Module 6 - JS Fundamentals/4-Strings-Template-Literals|4. String Methods]]
- [x] [[Module 6 - JS Fundamentals/5-Operators|5. Operators (== vs ===)]]
- [x] [[Module 6 - JS Fundamentals/6-Conditionals|6. If/Else & Switch]]
- [x] [[Module 6 - JS Fundamentals/7-Loops|7. Loops (For, While, For..of)]]

### **Module 7: Arrays & Objects** 📦
- [x] [[Module 7 - Arrays Objects Functions/README|Module Overview]]
- [x] [[Module 7 - Arrays Objects Functions/1-Arrays|1. Array Methods (Push/Pop/Slice)]]
- [x] [[Module 7 - Arrays Objects Functions/2-Functions|2. Arrow Functions]]
- [x] [[Module 7 - Arrays Objects Functions/3-Rest-Spread|3. Rest & Spread Operators]]
- [x] [[Module 7 - Arrays Objects Functions/4-Objects|4. Object Properties & Methods]]
- [x] [[Module 7 - Arrays Objects Functions/5-Object-Creation|5. Factory vs Constructors]]
- [x] [[Module 7 - Arrays Objects Functions/6-Value-Reference|6. Pass by Value vs Reference]]
- [x] [[Module 7 - Arrays Objects Functions/7-Copy-JSON|7. Deep vs Shallow Copy]]

### **Module 8: Higher-Order Functions** 🧠
- [x] [[Module 8 - HOF Callbacks/README|Module Overview]]
- [x] [[Module 8 - HOF Callbacks/1-Callbacks|1. Callback Concept]]
- [x] [[Module 8 - HOF Callbacks/2-Higher-Order-Functions|2. Understanding HOFs]]
- [x] [[Module 8 - HOF Callbacks/3-Built-in-HOF|3. map, filter, reduce]]

### **Module 9: JS Utilities** 🛠️
- [x] [[Module 9 - JS Utilities/README|Module Overview]]
- [x] [[Module 9 - JS Utilities/1-Math-Object|1. Math Object]]
- [x] [[Module 9 - JS Utilities/2-Date-Object|2. Date Object]]

### **Module 10: DOM & Events** 🖱️
- [x] [[Module 10 - DOM Events/README|Module Overview]]
- [x] [[Module 10 - DOM Events/1-DOM-Structure|1. DOM Tree Structure]]
- [x] [[Module 10 - DOM Events/2-Selecting-Elements|2. QuerySelectors]]
- [x] [[Module 10 - DOM Events/3-Updating-Content|3. innerHTML vs textContent]]
- [x] [[Module 10 - DOM Events/4-Event-Listeners|4. Event Listeners]]
- [x] [[Module 10 - DOM Events/5-Dynamic-Elements|5. Creating Elements (Append)]]
- [x] [[Module 10 - DOM Events/6-Form-Validation|6. Live Form Validation]]
- [x] [[Module 10 - DOM Events/7-Timers|7. Timers (SetTimeout)]]

### **Module 11: Modern JS Concepts** 🚀
- [x] [[Module 11 - Modern JS/README|Module Overview]]
- [x] [[Module 11 - Modern JS/1-Execution-Context|1. Call Stack & Context]]
- [x] [[Module 11 - Modern JS/2-Hoisting|2. Hoisting]]
- [x] [[Module 11 - Modern JS/3-Scope|3. Scope (Block/Global)]]
- [x] [[Module 11 - Modern JS/4-Closures|4. Closures]]
- [x] [[Module 11 - Modern JS/5-Event-Propagation|5. Bubbling & Capturing]]
- [x] [[Module 11 - Modern JS/6-Callback-Hell|6. Async Problems]]

### **Module 12: Async JavaScript** ⏳
- [x] [[Sem Exam/1-Frontend-Dev/Module 12 - Async JS/README|Module Overview]]
- [x] [[1-Sync-Async|1. Sync vs Async]]
- [x] [[2-Event-Loop|2. Event Loop]]
- [x] [[3-Promises|3. Promises]]
- [x] [[4-Async-Await|4. Async/Await]]
- [x] [[5-Error-Handling|5. Try/Catch]]
- [x] [[6-API-Requests|6. Fetch API]]

---
> [[../Sem-Exam-Hub|Back to Main Master Hub]]
