# 📊 Moments, Skewness & Kurtosis - Complete Notes

---

## 📌 MOMENTS

> [!INFO] **Definition: Moments**
> Moments are **quantitative measures** that describe the shape of a probability distribution or dataset. They provide information about:
> - Central tendency
> - Dispersion
> - Asymmetry (Skewness)
> - Peakedness (Kurtosis)

**Types of Moments:**
1. Central Moments (about mean)
2. Raw Moments (about origin)
3. Moments about Arbitrary Point

---

## 📌 CENTRAL MOMENTS

> [!INFO] **Definition: Central Moments**
> Moments calculated **about the mean** of a distribution. They describe shape characteristics relative to the center.

### Formula for Individual Series

```
μᵣ = Σ(xᵢ - x̄)ʳ / n

where:
μᵣ = rth central moment
x̄ = mean
n = number of observations
```

### Formula for Discrete/Continuous Series

```
μᵣ = Σf(x - x̄)ʳ / N

where:
N = Σf (total frequency)
```

---

### Interpretation of Central Moments

| Moment | Symbol | Meaning |
|--------|--------|---------|
| **First** | μ₁ | Always = **0** (no practical use) |
| **Second** | μ₂ | **Variance** - spread of data |
| **Third** | μ₃ | **Skewness** - asymmetry |
| **Fourth** | μ₄ | **Kurtosis** - peakedness & tail heaviness |

> [!TIP] **Note**
> The first central moment (μ₁) is always **zero**.

---

### Example 1: Individual Series

**Data:** 2, 4, 6, 8, 10. Calculate μ₂ (variance) and μ₃.

**Solution:**
```
Step 1: Find mean
x̄ = (2 + 4 + 6 + 8 + 10) / 5 = 30 / 5 = 6

Step 2: Calculate μ₂
μ₂ = [(2-6)² + (4-6)² + (6-6)² + (8-6)² + (10-6)²] / 5
μ₂ = [16 + 4 + 0 + 4 + 16] / 5
μ₂ = 40 / 5
μ₂ = 8

Step 3: Calculate μ₃
μ₃ = [(2-6)³ + (4-6)³ + (6-6)³ + (8-6)³ + (10-6)³] / 5
μ₃ = [-64 + (-8) + 0 + 8 + 64] / 5
μ₃ = 0
```

**Results:** μ₂ = 8, μ₃ = 0

---

### Example 2: Discrete Series

**Calculate μ₁, μ₂, μ₃, μ₄:**

| x | 10 | 15 | 20 | 25 | 30 |
|---|----|----|----|----|-----|
| f | 2 | 5 | 4 | 9 | 5 |

**Solution:**

**Step 1: Create calculation table**

| x | f | fx | x - x̄ | f(x - x̄) | f(x - x̄)² | f(x - x̄)³ | f(x - x̄)⁴ |
|---|---|----|----|----------|-----------|-----------|-----------|
| 10 | 2 | 20 | -12 | -24 | 288 | -3456 | 41472 |
| 15 | 5 | 75 | -7 | -35 | 245 | -1715 | 12005 |
| 20 | 4 | 80 | -2 | -8 | 16 | -32 | 64 |
| 25 | 9 | 225 | 3 | 27 | 81 | 243 | 729 |
| 30 | 5 | 150 | 8 | 40 | 320 | 2560 | 20480 |
| **Σ** | **25** | **550** | | **0** | **950** | **-2400** | **74750** |

**Step 2: Calculate mean**
```
x̄ = Σfx / N = 550 / 25 = 22
```

**Step 3: Calculate moments**
```
μ₁ = Σf(x - x̄) / N = 0 / 25 = 0
μ₂ = Σf(x - x̄)² / N = 950 / 25 = 38
μ₃ = Σf(x - x̄)³ / N = -2400 / 25 = -96
μ₄ = Σf(x - x̄)⁴ / N = 74750 / 25 = 2990
```

**Results:** μ₁ = 0, μ₂ = 38, μ₃ = -96, μ₄ = 2990

---

### Example 3: Continuous Series

**Find first 4 moments around mean:**

| C.I | 0-10 | 10-20 | 20-30 | 30-40 |
|-----|------|-------|-------|-------|
| f | 1 | 4 | 3 | 2 |

