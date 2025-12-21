# ⚖️ Sorting Analysis

## 🎯 **Comparing Algorithms**

> [!SUCCESS] **Goal**: Knowing **When** to use **What**.

---

## 🏗️ **Comparison Chart**

| Algorithm | Best Case | Worse Case | Space | Stable? | Best Use Case |
|-----------|-----------|------------|-------|---------|---------------|
| **Bubble** | O(n) | O(n²) | O(1) | Yes | Educational only |
| **Insertion** | O(n) | O(n²) | O(1) | Yes | Small or Nearly Sorted arrays |
| **Selection** | O(n²) | O(n²) | O(1) | No | Minimizing Swaps (Write heavy memory) |
| **Merge Sort**| O(n log n)| O(n log n)| O(n) | Yes | Linked Lists, Reliable speed |
| **Quick Sort**| O(n log n)| O(n²) | O(log n)| No | Arrays, Fastest on average |

---

## ⚓ **Stability**

> [!INFO] **Definition**: A Stable algorithm preserves the relative order of equal elements.
> **Example**: Sorting a list of Students by Name, then by Grade.
> - **Input**: `[(Bob, 80), (Alice, 90), (Charlie, 80)]`
> - **Stable Sort** (by Grade): `[(Bob, 80), (Charlie, 80), (Alice, 90)]` (Bob stays before Charlie).
> - **Unstable**: Bob and Charlie might swap places.

**Stable Algorithms**: Bubble, Insertion, Merge.
**Unstable**: Selection, Quick, Heap.

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Insertion** = Best for "Nearly Sorted" 🃏.
> - **Merge** = Consistent but uses extra Space 💾.
> - **Quick** = Fastest normally, but worst case sucks (O(n²)) ⚡.
> - **Selection** = Never Stable (Jumps over items) 🚫.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Which algorithm is best for a list that is already 99% sorted?
> > [!SUCCESS]- Answer
> > **Insertion Sort** (O(n)).

> [!QUESTION] **Q2**: Why is Merge Sort preferred for Linked Lists?
> > [!SUCCESS]- Answer
> > Accessing memory in lists is slow for random access (Quick Sort), but Merge Sort works sequentially and doesn't require extra space if implemented well for lists.

> [!QUESTION] **Q3**: What is the Space Complexity of Merge Sort?
> > [!SUCCESS]- Answer
> > **O(n)**. It needs temporary arrays to merge.

> [!QUESTION] **Q4**: Why is Quick Sort usually preferred over Merge Sort for Arrays?
> > [!SUCCESS]- Answer
> > Better locality of reference (Cache friendly) and no O(n) space overhead.

> [!QUESTION] **Q5**: Give an example where Stability matters.
> > [!SUCCESS]- Answer
> > Sorting a spreadsheet: First sort by Date, then by Name. You want the dates to remain ordered for each name.

---

Back to: [[Sem Exam/2-DSA/Module 3 - Searching & Linked List/README|Module 3 Hub]] | [[../DSA-Hub|DSA Hub]]
