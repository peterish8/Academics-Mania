# 📊 Measures of Central Tendency - Complete Notes

> [!INFO] **Definition: Central Tendency**
> A single value or central value that represents a large set of data. Also called "Average" or "Measure of Center".

**Examples:** Average marks in semester, average salary in company

---

## 📌 Why Measure Central Tendency?

| Reason | Example |
|--------|---------|
| **Summarize Data** | Represents entire dataset with one value |
| **Compare Groups** | "Company A avg: ₹40,000 vs Company B: ₹55,000" |
| **Handle Outliers** | Different measures (mean, median, mode) for skewed data |
| **Handle Missing Values** | Use central value to fill gaps |

---

## 📌 Types of Data Series

| Series Type | Description | Example |
|-------------|-------------|---------|
| **Individual** | Raw, ungrouped values (no frequencies) | Marks: {45, 50, 60, 70, 80} |
| **Discrete** | Distinct values with frequencies | Marks: 45(f=2), 50(f=5), ... |
| **Continuous** | Class intervals with frequencies | 40-50(f=2), 50-60(f=5), ... |

---

## 📌 1. MEAN (Arithmetic Mean)

> [!INFO] **Definition: Mean (x̄)**
> The value obtained by dividing the **sum of all observations** by the **total number of observations**.

---

### Formula for Individual Series

**Direct Method:**
```
Mean (x̄) = Σxi / n
```

**Shortcut Method:**
```
Mean (x̄) = A + (Σd / n)
where: A = Assumed mean
       d = x - A
```

---

### Example 1: Individual Series

**Question:** Find mean of 50, 60, 70, 80, 90

**Direct Method:**
```
Mean = (50 + 60 + 70 + 80 + 90) / 5
Mean = 350 / 5 = 70
```

**Shortcut Method (A = 70):**

| x | d = x - A |
|---|-----------|
| 50 | -20 |
| 60 | -10 |
| 70 | 0 |
| 80 | 10 |
| 90 | 20 |
| **Σd = 0** | |

```
Mean = A + (Σd / n)
Mean = 70 + (0 / 5) = 70
```

---

### Formula for Discrete Series

**Direct Method:**
```
Mean (x̄) = Σ(fi × xi) / n
```

**Shortcut Method:**
```
Mean (x̄) = A + (Σf·d / n)
where: d = x - A
```

---

### Example 2: Discrete Series

**Question:** Find mean for:

| x | 10 | 20 | 30 | 40 |
|---|----|----|----|----|
| f | 2 | 3 | 4 | 1 |

**Direct Method:**

| x | f | f·x |
|---|---|-----|
| 10 | 2 | 20 |
| 20 | 3 | 60 |
| 30 | 4 | 120 |
| 40 | 1 | 40 |
| **Total** | **10** | **240** |

```
Mean = Σ(f·x) / n = 240 / 10 = 24
```

---

### Formula for Continuous Series

**Class Midpoint:** x = (Lower limit + Upper limit) / 2

**Direct Method:**
```
Mean = Σf·x / n
```

**Shortcut Method:**
```
Mean = A + (Σf·d / n)
```

**Step Deviation Method:**
```
Mean = A + h × (Σf·u / n)
where: u = (x - A) / h
       h = class width
```

---

### Example 3: Continuous Series

**Question:** Find mean for:

| C.I | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |
|-----|------|-------|-------|-------|-------|
| f | 2 | 3 | 7 | 6 | 2 |

**Direct Method:**

| C.I | x | f | f·x |
|-----|---|---|-----|
| 0-10 | 5 | 2 | 10 |
| 10-20 | 15 | 3 | 45 |
| 20-30 | 25 | 7 | 175 |
| 30-40 | 35 | 6 | 210 |
| 40-50 | 45 | 2 | 90 |
| **Total** | | **20** | **530** |

```
Mean = 530 / 20 = 26.5
```

**Step Deviation Method (A = 25, h = 10):**

