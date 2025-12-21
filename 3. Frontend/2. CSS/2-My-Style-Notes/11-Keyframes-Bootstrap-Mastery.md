# 🎬 Keyframes & Bootstrap Mastery

## 🎯 CSS Animations with @keyframes

### 🌟 Animation vs Transition

| Feature | Transition | Animation |
|---------|------------|-----------|
| **Trigger** | User interaction (hover, focus) | Automatic or programmatic |
| **States** | 2 states (start → end) | Multiple states (keyframes) |
| **Control** | Limited (duration, easing) | Full control (timing, iteration, direction) |
| **Complexity** | Simple property changes | Complex multi-step sequences |

**Memory Trick**: "Transition = Two states, Animation = All states"

---

## 🎬 @keyframes Deep Dive

### 🏗️ Basic Syntax Structure

```css
@keyframes animationName {
  from { /* Starting state (0%) */ }
  to { /* Ending state (100%) */ }
}

/* OR with percentages */
@keyframes animationName {
  0% { /* Starting state */ }
  25% { /* Quarter way */ }
  50% { /* Halfway */ }
  75% { /* Three quarters */ }
  100% { /* Ending state */ }
}
```

### 🎛️ Animation Property Breakdown

```css
.element {
  animation: name duration timing-function delay iteration-count direction fill-mode;
}
```

#### 📋 Animation Properties Explained

| Property | Values | Description |
|----------|--------|-------------|
| **name** | `animationName` | References @keyframes |
| **duration** | `2s`, `500ms` | How long animation runs |
| **timing-function** | `ease`, `linear`, `ease-in-out` | Speed curve |
| **delay** | `1s`, `500ms` | Wait before starting |
| **iteration-count** | `1`, `3`, `infinite` | How many times to repeat |
| **direction** | `normal`, `reverse`, `alternate` | Play direction |
| **fill-mode** | `forwards`, `backwards`, `both` | State before/after |

---

## 🎨 Animation Examples Breakdown

### 1️⃣ Fade-In Animation

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  opacity: 0;                    /* Start invisible */
  animation: fadeIn 2s forwards; /* Animate to visible, stay visible */
}
```

**Key Insights**:
- **`forwards`** → Keeps final state after animation
- **Initial opacity: 0** → Ensures element starts invisible
- **Use case** → Page load animations, content reveals

### 2️⃣ Slide-In Animation

```css
@keyframes slideIn {
  from { transform: translateX(-200px); }
  to { transform: translateX(0); }
}

.slide-box {
  animation: slideIn 2s ease-out forwards;
}
```

**Animation Flow**:
1. **Start** → 200px left of normal position
2. **End** → Normal position (translateX(0))
3. **Easing** → `ease-out` for natural deceleration
4. **Result** → Smooth slide-in from left

### 3️⃣ Bouncing Ball (Multi-step)

```css
@keyframes bounce {
  0%, 100% { top: 0; }      /* Start and end at top */
  50% { top: 150px; }       /* Halfway, drop to bottom */
}

.ball {
  position: relative;
  animation: bounce 1s ease-in-out infinite;
}
```

**Animation Breakdown**:
- **0%** → Ball at top
- **50%** → Ball drops to bottom (150px down)
- **100%** → Ball returns to top
- **`infinite`** → Repeats forever
- **`ease-in-out`** → Natural acceleration/deceleration

---

## 🚀 Advanced Animation Techniques

### 🎯 Complex Multi-Property Animations

```css
@keyframes complexMove {
  0% {
    transform: translateX(0) rotate(0deg) scale(1);
    background-color: #ff6b6b;
    border-radius: 0;
  }
  25% {
    transform: translateX(100px) rotate(90deg) scale(1.2);
    background-color: #4ecdc4;
    border-radius: 25%;
  }
  50% {
    transform: translateX(100px) translateY(100px) rotate(180deg) scale(0.8);
    background-color: #45b7d1;
    border-radius: 50%;
  }
  75% {
    transform: translateX(0) translateY(100px) rotate(270deg) scale(1.1);
    background-color: #96ceb4;
    border-radius: 25%;
  }
  100% {
    transform: translateX(0) rotate(360deg) scale(1);
    background-color: #ffeaa7;
    border-radius: 0;
  }
}
```

### 🎨 Animation Timing Functions

```css
/* Built-in timing functions */
.linear { animation-timing-function: linear; }           /* Constant speed */
.ease { animation-timing-function: ease; }               /* Slow-fast-slow */
.ease-in { animation-timing-function: ease-in; }         /* Slow start */
.ease-out { animation-timing-function: ease-out; }       /* Slow end */
.ease-in-out { animation-timing-function: ease-in-out; } /* Slow start & end */

/* Custom cubic-bezier curves */
.custom { animation-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55); }
```

### 🔄 Animation Direction & Fill Mode

```css
.animation-controls {
  animation-direction: alternate;    /* Forward, then reverse */
  animation-fill-mode: both;         /* Apply first & last keyframe styles */
  animation-iteration-count: 3;      /* Run 3 times */
}
```

---

## 🎯 Real-World Animation Patterns

### 🌊 Loading Animations

```css
/* Spinning loader */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.loader { animation: spin 1s linear infinite; }

/* Pulsing dot */
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.5); opacity: 0.5; }
}
.pulse-dot { animation: pulse 1.5s ease-in-out infinite; }

/* Three-dot loader */
.dot-loader span {
  animation: dotPulse 1.4s ease-in-out infinite;
}
.dot-loader span:nth-child(2) { animation-delay: 0.2s; }
.dot-loader span:nth-child(3) { animation-delay: 0.4s; }
```

### 🎨 Hover Animations

```css
/* Shake effect */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}
.shake:hover { animation: shake 0.5s ease-in-out; }

