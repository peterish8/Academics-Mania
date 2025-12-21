# 🔤 Character Frequency Problems

## 🎯 What You'll Learn
- Building frequency maps (dictionaries)
- Sorting by frequency
- Handling odd/even character counts
- String manipulation techniques

**Previous**: [[02-Basic-Array-Operations]] | **Next**: [[04-String-Dictionary-Problems]]

---

## 📚 Problems Covered

1. [[Sort-Characters-by-Frequency]]
2. [[Longest-Palindrome-by-Frequency]]

---

## 📊 Understanding Frequency Maps

### What is a Frequency Map?

A **frequency map** (or frequency dictionary) counts how many times each element appears.

**Structure:**
```python
freq = {
    'element': count,
    'element2': count2
}
```

---

### Building a Frequency Map - Template

```python
# Template for any frequency counting
freq = {}

for item in collection:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Shorter version using .get()
freq = {}
for item in collection:
    freq[item] = freq.get(item, 0) + 1
```

**Example:**
```python
s = "hello"
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

## 🔄 Problem 1: Sort Characters by Frequency (LeetCode 451)

### Problem Statement
Given a string `s`, sort characters by **decreasing frequency**.

**Examples:**
```
Input: "tree"
Output: "eetr" or "eert"
(e appears 2 times, t and r appear once)

Input: "cccaaa"
Output: "cccaaa" or "aaaccc"

Input: "Aabb"
Output: "bbAa" or "bbaA"
```

---

### 💡 Approach

**3 Steps:**
1. **Count frequency** → Build frequency dictionary
2. **Sort by frequency** → Sort items by count (descending)
3. **Build result** → Multiply char by its frequency

---

### 🔍 Dry Run

**Input**: `s = "tree"`

**Step 1: Count Frequency**
```
Loop through "tree":
  t → freq = {'t': 1}
  r → freq = {'t': 1, 'r': 1}
  e → freq = {'t': 1, 'r': 1, 'e': 1}
  e → freq = {'t': 1, 'r': 1, 'e': 2}

Final freq: {'t': 1, 'r': 1, 'e': 2}
```

**Step 2: Sort by Frequency**
```python
# freq.items() gives [('t', 1), ('r', 1), ('e', 2)]
# Sort by second element (count) in descending order

sorted_dict = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Result: [('e', 2), ('t', 1), ('r', 1)]
```

**Understanding `lambda x: x[1]`:**
```
x = ('e', 2)
x[0] = 'e'  ← character
x[1] = 2    ← frequency (we sort by this)
```

**Step 3: Build Result String**
```
Start with ans = ""

i=0: ('e', 2)
  → ans += 'e' * 2 = "ee"

i=1: ('t', 1)
  → ans += 't' * 1 = "eet"

i=2: ('r', 1)
  → ans += 'r' * 1 = "eetr"

Final answer: "eetr" ✓
```

---

### ✅ Solution Code

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequency of each character
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Step 2: Sort by frequency (descending)
        sorted_dict = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Build output string
        ans = ""
        for i in range(len(sorted_dict)):
            char = sorted_dict[i][0]
            count = sorted_dict[i][1]
            ans += char * count
        
        return ans
```

**Cleaner Version:**
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequency
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Sort by frequency descending
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Build result
        return ''.join(char * count for char, count in sorted_chars)
```

---

### 📊 Complexity Analysis

**Time Complexity:**
```
Step 1 (counting): O(n) where n = len(s)
Step 2 (sorting): O(k log k) where k = unique chars
Step 3 (building): O(n)

Overall: O(n + k log k)
Since k ≤ n, this is efficient!
```

**Space Complexity:**
```
Frequency dict: O(k)
Sorted list: O(k)
Result string: O(n)

Overall: O(n + k)
```

---

### 🎯 Key Concepts

**Dictionary Sorting:**
```python
# Sort by key (alphabetically)
sorted(freq.items(), key=lambda x: x[0])

# Sort by value (frequency)
sorted(freq.items(), key=lambda x: x[1])

# Sort by value descending
sorted(freq.items(), key=lambda x: x[1], reverse=True)
```

**String Multiplication:**
```python
'a' * 3  # → "aaa"
'hi' * 2  # → "hihi"
```

---

## 🔄 Problem 2: Longest Palindrome (LeetCode 409)

### Problem Statement
Given a string `s`, return the **length** of the longest palindrome that can be built using those letters.

**Note:** This doesn't find a substring - it calculates the maximum possible palindrome length!

**Examples:**
```
Input: "abccccdd"
Output: 7
Explanation: "dccaccd" or "dcbcbcd" (both length 7)

Input: "a"
Output: 1

Input: "aabbcc"
Output: 6
```

---

### 💡 Palindrome Properties

**Key Insights:**

1. **Palindrome structure:**
   ```
   left | center | right
   "aba" → a | b | a
   "abba" → ab | | ba
   ```

2. **Character rules:**
   - **Even count** → Use all characters
   - **Odd count** → Use (count - 1), save 1 for center

3. **Center character:**
   - Only **one** odd-count character can be in center
   - If ANY odd count exists → add 1 to final length

---

### 🔍 Dry Run

**Input**: `s = "abccccdd"`

**Step 1: Count Frequency**
```
Loop through "abccccdd":
  a → freq = {'a': 1}
  b → freq = {'a': 1, 'b': 1}
  c → freq = {'a': 1, 'b': 1, 'c': 1}
  c → freq = {'a': 1, 'b': 1, 'c': 2}
  c → freq = {'a': 1, 'b': 1, 'c': 3}
  c → freq = {'a': 1, 'b': 1, 'c': 4}
  d → freq = {'a': 1, 'b': 1, 'c': 4, 'd': 1}
  d → freq = {'a': 1, 'b': 1, 'c': 4, 'd': 2}

