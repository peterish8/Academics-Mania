# PDF 12: Sets in Python - Quick Summary

## 🎯 Set Essentials

### Definition & Properties
- **Set**: Unordered collection of **unique**, immutable elements
- **Key Properties**: No duplicates, Unordered, Mutable (can add/remove), Not indexable
- **Elements**: Must be immutable (numbers, strings, tuples) - no lists/dicts

### Creation & Basic Operations
```python
# Creation
s = set()                    # Empty set (NOT {})
s1 = {1, 2, 3, 4}           # With values
s2 = set([1, 2, 3, 4])      # From list

# Basic operations
s.add(5)                     # Add single element
s.update([6, 7])             # Add multiple elements
print(len(s))                # Length
print(2 in s)                # Membership test
```

## 🔥 Essential Methods

| Method | Purpose | Behavior |
|--------|---------|----------|
| `add(x)` | Add element | No effect if already exists |
| `update(iterable)` | Add multiple | Merges with existing |
| `remove(x)` | Remove element | **Error** if not found |
| `discard(x)` | Remove element | **No error** if not found |
| `pop()` | Remove random | Returns removed element |
| `clear()` | Empty set | Removes all elements |
| `copy()` | Shallow copy | Returns new set |

## ⚡ Set Operations (Mathematical)

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (all unique elements)
A | B           # {1, 2, 3, 4, 5, 6}
A.union(B)      # Same as above

# Intersection (common elements)
A & B           # {3, 4}
A.intersection(B)  # Same as above

# Difference (in A but not B)
A - B           # {1, 2}
A.difference(B) # Same as above

# Symmetric Difference (unique to each)
A ^ B           # {1, 2, 5, 6}
A.symmetric_difference(B)  # Same as above
```

## 🎯 Set Relationships

```python
A = {1, 2}
B = {1, 2, 3}
C = {4, 5}

# Subset/Superset
A.issubset(B)      # True (A ⊆ B)
B.issuperset(A)    # True (B ⊇ A)

# Disjoint (no common elements)
A.isdisjoint(C)    # True (no overlap)
```

## 🔥 Common Exam Patterns

### 1. Remove Duplicates from List
```python
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))     # [1, 2, 3, 4]
```

### 2. Find Common Elements
```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))  # [3, 4]
```

### 3. Find Unique Elements (Symmetric Difference)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
unique_elements = A ^ B      # {1, 2, 5, 6}
```

### 4. Subarray Sum Zero Algorithm
```python
def subarray_sum_zero(arr):
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)
    return False
```

## ⚠️ Key Differences

### remove() vs discard()
- `remove(x)` → Raises KeyError if x not found
- `discard(x)` → No error if x not found (safe removal)

### {} vs set()
- `{}` → Creates empty **dictionary**
- `set()` → Creates empty **set**

### Set vs List
| Feature | Set | List |
|---------|-----|------|
| **Duplicates** | Not allowed | Allowed |
| **Order** | Unordered | Ordered |
| **Indexing** | No | Yes |
| **Mutability** | Mutable | Mutable |
| **Use Case** | Unique items | Ordered collection |

## ⚡ Quick Tips
- **Fast membership testing**: `x in set` is O(1) vs O(n) for lists
- **Automatic deduplication**: Converting list to set removes duplicates
- **Mathematical operations**: Use `|`, `&`, `-`, `^` for set operations
- **Immutable elements only**: Can't store lists or dicts in sets
- **Unordered**: Don't rely on element order

## 🎯 Iteration
```python
s = {1, 2, 3}
for element in s:
    print(element)  # Order not guaranteed
```

---
*Previous: [[PDF-11-Dictionaries-Quick-Summary]] | Next: [[PDF-13-File-Handling-Quick-Summary]]*

#sets #python #unique-elements #mathematical-operations #exam-prep