# 🎮 Level 8: Final Boss 🏆

> [!CAUTION] **Final Boss Level!**
> The ultimate challenge! Complete all 5 questions to become a Math Master! 👑

---

## 📝 Questions (5)

- [x] **Q71.** The harmonic mean of 6 and 12 is:
  - (a) 8
  - (b) 9
  - (c) 10
  - (d) 7
  
  > [!SUCCESS]- Answer
  > **Answer: (a) 8**
  > 
  > **Why:** HM = n/(Σ(1/x))
  > 
  > **Common Confusion:** Using AM or GM formula
  > 
  > **Formula:** HM = 2/(1/a + 1/b) for two numbers
  > 
  > **Steps:**
  > 1. HM = 2/(1/6 + 1/12)
  > 2. = 2/(2/12 + 1/12)
  > 3. = 2/(3/12)
  > 4. = 2 × 4 = 8

- [x] **Q72.** A bag contains 5 red balls and 7 blue balls. Two balls are drawn at random without replacement. Find the probability that both balls drawn are red.
  - (a) 4/33
  - (b) none
  - (c) 2/33
  - (d) 5/33
  
  > [!SUCCESS]- Answer
  > **Answer: (d) 5/33**
  > 
  > **Why:** Dependent events (without replacement)
  > 
  > **Common Confusion:** Treating as independent
  > 
  > **Formula:** P(R₁ ∩ R₂) = P(R₁) × P(R₂|R₁)
  > 
  > **Steps:**
  > 1. Total = 5 + 7 = 12
  > 2. P(R₁) = 5/12
  > 3. P(R₂|R₁) = 4/11 (4 red left, 11 total)
  > 4. P(both red) = (5/12) × (4/11)
  > 5. = 20/132 = 5/33

- [x] **Q73.** In a class of 80 students, 35 play cricket, 45 play football, and 15 play both. How many play neither?
  - (a) 16.5
  - (b) 14
  - (c) 16
  - (d) 15
  
  > [!SUCCESS]- Answer
  > **Answer: (d) 15**
  > 
  > **Why:** Use inclusion-exclusion principle
  > 
  > **Common Confusion:** Forgetting to subtract those who play both
  > 
  > **Formula:** n(A∪B) = n(A) + n(B) - n(A∩B)
  > 
  > **Steps:**
  > 1. Total = 80
  > 2. n(C∪F) = 35 + 45 - 15 = 65
  > 3. Neither = 80 - 65 = 15

- [x] **Q74.** Class Interval (x): 0–10, 10–20, 20–30, 30–40, 40–50, 50–60, 60–70  
  Frequency (f): 4, 8, 14, 22, 18, 12, 6  
  Find Q₁, D₇, and P₉₀ for the following grouped data:
  - (a) Q₁: 26, D₇: 46.43, P₉₀: 58
  - (b) Q₁: 26.43, D₇: 46, P₉₀: 58
  - (c) Q₁: 26.43, D₇: 46, P₉₀: 58.43
  - (d) None
  
  > [!SUCCESS]- Answer
  > **Answer: (b) Q₁: 26.43, D₇: 46, P₉₀: 58**
  > 
  > **Why:** Use formulas for grouped data
  > 
  > **Common Confusion:** Wrong class identification or CF errors
  > 
  > **Formula:** Value = L + [(Position - CF)/f] × h
  > 
  > **Steps:**
  > 1. N = 84, CF: 4, 12, 26, 48, 66, 78, 84
  > 2. **Q₁:** Position = N/4 = 21 → class 20-30
  >    - L=20, CF=12, f=14, h=10
  >    - Q₁ = 20 + [(21-12)/14]×10 = 20 + 6.43 = 26.43
  > 3. **D₇:** Position = 7N/10 = 58.8 → class 40-50
  >    - L=40, CF=48, f=18, h=10
  >    - D₇ = 40 + [(58.8-48)/18]×10 = 40 + 6 = 46
  > 4. **P₉₀:** Position = 90N/100 = 75.6 → class 50-60
  >    - L=50, CF=66, f=12, h=10
  >    - P₉₀ = 50 + [(75.6-66)/12]×10 = 50 + 8 = 58

- [x] **Q75.** Which of the following distributions has β₂ > 3?
  - (a) Mesokurtic
  - (b) Platykurtic
  - (c) Leptokurtic
  - (d) Symmetric
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Leptokurtic**
  > 
  > **Why:** Leptokurtic = heavy tails, sharp peak
  > 
  > **Common Confusion:** Mesokurtic has β₂ = 3
  > 
  > **Remember:**
  > - β₂ > 3: Leptokurtic (heavy tails)
  > - β₂ = 3: Mesokurtic (normal)
  > - β₂ < 3: Platykurtic (light tails)

---

## 🎯 Progress Tracker

```dataviewjs
const tasks = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/Level-8-Final-Boss.md").file.tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

dv.paragraph(`**Completion:** ${completed}/${total} questions`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">${percent}%</div></div>`);
```

> [!SUCCESS] **🎉 CONGRATULATIONS! 🎉**
> Once you've checked all boxes, you've mastered all 75 questions!
> 
> **You are now a Mathematics for AI/ML Expert!** 👑

---

## 🏆 Achievement Unlocked

**Total Questions Completed:** 75/75

**Levels Mastered:**
- ✅ Level 1: Foundation Basics
- ✅ Level 2: Basic Concepts
- ✅ Level 3: Intermediate Skills
- ✅ Level 4: Applied Concepts
- ✅ Level 5: Calculation Skills
- ✅ Level 6: Advanced Problems
- ✅ Level 7: Expert Level
- ✅ Level 8: Final Boss

---

[[Level-7-Expert-Level|← Level 7]] | [[Sample-Paper-Hub|🏠 Hub]]