| C.I | x | u = (x-A)/h | f | f·u |
|-----|---|-------------|---|-----|
| 0-10 | 5 | -2 | 2 | -4 |
| 10-20 | 15 | -1 | 3 | -3 |
| 20-30 | 25 | 0 | 7 | 0 |
| 30-40 | 35 | 1 | 6 | 6 |
| 40-50 | 45 | 2 | 2 | 4 |
| **Total** | | | **20** | **3** |

```
Mean = A + h × (Σf·u / n)
Mean = 25 + 10 × (3 / 20)
Mean = 25 + 1.5 = 26.5
```

---

## 📌 Combined Arithmetic Mean

> [!INFO] **Definition: Combined Mean**
> Average when combining several groups where only the mean and size of each group are known.

**Formula:**
```
Combined Mean = (n₁x̄₁ + n₂x̄₂ + ...) / (n₁ + n₂ + ...)
```

---

### Example: Combined Mean

**Question:** Section A: 30 students, avg marks 72. Section B: 40 students, avg marks 68. Find overall average.

**Solution:**
```
Total marks (A) = 30 × 72 = 2160
Total marks (B) = 40 × 68 = 2720
Total marks = 4880
Total students = 70

Combined Average = 4880 / 70 = 69.71
```

---

## 📌 2. MEDIAN

> [!INFO] **Definition: Median**
> The **middle value** when data is arranged in ascending or descending order.

**Formula:**
- If n is **odd**: Median = (n+1)/2 th value
- If n is **even**: Median = Average of (n/2) and (n/2 + 1) th values

---

### Example 4: Median (Odd n)

**Question:** Find median of 15, 25, 10, 20, 30, 45, 35

**Solution:**
```
Arrange: 10, 15, 20, 25, 30, 35, 45
n = 7 (odd)

Median position = (7 + 1) / 2 = 4th value
Median = 25
```

---

### Example 5: Median (Even n)

**Question:** Find median of 15, 25, 10, 20, 30, 35

**Solution:**
```
Arrange: 10, 15, 20, 25, 30, 35
n = 6 (even)

Median = Average of 3rd and 4th values
Median = (20 + 25) / 2 = 22.5
```

---

### Median for Discrete Series

**Steps:**
1. Find cumulative frequency (CF)
2. Find n/2
3. Locate median class (where CF ≥ n/2)
4. Median = corresponding x value

---

### Example 6: Discrete Series Median

**Question:**

| Marks | 10 | 20 | 30 | 40 | 50 | 60 | 70 |
|-------|----|----|----|----|----|----|-----|
| f | 5 | 8 | 12 | 20 | 10 | 3 | 2 |

**Solution:**

| Marks | f | CF |
|-------|---|-----|
| 10 | 5 | 5 |
| 20 | 8 | 13 |
| 30 | 12 | 25 |
| 40 | 20 | **45** |
| 50 | 10 | 55 |
| 60 | 3 | 58 |
| 70 | 2 | 60 |

```
n = 60 (even)
Median position = 30th and 31st values

Both fall in CF = 45 (Marks = 40)
Median = 40
```

---

### Median for Continuous Series

**Formula:**
```
Median = L + [(n/2 - CF) / f] × h

where:
L = Lower boundary of median class
CF = Cumulative frequency before median class
f = Frequency of median class
h = Class width
```

---

### Example 7: Continuous Series Median

**Question:**

| Daily Wages | 0-50 | 50-100 | 100-150 | 150-200 | 200-250 | 250-300 |
|-------------|------|--------|---------|---------|---------|---------|
| f | 5 | 8 | 15 | 25 | 16 | 6 |

**Solution:**

| Wages | f | CF |
|-------|---|-----|
| 0-50 | 5 | 5 |
| 50-100 | 8 | 13 |
| 100-150 | 15 | **28** |
| 150-200 | 25 | **53** ← Median class |
| 200-250 | 16 | 69 |
| 250-300 | 6 | 75 |

```
n = 75 (odd)
n/2 = 37.5

Median class: 150-200 (CF = 53 ≥ 37.5)
L = 150, CF = 28, f = 25, h = 50

Median = 150 + [(37.5 - 28) / 25] × 50
Median = 150 + 19 = ₹169
```

---

## 📌 3. MODE

