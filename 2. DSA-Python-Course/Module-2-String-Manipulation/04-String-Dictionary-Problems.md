Understanding `sorted(freq, key=lambda x: freq[x])`

**Breaking it down:**

```python
freq = {1: 3, 2: 2, 3: 1}

# sorted(freq) sorts just the keys
sorted(freq)  # [1, 2, 3] - sorted by key value

# sorted(freq, key=lambda x: freq[x]) sorts keys by their frequency
sorted(freq, key=lambda x: freq[x])  # [3, 2, 1]

# With reverse=True
sorted(freq, key=lambda x: freq[x], reverse=True)  # [1, 2, 3]
```

**What `lambda x: freq[x]` does:**
```
For element x=1: lambda returns freq[1] = 3
For element x=2: lambda returns freq[2] = 2  
For element x=3: lambda returns freq[3] = 1

Sorts: [1(3), 2(2), 3(1)] by those numbers
Result: [1, 2, 3] when reverse=True
```

---

### Another Example

**Input:** `nums = [4,1,-1,2,-1,2,3]`, `k = 2`

```
Step 1: Count
  freq = {4: 1, 1: 1, -1: 2, 2: 2, 3: 1}

Step 2: Sort by frequency
  Frequencies: -1→2, 2→2, 4→1, 1→1, 3→1
  
  Elements with freq 2: [-1, 2]
  Elements with freq 1: [4, 1, 3]
  
  Sorted: [-1, 2, 4, 1, 3] or [2, -1, 4, 1, 3]
  (order can vary for same frequency)

Step 3: Top k=2
  Result: [-1, 2] or [2, -1] ✓
```

---

## 🎓 Dictionary Patterns Summary

### Pattern 1: Existence Check (Jewels and Stones)

```python
# Create lookup dictionary
lookup = {item: True for item in collection}

# Or use set
lookup = set(collection)

# Check membership - O(1)
if element in lookup:
    # do something
```

**Use when:**
- Need to check if element exists
- Membership testing is frequent
- Order doesn't matter

---

### Pattern 2: Frequency Counting (Top K)

```python
# Count occurrences
freq = {}
for item in collection:
    freq[item] = freq.get(item, 0) + 1

# Sort by frequency
sorted_items = sorted(freq, key=lambda x: freq[x], reverse=True)

# Get top k
top_k = sorted_items[:k]
```

**Use when:**
- Need to count occurrences
- Find most/least frequent elements
- Group by frequency

---

### Pattern 3: Dictionary Comprehension

```python
# Create dict from iterable
jewels_dict = {j: True for j in jewels}

# With enumeration
index_dict = {val: idx for idx, val in enumerate(arr)}

# With condition
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
```

---

## 🔄 Common Dictionary Operations

### Creating Dictionaries

```python
# Empty dict
d = {}
d = dict()

# From list of tuples
d = dict([('a', 1), ('b', 2)])

# Comprehension
d = {x: x**2 for x in range(5)}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
```

---

### Accessing Values

```python
# Direct access (KeyError if not exists)
value = d['key']

# Safe access with default
value = d.get('key', default_value)

# Get all keys
keys = d.keys()

# Get all values  
values = d.values()

# Get all items (key-value pairs)
items = d.items()
```

---

### Modifying Dictionaries

```python
# Add/Update
d['key'] = value

# Increment count
d['key'] = d.get('key', 0) + 1

# Delete
del d['key']
removed_value = d.pop('key', default)

# Check if key exists
if 'key' in d:
    # do something

# Merge dictionaries (Python 3.9+)
d3 = d1 | d2
```

---

## ✅ DO / ❌ AVOID

### ✅ DO

- Use dictionaries for O(1) lookups
- Use `.get(key, default)` to avoid KeyError
- Use dictionary comprehension for cleaner code
- Remember: dictionaries preserve insertion order (Python 3.7+)
- Use `collections.Counter` for frequency counting (even easier!)

```python
from collections import Counter

# Instead of manual counting
freq = Counter(nums)
top_k = freq.most_common(k)  # Returns [(element, count), ...]
```

---

### ❌ AVOID

- Using lists when you need fast lookups
- Iterating through dictionary to find a value (use inverse dict instead)
- Forgetting that dictionary keys must be immutable (no lists as keys!)
- Not handling missing keys (use `.get()` or check with `in`)
- Assuming dictionaries are sorted in Python < 3.7

---

## 🔗 Related Topics

- [[03-Character-Frequency-Problems]] - More frequency patterns
- [[Valid-Anagram]] - Dictionary comparison
- [[Two-Sum]] - Dictionary for O(n) solution
- [[Group-Anagrams]] - Advanced dictionary usage

---

## 📝 Practice Problems

### Easy
1. LeetCode 771 - Jewels and Stones
2. LeetCode 1 - Two Sum
3. LeetCode 383 - Ransom Note

### Medium  
1. LeetCode 347 - Top K Frequent Elements
2. LeetCode 49 - Group Anagrams
3. LeetCode 692 - Top K Frequent Words

### Advanced
1. LeetCode 895 - Maximum Frequency Stack
2. LeetCode 1152 - Analyze User Website Visit Pattern

---

## 🧪 Test Your Understanding

### Challenge 1: Two Sum
```
Given nums = [2,7,11,15], target = 9
Return indices [0,1] because nums[0] + nums[1] = 9

Hint: Use dictionary to store {value: index}
```

### Challenge 2: Group Anagrams
```
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Hint: Use sorted string as dictionary key
```

### Challenge 3: First Unique Character
```
Input: "leetcode"
Output: 0 (first non-repeating char is 'l' at index 0)

Hint: Count frequency, then find first with count=1
```

---

## 🎨 Visual: Dictionary vs List Lookup

```
List Lookup: O(n)
[1, 2, 3, 4, 5]
 ↓  ↓  ↓  ↓  ↓
Check each element until found

Dictionary Lookup: O(1)
{1: True, 2: True, 3: True, 4: True, 5: True}
        ↓
Direct access via hash

Speed comparison for 1000 items:
List: 500 comparisons average
Dict: 1 hash calculation ⚡
```

---

## 📚 Advanced: Counter Class

```python
from collections import Counter

# Automatic frequency counting
nums = [1, 1, 1, 2, 2, 3]
freq = Counter(nums)
# Counter({1: 3, 2: 2, 3: 1})

# Get top k most common
top_k = freq.most_common(2)
# [(1, 3), (2, 2)]

# Get just the elements
elements = [elem for elem, count in top_k]
# [1, 2]

# Arithmetic operations
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'b'])
c1 + c2  # Counter({'a': 3, 'b': 3, 'c': 1})
c1 - c2  # Counter({'a': 1, 'c': 1})
```

---

**Previous**: [[03-Character-Frequency-Problems]] | **Next**: [[05-Prefix-Sum-Technique]]

Back to: [[README of Frontend]]
