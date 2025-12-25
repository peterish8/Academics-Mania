# 🧠 Logic and Critical Thinking - Complete Notes

> [!INFO] **Definition: Proposition**
> A statement that is either **True** or **False**. Also called a "statement".

> [!INFO] **Definition: Logic**
> The framework/rules that tells us whether a statement is True or False using reasoning.

---

## 📌 Why Study Logic?
- ✅ Develop clear and critical thinking
- ✅ Programming: if-else, loops, conditions
- ✅ Databases: queries using AND, OR, NOT
- ✅ Everyday reasoning and decision making

---

## 📌 Types of Propositions

| Type | Definition | Example |
|------|------------|---------|
| **Simple** | Cannot be broken down further | "The sky is blue" |
| **Compound** | Combines two or more simple propositions | "It is raining AND it is cold" |

---

## 📌 Truth Value

> [!INFO] **Definition: Truth Value**
> The label (True or False) we assign to a proposition.
> - True → denoted by **"T"** or **1**
> - False → denoted by **"F"** or **0**

**Examples:**
- `1 < 4` → Truth value is **T**
- `14 is odd` → Truth value is **F**

---

## 📌 Logical Connectives

| Connective | Symbol | Name | Example (p = raining, q = cold) |
|------------|--------|------|--------------------------------|
| AND | ∧ | Conjunction | p ∧ q = "It is raining and cold" |
| OR | ∨ | Disjunction | p ∨ q = "It is raining or cold" |
| NOT | ¬ or ~ | Negation | ~p = "It is not raining" |
| IF...THEN | → | Conditional | p → q = "If raining, then cold" |
| IFF | ↔ | Biconditional | p ↔ q = "Raining iff cold" |
| XOR | ⊕ | Exclusive OR | p ⊕ q = "Either one, not both" |
| NOR | ↓ | NOT OR | p ↓ q = "Neither raining nor cold" |
| NAND | ↑ | NOT AND | p ↑ q = "Not both at same time" |

---

## 📌 Truth Tables

> **Formula:** Number of combinations = **2ⁿ** (where n = number of propositions)

### Conjunction (AND) - p ∧ q
> True only when **ALL** propositions are true.

| p | q | p ∧ q |
|---|---|-------|
| T | T | **T** |
| T | F | F |
| F | T | F |
| F | F | F |

---

### Disjunction (OR) - p ∨ q
> True when **at least one** proposition is true.

| p | q | p ∨ q |
|---|---|-------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | **F** |

---

### Negation (NOT) - ~p
> Reverses the truth value.

| p | ~p |
|---|-----|
| T | F |
| F | T |

---

### Conditional (IF...THEN) - p → q
> False **only when** first is True and second is False.

| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

---

### Biconditional (IFF) - p ↔ q
> True when **both have same truth value**.

| p | q | p ↔ q |
|---|---|-------|
| T | T | **T** |
| T | F | F |
| F | T | F |
| F | F | **T** |

---

### Exclusive OR (XOR) - p ⊕ q
> True if **exactly one** is true.

| p | q | p ⊕ q |
|---|---|-------|
| T | T | F |
| T | F | **T** |
| F | T | **T** |
| F | F | F |

---

### NOR (NOT OR) - p ↓ q
> True only if **both are false**. Equivalent to ¬(p ∨ q)

| p | q | p ∨ q | p ↓ q |
|---|---|-------|-------|
| T | T | T | F |
| T | F | T | F |
| F | T | T | F |
| F | F | F | **T** |

---

### NAND (NOT AND) - p ↑ q
> False only if **both are true**. Equivalent to ¬(p ∧ q)

| p | q | p ∧ q | p ↑ q |
|---|---|-------|-------|
| T | T | T | **F** |
| T | F | F | T |
| F | T | F | T |
| F | F | F | T |

---

## 📌 Tautology, Contradiction & Contingency

| Type | Definition | Example |
|------|------------|---------|
| **Tautology** | Always **True** for all combinations | p ∨ ~p |
| **Contradiction** | Always **False** for all combinations | p ∧ ~p |
| **Contingency** | Sometimes True, sometimes False | p ∧ q |

---

## 📌 De Morgan's Laws

> [!SUCCESS] **First Law**
> ¬(p ∧ q) ≡ ¬p ∨ ¬q
> "NOT (A AND B)" = "NOT A OR NOT B"

> [!SUCCESS] **Second Law**
> ¬(p ∨ q) ≡ ¬p ∧ ¬q
> "NOT (A OR B)" = "NOT A AND NOT B"

---

## 💻 Solved Examples

### Example 1: Create truth table for (p ∧ q) ∨ q

| p | q | p ∧ q | (p ∧ q) ∨ q |
|---|---|-------|-------------|
| T | T | T | T |
| T | F | F | F |
| F | T | F | T |
| F | F | F | F |

---

### Example 2: Prove p ∧ q → p ∨ q is a Tautology

| p | q | p ∧ q | p ∨ q | p ∧ q → p ∨ q |
|---|---|-------|-------|---------------|
| T | T | T | T | **T** |
| T | F | F | T | **T** |
| F | T | F | T | **T** |
| F | F | F | F | **T** |

✅ All values are T → **Tautology**

---

### Example 3: Identify (p ⊕ q) ∧ (p ↔ q)

| p | q | p ⊕ q | p ↔ q | (p ⊕ q) ∧ (p ↔ q) |
|---|---|-------|-------|-------------------|
| T | T | F | T | F |
| T | F | T | F | F |
| F | T | T | F | F |
| F | F | F | T | F |

✅ All values are F → **Contradiction**

---

## 🧠 Key Points
- **Proposition** = Statement that is T or F
- **Simple** = Cannot break down, **Compound** = Combined
- **AND** = All true, **OR** = At least one true
- **→** = False only when T→F
- **↔** = Same truth values
- **XOR** = Exactly one true
- **NAND/NOR** = Negation of AND/OR
- **Tautology** = Always T, **Contradiction** = Always F
- **De Morgan**: Flip AND/OR when negating

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: When is a Conditional (p → q) false?
>> [!SUCCESS]- Answer
>> Only when **p is True** and **q is False**.

> [!QUESTION] Q2: What is the difference between XOR and OR?
>> [!SUCCESS]- Answer
>> **OR** = at least one true. **XOR** = exactly one true (not both).

> [!QUESTION] Q3: What is De Morgan's First Law?
>> [!SUCCESS]- Answer
>> ¬(p ∧ q) ≡ ¬p ∨ ¬q (NOT of AND = OR of NOTs)

> [!QUESTION] Q4: What is a Contingency?
>> [!SUCCESS]- Answer
>> A proposition that is **sometimes True and sometimes False**.

> [!QUESTION] Q5: How many rows in truth table for 3 propositions?
>> [!SUCCESS]- Answer
>> **2³ = 8 rows**

---

[[Math-AI-ML-Hub|← Back to Math Hub]]
