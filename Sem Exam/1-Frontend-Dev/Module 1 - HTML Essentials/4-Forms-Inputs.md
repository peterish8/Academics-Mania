# 📝 Forms & Input Types

## 🎯 **What are Forms?**

> [!SUCCESS] **Definition**: HTML elements to collect user input and send data to servers
> The **conversation starters** of the web! 💬

**📍 Key Points:**
- Forms enable two-way communication with users
- Can collect text, selections, files, etc.
- Essential for login, registration, search, checkout
- Data sent via HTTP (GET/POST) to servers

---

## 🏗️ **Form Structure**

> [!INFO] **Definition**: Forms need a container and input elements

**📍 Key Attributes:**
- `action` = Where data is sent (URL)
- `method` = How data is sent (GET/POST)
- `enctype` = Encoding type (for file uploads)

**🎨 Visual:**
```html
<form action="/submit" method="post">
  │        │              │
  │        │              └── HOW to send (POST = hidden)
  │        └───────────────── WHERE to send
  └────────────────────────── Form container
  
    <input type="text" name="username">
           │                 │
           │                 └── Data identifier
           └───────────────────── Input type
</form>
```

**🎯 Use Cases:**
```html
<!-- Basic form -->
<form action="/login" method="post">
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>

<!-- File upload form -->
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="document">
    <button type="submit">Upload</button>
</form>
```

---

## 📝 **Text Input Types**

> [!INFO] **Definition**: Various input types for collecting text data

### **Basic Text Inputs:**

| Type | Purpose | Validation |
|------|---------|------------|
| `text` | General text | None |
| `email` | Email address | Checks @ symbol |
| `password` | Hidden text | None (just hides) |
| `search` | Search queries | Adds search styling |
| `url` | Website URLs | Checks URL format |
| `tel` | Phone numbers | None (varies by country) |

**🎯 Examples:**
```html
<!-- Text input -->
<input type="text" name="fullname" placeholder="Your name">

<!-- Email with validation -->
<input type="email" name="email" placeholder="user@email.com" required>

<!-- Password (hidden) -->
<input type="password" name="password" placeholder="Enter password">

<!-- Search box -->
<input type="search" name="query" placeholder="Search...">

<!-- URL field -->
<input type="url" name="website" placeholder="https://example.com">

<!-- Phone number -->
<input type="tel" name="phone" placeholder="+1-234-567-8900">
```

---

## 🔢 **Number & Range Inputs**

> [!INFO] **Definition**: Inputs for numeric values with validation

**🎨 Visual:**
```
type="number"  → [25    ] ↑↓   ← spinners
type="range"   → ●━━━━━━━━━━    ← slider
```

**🎯 Examples:**
```html
<!-- Number with min/max -->
<input type="number" name="age" min="1" max="120" step="1">

<!-- Number with step -->
<input type="number" name="price" min="0" step="0.01">

<!-- Range slider -->
<input type="range" name="volume" min="0" max="100" value="50">

<!-- With output display -->
<input type="range" id="slider" min="0" max="100" value="50" 
       oninput="output.value = this.value">
<output id="output">50</output>
```

**📍 Key Attributes:**
| Attribute | Purpose |
|-----------|---------|
| `min` | Minimum allowed value |
| `max` | Maximum allowed value |
| `step` | Increment amount |
| `value` | Default value |

---

## 📅 **Date & Time Inputs**

> [!INFO] **Definition**: Native date/time pickers (browser provides UI)

**🎨 Visual:**
```
type="date"           → [📅 2024-01-15     ]
type="time"           → [🕐 14:30          ]
type="datetime-local" → [📅 2024-01-15 14:30]
type="month"          → [📅 January 2024   ]
type="week"           → [📅 Week 3, 2024   ]
```

**🎯 Examples:**
```html
<!-- Date picker -->
<input type="date" name="birthday" min="1900-01-01" max="2024-12-31">

<!-- Time picker -->
<input type="time" name="appointment">

<!-- Date and time -->
<input type="datetime-local" name="event">

<!-- Month selector -->
<input type="month" name="cardExpiry">

<!-- Week selector -->
<input type="week" name="deliveryWeek">
```

---

## ✅ **Selection Inputs**

> [!INFO] **Definition**: Let users choose from predefined options

### **Radio Buttons (Choose ONE):**
```html
<!-- Same 'name' = same group -->
<input type="radio" name="size" value="small" id="small">
<label for="small">Small</label>

<input type="radio" name="size" value="medium" id="medium" checked>
<label for="medium">Medium</label>

<input type="radio" name="size" value="large" id="large">
<label for="large">Large</label>
```

### **Checkboxes (Choose MULTIPLE):**
```html
<input type="checkbox" name="toppings" value="cheese" id="cheese">
<label for="cheese">🧀 Cheese</label>

<input type="checkbox" name="toppings" value="pepperoni" id="pepperoni">
<label for="pepperoni">🍕 Pepperoni</label>

<input type="checkbox" name="toppings" value="mushroom" id="mushroom" checked>
<label for="mushroom">🍄 Mushroom</label>
```

