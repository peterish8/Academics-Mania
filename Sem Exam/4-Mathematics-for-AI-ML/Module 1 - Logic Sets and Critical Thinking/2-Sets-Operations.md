# 🎱 Sets & Venn Diagrams

## 📌 1. Set Terminology
- **Set**: Collection of distinct objects. $A = \{1, 2, 3\}$
- **Elements**: Members of a set. $1 \in A$
- **Empty Set**: $\emptyset = \{\}$
- **Subset**: $A \subseteq B$ (Every element of A is in B)

## 🛠️ 2. Set Operations
| Operation | Symbol | Definition |
| :--- | :---: | :--- |
| **Union** | $A \cup B$ | Elements in A **OR** B |
| **Intersection** | $A \cap B$ | Elements in A **AND** B |
| **Difference** | $A - B$ | Elements in A **BUT NOT** in B |
| **Complement** | $A'$ or $A^c$ | Elements NOT in A (in Universe) |
| **Cartesian Product** | $A \times B$ | Ordered pairs $(a, b)$ |

## 🖼️ 3. Venn Diagrams
Visual representation using circles. Useful for solving problems like "How many people like both Coffee and Tea?"

Formula:  
$|A \cup B| = |A| + |B| - |A \cap B|$

---

## 📌 4. Ordered Pairs & Cartesian Product

> [!INFO] **Definition: Ordered Pair**
> A pair of elements where **order matters**: $(a, b) \neq (b, a)$ unless $a = b$.

> [!INFO] **Definition: Cartesian Product**
> $A \times B$ = Set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$.

**Example:**
```
A = {1, 2}
B = {x, y}

A × B = {(1,x), (1,y), (2,x), (2,y)}
```

**Properties:**
- $|A \times B| = |A| \times |B|$ (number of pairs)
- $(a, b) = (c, d)$ only if $a = c$ AND $b = d$
- $A \times B \neq B \times A$ (unless A = B)

---
> [[Sem Exam/4-Mathematics-for-AI-ML/Module 1 - Logic Sets and Critical Thinking/README|🔙 Back to Module 1 Overview]] | [[../Math-AI-ML-Hub|🏠 Back to Subject Hub]]
