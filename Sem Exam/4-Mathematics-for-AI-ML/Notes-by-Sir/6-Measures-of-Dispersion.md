# 📊 Measures of Dispersion - Complete Notes

---

## 📌 QUARTILES

> [!INFO] **Definition: Quartiles**
> Quartiles divide the data into **4 equal parts**.

### Quartile Positions

| Quartile | Position | Meaning |
|----------|----------|---------|
| **Q₁** (First Quartile) | 25% | 25% of data lies below it |
| **Q₂** (Second Quartile) | 50% | 50% of data lies below it (Median) |
| **Q₃** (Third Quartile) | 75% | 75% of data lies below it |

---

### Formula for Individual & Discrete Series

```
Qₖ = k(n + 1)/4 th term

where k = 1, 2, or 3
```

---

### Example 1: Individual Series

**Data:** 5, 7, 9, 12, 13, 20, 21, 25

**Solution:**

Here n = 8

**Finding Q₁:**
```
Q₁ = (8 + 1)/4 th term
Q₁ = 2.25th term
Q₁ = 2nd term + 0.25(3rd term - 2nd term)
Q₁ = 7 + 0.25(9 - 7)
Q₁ = 7 + 0.5
Q₁ = 7.5
```

**Finding Q₂:**
```
Q₂ = 2(8 + 1)/4 th term
Q₂ = 4.5th term
Q₂ = 4th term + 0.5(5th term - 4th term)
Q₂ = 12 + 0.5(13 - 12)
Q₂ = 12.5
```

**Finding Q₃:**
```
Q₃ = 3(8 + 1)/4 th term
Q₃ = 6.75th term
Q₃ = 6th term + 0.75(7th term - 6th term)
Q₃ = 20 + 0.75(21 - 20)
Q₃ = 20.75
```

**Results:** Q₁ = 7.5, Q₂ = 12.5, Q₃ = 20.75

---

### Example 2: Discrete Series - Find Q₃

| x | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| f | 4 | 7 | 12 | 9 | 5 | 3 |
| **CF** | 4 | 11 | 23 | 32 | 37 | 40 |

**Solution:**
```
n = 40

Q₃ = 3(n + 1)/4 th term
Q₃ = 3(41)/4 th term
Q₃ = 30.75th term

Looking at CF, 30.75th term falls in x = 5
Therefore, Q₃ = 5
```

---

### Formula for Continuous Series

```
Qₖ = L + [(kN/4 - CF)/f] × h

where:
L = Lower boundary of quartile class
N = Total frequency
CF = Cumulative frequency before quartile class
f = Frequency of quartile class
h = Class width
k = 1, 2, or 3
```

---

### Example 3: Continuous Series - Find Q₁ and Q₃

| C.I | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 |
|-----|------|-------|-------|-------|-------|-------|-------|
| f | 5 | 9 | 16 | 25 | 20 | 15 | 10 |
| **CF** | 5 | 14 | 30 | 55 | 75 | 90 | 100 |

**Solution:**

Here, N = 100, h = 10

**Finding Q₁:**
```
kN/4 = 1(100)/4 = 25th term

Quartile class: 20-30 (CF = 30 ≥ 25)
L = 20, CF = 14, f = 16, h = 10

Q₁ = 20 + [(100/4 - 14)/16] × 10
Q₁ = 20 + [(25 - 14)/16] × 10
Q₁ = 20 + 6.875
Q₁ = 26.875
```

**Finding Q₃:**
```
kN/4 = 3(100)/4 = 75th term

Quartile class: 40-50 (CF = 75 ≥ 75)
L = 40, CF = 55, f = 20, h = 10

Q₃ = 40 + [(75 - 55)/20] × 10
Q₃ = 40 + 10
Q₃ = 50
```

**Results:** Q₁ = 26.875, Q₃ = 50

---

## 📌 DECILES

> [!INFO] **Definition: Deciles**
> Deciles divide the data into **10 equal parts**.

