# 🎨 Colors, Typography & Fonts

## 🎨 **CSS Colors**

> [!SUCCESS] **Ways to Define Color**:

### **1. Keywords**
> Generic names. Limited (140 names).
```css
color: red;
background-color: transparent;
```

### **2. Hexadecimal (Hex)**
> Most common. Uses `#RRGGBB` (Red, Green, Blue).
```css
color: #ff0000; /* Red */
color: #000000; /* Black */
color: #ffffff; /* White */
```
- range: 00 to FF.

### **3. RGB / RGBa**
> Functional notation. `rgb(Red, Green, Blue)`.
> **RGBa** adds **Alpha** (transparency).
```css
color: rgb(255, 0, 0);       /* Red */
color: rgba(0, 0, 0, 0.5);   /* 50% Transparent Black */
```

### **4. HSL / HSLa (Designer's Favorite 🌟)**
> **H**ue (Color circle), **S**aturation (Intensity), **L**ightness.
```css
color: hsl(120, 100%, 50%); /* Green */
```
- Easiest to adjust (e.g., make it darker: lower L).

---

## 🔡 **Typography Basics**

### **1. Font Family**
> Defines the typeface.
```css
font-family: "Helvetica Neue", Arial, sans-serif;
```
- **Web Safe Fonts**: Arial, Verdana, Times New Roman (Installed on most PCs).
- **Web Fonts**: Google Fonts (Downloaded from web).
- **Fallback**: Always list multiple fonts ending with a generic family (`sans-serif` or `serif`).

### **2. Font Size**
> Common units: `px` (fixed), `rem` (relative to root), `em` (relative to parent).
```css
font-size: 16px;
```

### **3. Font Weight**
> Thickness of text.
- `normal` (400)
- `bold` (700)
```css
font-weight: 700;
```

### **4. Text Alignment & Decoration**
```css
text-align: center; /* left, right, justify */
text-decoration: none; /* Removes underline from links */
line-height: 1.5; /* Line spacing - Critical for readability! */
```

---

## 🌍 **Web Fonts (Google Fonts)**

> [!TIP] **How to use Custom Fonts**:
> 1. Go to fonts.google.com
> 2. Select a font (e.g., Robot, Poppins).
> 3. Copy the `<link>` tag into your HTML `<head>`.
> 4. Use it in CSS.

**Example:**
```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```
```css
body {
    font-family: 'Roboto', sans-serif;
}
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Serif** = Has feet (Times New Roman) 👢
> - **Sans-Serif** = No feet (Arial) 🦶 ("Sans" means "without")
> - **RGBA** = RGB + **A**lpha (Transparency) 👻
> - **lh** = **L**ine **H**eight (Breathing room for text) 🫁

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What does the 'a' in RGBa stand for?
> > [!SUCCESS]- Answer
> > **Alpha**. It controls the opacity/transparency of the color (0 = invisible, 1 = solid).

> [!QUESTION] **Q2**: Why should you define multiple fonts in `font-family`?
> > [!SUCCESS]- Answer
> > It's a "font stack" or fallback system. If the user doesn't have the first font installed, the browser tries the second, and so on.

> [!QUESTION] **Q3**: What is the generic font family for fonts WITHOUT decorative "feet" or lines at the ends?
> > [!SUCCESS]- Answer
> > `sans-serif` (e.g., Arial, Helvetica).

> [!QUESTION] **Q4**: Which CSS property adds space between lines of text?
> > [!SUCCESS]- Answer
> > `line-height`. Good usage (e.g., 1.5 or 1.6) improves readability significantly.

> [!QUESTION] **Q5**: Is `# FFF` valid hex code?
> > [!SUCCESS]- Answer
> > Yes! It's the shorthand for `#FFFFFF` (White). `#000` is black.

---

Back to: [[Sem Exam/Frontend-Dev/Module 2 - CSS Foundations/README|Module 2 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