Final: {'a': 1, 'b': 1, 'c': 4, 'd': 2}
```

**Step 2: Calculate Palindrome Length**
```
res = 0

Check 'a': 1
  1 % 2 == 0? NO (odd)
  → res += (1 - 1) = 0
  → freq['a'] = 1 (mark as odd)
  res = 0

Check 'b': 1
  1 % 2 == 0? NO (odd)
  → res += (1 - 1) = 0
  → freq['b'] = 1 (mark as odd)
  res = 0

Check 'c': 4
  4 % 2 == 0? YES (even)
  → res += 4
  res = 4

Check 'd': 2
  2 % 2 == 0? YES (even)
  → res += 2
  res = 6
```

**Step 3: Check for Center Character**
```
freq.values() = [1, 1, 4, 2]

Is 1 in values? YES
→ We have odd-count characters
→ Add 1 to center: res += 1
→ res = 7

Final answer: 7 ✓
```

**Example Palindrome:**
```
d c c a c c d
↑ ← c c c → ↑
6 chars + 1 center = 7
```

---

### 🎨 Visual Understanding

**Input: "abccccdd"**

```
Frequencies:
a: 1 (odd)  → use 0, save 1
b: 1 (odd)  → use 0, save 1
c: 4 (even) → use 4
d: 2 (even) → use 2

Total usable: 0 + 0 + 4 + 2 = 6
Center: 1 (pick any odd character)
Result: 6 + 1 = 7

Possible palindrome:
  d c c [a] c c d
  ← left | center | right →
```

---

### ✅ Solution Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: Count frequency
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        res = 0
        
        # Step 2: Calculate palindrome length
        for char, count in freq.items():
            if count % 2 == 0:
                # Even count: use all
                res += count
            else:
                # Odd count: use (count - 1)
                res += (count - 1)
                freq[char] = 1  # Mark one leftover
        
        # Step 3: Add center character if any odd exists
        if 1 in freq.values():
            res += 1
        
        return res
```

**Cleaner Version:**
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        res = 0
        has_odd = False
        
        for count in freq.values():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                has_odd = True
        
        # If any odd exists, we can place one in center
        if has_odd:
            res += 1
        
        return res
```

---

### 📊 Complexity Analysis

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single pass to count + iterate dict |
| Space | O(k) | Dictionary with k unique chars |

Where:
- `n = len(s)`
- `k = number of unique characters` (at most 52 for letters)

---

### 🎯 Another Example

**Input**: `s = "aabbccc"`

```
Frequency: {'a': 2, 'b': 2, 'c': 3}

Process:
  a: 2 (even) → add 2, res = 2
  b: 2 (even) → add 2, res = 4
  c: 3 (odd)  → add 2, res = 6, mark has_odd

Add center: res = 7

Possible palindrome: "abcbcba" or "bacbcab"
Length: 7 ✓
```

---

## 🎓 Key Takeaways

### Frequency Map Patterns

**When to use:**
- Counting occurrences
- Finding duplicates
- Grouping by value
- Anagram problems

**Template:**
```python
freq = {}
for item in collection:
    freq[item] = freq.get(item, 0) + 1
```

---

### Sorting Dictionary by Value

```python
# Create dict
freq = {'a': 3, 'b': 1, 'c': 2}

# Sort by value (ascending)
sorted(freq.items(), key=lambda x: x[1])
# Result: [('b', 1), ('c', 2), ('a', 3)]

# Sort by value (descending)
sorted(freq.items(), key=lambda x: x[1], reverse=True)
# Result: [('a', 3), ('c', 2), ('b', 1)]
```

---

### ✅ DO

- Use `.get(key, default)` for cleaner code
- Consider odd/even properties for palindromes
- Remember: dictionary iteration is O(k), not O(n)
- Use `''.join()` instead of `+=` for string building (more efficient)

### ❌ AVOID

- Sorting entire string (O(n log n)) when frequency count works
- Forgetting that multiple palindromes can have same length
- Not handling edge cases (empty string, single character)
- Building strings in loops with `+=` (use list and join)

---

## 🔗 Related Topics

- [[04-String-Dictionary-Problems]] - More dictionary patterns
- [[Valid-Anagram]] - Similar frequency counting
- [[Group-Anagrams]] - Advanced frequency usage

---

## 📝 Practice Problems

### Easy
1. LeetCode 451 - Sort Characters by Frequency
2. LeetCode 409 - Longest Palindrome
3. LeetCode 387 - First Unique Character in a String

### Medium
1. LeetCode 347 - Top K Frequent Elements
2. LeetCode 890 - Find and Replace Pattern
3. LeetCode 1636 - Sort Array by Increasing Frequency

---

## 🧪 Test Your Understanding

Try these variations:
1. Return the actual palindrome string (not just length)
2. Find character with highest frequency
3. Remove minimum characters to make string palindrome

---

**Previous**: [[02-Basic-Array-Operations]] | **Next**: [[04-String-Dictionary-Problems]]

Back to: [[README of Frontend]]
