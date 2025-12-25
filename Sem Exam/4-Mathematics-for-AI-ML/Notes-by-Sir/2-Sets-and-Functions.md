# 🎱 Sets and Functions - Complete Notes

> [!INFO] **Definition: Set**
> A collection of distinct objects. Elements are written inside curly brackets `{ }`.

---

## 📌 Representation of Sets

### Roster Form
All elements listed explicitly, separated by commas.

**Examples:**
- A = {0, 2, 4, 6, 8, ...}
- B = {1, 3, 5, 7, 9, ...}

### Set-Builder Form
Describe the property (rule) that defines elements.

**Examples:**
- A = {x | x ∈ even numbers}
- B = {x | x ∈ odd numbers}

---

## 📌 Cardinality of Set

> [!INFO] **Definition: Cardinality**
> The number of distinct elements in a set. Denoted by **n(A)** or **|A|**.

**Examples:**
- A = {1, 2, 3, 4, 5} → |A| = **5**
- A = {a, b, {c, d}, e, f} → |A| = **5** (nested set counts as 1 element)

---

## 📌 Types of Sets

| Type | Definition | Example |
|------|------------|---------|
| **Empty Set** | No elements, denoted by ∅ or { } | {x \| x < 0, x = positive} |
| **Finite Set** | Countable elements | {1, 2, 3, 4, 5} |
| **Infinite Set** | Infinitely many elements | ℕ = {1, 2, 3, ...} |
| **Singleton Set** | Exactly one element | {5} |
| **Equal Sets** | Same elements | {1,2,3} = {3,2,1} |
| **Equivalent Sets** | Same number of elements | {1,2,3} ~ {p,q,r} |
| **Universal Set** | Contains all elements | U = {1,2,3,4,5,6} |
| **Disjoint Sets** | No common elements | A∩B = ∅ |

---

## 📌 Subsets & Power Sets

### Subset (⊆)
A ⊆ B if every element of A is in B.

**Example:** A = {1, 2, 3}
- Subsets: { }, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}

### Proper Subset (⊂)
A ⊂ B if A ⊆ B but A ≠ B.

**Example:** A = {1, 2, 3}
- Proper Subsets: { }, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}

### Improper Subset
A set is subset of itself: A ⊆ A

### Power Set - P(A)
Set of all subsets.

> **Formula:** Number of elements in P(A) = **2ⁿ**

