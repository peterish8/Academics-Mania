# 🧶 Strings: Immutability & Slicing

## 🎯 **String Immutability**

> [!WARNING] **The Rule**: You CANNOT change characters in a string.
> `s[0] = "a"` ❌ **TypeError**!

**Why?**
- Strings are stored in a specialized memory area.
- Optimization: Identical strings can point to the same memory (String Interning).

**Workaround (Modifying Strings):**
Convert to list -> Modify -> Join back.
```python
s = "hello"
lst = list(s)       # ['h', 'e', 'l', 'l', 'o']
lst[0] = 'y'
s = "".join(lst)    # "yello"
```

---

## 🔪 **Slicing Power**

> `string[start:stop:step]`

- `start`: Inclusive. Default 0.
- `stop`: Exclusive. Default End.
- `step`: Jump size. Default 1.

### **Common Recipes** 📖

| Operation | Code | Example ("Python") |
|-----------|------|--------------------|
| **First 3** | `s[:3]` | "Pyt" |
| **Last 3** | `s[-3:]` | "hon" |
| **Reverse** | `s[::-1]` | "nohtyP" 🌟 |
| **Skip 1** | `s[::2]` | "Pto" |
| **Copy** | `s[:]` | "Python" |

---

## ⚡ **String Performance Trap**

> [!TIP] **Avoid concatenation in loops!** 🛑

```python
# BAD O(n^2) 🐢
res = ""
for char in large_list:
    res += char  # Creates a NEW string every single time!

# GOOD O(n) 🐇
res_list = []
for char in large_list:
    res_list.append(char)
final_res = "".join(res_list) # Joins once at the end
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Immutable** = Read-Only 🔒.
> - **Join** > **Plus** (For many strings).
> - **[::-1]** = The Magic Reverser ⏪.
> - **Stop is Exclusive** = "Up to, but not including" 🛑.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Is `s = s + "a"` valid in Python?
> > [!SUCCESS]- Answer
> > Yes, but it creates a **completely new string** and reassigns `s` to point to it. The old string is garbage collected.

> [!QUESTION] **Q2**: What does `s[1:-1]` do?
> > [!SUCCESS]- Answer
> > Removes the first and last character (Returns from index 1 up to last-1).

> [!QUESTION] **Q3**: How do you modify the 3rd character of a string efficiently?
> > [!SUCCESS]- Answer
> > Convert to list, modify, then join.

> [!QUESTION] **Q4**: What is the Time Complexity of checking `len(s)`?
> > [!SUCCESS]- Answer
> > **O(1)**. Python stores the length as a property of the string object.

> [!QUESTION] **Q5**: What happens if `start` index in a slice is bigger than string length?
> > [!SUCCESS]- Answer
> > No error. It just returns an empty string `""`. Python slicing is very forgiving.

---

Back to: [[Sem Exam/2-DSA/Module 1 - Intro & Arrays/README|Module 1 Hub]] | [[../DSA-Hub|DSA Hub]]
