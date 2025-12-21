# 📈 Max Subarray (Kadane's Algorithm)

## 🎯 **The Problem**

> [!QUESTION] **Goal**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
> **Input**: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
> **Output**: `6` (Subarray is `[4, -1, 2, 1]`)

---

## 🐌 **Brute Force (O(n²))**

> Check every possible subarray.
```python
max_sum = float('-inf')
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += nums[j]
        max_sum = max(max_sum, current_sum)
```
> **Verdict**: Too slow for large inputs! 🐢

---

## 🐇 **Kadane's Algorithm (O(n))**

> [!TIP] **Intuition**:
> "Do I start a **new** train here, or do I join the **existing** train?"
> If the train coming to me carries "Negative Vibes" (negative sum), I ditch it and start fresh!

**Logic:**
1.  Iterate through the array.
2.  Maintain `current_sum`.
3.  Combine `previous_sum` + `current_number`.
4.  **Decision**: If `current_sum` drops below `current_number` (meaning previous sum was negative dragging us down), **Reset** start to current number.
5.  Always update `global_max`.

```python
def maxSubArray(nums):
    current_sum = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)):
        # Should we restart at nums[i], or extend the existing sum?
        # Equivalent to: current_sum = max(nums[i], current_sum + nums[i])
        if current_sum < 0:
            current_sum = nums[i] # Restart train 🚂
        else:
            current_sum += nums[i] # Join train 🚃
            
        if current_sum > global_max:
            global_max = current_sum
            
    return global_max
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Negative Baggage Rule**: If your past (prefix sum) is negative, cut it off! ✂️
> - **Complexity**: O(n) Time, O(1) Space.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Does Kadane's algorithm work if all numbers are negative?
> > [!SUCCESS]- Answer
> > Yes! It will pick the single largest element (least negative number), e.g., `[-5, -2, -9] -> -2`.

> [!QUESTION] **Q2**: What is the space complexity of Kadane's?
> > [!SUCCESS]- Answer
> > **O(1)**. We only store two variables (`current` and `max`).

> [!QUESTION] **Q3**: Can we use this logic for "Max Subarray Product"?
> > [!SUCCESS]- Answer
> > Not directly. Negatives flip signs in products, so you need to track both Max AND Min product.

> [!QUESTION] **Q4**: What if the array is empty?
> > [!SUCCESS]- Answer
> > Usually returns 0 or throws error depending on constraints. Standard problem assumes at least 1 element.

> [!QUESTION] **Q5**: How to handle "Print the Subarray" too?
> > [!SUCCESS]- Answer
> > Track `start` and `end` indices. Reset `start` whenever you start a new train. Update `end` and `best_start` whenever `global_max` updates.

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
