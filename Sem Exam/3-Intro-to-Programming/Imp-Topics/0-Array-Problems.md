# 0️⃣ Array Problems - Second Largest & Largest

---

## 📌 Second Largest Element

> **Goal**: Find the second largest element in an array in a single pass.

> [!TIP] **Key Insight**: Track both `largest` and `second_largest` while traversing.

```python
def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    largest = float('-inf')
    second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest  # Previous largest becomes second
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else -1

# TEST
arr = [12, 35, 1, 10, 34, 1]
print("Array:", arr)
print("Second Largest:", second_largest(arr))  # 34
```

---

## 📌 Largest & Second Largest Together

> **Goal**: Return both largest and second largest in one traversal.

```python
def largest_and_second(arr):
    if len(arr) < 2:
        return None, None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return first, second

# TEST
arr = [12, 35, 1, 10, 34, 1]
first, second = largest_and_second(arr)
print(f"Largest: {first}, Second Largest: {second}")
```

---

## ⏱️ Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) - Single pass |
| **Space** | O(1) - Only 2 variables |

---

## 🧠 Key Points
- Track two variables: `largest` and `second`
- Update `second = largest` before updating `largest`
- Check `num != largest` to handle duplicates

---

Back to: [[Imp-Topics-Hub|ICP Topics Hub]]
