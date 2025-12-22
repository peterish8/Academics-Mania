# 2️⃣ String Algorithms

---

## 📌 Substring vs Subsequence

| Type | Definition | Example |
|------|------------|---------|
| **Substring** | Contiguous characters | "cat" in "s**cat**ter" |
| **Subsequence** | Order maintained, gaps allowed | "ace" in "**a**b**c**d**e**" |

---

## 📌 Common String Methods

```python
s = "Hello World"

# split() - Split string into list
print(s.split())       # ['Hello', 'World']
print(s.split('o'))    # ['Hell', ' W', 'rld']

# join() - Join list into string
words = ['a', 'b', 'c']
print('-'.join(words))  # 'a-b-c'
print(''.join(words))   # 'abc'

# find() - Find first occurrence (returns -1 if not found)
print(s.find('o'))      # 4
print(s.find('x'))      # -1

# rfind() - Find last occurrence
print(s.rfind('o'))     # 7

# replace() - Replace substring
print(s.replace('World', 'Python'))  # 'Hello Python'

# Other useful methods
print(s.lower())        # 'hello world'
print(s.upper())        # 'HELLO WORLD'
print(s.strip())        # Remove whitespace
print(s.startswith('He'))  # True
print(s.endswith('ld'))    # True
print(s.isalnum())      # False (has space)
print(s.isalpha())      # False (has space)
```

---

## 📌 Substring Problems

### Check if Substring Exists
```python
def hasSubstring(main, sub):
    return sub in main  # O(n*m)

# TEST
print(hasSubstring("hello", "ell"))  # True
```

### Find All Occurrences
```python
def findAll(main, sub):
    indices = []
    start = 0
    while True:
        idx = main.find(sub, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1
    return indices

# TEST
print(findAll("ababa", "aba"))  # [0, 2]
```

---

## 📌 Subsequence Problems

### Is Subsequence
```python
def isSubsequence(s, t):
    i = 0  # Pointer for s
    for char in t:
        if i < len(s) and char == s[i]:
            i += 1
    return i == len(s)

# TEST
print(isSubsequence("ace", "abcde"))  # True
print(isSubsequence("aec", "abcde"))  # False
```

---

## 🧠 Key Points
- **Substring**: Use `in`, `find()`, `rfind()`
- **Subsequence**: Two pointer technique
- **split/join**: Convert between string and list
- **Time**: `find()` is O(n*m), `in` is O(n*m)

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
