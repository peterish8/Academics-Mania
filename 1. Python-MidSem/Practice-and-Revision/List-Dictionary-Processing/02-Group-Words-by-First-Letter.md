# Group Words by First Letter

#dictionary-processing #sets #string-manipulation #grouping #data-structures

---

## Problem Statement

Given a list of words, create a dictionary where:
- **Keys** → First letters of the words
- **Values** → Sets of words starting with that letter

**Example**: 
- Input: `['apple', 'banana', 'cherry', 'apricot', 'blueberry']`
- Output: `{'a': {'apple', 'apricot'}, 'b': {'banana', 'blueberry'}, 'c': {'cherry'}}`

---

## Algorithm Approach

### Core Concept
Group words by their first character using a dictionary with sets as values.

### Step-by-Step Logic
1. **Initialize** empty dictionary `result`
2. **Loop** through each word in the input list
3. **Extract** first letter using `word[0]`
4. **Check** if letter exists as key in dictionary
5. **If not exists** → create new set for that letter
6. **Add** word to the corresponding set
7. **Return** the final dictionary

### Visual Representation
```
Input: ['apple', 'banana', 'cherry', 'apricot', 'blueberry']

Process each word:
'apple' → first_letter = 'a' → result = {'a': {'apple'}}
'banana' → first_letter = 'b' → result = {'a': {'apple'}, 'b': {'banana'}}
'cherry' → first_letter = 'c' → result = {'a': {'apple'}, 'b': {'banana'}, 'c': {'cherry'}}
'apricot' → first_letter = 'a' → result = {'a': {'apple', 'apricot'}, 'b': {'banana'}, 'c': {'cherry'}}
'blueberry' → first_letter = 'b' → result = {'a': {'apple', 'apricot'}, 'b': {'banana', 'blueberry'}, 'c': {'cherry'}}
```

---

## Code Implementation

```python
def group_words(words):
    """
    Group words by their first letter.
    
    Args:
        words (list): List of strings
    
    Returns:
        dict: Dictionary with first letters as keys and sets of words as values
    """
    result = {}
    
    for word in words:
        first_letter = word[0]  # Extract first character
        
        if first_letter not in result:
            result[first_letter] = set()  # Create new set if key doesn't exist
        
        result[first_letter].add(word)  # Add word to corresponding set
    
    return result

# Example usage
word_list = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
grouped = group_words(word_list)
print(f"Input: {word_list}")
print(f"Output: {grouped}")
```

---

## Detailed Dry Run

### Example: words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']

**Initial Setup:**
```
words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
result = {}
```

**Iteration Process:**

| Step | word | first_letter | Key exists? | Action | result |
|------|------|--------------|-------------|--------|--------|
| 1 | 'apple' | 'a' | ✗ No | Create set, add 'apple' | `{'a': {'apple'}}` |
| 2 | 'banana' | 'b' | ✗ No | Create set, add 'banana' | `{'a': {'apple'}, 'b': {'banana'}}` |
| 3 | 'cherry' | 'c' | ✗ No | Create set, add 'cherry' | `{'a': {'apple'}, 'b': {'banana'}, 'c': {'cherry'}}` |
| 4 | 'apricot' | 'a' | ✓ Yes | Add to existing set | `{'a': {'apple', 'apricot'}, 'b': {'banana'}, 'c': {'cherry'}}` |
| 5 | 'blueberry' | 'b' | ✓ Yes | Add to existing set | `{'a': {'apple', 'apricot'}, 'b': {'banana', 'blueberry'}, 'c': {'cherry'}}` |

**Final Result:** 
```python
{
    'a': {'apple', 'apricot'}, 
    'b': {'banana', 'blueberry'}, 
    'c': {'cherry'}
}
```

### Example 2: words = ['cat', 'dog', 'cow', 'duck']

| Step | word | first_letter | Key exists? | Action | result |
|------|------|--------------|-------------|--------|--------|
| 1 | 'cat' | 'c' | ✗ No | Create set, add 'cat' | `{'c': {'cat'}}` |
| 2 | 'dog' | 'd' | ✗ No | Create set, add 'dog' | `{'c': {'cat'}, 'd': {'dog'}}` |
| 3 | 'cow' | 'c' | ✓ Yes | Add to existing set | `{'c': {'cat', 'cow'}, 'd': {'dog'}}` |
| 4 | 'duck' | 'd' | ✓ Yes | Add to existing set | `{'c': {'cat', 'cow'}, 'd': {'dog', 'duck'}}` |