/* Bounce in */
@keyframes bounceIn {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.05); opacity: 1; }
  70% { transform: scale(0.9); }
  100% { transform: scale(1); }
}
.bounce-in:hover { animation: bounceIn 0.6s ease-out; }
```

---

## 🅱️ Bootstrap Framework Mastery

### 🎯 What Makes Bootstrap Special?

**Core Philosophy**: "Mobile-first, responsive, component-based design system"

#### 🏗️ Bootstrap Architecture
1. **CSS Reset** → Normalize browser differences
2. **Grid System** → 12-column responsive layout
3. **Components** → Pre-built UI elements
4. **Utilities** → Helper classes for quick styling
5. **JavaScript** → Interactive components

---

### 📐 Bootstrap Grid System

#### 🎯 Grid Breakpoints
| Breakpoint | Class Prefix | Screen Size |
|------------|--------------|-------------|
| Extra Small | `col-` | < 576px |
| Small | `col-sm-` | ≥ 576px |
| Medium | `col-md-` | ≥ 768px |
| Large | `col-lg-` | ≥ 992px |
| Extra Large | `col-xl-` | ≥ 1200px |
| Extra Extra Large | `col-xxl-` | ≥ 1400px |

#### 🏗️ Grid Structure
```html
<div class="container">           <!-- Fixed-width container -->
  <div class="row">              <!-- Horizontal group -->
    <div class="col-md-6">       <!-- 6/12 columns on medium+ screens -->
      Content 1
    </div>
    <div class="col-md-6">       <!-- 6/12 columns on medium+ screens -->
      Content 2
    </div>
  </div>
</div>
```

#### 🎯 Responsive Grid Examples
```html
<!-- Different sizes for different screens -->
<div class="col-12 col-sm-6 col-md-4 col-lg-3">
  <!-- Mobile: full width, Tablet: half, Desktop: third, Large: quarter -->
</div>

<!-- Offset columns -->
<div class="col-md-6 offset-md-3">
  <!-- 6 columns wide, offset by 3 (centered) -->
</div>
```

---

### 🎨 Bootstrap Components

#### 🔘 Buttons
```html
<!-- Button variants -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>

<!-- Button sizes -->
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-sm">Small</button>
```

#### 🃏 Cards
```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Card description text.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

#### 🧭 Navigation
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Brand</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">About</a></li>
      </ul>
    </div>
  </div>
</nav>
```

---

### 🛠️ Bootstrap Utilities

#### 📏 Spacing Utilities
```html
<!-- Margin utilities -->
<div class="m-3">Margin all sides</div>
<div class="mt-2 mb-4">Margin top 2, bottom 4</div>
<div class="mx-auto">Horizontal center</div>

<!-- Padding utilities -->
<div class="p-3">Padding all sides</div>
<div class="px-4 py-2">Padding horizontal 4, vertical 2</div>
```

#### 🎨 Color Utilities
```html
<!-- Text colors -->
<p class="text-primary">Primary text</p>
<p class="text-success">Success text</p>
<p class="text-danger">Danger text</p>

<!-- Background colors -->
<div class="bg-primary text-white">Primary background</div>
<div class="bg-light">Light background</div>
```

#### 📐 Display & Flexbox
```html
<!-- Display utilities -->
<div class="d-none d-md-block">Hidden on mobile, visible on desktop</div>
<div class="d-flex justify-content-center align-items-center">
  Centered content
</div>

<!-- Flexbox utilities -->
<div class="d-flex flex-column flex-md-row">
  <div class="flex-fill">Flexible item</div>
</div>
```

---

## 🚀 Bootstrap Best Practices

### 🎯 Customization Strategy

#### 🎨 CSS Custom Properties
```css
:root {
  --bs-primary: #007bff;
  --bs-secondary: #6c757d;
  --bs-success: #28a745;
}
```

#### 🛠️ SASS Customization
```scss
// Override Bootstrap variables
$primary: #007bff;
$secondary: #6c757d;
$border-radius: 0.5rem;

// Import Bootstrap
@import "bootstrap/scss/bootstrap";
```

### 📱 Responsive Design Tips

#### 🎯 Mobile-First Approach
```html
<!-- Start with mobile layout, enhance for larger screens -->
<div class="col-12 col-md-6 col-lg-4">
  <!-- Mobile: full width, Tablet: half, Desktop: third -->
</div>
```

#### 🔧 Utility-First Styling
```html
<!-- Use utilities for quick styling -->
<div class="d-flex justify-content-between align-items-center p-3 bg-light rounded">
  <h5 class="mb-0">Title</h5>
  <button class="btn btn-primary btn-sm">Action</button>
</div>
```

---

## 🧠 Key Takeaways

### 🎬 Animation Mastery
1. **@keyframes** → Define multi-step animations
2. **Animation properties** → Control timing, iteration, direction
3. **Performance** → Use transform and opacity for smooth animations
4. **User experience** → Subtle animations enhance, don't distract

### 🅱️ Bootstrap Efficiency
1. **Grid system** → Responsive layouts made easy
2. **Components** → Pre-built, tested UI elements
3. **Utilities** → Quick styling without custom CSS
4. **Customization** → Override variables for brand consistency

### 🎯 Development Workflow
1. **Start with Bootstrap** → Rapid prototyping and development
2. **Customize gradually** → Override defaults as needed
3. **Add animations** → Enhance user experience with CSS animations
4. **Optimize performance** → Remove unused Bootstrap components

**Memory Trick**: "Bootstrap = Building blocks, Animations = Bringing life to blocks"