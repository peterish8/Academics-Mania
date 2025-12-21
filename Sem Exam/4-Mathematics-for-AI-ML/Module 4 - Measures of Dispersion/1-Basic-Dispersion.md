# 📉 Range, QD, MAD

## 📌 1. Range
Simplest measure.
$Range = Max - Min$
- **Pros**: Easy to calculate.
- **Cons**: Only uses 2 values; very sensitive to outliers.

## 📌 2. Quartile Deviation (QD)
Semi-Interquartile Range.
$QD = \frac{Q_3 - Q_1}{2}$
- **Pros**: Good for skewed data (ignores outliers).
- **Cons**: Ignores 50% of the data.

## 📌 3. Mean Absolute Deviation (MAD)
Average of absolute distances from the Mean (or Median).
$MAD = \frac{\sum |x - \bar{x}|}{n}$
- **Pros**: Uses all values.
- **Cons**: Mathematically hard to work with (absolute values).

---
> [[Sem Exam/4-Mathematics-for-AI-ML/Module 4 - Measures of Dispersion/README|🔙 Back to Module 4 Overview]] | [[../Math-AI-ML-Hub|🏠 Back to Subject Hub]]
