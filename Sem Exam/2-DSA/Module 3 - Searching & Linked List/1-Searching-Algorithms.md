# 🔍 Searching Algorithms

## 🎯 **Linear vs Binary**

### **1. Linear Search**
> **O(n)**. Iterate one by one. Correct for ANY list (sorted or not).

### **2. Binary Search**
> **O(log n)**. Divide & Conquer.
> **Constraint**: Array MUST be **Sorted**.

```python
def binarySearch(arr, target):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = l + (r - l) // 2  # Safe Mid Formula
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1 # Look Right
        else:
            r = mid - 1 # Look Left
            
    return -1 # Not found

# TEST
arr = [1, 3, 5, 7, 9, 11, 13]
print("Array:", arr)
print("Find 7:", binarySearch(arr, 7))
print("Find 4:", binarySearch(arr, 4))
```

---

## ⚡ **Advanced Searching**

### **1. Mid Formula Overflow**
> In languages like C++/Java, `(l+r)/2` can crash if numbers are huge.
> **Fix**: `mid = l + (r - l) // 2`. (Not needed in Python, but good interview knowledge!).

### **2. First/Last Occurrence**
> Don't stop when `arr[mid] == target`! Store result and continue.
> - To find **First**: Store mid, move `r = mid - 1` (Keep looking left).
> - To find **Last**: Store mid, move `l = mid + 1` (Keep looking right).

### **3. Rotated Sorted Array**
> Array `[4, 5, 1, 2, 3]` is sorted but rotated.
> Logic: One half is ALWAYS sorted. Find which half, then proceed.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Binary Search** = Phonebook method (Open middle, discard half).
> - **Condition**: `l <= r` (Don't forget the equal!).
> - **Sorted** = Binary Search signal 📶.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the worst case complexity of Binary Search?
> > [!SUCCESS]- Answer
> > **O(log n)**.

> [!QUESTION] **Q2**: Can Binary Search work on Linked Lists?
> > [!SUCCESS]- Answer
> > No (Efficiently). You cannot jump to `mid` instantly in a Linked List.

> [!QUESTION] **Q3**: What happens if `l` becomes greater than `r`?
> > [!SUCCESS]- Answer
> > The loop terminates, meaning the element is not found.

> [!QUESTION] **Q4**: How to handle duplicates in Binary Search?
> > [!SUCCESS]- Answer
> > Standard BS finds *any* one of them. Use First/Last Logic to find specific ones.

> [!QUESTION] **Q5**: Why calculating mid as `(l+r)//2` is risky in C++?
> > [!SUCCESS]- Answer
> > Integer Overflow if `l` and `r` are both close to 2 billion.

---

Back to: [[Sem Exam/2-DSA/Module 3 - Searching & Linked List/README|Module 3 Hub]] | [[../DSA-Hub|DSA Hub]]