---

## Enhanced Implementation with Debugging

```python
def group_words_debug(words):
    """
    Group words with step-by-step debugging output.
    """
    print(f"Grouping words: {words}")
    print("-" * 60)
    
    result = {}
    
    for i, word in enumerate(words, 1):
        first_letter = word[0]
        key_exists = first_letter in result
        
        if not key_exists:
            result[first_letter] = set()
            action = f"Create new set for '{first_letter}'"
        else:
            action = f"Add to existing set for '{first_letter}'"
        
        result[first_letter].add(word)
        
        print(f"Step {i}: word='{word}' → first_letter='{first_letter}'")
        print(f"         Key exists: {key_exists} → {action}")
        print(f"         Current result: {dict(result)}")  # Convert sets to display properly
        print()
    
    print("-" * 60)
    print(f"Final result: {dict(result)}")
    return result

# Test with debugging
test_cases = [
    ['apple', 'banana', 'cherry', 'apricot', 'blueberry'],
    ['cat', 'dog', 'cow', 'duck'],
    ['python', 'programming', 'practice']
]

for test_words in test_cases:
    group_words_debug(test_words)
    print()
```

**Sample Output:**
```
Grouping words: ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
------------------------------------------------------------
Step 1: word='apple' → first_letter='a'
         Key exists: False → Create new set for 'a'
         Current result: {'a': {'apple'}}

Step 2: word='banana' → first_letter='b'
         Key exists: False → Create new set for 'b'
         Current result: {'a': {'apple'}, 'b': {'banana'}}

Step 3: word='cherry' → first_letter='c'
         Key exists: False → Create new set for 'c'
         Current result: {'a': {'apple'}, 'b': {'banana'}, 'c': {'cherry'}}

Step 4: word='apricot' → first_letter='a'
         Key exists: True → Add to existing set for 'a'
         Current result: {'a': {'apple', 'apricot'}, 'b': {'banana'}, 'c': {'cherry'}}

Step 5: word='blueberry' → first_letter='b'
         Key exists: True → Add to existing set for 'b'
         Current result: {'a': {'apple', 'apricot'}, 'b': {'banana', 'blueberry'}, 'c': {'cherry'}}
```

---

## Alternative Implementations

### Method 1: Using defaultdict
```python
from collections import defaultdict

def group_words_defaultdict(words):
    """Using defaultdict to automatically create sets."""
    result = defaultdict(set)
    
    for word in words:
        result[word[0]].add(word)
    
    return dict(result)  # Convert back to regular dict

# Test
print(group_words_defaultdict(['apple', 'banana', 'cherry', 'apricot']))
```

### Method 2: Using setdefault()
```python
def group_words_setdefault(words):
    """Using dict.setdefault() method."""
    result = {}
    
    for word in words:
        result.setdefault(word[0], set()).add(word)
    
    return result

# Test
print(group_words_setdefault(['apple', 'banana', 'cherry', 'apricot']))
```

### Method 3: Dictionary Comprehension with groupby
```python
from itertools import groupby

def group_words_groupby(words):
    """Using itertools.groupby (requires sorted input)."""
    # Sort words by first letter first
    sorted_words = sorted(words, key=lambda x: x[0])
    
    return {
        key: set(group) 
        for key, group in groupby(sorted_words, key=lambda x: x[0])
    }

# Test
print(group_words_groupby(['apple', 'banana', 'cherry', 'apricot']))
```

---

## Edge Cases & Variations

### Handling Edge Cases
```python
def group_words_robust(words):
    """Robust version with input validation."""
    # Input validation
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    
    if not words:  # Empty list
        return {}
    
    result = {}
    
    for word in words:
        # Skip empty strings or non-string elements
        if not isinstance(word, str) or not word:
            continue
        
        first_letter = word[0].lower()  # Case-insensitive grouping
        
        if first_letter not in result:
            result[first_letter] = set()
        
        result[first_letter].add(word)
    
    return result

# Test edge cases
test_cases = [
    [],                                    # Empty list
    [''],                                  # Empty string
    ['Apple', 'apple', 'APPLE'],          # Case variations
    ['123', 'abc', '456'],                # Numbers and letters
    [None, 'apple', 123, 'banana'],       # Mixed types
]

for test in test_cases:
    try:
        result = group_words_robust(test)
        print(f"{test} → {result}")
    except Exception as e:
        print(f"{test} → Error: {e}")
```