**Solution:**
```
x̄ = 21
μ₁ = 0
μ₂ = 84
μ₃ = 72
μ₄ = 14832
```

---

## 📌 MOMENTS ABOUT ARBITRARY POINT

> [!INFO] **Definition**
> Moments calculated about **any chosen point A** (not necessarily the mean).

### Formula for Individual Series

```
μᵣ'(A) = Σ(xᵢ - A)ʳ / n
```

### Formula for Discrete/Continuous Series

```
μᵣ'(A) = Σf(x - A)ʳ / N
```

---

### Example 1: Individual Series

**Data:** x = 2, 4, 6 and A = 4

**Solution:**
```
μ₁'(A) = [(2-4) + (4-4) + (6-4)] / 3 = 0 / 3 = 0

μ₂'(A) = [(2-4)² + (4-4)² + (6-4)²] / 3
μ₂'(A) = [4 + 0 + 4] / 3 = 8/3 = 2.67

μ₃'(A) = [(2-4)³ + (4-4)³ + (6-4)³] / 3
μ₃'(A) = [-8 + 0 + 8] / 3 = 0

μ₄'(A) = [(2-4)⁴ + (4-4)⁴ + (6-4)⁴] / 3
μ₄'(A) = [16 + 0 + 16] / 3 = 32/3 = 10.67
```

**Results:** μ₁' = 0, μ₂' = 2.67, μ₃' = 0, μ₄' = 10.67

---

### Example 2: Discrete Series - A = 105

**Find μ₁', μ₂', μ₃' about A = 105:**

| x | 98 | 102 | 105 | 107 | 110 |
|---|----|----|-----|-----|-----|
| f | 2 | 3 | 5 | 3 | 2 |

**Solution:**

| x | f | x - A | f(x - A) | f(x - A)² | f(x - A)³ |
|---|---|-------|----------|-----------|-----------|
| 98 | 2 | -7 | -14 | 98 | -686 |
| 102 | 3 | -3 | -9 | 27 | -81 |
| 105 | 5 | 0 | 0 | 0 | 0 |
| 107 | 3 | 2 | 6 | 12 | 24 |
| 110 | 2 | 5 | 10 | 50 | 250 |
| **Σ** | **15** | | **-7** | **187** | **-493** |

```
N = 15
μ₁'(A) = -7/15 = -0.466
μ₂'(A) = 187/15 = 12.466
μ₃'(A) = -493/15 = -32.866
```

**Results:** μ₁' = -0.466, μ₂' = 12.466, μ₃' = -32.866

---

## 📌 RAW MOMENTS

> [!INFO] **Definition: Raw Moments**
> Moments calculated **about the origin (zero)** of a distribution.

### Formula for Individual Series

```
μᵣ' = Σxᵢʳ / n
```

### Formula for Discrete/Continuous Series

```
μᵣ' = Σfxʳ / N
```

---

### Example 1: Individual Series

**Data:** 2, 4, 6, 8, 10

**Solution:**
```
μ₁' = (2 + 4 + 6 + 8 + 10) / 5 = 30/5 = 6

μ₂' = (4 + 16 + 36 + 64 + 100) / 5 = 220/5 = 44

μ₃' = (8 + 64 + 216 + 512 + 1000) / 5 = 1800/5 = 360

μ₄' = (16 + 256 + 1296 + 4096 + 10000) / 5 = 15664/5 = 3132.8
```

**Results:** μ₁' = 6, μ₂' = 44, μ₃' = 360, μ₄' = 3132.8

---

### Relation Between Central and Raw Moments

```
μ₁ = 0
μ₂ = μ₂' - (μ₁')²
μ₃ = μ₃' - 3μ₁'μ₂' + 2(μ₁')³
μ₄ = μ₄' - 4μ₁'μ₃' + 6(μ₁')²μ₂' - 3(μ₁')⁴
```

---

## 📌 SKEWNESS

> [!INFO] **Definition: Skewness**
> A statistical measure that describes the **asymmetry** of a probability distribution about its mean.

### Types of Skewness

#### 1. Positive Skewness (Right-Skewed)

- Long tail towards the **right**
- **Mean > Median > Mode**

#### 2. Negative Skewness (Left-Skewed)

