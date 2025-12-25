# 🎮 Level 4: Applied Concepts

> [!TIP] **Level 4 Unlocked!**
> Mastering applications. Complete all 10 questions to unlock Level 5! 🔥

---

## 📝 Questions (10)

- [ ] **Q31.** Which of the following is a measure of dispersion?
  - (a) Mean
  - (b) Median
  - (c) Standard deviation
  - (d) Mode
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Standard deviation**
  > 
  > **Why:** SD measures spread/variability of data
  > 
  > **Common Confusion:** Mean, Median, Mode are central tendency (not dispersion)
  > 
  > **Dispersion measures:** SD, Variance, Range, IQR

- [ ] **Q32.** If the variance of a dataset is zero, then the data values are:
  - (a) Highly scattered
  - (b) All equal
  - (c) Positively skewed
  - (d) Random
  
  > [!SUCCESS]- Answer
  > **Answer: (b) All equal**
  > 
  > **Why:** Variance = 0 means NO variation = all values same
  > 
  > **Common Confusion:** Zero variance ≠ scattered data
  > 
  > **Logic:** If all values = x̄, then (x-x̄)² = 0 for all x

- [ ] **Q33.** Which graph is used to represent cumulative frequency?
  - (a) Histogram
  - (b) Frequency polygon
  - (c) Ogive
  - (d) Pie chart
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Ogive**
  > 
  > **Why:** Ogive = cumulative frequency curve
  > 
  > **Common Confusion:** Histogram shows frequency (not cumulative)
  > 
  > **Types:** Less than ogive, More than ogive

- [ ] **Q34.** Which logic gives output "False" only when both inputs are "True"?
  - (a) AND
  - (b) OR
  - (c) NAND
  - (d) XOR
  
  > [!SUCCESS]- Answer
  > **Answer: (c) NAND**
  > 
  > **Why:** NAND = NOT(AND) = opposite of AND
  > 
  > **Common Confusion:** AND gives True when both True
  > 
  > **Truth:** NAND(T,T) = F, all other combinations = T

- [ ] **Q35.** The complement of NAND is:
  - (a) OR
  - (b) AND
  - (c) XOR
  - (d) NOR
  
  > [!SUCCESS]- Answer
  > **Answer: (b) AND**
  > 
  > **Why:** NOT(NAND) = NOT(NOT(AND)) = AND
  > 
  > **Common Confusion:** Double negation cancels out
  > 
  > **Logic:** Complement of NAND = AND

- [ ] **Q36.** If f(x)=2x+5, then f⁻¹(x) is:
  - (a) (x−5)/2
  - (b) (x+5)/2
  - (c) 2x−5
  - (d) 5−2x
  
  > [!SUCCESS]- Answer
  > **Answer: (a) (x−5)/2**
  > 
  > **Why:** Inverse function reverses the operation
  > 
  > **Common Confusion:** Sign errors when solving for x
  > 
  > **Steps:**
  > 1. Let y = 2x + 5
  > 2. Swap: x = 2y + 5
  > 3. Solve for y: 2y = x - 5
  > 4. y = (x-5)/2
  > 5. f⁻¹(x) = (x-5)/2

- [ ] **Q37.** If f(x)=x−4, then f⁻¹(x) is:
  - (a) x−4
  - (b) x+4
  - (c) 4−x
  - (d) x/4
  
  > [!SUCCESS]- Answer
  > **Answer: (b) x+4**
  > 
  > **Why:** Inverse undoes the subtraction
  > 
  > **Common Confusion:** Forgetting to reverse the operation
  > 
  > **Steps:**
  > 1. y = x - 4
  > 2. x = y - 4
  > 3. y = x + 4
  > 4. f⁻¹(x) = x + 4

- [ ] **Q38.** A function that is both one-to-one and onto is called:
  - (a) Into function
  - (b) Many-to-one function
  - (c) Bijective function
  - (d) Constant function
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Bijective function**
  > 
  > **Why:** Bijective = Injective (1-1) + Surjective (onto)
  > 
  > **Common Confusion:** Into is NOT onto
  > 
  > **Remember:** Bijective = perfect pairing (one-to-one correspondence)

- [ ] **Q39.** If the mean of a data set is 20 and number of observations is 5, then the total sum of observations is:
  - (a) 80
  - (b) 90
  - (c) 100
  - (d) 120
  
  > [!SUCCESS]- Answer
  > **Answer: (c) 100**
  > 
  > **Why:** Mean = Sum/n, so Sum = Mean × n
  > 
  > **Common Confusion:** Dividing instead of multiplying
  > 
  > **Formula:** Sum = Mean × n
  > 
  > **Steps:**
  > 1. Mean = 20, n = 5
  > 2. Sum = 20 × 5 = 100

- [ ] **Q40.** Which distribution has zero skewness?
  - (a) Positively skewed
  - (b) Negatively skewed
  - (c) Symmetric
  - (d) Leptokurtic
  
  > [!SUCCESS]- Answer
  > **Answer: (c) Symmetric**
  > 
  > **Why:** Symmetric = no skewness = Mean = Median = Mode
  > 
  > **Common Confusion:** Leptokurtic refers to kurtosis (not skewness)
  > 
  > **Remember:** Skewness = 0 for symmetric distributions

---

## 🎯 Progress Tracker

```dataviewjs
const tasks = dv.page("4-Mathematics-for-AI-ML/Sample-Paper/Level-4-Applied-Concepts.md").file.tasks;
const completed = tasks.filter(t => t.completed).length;
const total = tasks.length;
const percent = total === 0 ? 0 : Math.round((completed / total) * 100);

dv.paragraph(`**Completion:** ${completed}/${total} questions`);
dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 12px;">${percent}%</div></div>`);
```

> [!SUCCESS] **Level Complete!**
> Once you've checked all boxes, proceed to [[Level-5-Calculation-Skills|Level 5 →]]

---

[[Level-3-Intermediate-Skills|← Level 3]] | [[Sample-Paper-Hub|🏠 Hub]]
