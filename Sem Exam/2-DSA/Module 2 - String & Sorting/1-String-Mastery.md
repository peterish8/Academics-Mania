# 🔡 String Mastery

## 🎯 **Common String Problems**

> [!SUCCESS] **Goal**: Manipulate text efficiently.
> **Recall**: Strings are immutable in Python!

---

## 🔄 **1. Reversal & Palindromes**

**Palindrome**: Reads same forwards and backwards ("racecar").
```python
def isPalindrome(s):
    # Method 1: Slicing (Easy)
    return s == s[::-1]

    # Method 2: Two Pointers (Interview Safe)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]: return False
        l += 1
        r -= 1
    return True
```

---

## 🔠 **2. Anagrams**

**Anagram**: Same characters, different order ("listen" -> "silent").
```python
from collections import Counter

def isAnagram(s1, s2):
    return Counter(s1) == Counter(s2) # O(n) Time, O(1) Space (26 chars)
```

---

## 🧵 **3. Substrings vs Subsequences**

- **Substring**: Contiguous part. "cat" inside "scatter".
- **Subsequence**: Non-contiguous but order maintained. "ace" inside "**a**b**c**d**e**".

**Checking Substring**:
```python
if "sub" in string: ... # O(n*m)
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Anagram** = Count characters. 📊
> - **Palindrome** = Two Pointers meeting in middle. 👈👉
> - **Immutable** = Don't loop `s += char`.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Time complexity of `s == s[::-1]`?
> > [!SUCCESS]- Answer
> > **O(n)**. The string must be traversed to copy/reverse it.

> [!QUESTION] **Q2**: Difference between Substring and Subsequence?
> > [!SUCCESS]- Answer
> > **Continuous** (Substring) vs **Skipping Allowed** (Subsequence).

> [!QUESTION] **Q3**: How to check if "abc" is an anagram of "cba"?
> > [!SUCCESS]- Answer
> > Sort both strings (`O(n log n)`) OR use a frequency map (`O(n)`).

> [!QUESTION] **Q4**: How to reverse a string in-place in Python?
> > [!SUCCESS]- Answer
> > You can't (Strings immutable). You must convert to list `lst.reverse()` then join.

> [!QUESTION] **Q5**: What algorithm is used for advanced String Matching?
> > [!SUCCESS]- Answer
> > KMP (Knuth-Morris-Pratt) or Rabin-Karp (Rolling Hash). `in` keyword usually does naive checking.

---

Back to: [[Sem Exam/2-DSA/Module 2 - String & Sorting/README|Module 2 Hub]] | [[../DSA-Hub|DSA Hub]]
