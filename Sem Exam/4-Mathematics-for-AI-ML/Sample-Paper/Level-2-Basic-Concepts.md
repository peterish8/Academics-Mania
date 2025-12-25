# 🎮 Level 2: Basic Concepts

> [!TIP] **Level 2 Unlocked!**
> Building on fundamentals. Complete all 10 questions to unlock Level 3! 🎯

---

## 📝 Questions (10)

- [ ] **Q11.** If U={1,2,3,4,5} and A={1,3}, then A′ is:
  - (a) {1,3}
  - (b) {2,4,5}
  - (c) {4,5}
  - (d) {2,3,4}
  
  > [!SUCCESS]- Answer
  > **Answer: (b) {2,4,5}**
  > 
  > **Why:** A' = complement = all elements in U but NOT in A
  > 
  > **Common Confusion:** Forgetting elements (missing 2 or 5)
  > 
  > **Steps:**
  > 1. U = {1,2,3,4,5}
  > 2. A = {1,3}
  > 3. A' = U - A = {2,4,5}

- [ ] **Q12.** If P(A)=0.6, then P(A′) is:
  - (a) 0.6
  - (b) 0.4
  - (c) 1.6
  - (d) 0
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 0.4**
  > 
  > **Why:** Complement rule: P(A) + P(A') = 1
  > 
  > **Common Confusion:** Thinking P(A') = P(A)
  > 
  > **Formula:** P(A') = 1 - P(A)
  > 
  > **Steps:**
  > 1. P(A) = 0.6
  > 2. P(A') = 1 - 0.6 = 0.4

- [ ] **Q13.** The data 3, 7, 7, 9, 11 has mode:
  - (a) 3
  - (b) 7
  - (c) 9
  - (d) No mode
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 7**
  > 
  > **Why:** Mode = most frequently occurring value
  > 
  > **Common Confusion:** Choosing median (7) by coincidence
  > 
  > **Steps:**
  > 1. Count frequency: 3(1), 7(2), 9(1), 11(1)
  > 2. Highest frequency = 2 (for value 7)
  > 3. Mode = 7

- [ ] **Q14.** The median of the data 5, 2, 9, 4, 7 is:
  - (a) 4
  - (b) 5
  - (c) 7
  - (d) 9
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 5**
  > 
  > **Why:** Median = middle value after arranging in order
  > 
  > **Common Confusion:** Using unsorted data
  > 
  > **Steps:**
  > 1. Arrange: 2, 4, 5, 7, 9
  > 2. n = 5 (odd)
  > 3. Position = (5+1)/2 = 3rd term
  > 4. Median = 5

- [ ] **Q15.** The range of the data 5, 11, 18, 3, 20 is:
  - (a) 15
  - (b) 17
  - (c) 18
  - (d) 20
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 17**
  > 
  > **Why:** Range = Maximum - Minimum
  > 
  > **Common Confusion:** Choosing max value (20) instead of range
  > 
  > **Formula:** Range = Max - Min
  > 
  > **Steps:**
  > 1. Max = 20
  > 2. Min = 3
  > 3. Range = 20 - 3 = 17

- [ ] **Q16.** If A={2,4,6} and B={1,2,3}, then A∩B is:
  - (a) {1,3}
  - (b) {2}
  - (c) {2,4}
  - (d) ∅
  
  > [!SUCCESS]- Answer
  > **Answer: (b) {2}**
  > 
  > **Why:** A∩B = intersection = common elements in both sets
  > 
  > **Common Confusion:** Union (A∪B) vs Intersection (A∩B)
  > 
  > **Steps:**
  > 1. A = {2,4,6}
  > 2. B = {1,2,3}
  > 3. Common element = 2 only
  > 4. A∩B = {2}

- [ ] **Q17.** Which of the following is a discrete variable?
  - (a) Height of students
  - (b) Weight of objects
  - (c) Number of absentees
  - (d) Temperature
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Number of absentees**
  > 
  > **Why:** Discrete = countable, whole numbers only
  > 
  > **Common Confusion:** Continuous variables can have decimals
  > 
  > **Remember:**
  > - Discrete: Count (0,1,2,3...) - students, cars, books
  > - Continuous: Measure (can have decimals) - height, weight, temp

- [ ] **Q18.** The arithmetic mean of first 10 natural numbers is:
  - (a) 4.5
  - (b) 5
  - (c) 5.5
  - (d) 6
  
  > [!SUCCESS]- Answer
  > **Answer: (c) 5.5**
  > 
  > **Why:** Mean = Sum/n
  > 
  > **Common Confusion:** Using wrong formula or forgetting to divide
  > 
  > **Formula:** Mean = (n+1)/2 for first n natural numbers
  > 
  > **Steps:**
  > 1. First 10 natural numbers: 1,2,3...10
  > 2. Sum = 10(11)/2 = 55
  > 3. Mean = 55/10 = 5.5
  > OR: Mean = (10+1)/2 = 5.5

- [ ] **Q19.** If a set has 6 elements, how many subsets does it have?
  - (a) 6
  - (b) 12
  - (c) 32
  - (d) 64
  
  > [!SUCCESS]- Answer
  > **Answer: (d) 64**
  > 
  > **Why:** Number of subsets = 2^n (including empty set)
  > 
  > **Common Confusion:** Confusing with proper subsets (2^n - 1)
  > 
  > **Formula:** Total subsets = 2^n
  > 
  > **Steps:**
  > 1. n = 6
  > 2. Subsets = 2^6 = 64

- [ ] **Q20.** The number of elements in the power set of {a,b,c} is:
  - (a) 3
  - (b) 6
  - (c) 8
  - (d) 9
  
  > [!SUCCESS]- Answer
  > **Answer: (c) 8**
  > 
  > **Why:** Power set contains ALL subsets
  > 
  > **Common Confusion:** Counting only proper subsets
  > 
  > **Formula:** |P(A)| = 2^n where n = |A|
  > 
  > **Steps:**
  > 1. A = {a,b,c}, n = 3
  > 2. |P(A)| = 2^3 = 8
  > 3. Subsets: ∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}

---

## 🎯 Progress Tracker

```dataviewjs
const tasks = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/Level-2-Basic-Concepts.md").file.tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

dv.paragraph(`**Completion:** ${completed}/${total} questions`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">${percent}%</div></div>`);
```

> [!SUCCESS] **Level Complete!**
> Once you've checked all boxes, proceed to [[Level-3-Intermediate-Skills|Level 3 →]]

---

[[Level-1-Foundation-Basics|← Level 1]] | [[Sample-Paper-Hub|🏠 Hub]]
