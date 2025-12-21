# 🌟 HTML Basics - My Style Notes

## 🎯 **What is HTML?**

> [!SUCCESS] **Definition**: HTML = HyperText Markup Language
> The **skeleton structure** of every website! 🦴

**🎯 Use Cases:**
- Create web pages and websites
- Structure content (headings, paragraphs, lists)
- Add images, links, and forms
- Build the foundation for CSS styling

---

## 🏷️ **Tags**

> [!INFO] **Definition**: Tags define different types of content
> Written in angle brackets `< >` - most come in pairs!

**📍 Key Points:**
- Opening tag: `<tagname>`
- Closing tag: `</tagname>`
- Self-closing: `<img>`, `<br>`

**🎨 Visual:**
```
<p>Hello World</p>
 ↑      ↑       ↑
open content close
```

**🎯 Use Cases:**
- `<h1>` for main titles
- `<p>` for paragraphs
- `<img>` for pictures
- `<a>` for links

---

## 🧩 **Elements**

> [!INFO] **Definition**: Complete package = Opening tag + Content + Closing tag

**📍 Key Points:**
- Element = Tag + Content + Closing Tag
- The **whole thing** is called an element
- Elements can be nested inside other elements

**🎨 Visual:**
```
<h1>Welcome!</h1>
└─────────────────┘
   This is ONE element
```

**🎯 Use Cases:**
- `<h1>Main Title</h1>` - heading element
- `<p>Some text</p>` - paragraph element
- `<strong>Important</strong>` - emphasis element

---

## ⚙️ **Attributes**

> [!INFO] **Definition**: Extra information added to opening tags
> Like **stickers with details** on your containers! 🏷️

**📍 Key Points:**
- Always in opening tag only
- Format: `name="value"`
- Multiple attributes allowed
- Provide extra functionality

**🎨 Visual:**
```
<img src="cat.jpg" alt="Cute cat" width="300">
     ↑─────────┘ ↑─────────┘ ↑──────────┘
    attribute1   attribute2   attribute3
```

**🎯 Use Cases:**
- `src` - image source path
- `alt` - description for screen readers
- `width/height` - size control
- `href` - link destination
- `id/class` - for CSS styling

---

## 🏗️ **HTML Structure**

> [!INFO] **Definition**: Basic skeleton that every HTML page needs
> Like the **blueprint** of a house! 🏠

**📍 Key Points:**
- `<!DOCTYPE html>` - tells browser it's HTML5
- `<html>` - wraps everything
- `<head>` - metadata (not visible)
- `<body>` - visible content

**🎨 Visual:**
```
<!DOCTYPE html>     ← "I'm HTML5!"
<html>              ← House wrapper
  <head>            ← Behind scenes
    <title>...</title>
  </head>
  <body>            ← What users see
    <h1>Hello!</h1>
  </body>
</html>
```

**🎯 Use Cases:**
- Every HTML page needs this structure
- `<head>` for page title, CSS links
- `<body>` for all visible content

---

## 📝 **Text Elements**

### **📏 Headings (h1-h6)**

> [!INFO] **Definition**: Create titles and subtitles with hierarchy
> h1 = largest, h6 = smallest - like newspaper headlines!

**📍 Key Points:**
- 6 levels of headings (h1, h2, h3, h4, h5, h6)
- h1 should be used once per page (main title)
- Use in order (don't skip levels)
- Important for SEO and accessibility

**🎨 Visual Size:**
```
h1 → HUGE TITLE
h2 → Big Section
h3 → Medium Subsection
h4 → Small heading
h5 → tiny heading
h6 → very tiny
```

**🎯 Use Cases:**
- `<h1>` - Page main title
- `<h2>` - Major sections
- `<h3>` - Subsections
- `<h4-h6>` - Minor headings

---

### **💪 Bold Text**

> [!INFO] **Definition**: Make text bold - but choose wisely!

**📍 Key Points:**
- `<strong>` = Important meaning (semantic)
- `<b>` = Just bold appearance (styling)
- Screen readers emphasize `<strong>`
- Use `<strong>` for warnings, key points

**🎨 Visual:**
```
<strong>IMPORTANT!</strong> → Bold + Meaningful
<b>bold text</b>         → Just Bold Look
```

**🎯 Use Cases:**
- `<strong>` - Safety warnings, key terms
- `<b>` - Product names, styling only

---

### **📐 Italic Text**

> [!INFO] **Definition**: Make text italic - with or without emphasis!

**📍 Key Points:**
- `<em>` = Emphasis meaning (semantic)
- `<i>` = Just italic appearance (styling)
- Screen readers stress `<em>` words
- Use `<em>` when tone changes

**🎨 Visual:**
```
<em>really important</em> → Italic + Emphasis
<i>book title</i>        → Just Italic Look
```

**🎯 Use Cases:**
- `<em>` - Stressed words, emphasis
- `<i>` - Book titles, foreign words

---

### **✏️ Special Text Elements**

> [!INFO] **Definition**: Special formatting for different purposes

**📍 Key Elements:**
- `<del>` - Deleted/removed text (strikethrough)
- `<ins>` - Inserted/added text (underlined)
- `<s>` - No longer accurate (strikethrough)
- `<u>` - Underlined text (styling only)

**🎨 Visual:**
```
<del>old price</del>     → old price (crossed out)
<ins>new content</ins>   → new content (underlined)
<s>outdated info</s>     → outdated info (crossed)
<u>underlined</u>        → underlined (underlined)
```

**🎯 Use Cases:**
- `<del>` - Show document edits
- `<ins>` - Show new additions
- `<s>` - Old prices, outdated info
- `<u>` - Rare underline styling

---

## 🎨 **Quick Examples**

### **🏠 Simple Page**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
</head>
<body>
    <h1>👋 Hi, I'm John!</h1>
    <p>I'm a <strong>web developer</strong> who loves <em>coding</em>!</p>
</body>
</html>
```

### **📱 Contact Info**
```html
<h2>📞 Contact Me</h2>
<p>Email: <strong>john@example.com</strong></p>
<p>Phone: <b>+1-234-567-8900</b></p>
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Tags** = Labels on boxes 🏷️
> - **Elements** = The whole box with content 📦
> - **Attributes** = Stickers with extra info ✨
> - **strong/em** = Meaning matters 🧠
> - **b/i** = Just styling 🎨

Back to: [[README of HTML]]