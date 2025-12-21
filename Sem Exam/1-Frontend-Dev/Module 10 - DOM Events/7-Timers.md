# ⏱️ Browser Timers

## 🎯 **Timing Events**

> [!SUCCESS] **Goal**: Delay code execution or repeat it at intervals.

---

## 🕰️ **1. setTimeout (Delay)**

> Runs **Once** after X milliseconds.
> "Wait 3 seconds, then say Hi."

```javascript
const timerId = setTimeout(() => {
    console.log("Hello!");
}, 3000); // 3000ms = 3s

// Cancel it
clearTimeout(timerId);
```

---

## 🔄 **2. setInterval (Repeat)**

> Runs **Repeatedly** every X milliseconds.
> "Say Hi every 1 second."

```javascript
let count = 0;
const intervalId = setInterval(() => {
    count++;
    console.log(count);
    
    if (count === 5) {
        clearInterval(intervalId); // Stop!
    }
}, 1000); // 1s
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Timeout** = Oven Timer (Ding! Done) 🔔
> - **Interval** = Heartbeat (Pulse... Pulse...) 💓
> - **Clear** = Stop button 🛑

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What unit is time measured in for these functions?
> > [!SUCCESS]- Answer
> > Milliseconds (1000ms = 1s).

> [!QUESTION] **Q2**: How do you stop a `setInterval` loop?
> > [!SUCCESS]- Answer
> > Use `clearInterval(id)`. You need to save the ID returned when you started it.

> [!QUESTION] **Q3**: Does `setTimeout` pause the rest of the code?
> > [!SUCCESS]- Answer
> > No! It is asynchronous (Non-blocking). The code simply continues, and the timeout callback runs later.

> [!QUESTION] **Q4**: What does `setInterval()` return in JavaScript?
> > [!SUCCESS]- Answer
> > A numeric ID (Timer ID) that you use to clear it later.

> [!QUESTION] **Q5**: If you set delay to 0ms, does it run immediately?
> > [!SUCCESS]- Answer
> > No. It puts the callback at the end of the "Event Loop" queue, so it runs after all current synchronous code is finished (effectively "ASAP").

---

Back to: [[Sem Exam/Frontend-Dev/Module 10 - DOM Events/README|Module 10 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