> [!INFO] **Definition: Mode**
> The value that occurs **most frequently** in a dataset. Shows the most common observation.

---

### Mode for Individual/Discrete Data

**Example 1:** Find mode of 2, 4, 4, 4, 5, 5, 6, 7

**Solution:** Mode = **4** (occurs 3 times)

**Example 2:** Discrete Series

| x | 10 | 20 | 30 | 40 | 50 |
|---|----|----|----|----|-----|
| f | 5 | 7 | **12** | 9 | 6 |

**Solution:** Mode = **30** (highest frequency = 12)

---

### Mode for Continuous Series

**Formula:**
```
Mode = L + [(f₁ - f₀) / (2f₁ - f₀ - f₂)] × h

where:
L = Lower boundary of modal class (class with highest frequency)
f₁ = Frequency of modal class
f₀ = Frequency of class before modal class
f₂ = Frequency of class after modal class
h = Class width
```

---

### Example: Continuous Series Mode

**Question:**

| C.I | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
|-----|------|-------|-------|-------|-------|-------|
| f | 5 | 9 | 12 | **20** | 10 | 4 |

**Solution:**
```
Modal class: 30-40 (highest frequency = 20)
L = 30, f₁ = 20, f₀ = 12, f₂ = 10, h = 10

Mode = 30 + [(20 - 12) / (2×20 - 12 - 10)] × 10
Mode = 30 + [8 / 18] × 10
Mode = 30 + 4.44
Mode = 34.44
```

---

## 📌 Relationship: Mean, Median, Mode

> [!SUCCESS] **Empirical Formula**
> **Mode = 3 × Median - 2 × Mean**

This relationship holds approximately for moderately skewed distributions.

---

### Example 1: Find Mode

**Question:** Mean = 50, Median = 45. Find Mode.

**Solution:**
```
Mode = 3 × Median - 2 × Mean
Mode = 3 × 45 - 2 × 50
Mode = 135 - 100 = 35
```

---

### Example 2: Symmetric Distribution

**Question:** In perfectly symmetrical distribution, Mean = 60. Find Median and Mode.

**Solution:**
```
In symmetric distribution: Mean = Median = Mode
Therefore, Median = 60, Mode = 60
```

---

## 📌 4. GEOMETRIC MEAN (GM)

> [!INFO] **Definition: Geometric Mean**
> The nth root of the product of n positive numbers. Useful for ratios, proportions, percentages, growth rates.

---

### Formula for Individual Series

```
GM = ⁿ√(x₁ × x₂ × x₃ × ... × xₙ)

OR (using logs):
GM = antilog [1/n × Σ log(x)]
```

---

### Example 1: Simple GM

**Question:** Find GM of 2, 4, 8

**Solution:**
```
GM = ³√(2 × 4 × 8)
GM = ³√64 = 4
```

---

### Example 2: GM using Logs

**Question:** Find GM of 10, 110, 120, 50, 52, 80, 37, 60

**Solution:**

| x | log(x) |
|---|--------|
| 10 | 1.0000 |
| 110 | 2.0414 |
| 120 | 2.0792 |
| 50 | 1.6990 |
| 52 | 1.7160 |
| 80 | 1.9031 |
| 37 | 1.5682 |
| 60 | 1.7782 |
| **Σ** | **13.7851** |

```
GM = antilog[1/n × Σ log(x)]
GM = antilog[1/8 × 13.7851]
GM = antilog[1.7231]
GM = 52.86
```

---

### Formula for Discrete Series

```
GM = antilog [1/n × Σ(f × log(x))]
```

---

### Example 3: Discrete GM

**Question:**

| x | 2 | 4 | 8 |
|---|---|---|---|
| f | 3 | 2 | 1 |

**Solution:**

| x | f | log(x) | f × log(x) |
|---|---|--------|------------|
| 2 | 3 | 0.3010 | 0.9030 |
| 4 | 2 | 0.6021 | 1.2042 |
| 8 | 1 | 0.9031 | 0.9031 |
| **Total** | **6** | | **3.0103** |

```
GM = antilog[1/n × Σ(f × log(x))]
GM = antilog[1/6 × 3.0103]
GM = antilog[0.5017]
GM = 3.17
```

