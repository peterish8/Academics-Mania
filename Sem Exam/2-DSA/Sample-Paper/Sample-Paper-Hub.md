# 📝 DSA Sample Paper - Quick Revision Hub

> [!WARNING] **Exam Focus!** These are the topics sir said will come. Master these!

> [!INFO] **Sample Paper Progress Tracker**
> 
> ```dataviewjs
> const tasks = dv.current().file.tasks;
> const completed = tasks.filter(t => t.completed).length;
> const total = tasks.length;
> const percent = total === 0 ? 0 : Math.round((completed / total) * 100);
> 
> dv.paragraph(`**Status:** ${completed}/${total} Topics Completed (**${percent}%**)`);
> dv.paragraph(`<div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);"><div style="width: ${percent}%; background-color: #4caf50; height: 100%; border-radius: 10px; transition: width 0.5s ease;"></div></div>`);
> ```

---

## 📋 Topics Checklist

### 1️⃣ Prefix Sum & Two Pointers
- [x] Running Sum of 1D Array (Prefix Sum)
- [x] Subarray Sum Equals K (Prefix Sum + HashMap)
- [x] Best Time to Buy and Sell Stock (Track Min + Greedy)
- [x] Two Sum II - Sorted Array (Two Pointers)
- [x] Remove Duplicates from Sorted Array (Two Pointers)
→ [[1-Prefix-Sum-Two-Pointers|📖 Read Notes]]

---

### 2️⃣ String Algorithms
- [x] Substring Problems (Contiguous chars)
- [x] Subsequence Problems (Two Pointer)
- [x] String Methods (split, join, find, replace, rfind)
→ [[2-String-Algorithms|📖 Read Notes]]

---

### 3️⃣ Kadane's Algorithm
- [x] Concept of Kadane's Algorithm (Reset if negative)
- [x] Maximum Subarray Sum (current_sum vs max_sum)
- [x] Time Complexity Analysis (O(n))
→ [[3-Kadanes-Algorithm|📖 Read Notes]]

---

### 4️⃣ Sorting Algorithms
- [x] Bubble Sort (Swap adjacent, swapped flag)
- [x] Selection Sort (Find min, swap to front)
- [x] Insertion Sort (Insert in sorted part)
- [x] Differences between all three (Stability, Swaps)
- [x] Time & Space Complexity (All O(n²), O(1) space)
→ [[4-Sorting-Algorithms|📖 Read Notes]]

---

### 5️⃣ Binary Search & Variations
- [ ] Basic Binary Search (while left <= right)
- [ ] Search Insert Position (return left)
- [ ] Sqrt(x) (Binary search on answer)
- [ ] Find Peak Element (Compare mid with mid+1)
- [ ] Search in Rotated Sorted Array (Check sorted half)
- [ ] Find Minimum in Rotated Array (Compare mid with right)
→ [[5-Binary-Search-Variations|📖 Read Notes]]

---

### 6️⃣ Array Manipulation
- [ ] Minimum Swaps to Sort (Cycle detection, k-1 swaps)
→ [[6-Array-Manipulation|📖 Read Notes]]

---

### 7️⃣ Linked List Operations
- [ ] Insert at Beginning/End/Position k (Pointer update)
- [ ] Delete from Beginning/End/Position k (Bypass node)
- [ ] Find Middle Node (Slow-Fast Pointers)
- [ ] Detect Cycle (Floyd's - slow meets fast)
→ [[7-Linked-List-Operations|📖 Read Notes]]

---

### 8️⃣ Linked List Types - Comparison
- [ ] Doubly Linked List (prev + next pointers)
- [ ] Circular Linked List (last → head)
- [ ] Comparison Table (Memory, Deletion, Use case)
→ [[8-Linked-List-Types|📖 Read Notes]]

---

### 9️⃣ Hashing Techniques
- [ ] Dictionary/HashMap (Key-Value, O(1) lookup)
- [ ] Set (Unique values only)
- [ ] Dict vs Set Comparison (Map vs Existence check)
→ [[9-Hashing-Techniques|📖 Read Notes]]

---

## 🚀 Study Order (By Priority)

| Time | Topic | 
|------|-------|
| 20 min | 🔴 Sorting Algorithms |
| 20 min | 🔴 Binary Search Variations |
| 25 min | 🔴 Linked List Operations |
| 10 min | 🟡 Kadane's Algorithm |
| 15 min | 🟡 Prefix Sum & Two Pointers |
| 10 min | 🟢 String Methods |
| 10 min | 🟢 Dict vs Set |

---

Good luck! 🍀
