# 👈 Two Pointer Technique 👉

## 🎯 **Concept**

> [!SUCCESS] **Definition**: Using two pointers (indices) to traverse an array, typically from different ends or speeds, to solve problems efficiently.
> **Goal**: Turn **O(n²)** nested loops into **O(n)** linear scans! ⚡

---

## 🛠️ **Scenario 1: Opposite Ends (Convergence)**
> Usually for **Sorted Arrays** or **Palindromes**.
> `Left` starts at 0, `Right` starts at end.

**Problem**: Find two numbers in sorted array that sum to Target.
```python
def twoSumSorted(arr, target):
    l, r = 0, len(arr) - 1
    
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == target:
            return (l, r)
        elif curr_sum < target:
            l += 1 # We need more! Move left up
        else:
            r -= 1 # We need less! Move right down
```

---

## 🐇 **Scenario 2: Fast & Slow (Tortoise & Hare)**
> Usually for **Linked Lists** or **Cycle Detection**.
> Both start at 0, but one moves faster (`+2`).

```python
# Finding middle of an array/list
slow = 0
fast = 0
while fast < len(arr):
    slow += 1
    fast += 2
# Slow is now at the midpoint!
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Sorted Array?** 👉 Think Two Pointers.
> - **Palindrome?** 👉 Think Two Pointers (Compare ends).
> - **Cycle?** 👉 Think Fast/Slow.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Can you use Two Pointers on an unsorted array for Two Sum?
> > [!SUCCESS]- Answer
> > No. Moving pointers (`l++` or `r--`) relies on the array being sorted to know *which* direction to adjust. Use a Hash Map for unsorted arrays.

> [!QUESTION] **Q2**: What is the Time Complexity of Two Pointers?
> > [!SUCCESS]- Answer
> > **O(n)**. Each element is touched at most once.

> [!QUESTION] **Q3**: How do you check if a string is a palindrome with two pointers?
> > [!SUCCESS]- Answer
> > Check `s[l] == s[r]`, increment `l`, decrement `r`. If mismatch, return False.

> [!QUESTION] **Q4**: In "Move Zeroes to End", how do pointers help?
> > [!SUCCESS]- Answer
> > One pointer tracks the position to insert non-zero, the other iterates the array finding them.

> [!QUESTION] **Q5**: What condition stops the `while` loop in convergence?
> > [!SUCCESS]- Answer
> > `while l < r`. (If they cross, you've checked everything).

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
