# 🏗️ HTML Document Structure & Overview

## 🎯 **What is HTML?**

> [!SUCCESS] **Definition**: HTML = HyperText Markup Language
> The **skeleton structure** of every website! 🦴 It defines WHAT content appears on the page.

**📍 Key Points:**
- HTML is NOT a programming language - it's a markup language
- Tells browser how to structure content
- Uses tags to define elements
- Foundation that CSS and JavaScript build upon

---

## 📄 **The DOCTYPE Declaration**

> [!INFO] **Definition**: Tells the browser which HTML version you're using
> Always the FIRST line of any HTML document! 🥇

**📍 Key Points:**
- `<!DOCTYPE html>` = HTML5 (current standard)
- Not actually an HTML tag - it's an instruction
- Case-insensitive but lowercase is convention
- Must be on line 1, no whitespace before it

**🎨 Visual:**
```html
<!DOCTYPE html>  ← "Hey browser, I'm HTML5!"
```

**✅ Do's:**
- Always include DOCTYPE first
- Use HTML5 DOCTYPE (simplest and most modern)

**❌ Don'ts:**
- Don't put anything before DOCTYPE
- Don't forget it (browser enters "quirks mode")

---

## 🌐 **The HTML Element**

> [!INFO] **Definition**: The root element that wraps ALL other content
> The **container** of your entire webpage! 📦

**📍 Key Points:**
- `<html>` is the root element
- Everything goes inside it
- `lang` attribute specifies language
- Important for accessibility and SEO

**🎨 Visual:**
```html
<!DOCTYPE html>
<html lang="en">    ← Root container opens
  <!-- Everything goes here -->
</html>             ← Root container closes
```

**🎯 Use Cases:**
```html
<html lang="en">     <!-- English -->
<html lang="ta">     <!-- Tamil -->
<html lang="hi">     <!-- Hindi -->
<html lang="ja">     <!-- Japanese -->
```

---

## 🧠 **The Head Element**

> [!INFO] **Definition**: Contains metadata - info ABOUT the page, not ON the page
> The **brain** of your document - invisible but essential! 🧠

**📍 Key Points:**
- Not visible to users
- Contains title, meta tags, links to CSS/JS
- Critical for SEO and browser behavior
- Should be before `<body>`

**🎨 Visual:**
```html
<head>
  <meta charset="UTF-8">           ← Character encoding
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Page</title>           ← Browser tab title
  <link rel="stylesheet" href="style.css">  ← CSS link
</head>
```

**🎯 Common Head Elements:**
| Element | Purpose |
|---------|---------|
| `<title>` | Browser tab title |
| `<meta>` | Metadata (charset, viewport, description) |
| `<link>` | External resources (CSS, favicon) |
| `<style>` | Internal CSS |
| `<script>` | JavaScript |

---

## 👁️ **The Body Element**

> [!INFO] **Definition**: Contains ALL visible content of your webpage
> Everything users SEE goes here! 👀

**📍 Key Points:**
- All visible content inside `<body>`
- Only ONE body per document
- Rendered by browser in order
- Where most of your HTML lives

**🎨 Visual:**
```html
<body>
  <header>...</header>     ← Visible!
  <main>...</main>         ← Visible!
  <footer>...</footer>     ← Visible!
</body>
```

---

## 🏠 **Complete HTML Structure**

> [!SUCCESS] **The Full Picture**: Every HTML page needs this skeleton!

**🎨 Complete Template:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A description of my page">
    <title>My Awesome Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Site</h1>
    </header>
    
    <main>
        <p>This is the main content!</p>
    </main>
    
    <footer>
        <p>&copy; 2024 My Site</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>
```

---

## 💡 **Pro Tips & Best Practices**

> [!TIP] **Suggestions** 💡
> - Use HTML5 semantic elements for better structure
> - Always set `lang` attribute for accessibility
> - Put CSS in `<head>`, JavaScript before `</body>`
> - Use proper indentation (2 or 4 spaces)
> - Validate your HTML using W3C Validator

**✅ Do's:**
- Include all essential meta tags
- Use meaningful page titles
- Follow proper nesting

**❌ Don'ts:**
- Don't skip the DOCTYPE
- Don't put content outside body
- Don't forget charset encoding

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **DOCTYPE** → Declaration "I'm HTML5!"
> - **html** → The **H**ouse wrapper
> - **head** → **H**idden info (metadata)
> - **body** → **B**ig visible content

```
📄 Document Structure = Building a House
┌─────────────────────────────────┐
│ DOCTYPE → Foundation            │
│ ┌─────────────────────────────┐ │
│ │ <html> → The House          │ │
│ │ ┌─────────────────────────┐ │ │
│ │ │ <head> → Blueprints 📋  │ │ │
│ │ └─────────────────────────┘ │ │
│ │ ┌─────────────────────────┐ │ │
│ │ │ <body> → Rooms 🏠       │ │ │
│ │ └─────────────────────────┘ │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the purpose of `<!DOCTYPE html>`?
> > [!SUCCESS]- Answer
> > It tells the browser that this document is HTML5 and should be rendered in standards mode, not quirks mode.

> [!QUESTION] **Q2**: What goes inside the `<head>` element?
> > [!SUCCESS]- Answer
> > Metadata about the page: title, meta tags (charset, viewport, description), links to CSS files, and sometimes scripts. This content is NOT visible to users.

> [!QUESTION] **Q3**: Why should you include `lang="en"` in the html tag?
> > [!SUCCESS]- Answer
> > It specifies the language of the document for screen readers (accessibility) and search engines (SEO). It helps browsers apply correct fonts and spell-checkers.

> [!QUESTION] **Q4**: What's the difference between `<head>` and `<body>`?
> > [!SUCCESS]- Answer
> > `<head>` contains invisible metadata (title, meta, links). `<body>` contains ALL visible content that users see on the page.

> [!QUESTION] **Q5**: Write a minimal valid HTML5 document structure.
> > [!SUCCESS]- Answer
> > ```html
> > <!DOCTYPE html>
> > <html lang="en">
> > <head>
> >     <meta charset="UTF-8">
> >     <title>My Page</title>
> > </head>
> > <body>
> >     <h1>Hello World</h1>
> > </body>
> > </html>
> > ```

---

Back to: [[Sem Exam/Frontend-Dev/Module 1 - HTML Essentials/README|Module 1 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