**Example:** A = {1, 2, 3}
- P(A) = {{ }, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
- |P(A)| = 2³ = **8**

---

## 📌 Ordered Pairs & Cartesian Product

> [!INFO] **Definition: Ordered Pair**
> A pair (a, b) where **order matters**: (a, b) ≠ (b, a) unless a = b.

> [!INFO] **Definition: Cartesian Product**
> A × B = {(a, b) | a ∈ A, b ∈ B}

**Example:**
```
A = {1, 2}, B = {x, y}
A × B = {(1,x), (1,y), (2,x), (2,y)}
|A × B| = |A| × |B| = 2 × 2 = 4
```

**Properties:**
- |A × B| = |A| × |B|
- A × B ≠ B × A (not commutative)
- (a, b) = (c, d) only if a = c AND b = d

---

## 📌 Operations on Sets

### 1. Union (∪)
A ∪ B = {x | x ∈ A **or** x ∈ B}

**Example:** A = {1,2,3}, B = {3,4,5} → A ∪ B = {1,2,3,4,5}

### 2. Intersection (∩)
A ∩ B = {x | x ∈ A **and** x ∈ B}

**Example:** A = {1,2,3}, B = {3,4,5} → A ∩ B = {3}

### 3. Difference (-)
A - B = {x | x ∈ A and x ∉ B}

**Example:** A = {1,2,3}, B = {3,4,5} → A - B = {1,2}

### 4. Complement (')
A' = {x | x ∈ U and x ∉ A}

**Example:** U = {1,2,3,4,5,6}, A = {1,2,3} → A' = {4,5,6}

---

## 📌 Properties of Set Operations

| Property | Law |
|----------|-----|
| **Commutative** | A ∪ B = B ∪ A |
| **Associative** | (A ∪ B) ∪ C = A ∪ (B ∪ C) |
| **Distributive** | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) |
| **Double Complement** | (A')' = A |

### De Morgan's Laws (for Sets)

> [!SUCCESS] **First Law**
> (A ∪ B)' = A' ∩ B'

> [!SUCCESS] **Second Law**
> (A ∩ B)' = A' ∪ B'

---

## 📌 Relations

> [!INFO] **Definition: Relation**
> A relation R from A to B is a subset of A × B. It shows how elements of A are connected to elements of B.

**Notation:** R ⊆ A × B

**Example:**
```
A = {1, 2, 3}, B = {a, b}
R = {(1, a), (2, a), (3, b)}
```

### Domain, Co-domain, Range

| Term | Definition | Example |
|------|------------|---------|
| **Domain** | All first elements (inputs) | {1, 2, 3} |
| **Co-domain** | Fixed set of possible outputs | {1, 2, 3, 4, ...} |
| **Image** | Actual output of specific input | f(2) = 4 |
| **Range** | Set of all actual outputs | {1, 4, 9} |

---

## 📌 Types of Relations

### Reflexive Relation
∀ a ∈ A, (a, a) ∈ R (every element related to itself)

**Example:** A = {1,2,3}, R = {(1,1), (2,2), (3,3), (1,2)}

### Symmetric Relation
If (a, b) ∈ R, then (b, a) ∈ R

**Example:** R = {(1,2), (2,1), (3,3)}

### Transitive Relation
If (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R

**Example:** If 1→2 and 2→3, then 1→3 must exist

### Equivalence Relation
Must be **Reflexive + Symmetric + Transitive**

---

## 📌 Partial Order & Total Order

### Partial Order Relation (POSET)
Must be:
1. **Reflexive**
2. **Anti-Symmetric** (if a≤b and b≤a, then a=b)
3. **Transitive**

**Example:** ({1, 2, 4}, |) where | = "divides"

### Total Order Relation (TOSET)
POSET + **Comparable** (any two elements can always be compared)

**Example:** (ℕ, ≤) - any two natural numbers can be compared

---

## 📌 Functions

> [!INFO] **Definition: Function**
> A special relation where each element of domain has **exactly one** image in codomain.

**Notation:** f : X → Y

**Requirements:**
- Every x ∈ X must have an image
- No x can have multiple images

---

## 📌 Types of Functions

### 1. One-One (Injective)
Different inputs → Different outputs

**Example:** f = {(1,a), (2,b), (3,c)}

### 2. Onto (Surjective)
Every element in codomain has at least one pre-image

**Example:** All elements of Y are "hit"

### 3. Bijective (One-One Onto)
Both injective and surjective

**Example:** Perfect pairing between X and Y

### 4. Many-One
Two or more inputs → Same output

**Example:** f = {(1,a), (2,a), (3,b)}

### 5. Into
Some elements of codomain have no pre-image

**Example:** Some elements of Y are not "hit"

---

## 📌 Inverse Function

> [!INFO] **Definition: Inverse Function**
> f⁻¹ exists only if f is **bijective** (one-one and onto).

**Example:**
```
f(x) = 3x + 2
y = 3x + 2
x = (y - 2)/3
f⁻¹(y) = (y - 2)/3
```

---

## 📌 Composite Functions

> [!INFO] **Definition: Composite**
> If f : A → B and g : B → C, then (g ∘ f)(x) = g(f(x))

**Properties:**
- (g ∘ f) ≠ (f ∘ g) (not commutative)
- Domain of (g ∘ f) = Domain of f
- Codomain of (g ∘ f) = Codomain of g

**Example:**
```
f(x) = 2x + 3
g(x) = x² - 1

(f ∘ g)(x) = f(g(x)) = 2(x² - 1) + 3 = 2x² + 1
(g ∘ f)(x) = g(f(x)) = (2x + 3)² - 1 = 4x² + 12x + 8
```

---

## 💻 Solved Examples

### Example 1: Cartesian Product

**Question:** A = {1, 2}, B = {x, y}, C = {8, 9}. Find A × B × C.

**Solution:**
```
A × B = {(1,x), (1,y), (2,x), (2,y)}
A × B × C = {(1,x,8), (1,y,8), (2,x,8), (2,y,8),
             (1,x,9), (1,y,9), (2,x,9), (2,y,9)}
```

---

### Example 2: Equivalence Relation

**Question:** Show R = {(a,b) | a,b ∈ ℤ, a-b divisible by 3} is equivalence.

**Solution:**
- **Reflexive:** a-a = 0, divisible by 3 ✅
- **Symmetric:** If a-b divisible by 3, then b-a = -(a-b) also divisible ✅
- **Transitive:** If (a-b) and (b-c) divisible, then (a-c) = (a-b)+(b-c) divisible ✅

Therefore **Equivalence Relation** ✅

---

### Example 3: Check if One-One and Onto

**Question:** f : ℤ → ℤ, f(x) = x + 5. Check one-one and onto.

**Solution:**
- **One-One:** f(a) = f(b) ⟹ a+5 = b+5 ⟹ a = b ✅
- **Onto:** For any y, x = y-5 exists ✅

Therefore **Bijective** ✅

---

## 🧠 Key Points
- **Set** = Collection of distinct objects
- **Power Set** elements = 2ⁿ
- **Cartesian Product** size = |A| × |B|
- **Relation** = Subset of A × B
- **Equivalence** = Reflexive + Symmetric + Transitive
- **POSET** = Reflexive + Anti-Symmetric + Transitive
- **TOSET** = POSET + Comparable
- **Function** = Each input has exactly one output
- **Bijective** = One-One + Onto
- **Inverse exists** only if bijective
- **Composite** is not commutative

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: How many elements in Power Set of {1, 2, 3, 4}?
>> [!SUCCESS]- Answer
>> 2⁴ = **16 elements**

> [!QUESTION] Q2: Is (A × B) = (B × A)?
>> [!SUCCESS]- Answer
>> **No**, unless A = B. Cartesian product is **not commutative**.

> [!QUESTION] Q3: What 3 properties make an Equivalence Relation?
>> [!SUCCESS]- Answer
>> **Reflexive, Symmetric, Transitive**

> [!QUESTION] Q4: When does inverse function f⁻¹ exist?
>> [!SUCCESS]- Answer
>> Only when f is **bijective** (one-one and onto).

> [!QUESTION] Q5: Is (f ∘ g) = (g ∘ f)?
>> [!SUCCESS]- Answer
>> **No**, composite functions are **not commutative** in general.

---

[[1-Logic-and-Critical-Thinking|← Previous]] | [[Math-AI-ML-Hub|🏠 Hub]]
