# 📐 Mathematics Formula Cheat Sheet - Last Minute Revision

> [!TIP] **Quick Reference**
> All essential formulas for Math AI/ML exam. Variables explained for each formula.

---

## 🎯 SET THEORY

### Power Set & Subsets
```
|P(A)| = 2ⁿ
```
- `|P(A)|` = Number of elements in power set
- `n` = Number of elements in set A
- **Total subsets** = 2ⁿ (includes empty set and set itself)
- **Proper subsets** = 2ⁿ - 1 (excludes the set itself)

### Cartesian Product
```
|A × B| = |A| × |B|
```
- `|A × B|` = Number of ordered pairs
- `|A|` = Cardinality (size) of set A
- `|B|` = Cardinality of set B

### Set Operations
```
n(A ∪ B) = n(A) + n(B) - n(A ∩ B)
```
- `n(A ∪ B)` = Elements in union (at least one set)
- `n(A ∩ B)` = Elements in intersection (both sets)

---

## 📊 MEASURES OF CENTRAL TENDENCY

### Arithmetic Mean (AM)

**Individual Series:**
```
x̄ = Σx / n
```

**Discrete Series:**
```
x̄ = Σfx / Σf
```

**Continuous Series:**
```
x̄ = Σf·m / Σf
```
- `x̄` = Mean
- `Σx` = Sum of all values
- `n` = Number of observations
- `f` = Frequency
- `m` = Mid-point of class interval

**Shortcut for first n natural numbers:**
```
Mean = (n + 1) / 2
```

### Median

**Individual Series (Odd):**
```
Median = ((n+1)/2)th term
```

**Individual Series (Even):**
```
Median = Average of (n/2)th and ((n/2)+1)th terms
```

**Grouped Data:**
```
Median = L + [(N/2 - CF) / f] × h
```
- `L` = Lower boundary of median class
- `N` = Total frequency (Σf)
- `CF` = Cumulative frequency before median class
- `f` = Frequency of median class
- `h` = Class width

### Mode

**Grouped Data:**
```
Mode = L + [(f₁ - f₀) / (2f₁ - f₀ - f₂)] × h
```
- `L` = Lower boundary of modal class
- `f₁` = Frequency of modal class
- `f₀` = Frequency of class before modal class
- `f₂` = Frequency of class after modal class
- `h` = Class width

### Geometric Mean (GM)
```
GM = ⁿ√(x₁ × x₂ × ... × xₙ)
```
For two numbers:
```
GM = √(a × b)
```

### Harmonic Mean (HM)
```
HM = n / (Σ(1/x))
```
For two numbers:
```
HM = 2 / (1/a + 1/b)
```

### AM-GM-HM Relationship
```
AM × HM = GM²
HM = GM² / AM
```
- Always: **AM ≥ GM ≥ HM**

---

## 📏 MEASURES OF DISPERSION

### Range
```
Range = Maximum - Minimum
```

### Coefficient of Range
```
Coefficient of Range = (Max - Min) / (Max + Min)
```

### Variance (σ²)

**Individual Series:**
```
σ² = Σ(x - x̄)² / n
```

**Discrete Series:**
```
σ² = Σf(x - x̄)² / N
```
- `σ²` = Variance
- `x̄` = Mean
- `N` = Σf (total frequency)

### Standard Deviation (SD)
```
σ = √(Variance)
```

### Coefficient of Variation (CV)
```
CV = (σ / x̄) × 100%
```
- `CV` = Coefficient of Variation (in %)
- `σ` = Standard Deviation
- `x̄` = Mean
- **Use:** Compare variability of different datasets

### Mean Deviation (MD)

**From Mean:**
```
MD = Σ|x - x̄| / n
```

**From Median:**
```
MD = Σ|x - Median| / n
```
- `|x - x̄|` = Absolute deviation from mean

---

## 📈 QUARTILES, DECILES, PERCENTILES

### Quartiles (Q₁, Q₂, Q₃)

**Individual Series:**
```
Q₁ = ((n+1)/4)th term
Q₂ = ((n+1)/2)th term (Median)
Q₃ = (3(n+1)/4)th term
```

**Grouped Data:**
```
Q₁ = L + [(N/4 - CF) / f] × h
Q₂ = L + [(N/2 - CF) / f] × h
Q₃ = L + [(3N/4 - CF) / f] × h
```

### Deciles (D₁ to D₉)

**Grouped Data:**
```
Dₖ = L + [(kN/10 - CF) / f] × h
```
- `k` = 1, 2, 3...9 (which decile)

**Special:** D₅ = Median

### Percentiles (P₁ to P₉₉)

**Grouped Data:**
```
Pₖ = L + [(kN/100 - CF) / f] × h
```
- `k` = 1, 2, 3...99 (which percentile)

**Special:**
- P₅₀ = Median = Q₂
- P₂₅ = Q₁
- P₇₅ = Q₃

---

## 🎲 PROBABILITY

### Basic Probability
```
P(A) = Number of favorable outcomes / Total outcomes
```
- `0 ≤ P(A) ≤ 1`
- `P(Impossible) = 0`
- `P(Sure event) = 1`