### **Dropdown Select:**
```html
<select name="country">
    <option value="">Choose country</option>
    <option value="usa">🇺🇸 USA</option>
    <option value="india" selected>🇮🇳 India</option>
    <option value="uk">🇬🇧 UK</option>
</select>

<!-- Multiple selection -->
<select name="skills" multiple size="4">
    <option value="html">HTML</option>
    <option value="css">CSS</option>
    <option value="js">JavaScript</option>
    <option value="react">React</option>
</select>
```

---

## 📄 **Textarea & Buttons**

> [!INFO] **Definition**: Multi-line text and form actions

### **Textarea:**
```html
<textarea name="message" rows="4" cols="50" 
          placeholder="Write your message here..."
          maxlength="500"></textarea>
```

### **Button Types:**
```html
<!-- Submit form -->
<button type="submit">Send</button>

<!-- Reset form -->
<button type="reset">Clear All</button>

<!-- Custom action (JavaScript) -->
<button type="button" onclick="doSomething()">Click Me</button>

<!-- Alternative submit -->
<input type="submit" value="Submit Form">
```

---

## 🏷️ **Labels & Accessibility**

> [!INFO] **Definition**: Labels connect text to inputs for accessibility

**🎯 Two Methods:**
```html
<!-- Method 1: Wrap input in label -->
<label>
    Username:
    <input type="text" name="username">
</label>

<!-- Method 2: Use 'for' attribute (RECOMMENDED) -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

**✅ Why Labels Matter:**
- Screen readers announce the label
- Clicking label focuses the input
- Larger click target for checkboxes/radios

---

## 🎛️ **Input Attributes**

> [!INFO] **Definition**: Attributes that modify input behavior

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `required` | Must be filled | `<input required>` |
| `disabled` | Cannot interact | `<input disabled>` |
| `readonly` | Can see, can't edit | `<input readonly>` |
| `placeholder` | Hint text | `placeholder="Enter name"` |
| `value` | Default value | `value="John"` |
| `maxlength` | Max characters | `maxlength="50"` |
| `minlength` | Min characters | `minlength="8"` |
| `pattern` | Regex validation | `pattern="[A-Za-z]+"` |
| `autofocus` | Focus on page load | `<input autofocus>` |
| `autocomplete` | Browser suggestions | `autocomplete="off"` |

**🎯 Examples:**
```html
<input type="text" 
       name="username" 
       required 
       minlength="3" 
       maxlength="20"
       placeholder="Username (3-20 chars)"
       pattern="[a-z0-9_]+"
       title="Lowercase letters, numbers, underscore only">
```

---

## 🎨 **Complete Form Example**

```html
<form action="/register" method="post">
    <h2>📝 Create Account</h2>
    
    <div class="form-group">
        <label for="fullname">Full Name:</label>
        <input type="text" id="fullname" name="fullname" required>
    </div>
    
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" 
               minlength="8" required>
    </div>
    
    <div class="form-group">
        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob">
    </div>
    
    <fieldset>
        <legend>Gender:</legend>
        <input type="radio" name="gender" value="male" id="male">
        <label for="male">Male</label>
        <input type="radio" name="gender" value="female" id="female">
        <label for="female">Female</label>
    </fieldset>
    
    <div class="form-group">
        <input type="checkbox" id="terms" name="terms" required>
        <label for="terms">I agree to the Terms & Conditions</label>
    </div>
    
    <button type="submit">Create Account</button>
    <button type="reset">Clear</button>
</form>
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **form** → The container 📦
> - **input** → Single-line data entry
> - **textarea** → Multi-line text
> - **select** → Dropdown choices
> - **radio** → Pick ONE (like radio stations) 📻
> - **checkbox** → Pick MULTIPLE ☑️

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What's the difference between `GET` and `POST` methods?
> > [!SUCCESS]- Answer
> > **GET**: Data visible in URL, limited size, use for search/filters. **POST**: Data hidden in request body, no size limit, use for sensitive data (login, forms with passwords).

> [!QUESTION] **Q2**: How do you make an input field mandatory?
> > [!SUCCESS]- Answer
> > Add the `required` attribute: `<input type="text" required>`. The form won't submit unless this field is filled.

> [!QUESTION] **Q3**: How do radio buttons know they're in the same group?
> > [!SUCCESS]- Answer
> > Radio buttons with the same `name` attribute are in the same group. Only one in the group can be selected at a time.

> [!QUESTION] **Q4**: What attribute connects a `<label>` to an `<input>`?
> > [!SUCCESS]- Answer
> > The `for` attribute on the label matches the `id` attribute on the input: `<label for="email">` connects to `<input id="email">`.

> [!QUESTION] **Q5**: What `enctype` is needed for file uploads?
> > [!SUCCESS]- Answer
> > `enctype="multipart/form-data"` is required for file uploads. Without it, only the filename is sent, not the actual file content.

---

Back to: [[Sem Exam/Frontend-Dev/Module 1 - HTML Essentials/README|Module 1 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