- Long tail towards the **left**
- **Mean < Median < Mode**

#### 3. Symmetric (No Skewness)

- Perfectly symmetric distribution
- **Mean = Median = Mode**

---

## 📌 COEFFICIENT OF SKEWNESS

### 1. Karl Pearson Coefficient of Skewness

**Pearson's First Coefficient (SKₚ):**
```
SKₚ = (Mean - Mode) / Standard Deviation
```
Use when: Distribution is clearly defined with single mode

**Pearson's Second Coefficient (SKₘ):**
```
SKₘ = 3(Mean - Median) / Standard Deviation
```
Use when: Grouped or large data (gives approximate answer)

**Interpretation:**
- SKₚ > 0 → Positively skewed
- SKₚ < 0 → Negatively skewed
- SKₚ = 0 → Symmetric distribution

---

#### Example 1: Basic Calculation

**Given:** Mean = 11.71, Mode = 6.58, S.D = 6.23

**Solution:**
```
SKₚ = (Mean - Mode) / S.D
SKₚ = (11.71 - 6.58) / 6.23
SKₚ = 5.13 / 6.23
SKₚ = 0.82
```

**Interpretation:** Positively skewed (right-skewed)

---

#### Example 2: Symmetric Data

**Data:** 2, 4, 6, 8, 10, 12, 14

**Solution:**
```
Mean = 8, Mode = No single mode (all equal frequency)
Median = 8

SKₚ = 0 (Symmetric distribution)
```

---

#### Example 3: Finding Standard Deviation

**Given:** Mean = 40, Mode = 45, SKₚ = -0.5. Find S.D.

**Solution:**
```
SKₚ = (Mean - Mode) / S.D
-0.5 = (40 - 45) / S.D
-0.5 = -5 / S.D
S.D = -5 / -0.5
S.D = 10
```

**Answer:** Standard Deviation = 10

---

### 2. Bowley's Coefficient of Skewness

> Also called **Quartile Coefficient of Skewness**

**Formula:**
```
SKᵦ = (Q₃ + Q₁ - 2Q₂) / (Q₃ - Q₁)

where:
Q₁ = First Quartile
Q₂ = Median
Q₃ = Third Quartile
```

**Range:** -1 to +1

**Related Formulas:**
```
Quartile Deviation = (Q₃ - Q₁) / 2
Coefficient of Quartile Deviation = (Q₃ - Q₁) / (Q₃ + Q₁)
```

---

#### Example 1: Individual Series

**Dataset:** 12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 45, 50

**Solution:**
```
n = 12

Q₁ = (12+1)/4 = 3.25th term = 19
Q₂ = 2(12+1)/4 = 6.5th term = 26.5
Q₃ = 3(12+1)/4 = 9.75th term = 37.5

SKᵦ = (Q₃ + Q₁ - 2Q₂) / (Q₃ - Q₁)
SKᵦ = (37.5 + 19 - 2(26.5)) / (37.5 - 19)
SKᵦ = (56.5 - 53) / 18.5
SKᵦ = 3.5 / 18.5
SKᵦ = 0.19 ≈ 0.21
```

**Interpretation:** Positively skewed

---

#### Example 2: Discrete Series

| x | 5 | 10 | 15 | 20 | 25 |
|---|---|----|----|----|----|
| Frequency | 2 | 5 | 8 | 4 | 1 |

**Solution:**
```
N = 20

Q₁ position = 20/4 = 5th term → Q₁ = 10
Q₂ position = 2(20)/4 = 10th term → Q₂ = 15
Q₃ position = 3(20)/4 = 15th term → Q₃ = 17.5

SKᵦ = (17.5 + 10 - 2(15)) / (17.5 - 10)
SKᵦ = (27.5 - 30) / 7.5
SKᵦ = -2.5 / 7.5
SKᵦ = -1/3
```

**Interpretation:** Negatively skewed

---

### 3. Kelly's Coefficient of Skewness

> Based on **deciles** or **percentiles**

**Formula:**
```
SKₖ = (D₉ + D₁ - 2×Median) / (D₉ - D₁)

OR

SKₖ = (P₉₀ + P₁₀ - 2×Median) / (P₉₀ - P₁₀)
```

