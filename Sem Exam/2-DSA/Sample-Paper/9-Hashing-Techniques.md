# 9️⃣ Hashing Techniques

---

## 📌 Dictionary (Hash Map)

> **Goal**: Store key-value pairs with O(1) average lookup, insert, delete.

```python
# Create
d = {}
d = dict()

# Insert
d['key'] = 'value'
d[1] = 100

# Access
print(d['key'])
print(d.get('key', 'default'))  # Safe access

# Delete
del d['key']

# Check existence
if 'key' in d:
    print("Found!")

# Iterate
for key in d:
    print(key, d[key])
for key, value in d.items():
    print(key, value)
```

### Optimal Use Cases
| Use Case | Example |
|----------|---------|
| **Frequency count** | Count character occurrences |
| **Two Sum** | Store value → index mapping |
| **Caching** | Memoization |
| **Grouping** | Group anagrams by sorted key |

---

## 📌 Set

> **Goal**: Store unique values only with O(1) average lookup, insert, delete.

```python
# Create
s = set()
s = {1, 2, 3}

# Add
s.add(4)

# Remove
s.remove(4)      # Raises error if not found
s.discard(4)     # Safe, no error

# Check existence
if 4 in s:
    print("Found!")

# Operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # Union: {1, 2, 3, 4}
print(a & b)  # Intersection: {2, 3}
print(a - b)  # Difference: {1}
```

---

## 📊 Dictionary vs Set

| Feature | Dictionary | Set |
|---------|------------|-----|
| **Stores** | Key-Value pairs | Only values |
| **Duplicates** | Keys unique | Values unique |
| **Lookup** | O(1) | O(1) |
| **Use when** | Need mapping | Need uniqueness |

---

## 📌 When to Use What?

### Use Dictionary:
- Need to **map** one thing to another
- Counting frequency
- Caching results
- Two Sum (value → index)

### Use Set:
- Only need to check **existence**
- Remove duplicates
- Contains Duplicate problem
- Intersection of arrays

---

## 💻 Examples

### Frequency Count (Dict)
> **Goal**: Count how many times each element appears.

```python
def frequency(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    return count

# TEST
print(frequency([1, 2, 2, 3, 3, 3]))
```

### Contains Duplicate (Set)
> **Goal**: Check if any element appears more than once.

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# TEST
print(containsDuplicate([1, 2, 3, 1]))  # True
```

### Two Sum (Dict)
> **Goal**: Find two numbers that add up to target. Return their indices.

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# TEST
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
```

---

## ⏱️ Complexity

| Operation | Dict | Set |
|-----------|------|-----|
| **Insert** | O(1) avg | O(1) avg |
| **Lookup** | O(1) avg | O(1) avg |
| **Delete** | O(1) avg | O(1) avg |
| **Worst case** | O(n) | O(n) |

---

## 🧠 Key Points
- **Dict**: Key-Value, use for mapping
- **Set**: Values only, use for uniqueness
- **Both O(1)**: Hash-based lookup
- **get()**: Safe dict access with default

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
