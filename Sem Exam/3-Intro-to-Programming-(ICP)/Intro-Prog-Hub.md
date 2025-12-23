# 🐍 Introduction to Programming Hub

> [!INFO] **Exam Preparation Hub**
> **Master Progress Tracker**
> 
> ```dataviewjs
> const tasks = dv.current().file.tasks;
> const completed = tasks.filter(t => t.completed).length;
> const total = tasks.length;
> const percent = total === 0 ? 0 : Math.round((completed / total) * 100);
> 
> dv.paragraph(`**Status:** ${completed}/${total} Topics Completed (**${percent}%**)`);
> dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease;"></div></div>`);
> ```

---

## 📚 **Checklist**

### **Module 1: Introduction to Programming using Python** 🐍
- [ ] [[Module 1 - Python Basics/README|Module Overview]]
- [ ] [[Module 1 - Python Basics/1-Python-Basics-Control-Flow|1. Python Basics & Control Flow]]
- [ ] [[Module 1 - Python Basics/2-Functions|2. Functions (def, return, scope)]]
- [ ] [[Module 1 - Python Basics/3-Strings|3. Strings (Methods, Slicing, f-strings)]]

### **Module 2: Core Python, Files, Errors, and Modules** 📂
- [ ] [[Module 2 - Core Python/README|Module Overview]]
- [ ] [[Module 2 - Core Python/1-Lists|1. Lists & List Comprehension]]
- [ ] [[Module 2 - Core Python/2-Tuples|2. Tuples & Unpacking]]
- [ ] [[Module 2 - Core Python/3-Dictionaries|3. Dictionaries (Key-Value, Methods)]]
- [ ] [[Module 2 - Core Python/4-Sets|4. Sets (Unordered, Operations)]]
- [ ] [[Module 2 - Core Python/5-File-Handling|5. File Handling (open, read, write)]]
- [ ] [[Module 2 - Core Python/6-Exception-Handling|6. Exception Handling (try, except)]]
- [ ] [[Module 2 - Core Python/7-Modules-Libraries|7. Modules & Libraries (import, pip)]]

### **Module 3: Object-Oriented Programming** 🧬
- [ ] [[Module 3 - OOP/README|Module Overview]]
- [ ] [[Module 3 - OOP/1-Classes-Objects|1. Classes & Objects]]
- [ ] [[Module 3 - OOP/2-Methods-Encapsulation|2. Methods & Encapsulation]]
- [ ] [[Module 3 - OOP/3-Inheritance|3. Inheritance (super, overriding)]]
- [ ] [[Module 3 - OOP/4-Polymorphism|4. Polymorphism & Duck Typing]]
- [ ] [[Module 3 - OOP/5-Abstract-Classes|5. Abstract Classes (ABCs)]]
- [ ] [[Module 3 - OOP/6-Special-Methods|6. Special / Magic Methods (__str__, __init__)]]

### **Module 4: Version Control System** 🐙
- [ ] [[Module 4 - Version Control/README|Module Overview]]
- [ ] [[Module 4 - Version Control/1-Git-Basics|1. Git Basics & Branching]]
- [ ] [[Module 4 - Version Control/2-Remote-Repos|2. Remote Repos & Pull Requests]]
- [ ] [[Module 4 - Version Control/3-Branching-Strategies|3. Branching Strategies]]
- [ ] [[Module 4 - Version Control/4-Open-Source|4. Open Source & Licenses]]
- [ ] [[Module 4 - Version Control/5-Contribution-Workflow|5. Contribution & Peer Review]]
- [ ] [[Module 4 - Version Control/6-Advanced-Git|6. Advanced Git (Rebase, Stash, Reset)]]
- [ ] [[Module 4 - Version Control/7-Repo-Hygiene|7. Commit Messages & Repo Hygiene]]

---
> [[../Sem-Exam-Hub|Back to Main Master Hub]]