**Positions:** D₁ (10%), D₂ (20%), D₃ (30%), ..., D₈ (80%), D₉ (90%)

---

### Formula for Individual & Discrete Series

```
Dₖ = k(n + 1)/10 th term

where k = 1, 2, 3, ..., 9
```

---

### Example 1: Individual Series - Find D₁ and D₉

**Data:** 18, 32, 25, 28, 15, 40, 22, 35, 30, 26, 20, 38

**Solution:**

**Step 1:** Arrange in ascending order
```
15, 18, 20, 22, 25, 26, 28, 30, 32, 35, 38, 40
```

Here, n = 12

**Finding D₁:**
```
D₁ = (12 + 1)/10 th term
D₁ = 1.3th term
D₁ = 1st term + 0.3(2nd term - 1st term)
D₁ = 15 + 0.3(18 - 15)
D₁ = 15 + 0.9
D₁ = 15.9
```

**Finding D₉:**
```
D₉ = 9(12 + 1)/10 th term
D₉ = 11.7th term
D₉ = 11th term + 0.7(12th term - 11th term)
D₉ = 38 + 0.7(40 - 38)
D₉ = 38 + 1.4
D₉ = 39.4
```

**Results:** D₁ = 15.9, D₉ = 39.4

---

### Example 2: Discrete Series - Find D₇

| x | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| f | 4 | 7 | 12 | 9 | 5 | 3 |
| **CF** | 4 | 11 | 23 | 32 | 37 | 40 |

**Solution:**
```
n = 40

D₇ = 7(40 + 1)/10 th term
D₇ = 28.7th term

Looking at CF, 28.7th term falls in x = 5
Therefore, D₇ = 5
```

---

### Formula for Continuous Series

```
Dₖ = L + [(kN/10 - CF)/f] × h

where:
L = Lower boundary of decile class
N = Total frequency
CF = Cumulative frequency before decile class
f = Frequency of decile class
h = Class width
k = 1, 2, 3, ..., 9
```

---

### Example 3: Continuous Series - Find D₉

| C.I | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 |
|-----|------|-------|-------|-------|-------|-------|-------|
| f | 5 | 9 | 16 | 25 | 20 | 15 | 10 |
| **CF** | 5 | 14 | 30 | 55 | 75 | 90 | 100 |

**Solution:**
```
N = 100, h = 10

kN/10 = 9(100)/10 = 90th term

Decile class: 50-60 (CF = 90 ≥ 90)
L = 50, CF = 75, f = 15, h = 10

D₉ = 50 + [(9(100)/10 - 75)/15] × 10
D₉ = 50 + [(90 - 75)/15] × 10
D₉ = 50 + 10
D₉ = 60
```

**Result:** D₉ = 60

---

## 📌 PERCENTILES

> [!INFO] **Definition: Percentiles**
> Percentiles divide the data into **100 equal parts**.

**Special Cases:**
- P₅₀ = Median
- P₂₅ = Q₁
- P₇₅ = Q₃

---

### Formula for Individual & Discrete Series

```
Pₖ = k(n + 1)/100 th term

where k = 1, 2, 3, ..., 99
```

---

### Example 1: Individual Series - Find P₁₀ and P₉₀

**Data:** 18, 32, 25, 28, 15, 40, 22, 35, 30, 26, 20, 38

**Solution:**

**Step 1:** Arrange in ascending order
```
15, 18, 20, 22, 25, 26, 28, 30, 32, 35, 38, 40
```

Here, n = 12

**Finding P₁₀:**
```
P₁₀ = 10(12 + 1)/100 th term
P₁₀ = 1.3th term
P₁₀ = 1st term + 0.3(2nd term - 1st term)
P₁₀ = 15 + 0.3(18 - 15)
P₁₀ = 15.9
```

**Finding P₉₀:**
```
P₉₀ = 90(12 + 1)/100 th term
P₉₀ = 11.7th term
P₉₀ = 11th term + 0.7(12th term - 11th term)
P₉₀ = 38 + 0.7(40 - 38)
P₉₀ = 39.4
```

