# 🎮 Level 7: Expert Level

> [!TIP] **Level 7 Unlocked!**
> Expert territory! Complete all 10 questions to unlock the Final Boss Level! 🏆

---

## 📝 Questions (10)

- [x] **Q61.** The number of elements in A×B if n(A)=4 and n(B)=3 is:
  - (a) 7
  - (b) 12
  - (c) 16
  - (d) 24
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 12**
  > 
  > **Why:** |A×B| = |A| × |B|
  > 
  > **Common Confusion:** Adding instead of multiplying
  > 
  > **Steps:**
  > 1. |A| = 4, |B| = 3
  > 2. |A×B| = 4 × 3 = 12

- [x] **Q62.** If events A and B are mutually exclusive, then:
  - (a) P(A∩B)=P(A)P(B)
  - (b) P(A∩B)=0
  - (c) P(A∪B)=0
  - (d) P(A)=P(B)
  
  > [!SUCCESS]- Answer
  > **Answer: (b) P(A∩B)=0**
  > 
  > **Why:** Mutually exclusive = cannot occur together
  > 
  > **Common Confusion:** (a) is for independent events
  > 
  > **Remember:** Mutually exclusive ≠ Independent

- [x] **Q63.** The standard deviation of the data 2, 4, 6, 8 is:
  - (a) 2
  - (b) 2.23
  - (c) 3
  - (d) 4
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 2.23**
  > 
  > **Why:** SD = √[Σ(x-x̄)²/n]
  > 
  > **Common Confusion:** Calculation errors
  > 
  > **Steps:**
  > 1. Mean = (2+4+6+8)/4 = 5
  > 2. Deviations: -3, -1, 1, 3
  > 3. Squared: 9, 1, 1, 9
  > 4. Variance = 20/4 = 5
  > 5. SD = √5 ≈ 2.236 ≈ 2.23

- [ ] **Q64.** 4, 9, 11, 13, 18, 20. Find MD from Median
  - (a) 4.1
  - (b) 4.3
  - (c) 4.5
  - (d) 4.7
  
  > [!SUCCESS]- Answer
  > **Answer: (c) 4.5**
  > 
  > **Why:** MD = Σ|x - Median|/n
  > 
  > **Common Confusion:** Using mean instead of median
  > 
  > **Steps:**
  > 1. Data already sorted
  > 2. Median = (11+13)/2 = 12
  > 3. |4-12| + |9-12| + |11-12| + |13-12| + |18-12| + |20-12|
  > 4. = 8 + 3 + 1 + 1 + 6 + 8 = 27
  > 5. MD = 27/6 = 4.5

- [x] **Q65.** The geometric mean of 4 and 16 is:
  - (a) 8
  - (b) 10
  - (c) 12
  - (d) 6
  
  > [!SUCCESS]- Answer
  > **Answer: (a) 8**
  > 
  > **Why:** GM = √(a × b) for two numbers
  > 
  > **Common Confusion:** Using AM formula
  > 
  > **Steps:**
  > 1. GM = √(4 × 16)
  > 2. GM = √64 = 8

- [x] **Q66.** The data having more values on right side is:
  - (a) Symmetric
  - (b) Negatively skewed
  - (c) Positively skewed
  - (d) Uniform
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Positively skewed**
  > 
  > **Why:** More values on right = tail extends right
  > 
  > **Common Confusion:** Direction of skew vs tail
  > 
  > **Remember:** Skewness named by tail direction, not bulk

- [x] **Q67.** Which relation is both reflexive and transitive but not symmetric?
  - (a) Equivalence
  - (b) Partial order
  - (c) Symmetric relation
  - (d) Identity relation
  
  > [!SUCCESS]- Answer
  > **Answer: (b) Partial order**
  > 
  > **Why:** Partial order = Reflexive + Transitive (NOT symmetric)
  > 
  > **Common Confusion:** Equivalence has all three properties
  > 
  > **Example:** ≤ relation (reflexive, transitive, not symmetric)

- [x] **Q68.** The probability of drawing a face card from a deck is:
  - (a) 1/13
  - (b) 3/13
  - (c) 1/4
  - (d) 1/2
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 3/13**
  > 
  > **Why:** 12 face cards (J,Q,K in 4 suits) out of 52
  > 
  > **Common Confusion:** Counting only one suit
  > 
  > **Steps:**
  > 1. Face cards = 3 per suit × 4 suits = 12
  > 2. Total = 52
  > 3. P = 12/52 = 3/13

- [x] **Q69.** The logical equivalence of (p→q) is:
  - (a) p∧q
  - (b) ¬p∨q
  - (c) p∨q
  - (d) ¬(p∧q)
  
  > [!SUCCESS]- Answer
  > **Answer: (b) ¬p∨q**
  > 
  > **Why:** Implication: p→q ≡ ¬p∨q
  > 
  > **Common Confusion:** Thinking it's p∧q
  > 
  > **Truth table:** Both give same results

- [x] **Q70.** If Mean = Median, the distribution is:
  - (a) Positively skewed
  - (b) Negatively skewed
  - (c) Symmetric
  - (d) Bimodal
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Symmetric**
  > 
  > **Why:** Mean = Median = Mode for symmetric distribution
  > 
  > **Common Confusion:** Bimodal can be symmetric or skewed
  > 
  > **Remember:** Symmetric ⇒ no skewness

---

## 🎯 Progress Tracker

```dataviewjs
const tasks = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/Level-7-Expert-Level.md").file.tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

dv.paragraph(`**Completion:** ${completed}/${total} questions`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">${percent}%</div></div>`);
```

> [!SUCCESS] **Level Complete!**
> Once you've checked all boxes, proceed to [[Level-8-Final-Boss|Level 8 - Final Boss →]]

---

[[Level-6-Advanced-Problems|← Level 6]] | [[Sample-Paper-Hub|🏠 Hub]]
