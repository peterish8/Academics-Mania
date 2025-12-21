# PDF 8: String Functions & find() Method - Quick Summary

## 🎯 find() Method Essentials

### Syntax & Purpose
```python
string.find(substring, start, end)
```
- **Returns**: Lowest index of substring (or -1 if not found)
- **Parameters**: 
  - `substring`: Text to search
  - `start`: Optional start position
  - `end`: Optional end position

### Key Examples
```python
s = "hello world, hello python"
s.find("hello")      # 0 (first occurrence)
s.find("hello", 1)   # 13 (search from index 1)
s.find("python")     # 19
s.find("bye")        # -1 (not found)
```

## 🔥 Exam Algorithms

### 1. Anagram Check Using count()
```python
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            return False
    return True
```

### 2. Replace Second Occurrence
```python
def replace_second_hello(s):
    first = s.find("hello")
    if first == -1:
        return s
    second = s.find("hello", first + len("hello"))
    if second == -1:
        return s
    return s[:second] + "hi" + s[second + len("hello"):]
```

## ⚡ Quick Reference

| Method | Returns | Use Case |
|--------|---------|----------|
| `find()` | Index or -1 | Safe searching |
| `index()` | Index or Exception | When sure substring exists |
| `count()` | Number of occurrences | Frequency counting |

## 🎯 Common Patterns
- **Multiple occurrences**: Use start parameter in find()
- **Anagram checking**: Compare character frequencies
- **String replacement**: Slice and reconstruct
- **Safe searching**: find() returns -1, index() raises exception

## ⚠️ Key Points
- find() is **case-sensitive**
- Returns **first occurrence** index
- Use **start parameter** for subsequent searches
- **-1 means not found** (never raises exception)

---
*Previous: [[PDF-7-Strings-Quick-Summary]] | Next: [[PDF-9-Lists-Quick-Summary]]*

#string-functions #find-method #python #exam-prep #algorithms