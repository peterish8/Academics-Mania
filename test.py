def isAnagram(s1, s2):
    # Quick check: different lengths can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Build frequency map for s1
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    count2 = {}
    for char in s2:
        count2[char] = count2.get(char, 0) + 1
    
    return count == count2

# TEST
print("listen, silent:", isAnagram("listen", "silent"))
print("hello, world:", isAnagram("hello", "world"))