### Case-Sensitive vs Case-Insensitive
```python
def group_words_case_sensitive(words):
    """Case-sensitive grouping."""
    result = {}
    for word in words:
        first_letter = word[0]  # Keep original case
        if first_letter not in result:
            result[first_letter] = set()
        result[first_letter].add(word)
    return result

def group_words_case_insensitive(words):
    """Case-insensitive grouping."""
    result = {}
    for word in words:
        first_letter = word[0].lower()  # Convert to lowercase
        if first_letter not in result:
            result[first_letter] = set()
        result[first_letter].add(word)
    return result

# Test both approaches
test_words = ['Apple', 'apple', 'Banana', 'banana', 'Cherry']
print("Case-sensitive:", group_words_case_sensitive(test_words))
print("Case-insensitive:", group_words_case_insensitive(test_words))
```

---

## Performance Analysis

### Time Complexity: O(n)
- We iterate through the list once: O(n)
- Each dictionary lookup/insertion: O(1) average case
- Each set addition: O(1) average case
- Total: O(n) where n is the number of words

### Space Complexity: O(n)
- Dictionary storage: O(k) where k is number of unique first letters
- Set storage: O(n) for all words
- Total: O(n) in worst case

### Memory Usage Comparison
```python
import sys

def memory_comparison():
    """Compare memory usage of different data structures."""
    words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry'] * 1000
    
    # Using sets (our approach)
    result_sets = group_words(words)
    
    # Using lists instead of sets
    result_lists = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in result_lists:
            result_lists[first_letter] = []
        result_lists[first_letter].append(word)
    
    print(f"Dictionary with sets: {sys.getsizeof(result_sets)} bytes")
    print(f"Dictionary with lists: {sys.getsizeof(result_lists)} bytes")
    
    # Sets automatically handle duplicates, lists don't
    print(f"Set 'a' size: {len(result_sets['a'])}")
    print(f"List 'a' size: {len(result_lists['a'])}")

memory_comparison()
```

---

## Practical Applications

### Word Index for Search Engine
```python
def create_word_index(documents):
    """Create searchable index of words by first letter."""
    word_index = {}
    
    for doc_id, document in enumerate(documents):
        words = document.lower().split()
        
        for word in words:
            if word:  # Skip empty strings
                first_letter = word[0]
                if first_letter not in word_index:
                    word_index[first_letter] = {}
                
                if word not in word_index[first_letter]:
                    word_index[first_letter][word] = set()
                
                word_index[first_letter][word].add(doc_id)
    
    return word_index

# Test
documents = [
    "apple banana cherry",
    "apricot blueberry",
    "cherry apple"
]

index = create_word_index(documents)
print("Word index:", index)
```

### Contact List Organizer
```python
def organize_contacts(contacts):
    """Organize contacts by first letter of name."""
    organized = group_words([contact['name'] for contact in contacts])
    
    # Create detailed contact groups
    detailed_groups = {}
    for letter, names in organized.items():
        detailed_groups[letter] = []
        for contact in contacts:
            if contact['name'] in names:
                detailed_groups[letter].append(contact)
    
    return detailed_groups

# Test
contacts = [
    {'name': 'Alice', 'phone': '123-456-7890'},
    {'name': 'Bob', 'phone': '234-567-8901'},
    {'name': 'Charlie', 'phone': '345-678-9012'},
    {'name': 'Anna', 'phone': '456-789-0123'}
]

organized_contacts = organize_contacts(contacts)
for letter, contact_list in organized_contacts.items():
    print(f"\n{letter.upper()}:")
    for contact in contact_list:
        print(f"  {contact['name']}: {contact['phone']}")
```

---

## Advanced Variations