---

### Formula for Continuous Series

```
GM = antilog [1/n × Σ(f × log(x))]
where x = class midpoint
```

**Same process as discrete, but use midpoints!**

---

## 📌 5. HARMONIC MEAN (HM)

> [!INFO] **Definition: Harmonic Mean**
> The reciprocal of the arithmetic mean of reciprocals. Useful for rates, ratios, speeds (average speed, velocity, efficiency).

---

### Formula for Individual Series

```
HM = n / Σ(1/x)
```

---

### Example 1: Simple HM

**Question:** Find HM of 4, 5, 6

**Solution:**
```
HM = 3 / (1/4 + 1/5 + 1/6)
HM = 3 / (0.25 + 0.20 + 0.1667)
HM = 3 / 0.6167
HM = 4.87
```

---

### Formula for Discrete Series

```
HM = n / Σ(f/x)
```

---

### Example 2: Discrete HM

**Question:**

| x | 2 | 4 | 8 |
|---|---|---|---|
| f | 3 | 4 | 3 |

**Solution:**

| x | f | f/x |
|---|---|-----|
| 2 | 3 | 1.5 |
| 4 | 4 | 1.0 |
| 8 | 3 | 0.375 |
| **Total** | **10** | **2.875** |

```
HM = n / Σ(f/x)
HM = 10 / 2.875
HM = 3.48
```

---

### Formula for Continuous Series

```
HM = n / Σ(f/x)
where x = class midpoint
```

---

## 📌 Relationship: AM, GM, HM

> [!SUCCESS] **Key Relationships**
> 1. **AM ≥ GM ≥ HM** (always true)
> 2. **AM × HM = GM²**

---

### Example 1: Find HM

**Question:** AM = 20, GM = 16. Find HM.

**Solution:**
```
AM × HM = GM²
20 × HM = 16²
20 × HM = 256
HM = 12.8
```

---

### Example 2: Find AM

**Question:** HM = 8, GM = 12. Find AM.

**Solution:**
```
AM × HM = GM²
AM × 8 = 12²
AM × 8 = 144
AM = 18
```

---

### Example 3: Find GM

**Question:** AM = 25, HM = 9. Find GM.

**Solution:**
```
AM × HM = GM²
25 × 9 = GM²
225 = GM²
GM = 15
```

---

## 🧠 Key Points
- **Mean** = Sum of all values / Number of values
- **Shortcut method** faster for large numbers (use assumed mean)
- **Step deviation** best for continuous series with constant class width
- **Combined mean** when combining multiple groups
- **Median** = Middle value (odd n) or average of 2 middle values (even n)
- **Median for continuous**: Use formula with cumulative frequency
- **Mode** = Most frequent value
- **Mode formula**: Use when data is grouped
- **Mode = 3Median - 2Mean** (empirical relationship)
- **GM** = Use for ratios, growth rates (multiply & take root)
- **HM** = Use for rates, speeds (reciprocals)
- **AM ≥ GM ≥ HM** always
- **AM × HM = GM²** 

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: When to use Shortcut method over Direct method?
>> [!SUCCESS]- Answer
>> When numbers are **large** or when they cluster around a central value. Choose A close to the center.

> [!QUESTION] Q2: What is the relationship between Mean, Median, Mode?
>> [!SUCCESS]- Answer
>> **Mode = 3 × Median - 2 × Mean** (for moderately skewed data)

> [!QUESTION] Q3: When to use GM instead of AM?
>> [!SUCCESS]- Answer
>> For **ratios, percentages, growth rates** - when data is multiplicative in nature.

> [!QUESTION] Q4: When to use HM?
>> [!SUCCESS]- Answer
>> For **rates and speeds** - like average speed, work rates, etc.

> [!QUESTION] Q5: If AM = 50 and HM = 32, what is GM?
>> [!SUCCESS]- Answer
>> **GM² = AM × HM = 50 × 32 = 1600**, so **GM = 40**

---

[[3-Data-Types-and-Collection|← Previous]] |[[Math-AI-ML-Hub|🏠 Hub]]
