# 🔡 String Mastery

## 🎯 **Common String Problems**

> [!SUCCESS] **Goal**: Manipulate text efficiently.
> **Recall**: Strings are immutable in Python!

---

## 🔄 **1. Reversal & Palindromes**

**Palindrome**: Reads same forwards and backwards ("racecar").
```python
def isPalindrome(s):
    # Two Pointers (Interview Safe)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]: return False
        l += 1
        r -= 1
    return True

# TEST
print("racecar:", isPalindrome("racecar"))
print("hello:", isPalindrome("hello"))
```

---

## 🔠 **2. Anagrams**

**Anagram**: Same characters, different order ("listen" -> "silent").
```python
def isAnagram(s1, s2):
    # Quick check: different lengths can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Build frequency map for s1
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    # Subtract counts using s2
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True

# TEST
print("listen, silent:", isAnagram("listen", "silent"))
print("hello, world:", isAnagram("hello", "world"))
```

**Why `count.get(char, 0)`?**
- Returns 0 if char not in dict (avoids KeyError)
- Cleaner than `if char in count` check

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
