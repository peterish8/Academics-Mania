# 0️⃣ Array Problems - Second Largest & Largest

---

## 📌 Largest + Second Largest Sum

> **Goal**: Find the sum of the largest and second largest elements in an array.

```python
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    
    # Sort the array
    a.sort()
    largest = a[-1]
    
    # Find second largest (handle duplicates)
    idx = -2
    for i in range(len(a)):
        if a[idx] == largest:
            idx -= 1
    second_largest = a[idx]
    max_sum = largest + second_largest
    
    print(max_sum)

# TEST (Single input)
a = [12, 35, 1, 10, 34, 1]
a.sort()
largest = a[-1]
idx = -2
while a[idx] == largest:
    idx -= 1
second_largest = a[idx]
print("Array:", [12, 35, 1, 10, 34, 1])
print("Largest:", largest)
print("Second Largest:", second_largest)
print("Sum:", largest + second_largest)
```

---

## 📌 Second Largest Among Three Numbers

> **Goal**: Given three numbers, find the second largest.

```python
# Program to find the second largest among three numbers

T = int(input())  # number of test cases

for _ in range(T):
    A, B, C = map(int, input().split())
    nums = [A, B, C]
    nums.sort()          # sort the three numbers
    print(nums[1])       # second largest is at index 1

# TEST (Single input)
A, B, C = 5, 10, 3
nums = [A, B, C]
nums.sort()
print(f"Numbers: {A}, {B}, {C}")
print(f"Sorted: {nums}")
print(f"Second Largest: {nums[1]}")
```

---

## 📌 Optimized Second Largest (Single Pass)

> **Goal**: Find the second largest without sorting (O(n) time).

```python
def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    largest = float('-inf')
    second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else -1

# TEST
arr = [12, 35, 1, 10, 34, 1]
print("Array:", arr)
print("Second Largest:", second_largest(arr))
```

---

## ⏱️ Complexity Comparison

| Approach | Time | Space |
|----------|------|-------|
| **Sort then pick** | O(n log n) | O(1) |
| **Single pass** | O(n) | O(1) |

---

## 🧠 Key Points
- **Sorting approach**: Simple but O(n log n)
- **Single pass**: Track `largest` and `second` in one loop
- Handle duplicates: Check `num != largest` before updating second

---

Back to: [[Imp-Topics-Hub|ICP Topics Hub]]
