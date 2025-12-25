# 🎮 Level 1: Foundation Basics (Beginner)

> [!TIP] **Level 1 Unlocked!**
> Master the fundamentals. Complete all 10 questions to unlock Level 2! 🚀

---

## 📝 Questions (10)

- [ ] **Q1.** Which logical operation produces output "True" only when both inputs are "True"?
  - (a) OR
  - (b) XOR
  - (c) AND
  - (d) NOR
  
  > [!SUCCESS]- Answer
  > **Answer: (c) AND**
  > 
  > **Why:** AND gate requires BOTH inputs to be True for output to be True.
  > 
  > **Common Confusion:** Students confuse with OR (needs at least one True)
  > 
  > **Quick Check:**
  > - AND: True AND True = True (both must be True)
  > - OR: True OR False = True (at least one True)

- [ ] **Q2.** A set containing a finite number of elements is called:
  - (a) Infinite set
  - (b) Empty set
  - (c) Finite set
  - (d) Universal set
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Finite set**
  > 
  > **Why:** Finite = countable/limited number of elements
  > 
  > **Common Confusion:** Empty set (has 0 elements, still finite)
  > 
  > **Examples:**
  > - Finite: {1,2,3}, {a,b}
  > - Infinite: Natural numbers, Real numbers

- [ ] **Q3.** The middle value of an ordered data set is called:
  - (a) Mean
  - (b) Mode
  - (c) Median
  - (d) Range
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Median**
  > 
  > **Why:** Median = middle value when data is arranged in order
  > 
  > **Common Confusion:** Mean (average), Mode (most frequent)
  > 
  > **Formula:**
  > - Odd n: Median = (n+1)/2 th term
  > - Even n: Median = average of n/2 and (n/2)+1 terms

- [ ] **Q4.** The probability of an impossible event is:
  - (a) 0
  - (b) 1
  - (c) −1
  - (d) Undefined
  
  > [!SUCCESS]- Answer
  > **Answer: (a) 0**
  > 
  > **Why:** Impossible event = cannot happen = P = 0
  > 
  > **Common Confusion:** Probability range is 0 to 1 (never negative)
  > 
  > **Remember:**
  > - Impossible event: P = 0
  > - Sure/Certain event: P = 1
  > - Any event: 0 ≤ P ≤ 1

- [ ] **Q5.** The probability of a sure event is:
  - (a) 0
  - (b) 0.5
  - (c) 1
  - (d) −1
  
  > [!SUCCESS]- Answer
  > **Answer: (c) 1**
  > 
  > **Why:** Sure event = definitely happens = P = 1
  > 
  > **Common Confusion:** 0.5 is for equally likely events (like fair coin)
  > 
  > **Example:** Probability of getting a number ≤ 6 on a dice = 6/6 = 1

- [ ] **Q6.** The set of all subsets of a set A is called:
  - (a) Universal set
  - (b) Power set
  - (c) Cartesian set
  - (d) Empty set
  
  > [!SUCCESS]- Answer
  > **Answer: (b) Power set**
  > 
  > **Why:** Power set P(A) = collection of ALL possible subsets
  > 
  > **Common Confusion:** Universal set (contains all elements under consideration)
  > 
  > **Formula:** If |A| = n, then |P(A)| = 2ⁿ
  > 
  > **Example:** A = {1,2} → P(A) = {∅, {1}, {2}, {1,2}} (4 subsets)

- [ ] **Q7.** Which of the following is NOT a measure of central tendency?
  - (a) Mean
  - (b) Median
  - (c) Variance
  - (d) Mode
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Variance**
  > 
  > **Why:** Variance measures DISPERSION (spread), not central tendency
  > 
  > **Common Confusion:** All measure "average" but variance measures spread
  > 
  > **Remember:**
  > - Central Tendency: Mean, Median, Mode (center of data)
  > - Dispersion: Variance, SD, Range (spread of data)

- [ ] **Q8.** The complement of OR is:
  - (a) AND
  - (b) XOR
  - (c) NAND
  - (d) NOR
  
  > [!SUCCESS]- Answer
  > **Answer: (d) NOR**
  > 
  > **Why:** NOR = NOT(OR) = complement of OR
  > 
  > **Common Confusion:** NAND is complement of AND, not OR
  > 
  > **De Morgan's Law:**
  > - NOR: NOT(A OR B) = (NOT A) AND (NOT B) = A' · B'
  > - In other words: NOR outputs True only when BOTH inputs are False


- [ ] **Q9.** Which logical connective represents biconditional?
  - (a) →
  - (b) ∧
  - (c) ↔
  - (d) ¬
  
  > [!SUCCESS]- Answer
  > **Answer: (c) ↔**
  > 
  > **Why:** ↔ means "if and only if" (both directions)
  > 
  > **Common Confusion:** → is implication (one direction only)
  > 
  > **Symbols:**
  > - → : Implication (if...then)
  > - ↔ : Biconditional (if and only if)
  > - ∧ : AND
  > - ¬ : NOT

- [ ] **Q10.** The Cartesian product A×B consists of:
  - (a) Sets
  - (b) Numbers
  - (c) Ordered pairs
  - (d) Functions
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Ordered pairs**
  > 
  > **Why:** A×B = {(a,b) | a∈A, b∈B} = set of ordered pairs
  > 
  > **Common Confusion:** Order matters! (a,b) ≠ (b,a)
  > 
  > **Formula:** |A×B| = |A| × |B|
  > 
  > **Example:** A={1,2}, B={3,4}
  > A×B = {(1,3), (1,4), (2,3), (2,4)} (4 ordered pairs)

---

## 🎯 Progress Tracker

```dataviewjs
const tasks = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/Level-1-Foundation-Basics.md").file.tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

dv.paragraph(`**Completion:** ${completed}/${total} questions`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">${percent}%</div></div>`);
```

> [!SUCCESS] **Level Complete!**
> Once you've checked all boxes, proceed to [[Level-2-Basic-Concepts|Level 2 →]]

---

[[Sample-Paper-Hub|🏠 Sample Paper Hub]]
