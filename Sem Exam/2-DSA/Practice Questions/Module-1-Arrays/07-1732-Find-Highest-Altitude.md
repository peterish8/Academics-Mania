# ═══════════════════════════════════════
# 📌 [1732] - Find the Highest Altitude
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Biker starts at altitude 0. Given gains between points. Return highest altitude reached.

## 💡 **Key Insight:**
Prefix sum: current = previous + gain. Track max during traversal.

## 🔧 **Optimal Approach:**
**Algorithm:** Prefix Sum with Max Tracking

**Steps:**
- altitude = 0, maxAlt = 0
- For each gain: altitude += gain, update maxAlt
- Return maxAlt

## 💻 **Code (Run Directly):**
```python
def largestAltitude(gain):
    altitude = 0
    max_alt = 0
    for g in gain:
        altitude += g
        max_alt = max(max_alt, altitude)
    return max_alt

# TEST
gain = [-5, 1, 5, 0, -7]
print("Input:", gain)
print("Output:", largestAltitude(gain))
```

## 🏃 **Dry Run:**
**Example:** gain = [-5, 1, 5, 0, -7]

```
iter | g  | altitude | max_alt
-----|-----|----------|--------
init | -  | 0        | 0
1    | -5 | -5       | 0
2    | 1  | -4       | 0
3    | 5  | 1        | 1
4    | 0  | 1        | 1
5    | -7 | -6       | 1
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Prefix Sum, Array

## ⚠️ **Gotcha:**
Include starting altitude 0 in comparison!
