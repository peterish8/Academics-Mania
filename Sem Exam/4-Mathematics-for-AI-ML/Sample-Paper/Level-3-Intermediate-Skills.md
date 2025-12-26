# 🎮 Level 3: Intermediate Skills

> [!TIP] **Level 3 Unlocked!**
> Applying concepts. Complete all 10 questions to unlock Level 4! 💪

---

## 📝 Questions (10)

- [x] **Q21.** A relation R on set A is said to be reflexive if:
  - (a) (a,b)∈R ⇒ (b,a)∈R
  - (b) (a,a)∈R for all a∈A
  - (c) (a,b),(b,c)∈R ⇒ (a,c)∈R
  - (d) R = ∅
  
  > [!SUCCESS]- Answer
  > **Answer: (b) (a,a)∈R for all a∈A**
  > 
  > **Why:** Reflexive = every element relates to itself
  > 
  > **Common Confusion:**
  > - (a) is Symmetric
  > - (c) is Transitive
  > 
  > **Remember:** Reflexive = self-loop for ALL elements

- [x] **Q22.** A relation which is reflexive, symmetric and transitive is called:
  - (a) Partial order
  - (b) Symmetric relation
  - (c) Equivalence relation
  - (d) Identity relation
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Equivalence relation**
  > 
  > **Why:** Equivalence = ALL three properties (R, S, T)
  > 
  > **Common Confusion:** Partial order is reflexive + transitive (NOT symmetric)
  > 
  > **Remember:** Equivalence = Reflexive + Symmetric + Transitive

- [x] **Q23.** Which of the following relations is symmetric?
  - (a) {(1,2)}
  - (b) {(1,2),(2,1)}
  - (c) {(1,1),(2,3)}
  - (d) {(1,2),(2,3)}
  
  > [!SUCCESS]- Answer
  > **Answer: (b) {(1,2),(2,1)}**
  > 
  > **Why:** Symmetric means if (a,b)∈R then (b,a)∈R
  > 
  > **Common Confusion:** Missing the reverse pair
  > 
  > **Check:** (1,2) is in R, so (2,1) must also be in R ✓

- [x] **Q24.** A function is called one-to-one if:
  - (a) Every element of codomain has a preimage
  - (b) Different domain elements map to different images
  - (c) Same domain elements map to different images
  - (d) It is not onto
  
  > [!SUCCESS]- Answer
  > **Answer: (b) Different domain elements map to different images**
  > 
  > **Why:** One-to-one (injective) = no two inputs give same output
  > 
  > **Common Confusion:** (a) describes Onto function
  > 
  > **Test:** If f(x₁) = f(x₂), then x₁ = x₂

- [x] **Q25.** A function where multiple domain elements map to one range element is:
  - (a) One-to-one
  - (b) Onto
  - (c) Many-to-one
  - (d) Bijective
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Many-to-one**
  > 
  > **Why:** Multiple inputs → same output = many-to-one
  > 
  > **Common Confusion:** Bijective is one-to-one AND onto
  > 
  > **Example:** f(x) = x² is many-to-one (f(2) = f(-2) = 4)

- [x] **Q26.** If events A and B are mutually exclusive, then P(A∩B) is:
  - (a) 1
  - (b) 0
  - (c) P(A)+P(B)
  - (d) Cannot be determined
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 0**
  > 
  > **Why:** Mutually exclusive = cannot happen together
  > 
  > **Common Confusion:** P(A∪B) = P(A) + P(B) for mutually exclusive
  > 
  > **Remember:** Mutually exclusive ⇒ P(A∩B) = 0

- [x] **Q27.** If two events A and B are independent, then:
  - (a) P(A∩B)=0
  - (b) P(A∩B)=P(A)+P(B)
  - (c) P(A∩B)=P(A)P(B)
  - (d) P(A∪B)=1
  
  > [!SUCCESS]- Answer
  > **Answer: (c) P(A∩B)=P(A)P(B)**
  > 
  > **Why:** Independent = one event doesn't affect the other
  > 
  > **Common Confusion:** Don't confuse with mutually exclusive
  > 
  > **Formula:** Independent ⇒ P(A∩B) = P(A) × P(B)

- [x] **Q28.** If A = {1,2,3} and B = {4,5}, then n(A×B) equals:
  - (a) 5
  - (b) 6
  - (c) 7
  - (d) 8
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 6**
  > 
  > **Why:** Cartesian product = all ordered pairs
  > 
  > **Common Confusion:** Adding |A| + |B| instead of multiplying
  > 
  > **Formula:** |A×B| = |A| × |B|
  > 
  > **Steps:**
  > 1. |A| = 3, |B| = 2
  > 2. |A×B| = 3 × 2 = 6

- [x] **Q29.** If n(A)=3, then number of proper subsets of A is:
  - (a) 6
  - (b) 7
  - (c) 8
  - (d) 9
  
  > [!SUCCESS]- Answer
  > **Answer: (b) 7**
  > 
  > **Why:** Proper subsets = all subsets EXCEPT the set itself
  > 
  > **Common Confusion:** Total subsets = 2^n (includes the set)
  > 
  > **Formula:** Proper subsets = 2^n - 1
  > 
  > **Steps:**
  > 1. n = 3
  > 2. Total subsets = 2^3 = 8
  > 3. Proper subsets = 8 - 1 = 7

- [x] **Q30.** The standard deviation is the square root of:
  - (a) Mean deviation
  - (b) Variance
  - (c) Range
  - (d) Quartile deviation
  
  > [!SUCCESS]- Answer
  > **Answer: (b) Variance**
  > 
  > **Why:** SD = √Variance (by definition)
  > 
  > **Common Confusion:** Mean deviation is different from SD
  > 
  > **Formula:** σ = √(Variance)
  > 
  > **Remember:** Variance = σ², SD = σ

---

## 🎯 Progress Tracker

```dataviewjs
const tasks = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/Level-3-Intermediate-Skills.md").file.tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

dv.paragraph(`**Completion:** ${completed}/${total} questions`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">${percent}%</div></div>`);
```

> [!SUCCESS] **Level Complete!**
> Once you've checked all boxes, proceed to [[Level-4-Applied-Concepts|Level 4 →]]

---

[[Level-2-Basic-Concepts|← Level 2]] | [[Sample-Paper-Hub|🏠 Hub]]
