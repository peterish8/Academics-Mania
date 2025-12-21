# 🧠 Logic Basics (Truth Tables, Connectives)

## 📌 1. Truth Values & Propositions
- **Proposition**: A statement that is either True or False (e.g., "It is raining").
- **Truth Value**: `True` (T, 1) or `False` (F, 0).

## 🔗 2. Logical Connectives
| Connective | Symbol | Meaning | Example |
| :--- | :---: | :--- | :--- |
| **Negation** | $\neg$ or ~ | NOT | $\neg p$ (Not p) |
| **Conjunction** | $\land$ | AND | $p \land q$ (Both True) |
| **Disjunction** | $\lor$ | OR | $p \lor q$ (At least one True) |
| **Implication** | $\rightarrow$ | IF...THEN | $p \rightarrow q$ (If p then q) |
| **Biconditional** | $\leftrightarrow$ | IFF | $p \leftrightarrow q$ (Same value) |

## 📊 3. Truth Tables
### **Implication ($p \rightarrow q$)**
False ONLY when $p$ is True and $q$ is False.
 
## 🔄 4. Related Conditionals
For an implication $p \rightarrow q$:
1. **Converse**: $q \rightarrow p$ (Flip it)
2. **Inverse**: $\neg p \rightarrow \neg q$ (Negate both)
3. **Contrapositive**: $\neg q \rightarrow \neg p$ (Flip and Negate)
   - *Note*: A statement is logically equivalent to its Contrapositive.

| p | q | $p \rightarrow q$ |
|---|---|---|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

## 🧩 4. Tautology vs Contradiction
- **Tautology**: Always True (e.g., $p \lor \neg p$)
- **Contradiction**: Always False (e.g., $p \land \neg p$)

---
> [[Sem Exam/4-Mathematics-for-AI-ML/Module 1 - Logic Sets and Critical Thinking/README|🔙 Back to Module 1 Overview]] | [[../Math-AI-ML-Hub|🏠 Back to Subject Hub]]
