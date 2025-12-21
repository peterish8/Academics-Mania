# ➕ Prefix Sum Technique

## 🎯 **Prefix Sum**

> [!SUCCESS] **Definition**: An array where `P[i]` stores the sum of all elements from index `0` to `i`.
> "Running Total".

**Input**: `[1, 2, 3, 4]`
**Prefix**: `[1, 3, 6, 10]`

---

## ⚡ **Why use it? (Range Sum Query)**

> [!QUESTION] **Problem**: "Calculate sum from index L to R".
> **Naive**: Loop from L to R. **O(n)** per query.
> **Prefix Way**: `P[R] - P[L-1]`. **O(1)** per query! 🚀

```python
# Build Prefix Array
nums = [1, 2, 3, 4, 5]
prefix = [0] * len(nums)
prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

# TEST
print("Original:", nums)
print("Prefix:  ", prefix)

# Query Range [1, 3] (Values 2, 3, 4 -> Sum 9)
L, R = 1, 3
sum_range = prefix[R] - prefix[L-1]
print(f"Sum from index {L} to {R}:", sum_range)
```
> **Note**: If `L=0`, formula is just `prefix[R]`.

---

## 🌍 **Real World Usage**

- **equilibrium** index (Where left sum == right sum).
- **Subarray Sum Equals K** (Using HashMap + Prefix).
- Image Processing (Integral Images).

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Pre** = Before/Past.
> - **Formula**: `Sum(L, R) = Pre[R] - Pre[L-1]`.
> - **Analogy**: To measure distance between Mile 10 and Mile 50, you don't drive it again. You subtract the markers: `50 - 10 = 40`.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the Time Complexity to BUILD the prefix array?
> > [!SUCCESS]- Answer
> > **O(n)**. You pass through the array once.

> [!QUESTION] **Q2**: What is the Time Complexity to ANSWER a range query?
> > [!SUCCESS]- Answer
> > **O(1)**. Simple subtraction.

> [!QUESTION] **Q3**: How to handle `L=0` in the formula `P[R] - P[L-1]`?
> > [!SUCCESS]- Answer
> > `P[-1]` would be invalid (or wrap around in Python). You check `if L == 0: return P[R]` OR pad the prefix array with an implementation leading 0.

> [!QUESTION] **Q4**: Can Prefix Sum work on 2D Arrays?
> > [!SUCCESS]- Answer
> > Yes! Used for summing sub-rectangles efficiently.

> [!QUESTION] **Q5**: Does Prefix Sum require extra space?
> > [!SUCCESS]- Answer
> > Yes, **O(n)** space is needed to store the prefix array.

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