**Range:** -1 to +1

---

#### Example: Using Percentiles

**Dataset:** 12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65

**Solution:**
```
P₉₀ = 62
P₁₀ = 13.8
Median = 30

SKₖ = (P₉₀ + P₁₀ - 2×Median) / (P₉₀ - P₁₀)
SKₖ = (62 + 13.8 - 2(30)) / (62 - 13.8)
SKₖ = (75.8 - 60) / 48.2
SKₖ = 15.8 / 48.2
SKₖ = 0.33
```

**Interpretation:** Positively skewed

---

## 📌 KURTOSIS

> [!INFO] **Definition: Kurtosis**
> A statistical measure that describes the **"tailedness"** of a probability distribution. It indicates how much variance is due to extreme deviations (outliers).

### Types of Kurtosis

| Type | Description | β₂ Value |
|------|-------------|----------|
| **Leptokurtic** | Heavy tails, sharp peak, more outliers | β₂ > 3 |
| **Mesokurtic** | Normal distribution | β₂ = 3 |
| **Platykurtic** | Light tails, flat peak, fewer outliers | β₂ < 3 |

---

### Moment Coefficient of Kurtosis

**Formula:**
```
β₂ = μ₄ / (μ₂)²

Excess Kurtosis:
γ₂ = β₂ - 3
```

**Interpretation:**
- β₂ > 3 (γ₂ > 0) → Leptokurtic
- β₂ = 3 (γ₂ = 0) → Mesokurtic (Normal)
- β₂ < 3 (γ₂ < 0) → Platykurtic

---

### Example 1: Individual Series

**Data:** 2, 4, 6, 8, 10

**Solution:**
```
x̄ = 6
μ₂ = 8
μ₄ = 108.8

β₂ = μ₄ / (μ₂)²
β₂ = 108.8 / (8)²
β₂ = 108.8 / 64
β₂ = 1.7

Excess Kurtosis (γ₂) = β₂ - 3
γ₂ = 1.7 - 3 = -1.3
```

**Interpretation:** Platykurtic (flatter than normal)

---

### Example 2: Discrete Series

| x | 1 | 2 | 3 |
|---|---|---|---|
| f | 2 | 3 | 5 |

**Solution:**
```
x̄ = 2.3
μ₂ = 0.61
μ₄ = 0.693

β₂ = 0.693 / (0.61)²
β₂ = 0.693 / 0.3721
β₂ = 1.86
```

**Interpretation:** Platykurtic (β₂ < 3)

---

## 🧠 Key Points

- **Moments** describe distribution shape (central tendency, spread, asymmetry, peakedness)
- **μ₁ = 0** always for central moments
- **μ₂ = Variance**, **μ₃ = Skewness**, **μ₄ = Kurtosis**
- **Skewness** measures asymmetry (left/right tail)
- **Karl Pearson:** Uses Mean, Mode, S.D
- **Bowley:** Uses Quartiles (Q₁, Q₂, Q₃)
- **Kelly:** Uses Deciles or Percentiles
- **Kurtosis** measures tail heaviness
- **β₂ = 3** for normal distribution

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is the value of first central moment (μ₁)?
>> [!SUCCESS]- Answer
>> **μ₁ = 0** always. It has no practical interpretation.

> [!QUESTION] Q2: If Mean = 50, Median = 48, Mode = 45, is the distribution positively or negatively skewed?
>> [!SUCCESS]- Answer
>> **Positively skewed** (Mean > Median > Mode)

> [!QUESTION] Q3: What does β₂ = 2.5 indicate about kurtosis?
>> [!SUCCESS]- Answer
>> **Platykurtic** (β₂ < 3) - flatter than normal distribution with lighter tails

> [!QUESTION] Q4: Which skewness coefficient uses quartiles?
>> [!SUCCESS]- Answer
>> **Bowley's Coefficient**: SKᵦ = (Q₃ + Q₁ - 2Q₂) / (Q₃ - Q₁)

> [!QUESTION] Q5: If SKₚ = -0.5, what does it indicate?
>> [!SUCCESS]- Answer
>> **Negatively skewed** (left-skewed) - tail extends to the left

---

[[7-Probability|← Previous]] | [[Math-AI-ML-Hub|🏠 Hub]]
