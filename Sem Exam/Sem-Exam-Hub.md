# 🎓 Sem Exam Master Hub

> [!INFO] **Exam Progress Tracker**
> Track your study progress across all subjects in one place!
> 
> ```dataviewjs
> const dsaTasks = dv.page("2-DSA/DSA-Hub.md").file.tasks;
> const feTasks = dv.page("1-Frontend-Dev/frontend-Sem-Hub.md").file.tasks;
> const ipTasks = dv.page("3-Intro-to-Programming/Intro-Prog-Hub.md").file.tasks;
> const mathTasks = dv.page("4-Mathematics-for-AI-ML/Math-AI-ML-Hub.md").file.tasks;
> const allTasks = [...dsaTasks, ...feTasks, ...ipTasks, ...mathTasks];
> const completed = allTasks.filter(t => t.completed).length;
> const total = allTasks.length;
> const percent = total === 0 ? 0 : Math.round((completed / total) * 100);
> 
> dv.paragraph(`**Overall Status:** ${completed}/${total} Topics Completed (**${percent}%**)`);
> dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease;"></div></div>`);
> ```

---

## 🎨 **Subject 1: Frontend Development**

![[1-Frontend-Dev/frontend-Sem-Hub#📚 **Checklist**]]

---

## 🐍 **Subject 2: Data Structures & Algorithms (DSA)**

![[2-DSA/DSA-Hub#📚 **Checklist**]]

---

## 🐍 **Subject 3: Introduction to Programming**

![[3-Intro-to-Programming/Intro-Prog-Hub#📚 **Checklist**]]

---

## 📊 **Subject 4: Mathematics for AI/ML**

![[4-Mathematics-for-AI-ML/Math-AI-ML-Hub#📚 **Checklist**]]

---

> Keep going! "The only bad workout is the one that didn't happen." 💪
