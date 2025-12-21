# 📝 Character Frequency - Quick Ref

## 🎯 HashMap Pattern

### **Basic Frequency Count**
```python
def charFrequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
```

### **Valid Anagram**
```python
def isAnagram(s, t):
    return sorted(s) == sorted(t)
    # OR: Counter(s) == Counter(t)
```

### **Most Frequent Character**
```python
def mostFrequent(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)
```

---

## ⚡ **Templates**

**Count Pattern**:
```python
freq = {}
for item in collection:
    freq[item] = freq.get(item, 0) + 1
```

**Compare Pattern**:
```python
freq1 = Counter(s1)
freq2 = Counter(s2)
return freq1 == freq2
```

---

## 🧠 **Key Points**
- Use `dict.get(key, 0)` for safe counting
- `Counter` from collections for quick frequency
- `max(dict, key=dict.get)` for most frequent

Back to: [[README of DSA Quick Ref]]