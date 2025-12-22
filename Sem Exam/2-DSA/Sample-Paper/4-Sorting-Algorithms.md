# 4️⃣ Sorting Algorithms

---

## 📌 Bubble Sort

> **Idea**: Compare adjacent pairs, swap if wrong order. Largest "bubbles" to end.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization: early exit
            break
    return arr

# TEST
print(bubble_sort([64, 34, 25, 12, 22]))
```

---

## 📌 Selection Sort

> **Idea**: Find minimum in unsorted part, swap to front.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:  # Optimization: skip if already in place
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# TEST
print(selection_sort([64, 25, 12, 22, 11]))
```

---

## 📌 Insertion Sort

> **Idea**: Pick element, insert into correct position in sorted part (like sorting cards).

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# TEST
print(insertion_sort([12, 11, 13, 5, 6]))
```

---

## 📊 Comparison Table

| Algorithm | Best | Average | Worst | Stable? | Swaps |
|-----------|------|---------|-------|---------|-------|
| **Bubble** | O(n) | O(n²) | O(n²) | ✅ Yes | Many |
| **Selection** | O(n²) | O(n²) | O(n²) | ❌ No | Minimum (n-1) |
| **Insertion** | O(n) | O(n²) | O(n²) | ✅ Yes | Moderate |

---

## 🔑 Key Differences

| Bubble | Selection | Insertion |
|--------|-----------|-----------|
| Swap neighbors | Find min, swap to front | Insert in sorted part |
| Best: O(n) if sorted | Always O(n²) | Best: O(n) if sorted |
| Stable | Not stable | Stable |
| Most swaps | Fewest swaps | Good for small arrays |

---

## ⏱️ Space Complexity
All three: **O(1)** - In-place sorting!

---

## 🧠 Key Points
- **Bubble**: Swap adjacent, `swapped` flag for optimization
- **Selection**: `min_idx != i` check to skip useless swaps
- **Insertion**: Best for nearly sorted arrays
- **Stable**: Equal elements maintain original order

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
