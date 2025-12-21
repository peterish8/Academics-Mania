# 🔗 Links & Forms - My Style Notes

## 🎯 **What are Links?**

> [!INFO] **Definition**: Anchor tags create clickable connections
> The **highways** of the internet! 🛣️

**📍 Key Points:**
- Use `<a>` tag with `href` attribute
- Can link to pages, emails, phones, sections
- Different states: unvisited (blue), visited (purple), active (red)
- Essential for website navigation

**🎯 Use Cases:**
- Navigate between pages
- Link to external websites
- Create email/phone links
- Jump to page sections

---

## 🌐 **Link Types**

### **🔗 Basic Links**

> [!INFO] **Definition**: Connect to other web pages or websites

**📍 Key Points:**
- `href` = destination URL
- `target="_blank"` = open in new tab
- `title` = tooltip on hover

**🎨 Visual:**
```
<a href="https://google.com">Visit Google</a>
   ↑                          ↑
destination               link text
```

**🎯 Use Cases:**
```html
<!-- Internal page -->
<a href="about.html">About Us</a>

<!-- External site -->
<a href="https://github.com" target="_blank">GitHub</a>

<!-- With tooltip -->
<a href="contact.html" title="Get in touch">Contact</a>
```

---

### **📧 Communication Links**

> [!INFO] **Definition**: Direct links to email and phone actions

**📍 Key Points:**
- `mailto:` opens email client
- `tel:` opens phone dialer
- Automatically formatted by browser

**🎨 Visual:**
```
mailto:john@example.com → Opens email to john@example.com
tel:+1234567890        → Opens phone dialer
```

**🎯 Use Cases:**
```html
<!-- Email link -->
<a href="mailto:hello@company.com">📧 Email Us</a>

<!-- Phone link -->
<a href="tel:+1-234-567-8900">📞 Call Now</a>

<!-- Email with subject -->
<a href="mailto:support@site.com?subject=Help">Get Support</a>
```

---

### **🎯 Internal Navigation**

> [!INFO] **Definition**: Jump to sections within the same page

**📍 Key Points:**
- Use `#` followed by element ID
- Target element needs `id` attribute
- Smooth scrolling to section

**🎨 Visual:**
```
<a href="#section1">Go to Section 1</a>
           ↑
    Links to element with id="section1"

<h2 id="section1">Section 1</h2>
        ↑
    Target destination
```

**🎯 Use Cases:**
```html
<!-- Navigation menu -->
<nav>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
</nav>

<!-- Target sections -->
<section id="home">...</section>
<section id="about">...</section>
<section id="contact">...</section>
```

---

## 📝 **What are Forms?**

> [!INFO] **Definition**: Collect user input and send data to servers
> The **conversation starters** of the web! 💬

**📍 Key Points:**
- Use `<form>` container with `action` and `method`
- Various input types for different data
- Essential for user interaction
- Foundation of web applications

**🎯 Use Cases:**
- User registration/login
- Contact forms
- Surveys and feedback
- Search functionality
- E-commerce checkout

---

## 🏗️ **Form Structure**

> [!INFO] **Definition**: Forms need container and input elements

**📍 Key Points:**
- `<form>` wraps all inputs
- `action` = where data goes
- `method` = how data is sent (GET/POST)
- Each input needs `name` attribute

**🎨 Visual:**
```
<form action="#" method="post">
  ↑       ↑         ↑
container destination method
  
  <input type="text" name="username">
         ↑           ↑
    input type   data name
</form>
```

**🎯 Use Cases:**
```html
<form action="/submit" method="post">
    <!-- All form inputs go here -->
    <button type="submit">Submit</button>
</form>
```

---

## 🎨 **Input Types**

### **📝 Text Inputs**

> [!INFO] **Definition**: Collect text-based information from users

**📍 Key Types:**
- `text` - general text input
- `email` - email validation
- `password` - hidden text
- `search` - search queries

**🎨 Visual:**
```
type="text"     → [John Doe        ]
type="email"    → [user@email.com  ] ✓ validation
type="password" → [••••••••••      ] hidden
type="search"   → [🔍 Search...    ] with icon
```

**🎯 Use Cases:**
```html
<input type="text" placeholder="Your name">
<input type="email" placeholder="your@email.com" required>
<input type="password" placeholder="Password">
<input type="search" placeholder="Search products...">
```

---

### **🔢 Number & Date Inputs**

> [!INFO] **Definition**: Collect numeric and date information with validation

