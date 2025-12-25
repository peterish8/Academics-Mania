# 🎮 Sample Paper Hub - Gamified Learning

> [!INFO] **Welcome to the Math Sample Paper Challenge!**
> Complete all 8 levels to master Mathematics for AI/ML! Each level builds on the previous one. Track your progress and level up! 🚀

---

## 📊 Overall Progress Tracker

```dataviewjs
const levels = [
    "Level-1-Foundation-Basics.md",
    "Level-2-Basic-Concepts.md",
    "Level-3-Intermediate-Skills.md",
    "Level-4-Applied-Concepts.md",
    "Level-5-Calculation-Skills.md",
    "Level-6-Advanced-Problems.md",
    "Level-7-Expert-Level.md",
    "Level-8-Final-Boss.md"
];

let totalQuestions = 0;
let completedQuestions = 0;

for (const level of levels) {
    const page = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/" + level);
    if (page?.file?.tasks) {
        const tasks = page.file.tasks;
        totalQuestions += tasks.length;
        completedQuestions += tasks.filter(t => t.completed).length;
    }
}

const percent = totalQuestions === 0 ? 0 : Math.round((completedQuestions / totalQuestions) * 100);

dv.paragraph(`**Overall Progress:** ${completedQuestions}/${totalQuestions} Questions Completed (**${percent}%**)`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 25px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">${percent}%</div></div>`);
```

---

## 🎯 Level System

### 🟢 Level 1: Foundation Basics
**Difficulty:** ⭐ Beginner  
**Questions:** 10  
**Topics:** Basic logic, sets, probability, central tendency

- [ ] Complete all 10 questions

[[Level-1-Foundation-Basics|Start Level 1 →]]

---

### 🟢 Level 2: Basic Concepts
**Difficulty:** ⭐⭐ Easy  
**Questions:** 10  
**Topics:** Set operations, complements, basic statistics

- [ ] Complete all 10 questions

[[Level-2-Basic-Concepts|Start Level 2 →]]

---

### 🟡 Level 3: Intermediate Skills
**Difficulty:** ⭐⭐⭐ Medium  
**Questions:** 10  
**Topics:** Relations, functions, probability rules

- [ ] Complete all 10 questions

[[Level-3-Intermediate-Skills|Start Level 3 →]]

---

### 🟡 Level 4: Applied Concepts
**Difficulty:** ⭐⭐⭐ Medium  
**Questions:** 10  
**Topics:** Dispersion, inverse functions, skewness

- [ ] Complete all 10 questions

[[Level-4-Applied-Concepts|Start Level 4 →]]

---

### 🟠 Level 5: Calculation Skills
**Difficulty:** ⭐⭐⭐⭐ Hard  
**Questions:** 10  
**Topics:** CV, means, MD, conditional probability

- [ ] Complete all 10 questions

[[Level-5-Calculation-Skills|Start Level 5 →]]

---

### 🟠 Level 6: Advanced Problems
**Difficulty:** ⭐⭐⭐⭐ Hard  
**Questions:** 10  
**Topics:** SD, kurtosis, bijective functions

- [ ] Complete all 10 questions

[[Level-6-Advanced-Problems|Start Level 6 →]]

---

### 🔴 Level 7: Expert Level
**Difficulty:** ⭐⭐⭐⭐⭐ Expert  
**Questions:** 10  
**Topics:** Complex relations, logical equivalence, distributions

- [ ] Complete all 10 questions

[[Level-7-Expert-Level|Start Level 7 →]]

---

### 🔴 Level 8: Final Boss
**Difficulty:** ⭐⭐⭐⭐⭐ Master  
**Questions:** 5  
**Topics:** Advanced calculations, grouped data, complex probability

- [ ] Complete all 5 questions

[[Level-8-Final-Boss|Start Level 8 →]]

---

## 📈 Exam Information

**Total Questions:** 75  
**Total Marks:** 50  
**Time:** 2 hours  
**Sections:**
- Section A: 50 questions × 0.5 marks = 25 marks
- Section B: 25 questions × 1 mark = 25 marks

---

## 🏆 Achievements

- [ ] **Beginner** - Complete Levels 1-2 (20 questions)
- [ ] **Intermediate** - Complete Levels 3-4 (40 questions)
- [ ] **Advanced** - Complete Levels 5-6 (60 questions)
- [ ] **Expert** - Complete Level 7 (70 questions)
- [ ] **Master** - Complete Level 8 (75 questions) 👑

---

## 💡 Study Tips

1. **Start from Level 1** - Build strong foundations
2. **Complete each level** before moving to the next
3. **Review wrong answers** using the notes
4. **Track your progress** with checkboxes
5. **Celebrate milestones** - Each level completed is an achievement!

---

## 📚 Quick Links to Notes

- [[1-Logic-and-Critical-Thinking|Logic Notes]]
- [[2-Sets-and-Functions|Sets & Functions]]
- [[4-Measures-of-Central-Tendency|Central Tendency]]
- [[6-Measures-of-Dispersion|Dispersion]]
- [[7-Probability|Probability]]
- [[8-Moments-Skewness-Kurtosis|Moments & Skewness]]

---

[[Math-AI-ML-Hub|← Back to Math Hub]]
