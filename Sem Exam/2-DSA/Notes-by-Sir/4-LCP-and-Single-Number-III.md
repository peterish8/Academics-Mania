# 🔤 Longest Common Prefix & Single Number III

## 🎯 **Two String/Bit Problems**

> [!SUCCESS] These cover important patterns: String comparison and Bit manipulation!

---

# 1️⃣ **Longest Common Prefix (LeetCode 14)**

## 📋 **Problem Statement**

> Given an array of strings `strs`, find the **longest common prefix** among them.
> If no common prefix exists, return `""`.

**Example:**
- Input: `["flower", "flow", "flight"]`
- Output: `"fl"`

---

## 🛠️ **Approach: Vertical Scanning**

> [!TIP] **Key Idea**
> Check characters **column by column**: compare `strs[i][j]` across all strings for fixed `j`.
> Stop when mismatch or some string ends.

**Visual:**
```
f l o w e r
f l o w
f l i g h t
↓ ↓ ✗
```
Stop at column 2 (index 2) → prefix = "fl"

---

## 💻 **Code (Runnable)**

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Use first string as reference
    for i, ch in enumerate(strs[0]):
        # Check this character against all other strings
        for s in strs[1:]:
            # If index out of bounds OR mismatch
            if i == len(s) or s[i] != ch:
                return strs[0][:i]
    
    # First string is the common prefix
    return strs[0]

# TEST
strs1 = ["flower", "flow", "flight"]
print("Input:", strs1)
print("Prefix:", longestCommonPrefix(strs1))

strs2 = ["dog", "racecar", "car"]
print("Input:", strs2)
print("Prefix:", longestCommonPrefix(strs2))
```

---

## ⏱️ **Complexity**

| Metric | Value |
|--------|-------|
| **Time** | O(S) where S = sum of all characters |
| **Space** | O(1) |

---

# 2️⃣ **Single Number III (LeetCode 260)**

## 📋 **Problem Statement**

> Given an array where exactly **two elements appear once** and all others appear **twice**, find those two unique elements.
> **Constraint**: O(1) space, O(n) time (use bit manipulation)

**Example:**
- Input: `[1, 2, 1, 3, 2, 5]`
- Output: `[3, 5]`

---

## 🧠 **Key Intuition (The Brutal Core Idea)**

> [!IMPORTANT] **The XOR Trick**
> 1. XOR all numbers → duplicates cancel (`x ^ x = 0`)
> 2. Result = `a ^ b` (XOR of the two unique numbers)
> 3. Find a **set bit** in result (that bit differs between `a` and `b`)
> 4. **Partition** numbers into two groups based on that bit
> 5. XOR within each group → get `a` and `b`!

**Why this works:**
- `xor_all & -xor_all` isolates the **rightmost set bit**
- That bit is guaranteed to be different between `a` and `b`

---

## 💻 **Code (Runnable)**

```python
def singleNumberIII(nums):
    # Step 1: XOR all numbers → a ^ b
    xor_all = 0
    for n in nums:
        xor_all ^= n
    
    # Step 2: Find rightmost set bit (differs between a and b)
    # diff = xor_all & (-xor_all) isolates lowest set bit
    diff = xor_all & -xor_all
    
    # Step 3: Partition and XOR to get the two unique numbers
    a = 0
    b = 0
    for n in nums:
        if n & diff:  # Bit is set
            a ^= n
        else:         # Bit is not set
            b ^= n
    
    return [a, b]

# TEST
nums = [1, 2, 1, 3, 2, 5]
print("Input:", nums)
print("Two unique numbers:", singleNumberIII(nums))
```

---

## 🏃 **Dry Run**

**Input:** `nums = [1, 2, 1, 3, 2, 5]` (unique: 3 and 5)

### Step 1: Calculate xor_all
```
1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5
= (1^1) ^ (2^2) ^ (3^5)
= 0 ^ 0 ^ 6
= 6 (binary: 110)
```

### Step 2: Find diff
```
xor_all = 6 (0110)
-xor_all = -6 (1010 in two's complement)
diff = 6 & -6 = 2 (0010)
```

### Step 3: Partition by diff (bit 1)

| Number | Binary | & diff | Group | Running XOR |
|--------|--------|--------|-------|-------------|
| 1 | 01 | 0 | B | b = 1 |
| 2 | 10 | 1 | A | a = 2 |
| 1 | 01 | 0 | B | b = 0 |
| 3 | 11 | 1 | A | a = 1 |
| 2 | 10 | 1 | A | a = 3 |
| 5 | 101 | 0 | B | b = 5 |

**Result:** `a = 3`, `b = 5` ✅

---

## ⏱️ **Complexity**

| Metric | Value |
|--------|-------|
| **Time** | O(n) - two passes |
| **Space** | O(1) |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **LCP**: Vertical scan column by column
> - **Single Number III**: XOR → Find diff bit → Partition → XOR groups
> - **Magic formula**: `x & -x` gives rightmost set bit

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What does `x ^ x` equal?
> > [!SUCCESS]- Answer
> > **0** - any number XOR itself is 0.

> [!QUESTION] **Q2**: Why use `xor_all & -xor_all`?
> > [!SUCCESS]- Answer
> > It isolates the **rightmost set bit**, which is guaranteed to differ between the two unique numbers.

> [!QUESTION] **Q3**: What if all strings in LCP array are identical?
> > [!SUCCESS]- Answer
> > Returns the entire first string (it IS the common prefix).

> [!QUESTION] **Q4**: Why does partitioning by a diff bit work?
> > [!SUCCESS]- Answer
> > The two unique numbers go to different groups (they differ at that bit). Duplicates go to same group and cancel.

> [!QUESTION] **Q5**: Time complexity of LCP vertical scan?
> > [!SUCCESS]- Answer
> > O(S) where S = total characters across all strings. Worst case: check every character.

---

Back to: [[Sem Exam/2-DSA/DSA-Hub|DSA Hub]]