**📍 Key Types:**
- `number` - numeric input with min/max
- `range` - slider input
- `date` - date picker
- `time` - time picker

**🎨 Visual:**
```
type="number"  → [25    ] ↑↓ spinners
type="range"   → ●━━━━━━━━━━ slider
type="date"    → [📅 2024-01-15] picker
type="time"    → [🕐 14:30     ] picker
```

**🎯 Use Cases:**
```html
<input type="number" min="1" max="100" placeholder="Age">
<input type="range" min="0" max="10" value="5">
<input type="date" name="birthday">
<input type="time" name="appointment">
```

---

### **🎯 Selection Inputs**

> [!INFO] **Definition**: Let users choose from predefined options

**📍 Key Types:**
- `radio` - choose one from group
- `checkbox` - choose multiple
- `select` - dropdown menu

**🎨 Visual:**
```
Radio:    ◉ Option 1  ○ Option 2  (choose one)
Checkbox: ☑ Option A  ☑ Option B  (choose multiple)
Select:   [Choose... ▼] dropdown
```

**🎯 Use Cases:**
```html
<!-- Radio buttons (same name = group) -->
<input type="radio" name="size" value="small" id="small">
<label for="small">Small</label>

<input type="radio" name="size" value="large" id="large">
<label for="large">Large</label>

<!-- Checkboxes (independent) -->
<input type="checkbox" id="newsletter" value="yes">
<label for="newsletter">Subscribe to newsletter</label>

<!-- Dropdown -->
<select name="country">
    <option value="">Choose country</option>
    <option value="usa">🇺🇸 USA</option>
    <option value="india">🇮🇳 India</option>
</select>
```

---

### **📄 Text Area & Buttons**

> [!INFO] **Definition**: Multi-line text and form actions

**📍 Key Elements:**
- `<textarea>` - multi-line text input
- `<button>` - clickable actions
- `type="submit"` - send form data
- `type="reset"` - clear form

**🎨 Visual:**
```
<textarea>     → ┌─────────────────┐
                 │ Multi-line text │
                 │ input area...   │
                 └─────────────────┘

<button>       → [  Submit Form  ] clickable
```

**🎯 Use Cases:**
```html
<textarea rows="4" cols="50" placeholder="Your message..."></textarea>

<button type="submit">Send Message</button>
<button type="reset">Clear Form</button>
<button type="button" onclick="doSomething()">Click Me</button>
```

---

## 🎨 **Real Examples**

### **📧 Contact Form**
```html
<form action="/contact" method="post">
    <h2>📞 Contact Us</h2>
    
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="subject">Subject:</label>
    <select id="subject" name="subject">
        <option value="">Choose topic</option>
        <option value="support">🛠️ Support</option>
        <option value="sales">💰 Sales</option>
        <option value="general">💬 General</option>
    </select>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4" required></textarea>
    
    <button type="submit">Send Message</button>
</form>
```

### **🎮 Survey Form**
```html
<form action="/survey" method="post">
    <h2>🎮 Gaming Survey</h2>
    
    <fieldset>
        <legend>Favorite game type:</legend>
        <input type="radio" name="game" value="action" id="action">
        <label for="action">🎯 Action</label>
        
        <input type="radio" name="game" value="puzzle" id="puzzle">
        <label for="puzzle">🧩 Puzzle</label>
    </fieldset>
    
    <fieldset>
        <legend>Platforms you own:</legend>
        <input type="checkbox" id="pc" name="platforms" value="pc">
        <label for="pc">💻 PC</label>
        
        <input type="checkbox" id="console" name="platforms" value="console">
        <label for="console">🎮 Console</label>
    </fieldset>
    
    <label for="hours">Hours per week:</label>
    <input type="range" id="hours" name="hours" min="0" max="40" value="10">
    
    <button type="submit">Submit Survey</button>
</form>
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Link Types** 🔗
> - **href** = **H**yperlink **REF**erence
> - **mailto:** = **MAIL TO** someone
> - **tel:** = **TEL**ephone number
> - **#section** = **#** jumps to ID

> [!TIP] **Form Elements** 📝
> - **input** = Single-line data
> - **textarea** = Multi-line text
> - **select** = Dropdown choices
> - **radio** = Pick **one** only (like radio stations)
> - **checkbox** = Pick **multiple** (check all that apply)

> [!SUCCESS] **Form Structure** 🏗️
> ```
> <form>           ← Container
>   <label>        ← Description
>   <input>        ← User input
>   <button>       ← Submit action
> </form>
> ```

Back to: [[README of HTML]]