# 🧠 Python Lists & Memory

## 🎯 **Python Lists as Arrays**

> [!SUCCESS] **Concept**: Python Lists are **Dynamic Arrays**.
> Unlike C++ static arrays, they grow automatically! 🌱

**Key Operations & Complexity:**
- **Access** (`arr[i]`): **O(1)** (Instant). It calculates memory address directly.
- **Update** (`arr[i] = 5`): **O(1)**.
- **Append** (`arr.append(5)`): **O(1)** (Amortized). Sometimes it resizes, but usually fast.
- **Insert/Delete** (`arr.insert(0, 5)`): **O(n)** ⚠️. It has to shift ALL other elements. This is slow!

---

## 💾 **Memory Layout**

> [!INFO] **Contiguous Memory**:
> Array elements are stored side-by-side in RAM.
> `[10, 20, 30]` might live at addresses `#100, #104, #108` (4 bytes each).

**Python Specifics**:
- Python lists actually store **references** (pointers) to objects, not the objects themselves.
- This allows lists to hold mixed types: `[1, "hello", True]`.

---

## 🔄 **Iteration Types**

### **1. Value Only**
```python
for num in nums:
    print(num)
```

### **2. Index & Value (Enumerate)** 🌟
> Use this when you need the position!
```python
for i, num in enumerate(nums):
    print(f"Index {i} has {num}")
```

### **3. Range (Index only)**
```python
for i in range(len(nums)):
    print(nums[i])
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Append** = Fast 🐇 (Add to end).
> - **Insert(0)** = Slow 🐢 (Shifts everyone).
> - **Contiguous** = Side-by-Side neighbors (Reference locality) 🏘️.
> - **Dynamic** = Elastic Waistband (Stretches as needed) 👖.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What is the time complexity of accessing the 5th element in a list of 1 million items?
> > [!SUCCESS]- Answer
> > **O(1)**. Access is constant time regardless of size.

> [!QUESTION] **Q2**: Why is `element in list` (Linear Search) considered O(n)?
> > [!SUCCESS]- Answer
> > Because in the worst case (element at the end or missing), it has to check every single item.

> [!QUESTION] **Q3**: Does a Python list enforce a single data type?
> > [!SUCCESS]- Answer
> > No. It is a dynamic array of object pointers, so it can hold mixed types.

> [!QUESTION] **Q4**: What happens to memory addresses when you slice a list `arr[1:3]`?
> > [!SUCCESS]- Answer
> > Python creates a **NEW** list with **NEW** references (Shallow Copy). It does not just point to the old chunk.

> [!QUESTION] **Q5**: Which is faster: `arr.pop()` or `arr.pop(0)`?
> > [!SUCCESS]- Answer
> > `arr.pop()` is **O(1)** (removes from end). `arr.pop(0)` is **O(n)** (removes from front and shifts everything).

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
