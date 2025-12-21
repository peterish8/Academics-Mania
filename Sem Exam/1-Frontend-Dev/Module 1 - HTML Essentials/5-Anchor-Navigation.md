# 🔗 Anchor Tags & Navigation

## 🎯 **What are Anchor Tags?**

> [!SUCCESS] **Definition**: The `<a>` tag creates a hyperlink to other pages, files, or locations.
> It's what makes the web a **web**! 🕸️

**📍 Key Points:**
- `href` attribute is mandatory (it tells where to go)
- Can link to:
  - Other web pages (internal or external)
  - Files (PDFs, images)
  - Email addresses (`mailto:`)
  - Phone numbers (`tel:`)
  - Specific sections on the same page (`#id`)

**🎨 Visual:**
```html
<a href="https://google.com">Go to Google</a>
   ↑                          ↑
Destination                Clickable Text
```

---

## 🌍 **Link Types**

### **1. Absolute URL**
> Links to a different website (full address).
```html
<a href="https://www.wikipedia.org">Wikipedia</a>
```

### **2. Relative URL**
> Links to a page within your own site.
```html
<a href="about.html">About Us</a>
<a href="contact/form.html">Contact Form</a>
```

### **3. Internal Link (Anchor)**
> Jumps to a specific part of the SAME page.
```html
<!-- The Link -->
<a href="#section2">Jump to Section 2</a>

<!-- The Destination -->
<h2 id="section2">Section 2</h2>
```

---

## 🎯 **Link Targets**

> [!INFO] **Definition**: The `target` attribute specifies WHERE to open the link.

| Value | Behavior |
|-------|----------|
| `_self` | Default. Opens in the same tab/window. |
| `_blank` | Opens in a **NEW** tab or window. |
| `_parent` | Opens in the parent frame. |
| `_top` | Opens in the full body of the window. |

**✅ Do's:**
- Use `target="_blank"` for external links so users don't leave your site.
- Always add `rel="noopener noreferrer"` with `target="_blank"` for security!

**🎨 Example:**
```html
<a href="https://google.com" target="_blank" rel="noopener noreferrer">
  Open Google in New Tab
</a>
```

---

## 📧 **Email & Phone Links**

> [!TIP] **Action Links**: trigger apps on the user's device!

### **Email Link**
Opens the default email app.
```html
<a href="mailto:support@example.com">Email Us</a>

<!-- With subject & body pre-filled -->
<a href="mailto:me@site.com?subject=Hello&body=I need help">
  Email Support
</a>
```

### **Phone Link**
Opens the dialer on mobile devices.
```html
<a href="tel:+1234567890">Call Us: +1 (234) 567-890</a>
```

---

## 🖼️ **Image Links**

> [!INFO] **Definition**: Making an image clickable.

Wrap the `<img>` tag inside an `<a>` tag.

```html
<a href="https://www.apple.com">
  <img src="apple-logo.png" alt="Apple Website" width="50">
</a>
```

---

## 💡 **Best Practices**

> [!TIP] **Suggestions** 💡

**✅ Do's:**
- Use descriptive text (e.g., "Read our Guide" instead of "Click Here").
- Check for broken links (404 errors).
- Use `title` attribute for tooltips.

**❌ Don'ts:**
- Don't link to empty `href=""` (reloads the page).
- Don't overuse `target="_blank"` (can be annoying).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **href** = **H**ypertext **REF**erence (Where to go?)
> - **target="_blank"** = Opens a **blank** new page 📄
> - **#** (Hashtag) = Jumps to an **ID** (Internal Destination) #️⃣

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What attribute is required for an anchor tag to work?
> > [!SUCCESS]- Answer
> > The `href` attribute (Hypertext Reference) is required to specify the destination URL.

> [!QUESTION] **Q2**: How do you open a link in a new tab?
> > [!SUCCESS]- Answer
> > Add `target="_blank"` to the `<a>` tag.

> [!QUESTION] **Q3**: What is the difference between an absolute and a relative URL?
> > [!SUCCESS]- Answer
> > Absolute URLs contain the full address (e.g., `https://google.com`), while relative URLs point to a file within the same website (e.g., `about.html`).

> [!QUESTION] **Q4**: How do you create a link that opens the user's email client?
> > [!SUCCESS]- Answer
> > Use `href="mailto:email@address.com"`.

> [!QUESTION] **Q5**: Why should you add `rel="noopener noreferrer"` when using `target="_blank"`?
> > [!SUCCESS]- Answer
> > It improves security by preventing the new page from accessing the `window.opener` object of the original page (preventing malicious redirects) and can improve performance.

---

Back to: [[Sem Exam/Frontend-Dev/Module 1 - HTML Essentials/README|Module 1 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
