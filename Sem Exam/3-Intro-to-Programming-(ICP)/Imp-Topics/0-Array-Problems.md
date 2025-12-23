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
```

---

## ⏱️ Complexity

| Approach | Time | Space |
|----------|------|-------|
| **Sort then pick** | O(n log n) | O(1) |

---

## 🧠 Key Points
- **sort()** puts smallest at front, largest at end
- `a[-1]` = largest, `a[-2]` = second largest
- Handle duplicates by checking if `a[idx] == largest`

---

← Previous: None | [[Imp-Topics-Hub|🏠 Hub]] | Next: [[1-OOPS-Fundamentals|→]]
