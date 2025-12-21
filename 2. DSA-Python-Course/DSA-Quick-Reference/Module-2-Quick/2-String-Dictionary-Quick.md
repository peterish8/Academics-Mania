# 🔍 String Dictionary - Quick Ref

## 🎯 Grouping Patterns

### **Group by First Letter**
```python
def groupByFirstLetter(words):
    groups = {}
    for word in words:
        key = word[0].lower()
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups
```

### **Group Anagrams**
```python
def groupAnagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

### **Word Pattern**
```python
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    p_to_w = {}
    w_to_p = {}
    
    for p, w in zip(pattern, words):
        if p in p_to_w and p_to_w[p] != w:
            return False
        if w in w_to_p and w_to_p[w] != p:
            return False
        p_to_w[p] = w
        w_to_p[w] = p
    
    return True
```

---

## ⚡ **Templates**

**Grouping Template**:
```python
groups = {}
for item in items:
    key = get_key(item)  # Define your key function
    if key not in groups:
        groups[key] = []
    groups[key].append(item)
```

**Bijection Template**:
```python
map1, map2 = {}, {}
for a, b in zip(seq1, seq2):
    if (a in map1 and map1[a] != b) or (b in map2 and map2[b] != a):
        return False
    map1[a] = b
    map2[b] = a
```

---

## 🧠 **Key Insights**
- **Anagrams**: Sort characters as key
- **Patterns**: Use bijection (two-way mapping)
- **Grouping**: Extract meaningful key function

Back to: [[README of DSA Quick Ref]]