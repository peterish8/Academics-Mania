# ═══════════════════════════════════════
# 📌 [205] - Isomorphic Strings
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Check if characters in s can be replaced to get t (one-to-one mapping).

## 💡 **Key Insight:**
Need bidirectional mapping. Each char in s maps to one in t and vice versa.

## 🔧 **Optimal Approach:**
**Algorithm:** Two HashMaps

**Steps:**
- Map s[i] -> t[i] and t[i] -> s[i]
- If mapping conflict, return False

## 💻 **Code (Run Directly):**
```python
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for c1, c2 in zip(s, t):
        if c1 in s_to_t and s_to_t[c1] != c2:
            return False
        if c2 in t_to_s and t_to_s[c2] != c1:
            return False
        s_to_t[c1] = c2
        t_to_s[c2] = c1
    
    return True

# TEST
print("egg, add:", isIsomorphic("egg", "add"))
print("foo, bar:", isIsomorphic("foo", "bar"))
print("paper, title:", isIsomorphic("paper", "title"))
```

## 🏃 **Dry Run:**
**Example:** s = "egg", t = "add"

```
i | s[i] | t[i] | s_to_t    | t_to_s
--|------|------|-----------|--------
0 | e    | a    | {e:a}     | {a:e}
1 | g    | d    | {e:a,g:d} | {a:e,d:g}
2 | g    | d    | match     | match

True
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(n)

## 🏷️ **Pattern Tag:** 
HashMap, String

## ⚠️ **Gotcha:**
Must check both directions (s->t AND t->s).