**Results:** P₁₀ = 15.9, P₉₀ = 39.4

---

### Example 2: Discrete Series - Find P₆₀

| x | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| f | 4 | 7 | 12 | 9 | 5 | 3 |
| **CF** | 4 | 11 | 23 | 32 | 37 | 40 |

**Solution:**
```
n = 40

P₆₀ = 60(40 + 1)/100 th term
P₆₀ = 24.6th term

Looking at CF, 24.6th term falls in x = 5
Therefore, P₆₀ = 5
```

---

### Formula for Continuous Series

```
Pₖ = L + [(kN/100 - CF)/f] × h

where:
L = Lower boundary of percentile class
N = Total frequency
CF = Cumulative frequency before percentile class
f = Frequency of percentile class
h = Class width
k = 1, 2, 3, ..., 99
```

---

### Example 3: Continuous Series - Find P₂₅, P₅₀, P₇₅

| C.I | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 |
|-----|------|-------|-------|-------|-------|-------|-------|
| f | 5 | 9 | 16 | 25 | 20 | 15 | 10 |
| **CF** | 5 | 14 | 30 | 55 | 75 | 90 | 100 |

**Solution:**

N = 100, h = 10

**Finding P₂₅:**
```
kN/100 = 25(100)/100 = 25th term

Percentile class: 20-30 (CF = 30 ≥ 25)
L = 20, CF = 14, f = 16, h = 10

P₂₅ = 20 + [(25 - 14)/16] × 10
P₂₅ = 20 + 6.875
P₂₅ = 26.875
```

**Finding P₅₀ (Median):**
```
kN/100 = 50(100)/100 = 50th term

Percentile class: 30-40 (CF = 55 ≥ 50)
L = 30, CF = 30, f = 25, h = 10

P₅₀ = 30 + [(50 - 30)/25] × 10
P₅₀ = 30 + 8
P₅₀ = 38
```

**Finding P₇₅:**
```
kN/100 = 75(100)/100 = 75th term

Percentile class: 40-50 (CF = 75 ≥ 75)
L = 40, CF = 55, f = 20, h = 10

P₇₅ = 40 + [(75 - 55)/20] × 10
P₇₅ = 40 + 10
P₇₅ = 50
```

**Results:** P₂₅ = 26.875, P₅₀ = 38, P₇₅ = 50

---

## 🧠 Key Points

- **Quartiles** divide data into 4 parts (Q₁, Q₂, Q₃)
- **Deciles** divide data into 10 parts (D₁ to D₉)
- **Percentiles** divide data into 100 parts (P₁ to P₉₉)
- **Q₂ = D₅ = P₅₀ = Median**
- **Q₁ = P₂₅** and **Q₃ = P₇₅**
- For individual/discrete: Use position formula with (n+1)
- For continuous: Use class formula with cumulative frequency

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What percentage of data lies below Q₃?
>> [!SUCCESS]- Answer
>> **75%** of data lies below the third quartile (Q₃).

> [!QUESTION] Q2: How are Q₂, D₅, and P₅₀ related?
>> [!SUCCESS]- Answer
>> They are all **equal to the Median**. Q₂ = D₅ = P₅₀ = Median

> [!QUESTION] Q3: For n=20, what position is Q₁?
>> [!SUCCESS]- Answer
>> Q₁ = (20+1)/4 = **5.25th term** (5th term + 0.25 of difference)

> [!QUESTION] Q4: What is the formula for D₇ in continuous series?
>> [!SUCCESS]- Answer
>> **D₇ = L + [(7N/10 - CF)/f] × h**

> [!QUESTION] Q5: If P₂₅ = 30 and P₇₅ = 60, what are Q₁ and Q₃?
>> [!SUCCESS]- Answer
>> **Q₁ = 30** (same as P₂₅) and **Q₃ = 60** (same as P₇₅)

---

[[5-Tabulation-and-Diagrams|← Previous]] | [[Math-AI-ML-Hub|🏠 Hub]]