### Multi-Level Grouping
```python
def group_words_multi_level(words, levels=2):
    """Group words by first N characters."""
    result = {}
    
    for word in words:
        if len(word) >= levels:
            key = word[:levels].lower()
        else:
            key = word.lower()
        
        if key not in result:
            result[key] = set()
        result[key].add(word)
    
    return result

# Test multi-level grouping
words = ['apple', 'application', 'apply', 'banana', 'band', 'cherry']
print("2-level grouping:", group_words_multi_level(words, 2))
print("3-level grouping:", group_words_multi_level(words, 3))
```

### Grouping by Word Length and First Letter
```python
def group_by_length_and_letter(words):
    """Group by both word length and first letter."""
    result = {}
    
    for word in words:
        length = len(word)
        first_letter = word[0].lower()
        key = (length, first_letter)
        
        if key not in result:
            result[key] = set()
        result[key].add(word)
    
    return result

# Test
words = ['cat', 'dog', 'apple', 'car', 'application', 'ant']
grouped = group_by_length_and_letter(words)
for (length, letter), word_set in grouped.items():
    print(f"Length {length}, starts with '{letter}': {word_set}")
```

---

## Testing Suite

```python
def test_group_words():
    """Comprehensive test suite for group_words function."""
    test_cases = [
        # (input, expected_output, description)
        (
            ['apple', 'banana', 'cherry'],
            {'a': {'apple'}, 'b': {'banana'}, 'c': {'cherry'}},
            "No duplicates"
        ),
        (
            ['apple', 'apricot', 'banana', 'blueberry'],
            {'a': {'apple', 'apricot'}, 'b': {'banana', 'blueberry'}},
            "Multiple words per letter"
        ),
        (
            [],
            {},
            "Empty list"
        ),
        (
            ['a'],
            {'a': {'a'}},
            "Single character word"
        ),
        (
            ['apple', 'apple', 'banana'],
            {'a': {'apple'}, 'b': {'banana'}},
            "Duplicate words (sets handle this)"
        )
    ]
    
    print("Testing group_words function:")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_words, expected, description) in enumerate(test_cases, 1):
        result = group_words(input_words)
        
        # Compare dictionaries (sets might be in different order)
        matches = (
            set(result.keys()) == set(expected.keys()) and
            all(result[key] == expected[key] for key in expected.keys())
        )
        
        status = "PASS" if matches else "FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: {input_words}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if matches:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    print(f"Success rate: {(passed/total)*100:.1f}%")

# Run comprehensive tests
test_group_words()
```

---

## Key Concepts Reinforced

> [!NOTE] **Core Concepts**
> - **Dictionary operations**: Creating, checking keys, adding values
> - **Set operations**: Creating sets, adding elements, automatic deduplication
> - **String indexing**: Accessing first character with `word[0]`
> - **Conditional logic**: Checking key existence with `in` operator
> - **Data structure choice**: Sets vs lists for unique collections

> [!TIP] **Best Practices**
> - Use sets when you need unique collections
> - Check key existence before accessing dictionary values
> - Handle empty inputs gracefully
> - Consider case sensitivity requirements
> - Use meaningful variable names (`first_letter`, `result`)

> [!WARNING] **Common Mistakes**
> - Forgetting to create new set when key doesn't exist
> - Using lists instead of sets (allows duplicates)
> - Not handling empty strings or invalid inputs
> - Case sensitivity issues
> - Modifying dictionary while iterating

---

## Related Topics
- [[01-Even-Numbers-Squared]] - List processing patterns
- [[Dictionary-Methods-get-items]] - Dictionary operations
- [[Sets]] - Set data structure and operations
- [[String-Indexing-and-Slicing]] - String character access

---

## Practice Problems

1. **Modify** to group by last letter instead of first
2. **Group** words by length instead of first letter
3. **Create** case-insensitive version that preserves original case
4. **Implement** using only lists (no sets) and handle duplicates manually

```python
# Practice solutions
def group_by_last_letter(words):
    result = {}
    for word in words:
        last_letter = word[-1].lower()
        if last_letter not in result:
            result[last_letter] = set()
        result[last_letter].add(word)
    return result

def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result

def group_words_lists_no_duplicates(words):
    result = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        if word not in result[first_letter]:  # Manual duplicate check
            result[first_letter].append(word)
    return result
```

**Next**: Explore more advanced data processing patterns or return to [[Python Todo-s]] →