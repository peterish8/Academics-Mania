# 🏗️ Semantic Elements

## 🎯 **What are Semantic Elements?**

> [!SUCCESS] **Definition**: Elements that clearly describe their meaning to both the browser and the developer.
> Readable code = Better code! 📖

**📍 Key Points:**
- **Non-semantic**: `<div>` and `<span>` (tells nothing about its content).
- **Semantic**: `<form>`, `<table>`, `<article>`, `<header>` (clearly defines its content).
- Helps with **SEO** (Search Engine Optimization).
- Critical for **Accessibility** (Screen readers).

---

## 🏛️ **Main Semantic Layout Elements**

> [!INFO] **Definition**: The major building blocks of a webpage layout.

### **1. `<header>`**
> Introduction content or navigational links.
> - Typically contains: Logo, Main Nav, Search bar.
> - **Note**: Can be used multiple times (e.g., header of an article).

### **2. `<nav>`**
> Navigation links.
> - Use for MAJOR navigation blocks (Main menu, Table of contents).
> - Not every group of links needs `<nav>`.

### **3. `<main>`**
> The dominant content of the `<body>`.
> - **Rule**: Only ONE `<main>` element per page.
> - Should not contain repeated content like sidebars or navs.

### **4. `<section>`**
> A thematic grouping of content.
> - Usually has a heading (`h2`-`h6`).
> - Example: "About Us", "Services", "Contact".

### **5. `<article>`**
> Self-contained, independent content.
> - Should make sense if distributed independently (e.g., RSS, syndication).
> - Examples: Blog posts, forum posts, news stories.

### **6. `<aside>`**
> Content aside from the main content.
> - Examples: Sidebars, call-out boxes, advertising.
> - Often indirectly related to the surrounding content.

### **7. `<footer>`**
> Footer for a document or section.
> - Contains: Copyright, contact info, sitemap, back-to-top links.

---

## 🎨 **Visual Layout Structure**

```
┌──────────────────────────────────────┐
│             <header>                 │
│  Logo         <nav>Links</nav>       │
├──────────────────────────────────────┤
│               <main>                 │
│                                      │
│  ┌──────────────────┐  ┌──────────┐  │
│  │    <section>     │  │ <aside>  │  │
│  │                  │  │          │  │
│  │ ┌──────────────┐ │  │ Sidebar  │  │
│  │ │  <article>   │ │  │ Ads      │  │
│  │ └──────────────┘ │  │ Related  │  │
│  │                  │  │          │  │
│  └──────────────────┘  └──────────┘  │
│                                      │
├──────────────────────────────────────┤
│              <footer>                │
│       Copyright © 2024               │
└──────────────────────────────────────┘
```

---

## 🧩 **Other Semantic Elements**

| Element | Description |
|---------|-------------|
| `<details>` | Creates a collapsible disclosure widget. |
| `<summary>` | The visible heading for the `<details>` element. |
| `<figure>` | Self-contained content (images, diagrams). |
| `<figcaption>`| Caption for the `<figure>`. |
| `<time>` | Defines a specific time/date. |
| `<mark>` | Highlighted text. |

**🎨 Example:**
```html
<figure>
  <img src="chart.jpg" alt="Sales Chart">
  <figcaption>Fig.1 - Yearly Sales Growth</figcaption>
</figure>

<details>
  <summary>Click to show more</summary>
  <p>Here is the hidden content!</p>
</details>
```

---

## 💡 **Why Search Engines Love Semantics**

1.  **Context**: Google knows `<nav>` contains links, not random text.
2.  **Indexing**: Helps bots understand what's the `<main>` content vs. `<aside>` noise.
3.  **Accessibility**: Screen readers can jump directly to `<nav>` or `<main>`.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **nav** = **NAV**igation 🧭
> - **aside** = **A-SIDE** (on the side) 📑
> - **article** = Like a newspaper **Article** (independent) 📰
> - **main** = The **Main** event (Only one!) 🌟

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Can you have multiple `<header>` elements on a single page?
> > [!SUCCESS]- Answer
> > Yes! You can have a main page `<header>`, but also a `<header>` inside each `<article>` or `<section>`.

> [!QUESTION] **Q2**: What is the difference between `<section>` and `<div>`?
> > [!SUCCESS]- Answer
> > `<section>` is semantic—it implies a thematic grouping of content, usually with a heading. `<div>` is non-semantic—it's just a generic container for styling with no meaning.

> [!QUESTION] **Q3**: Which element should wrap a blog post on a homepage listing?
> > [!SUCCESS]- Answer
> > The `<article>` element, because a blog post is independent, self-contained content.

> [!QUESTION] **Q4**: Where should copyright information typically go?
> > [!SUCCESS]- Answer
> > In the `<footer>` element.

> [!QUESTION] **Q5**: Why are semantic elements important for accessibility?
> > [!SUCCESS]- Answer
> > They allow screen readers (used by visually impaired users) to understand the structure of the page and provide shortcuts (e.g., "Jump to Navigation", "Skip to Main Content").

---

Back to: [[Sem Exam/Frontend-Dev/Module 1 - HTML Essentials/README|Module 1 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