### Complement
```
P(A') = 1 - P(A)
P(A) + P(A') = 1
```

### Addition Rule

**Mutually Exclusive:**
```
P(A ∪ B) = P(A) + P(B)
```
- When: Events cannot occur together
- `P(A ∩ B) = 0`

**Non-Mutually Exclusive:**
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```
- When: Events can occur together

### Multiplication Rule

**Independent Events:**
```
P(A ∩ B) = P(A) × P(B)
```
- When: One event doesn't affect the other

**Dependent Events:**
```
P(A ∩ B) = P(A) × P(B|A)
```
- When: Without replacement, affects probability

### Conditional Probability
```
P(A|B) = P(A ∩ B) / P(B)
```
- `P(A|B)` = Probability of A given B occurred

**For Independent Events:**
```
P(A|B) = P(A)
```

---

## 📊 MOMENTS

### Central Moments

**Individual Series:**
```
μᵣ = Σ(x - x̄)ʳ / n
```

**Discrete/Continuous:**
```
μᵣ = Σf(x - x̄)ʳ / N
```
- `μ₁` = Always 0
- `μ₂` = Variance
- `μ₃` = Related to Skewness
- `μ₄` = Related to Kurtosis

### Raw Moments

**Individual Series:**
```
μᵣ' = Σxʳ / n
```

**Discrete/Continuous:**
```
μᵣ' = Σfxʳ / N
```

### Relationship
```
μ₂ = μ₂' - (μ₁')²
μ₃ = μ₃' - 3μ₁'μ₂' + 2(μ₁')³
μ₄ = μ₄' - 4μ₁'μ₃' + 6(μ₁')²μ₂' - 3(μ₁')⁴
```

---

## 📉 SKEWNESS

### Karl Pearson's Coefficient

**First Coefficient:**
```
SKₚ = (Mean - Mode) / SD
```

**Second Coefficient:**
```
SKₚ = 3(Mean - Median) / SD
```
- `SKₚ > 0` : Positive skew (right tail)
- `SKₚ < 0` : Negative skew (left tail)
- `SKₚ = 0` : Symmetric

### Bowley's Coefficient
```
SKᵦ = (Q₃ + Q₁ - 2Q₂) / (Q₃ - Q₁)
```
- Range: -1 to +1
- `Q₂` = Median

### Kelly's Coefficient
```
SKₖ = (D₉ + D₁ - 2×Median) / (D₉ - D₁)
```
OR
```
SKₖ = (P₉₀ + P₁₀ - 2×Median) / (P₉₀ - P₁₀)
```

### Relationship for Skewness
- **Positive:** Mean > Median > Mode
- **Negative:** Mode > Median > Mean
- **Symmetric:** Mean = Median = Mode

---

## 📊 KURTOSIS

### Coefficient of Kurtosis
```
β₂ = μ₄ / (μ₂)²
```

### Excess Kurtosis
```
γ₂ = β₂ - 3
```

**Interpretation:**
- `β₂ > 3` (γ₂ > 0): **Leptokurtic** (heavy tails, sharp peak)
- `β₂ = 3` (γ₂ = 0): **Mesokurtic** (normal distribution)
- `β₂ < 3` (γ₂ < 0): **Platykurtic** (light tails, flat)

---

## 📐 QUARTILE DEVIATION

### Quartile Deviation (QD)
```
QD = (Q₃ - Q₁) / 2
```

### Coefficient of QD
```
Coefficient of QD = (Q₃ - Q₁) / (Q₃ + Q₁)
```

---

## 🎯 QUICK REMINDERS

### When to Use Which Mean?
- **Arithmetic Mean:** General average, normal data
- **Geometric Mean:** Growth rates, ratios, percentages
- **Harmonic Mean:** Rates, speeds, time problems

### Truth Tables (2 propositions)
- Number of rows = **2ⁿ** where n = propositions
- For 2 propositions: 4 rows
- For 3 propositions: 8 rows

### De Morgan's Laws
```
¬(p ∧ q) ≡ ¬p ∨ ¬q
¬(p ∨ q) ≡ ¬p ∧ ¬q
```

### Common Probability Values
- Fair coin: P(H) = P(T) = 1/2
- Fair dice: P(any number) = 1/6
- Deck of cards:
  - P(Red) = 26/52 = 1/2
  - P(Face card) = 12/52 = 3/13
  - P(Specific suit) = 13/52 = 1/4

---

## 💡 EXAM TIPS

1. **Always write units** where applicable
2. **Check answer ranges:**
   - Probability: 0 to 1
   - CV, Skewness, Kurtosis: as per formulas
3. **For grouped data:** Always create CF (Cumulative Frequency) table first
4. **Mean vs Median:**
   - Mean affected by outliers
   - Median is robust
5. **Mutually Exclusive ≠ Independent:**
   - ME: Cannot occur together
   - Indep: One doesn't affect other

---

[[Sample-Paper-Hub|🏠 Back to Hub]]
