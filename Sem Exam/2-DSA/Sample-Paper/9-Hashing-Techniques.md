# 9️⃣ Hashing Techniques

---

## 📌 Dictionary (Hash Map)

### What is it?
- Key-value pair storage
- **O(1)** average lookup, insert, delete

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

### What is it?
- Collection of **unique** values only
- No duplicates, no key-value pairs
- **O(1)** average lookup, insert, delete

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
```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# TEST
print(containsDuplicate([1, 2, 3, 1]))  # True
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
