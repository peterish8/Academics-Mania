# 🎲 Probability - Complete Notes

---

## 📌 BASIC CONCEPTS

> [!INFO] **Definition: Probability**
> Probability deals with the **likelihood or chance** of an event occurring. It is a numerical measure that quantifies certainty (or uncertainty) of an outcome.
> 
> **Range:** 0 (impossible) to 1 (certain)

### Key Terms

| Term | Definition | Example |
|------|------------|---------|
| **Experiment** | Action/process that leads to an outcome | Tossing a coin |
| **Sample Space** | All possible outcomes of an experiment | {Heads, Tails} |
| **Outcome** | Single result of an experiment | Getting Heads |
| **Event** | Specific outcome or set of outcomes | Getting an even number in dice roll |

---

### Basic Probability Formula

```
P(A) = Number of favorable outcomes / Total number of outcomes
```

**Example:** Find probability of getting a 4 in a dice roll

**Solution:**
```
Number of favorable outcomes = 1 (only one 4)
Total number of outcomes = 6 (1,2,3,4,5,6)

P(4) = 1/6
```

---

## 📌 SET OPERATIONS IN PROBABILITY

### Intersection of Events (A ∩ B)

> **Definition:** Events in which **both A and B** occur at the same time (A **AND** B)

**Example:** Rolling a dice and getting an odd number **AND** greater than 3
- Outcomes: {5} (only 5 is odd and greater than 3)

---

### Union of Events (A ∪ B)

> **Definition:** Event in which **at least one** of A or B occurs (A **OR** B)

**Example:** Rolling a dice and getting an odd number **OR** number greater than 3
- Outcomes: {1, 3, 4, 5, 6}

---

## 📌 ADDITION RULE OF PROBABILITY

> Helps calculate the probability that **at least one** of two events occur.

### 1. Mutually Exclusive Events (MEE)

> **Definition:** Events that **cannot occur at the same time**.

**Formula:**
```
P(A ∪ B) = P(A) + P(B)

Since P(A ∩ B) = 0 (impossible to occur together)
```

---

#### Example 1: Rolling a 2 OR a 5

**Question:** A fair six-sided die is rolled. What is the probability of rolling a 2 OR a 5?

**Solution:**
```
Sample Space: {1, 2, 3, 4, 5, 6}

Event A: Rolling a 2 → P(A) = 1/6
Event B: Rolling a 5 → P(B) = 1/6

Mutually Exclusive: Cannot roll both 2 and 5 simultaneously

P(A ∪ B) = P(A) + P(B)
P(2 OR 5) = 1/6 + 1/6 = 2/6 = 1/3
```

**Answer:** P(A ∪ B) = **1/3**

---

#### Example 2: Drawing a Heart OR a Club

**Question:** A card is drawn from a standard 52-card deck. What is the probability of drawing a Heart OR a Club?

**Solution:**
```
Total Cards: 52

Hearts: 13 cards → P(Heart) = 13/52
Clubs: 13 cards → P(Club) = 13/52

Mutually Exclusive: A card cannot be both Heart and Club

P(Heart ∪ Club) = P(Heart) + P(Club)
P(H ∪ C) = 13/52 + 13/52 = 26/52 = 1/2
```

**Answer:** P(H ∪ C) = **1/2**

---

### 2. Non-Mutually Exclusive Events (NMEE)

> **Definition:** Events that **can occur at the same time**.

**Formula:**
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

---

#### Example 1: Drawing a Heart OR a King

**Question:** A card is drawn from a standard 52-card deck. What is the probability of drawing a Heart OR a King?

**Solution:**
```
Total Cards: 52

Hearts: 13 cards → P(Heart) = 13/52
Kings: 4 cards → P(King) = 4/52
Heart AND King: 1 card (King of Hearts) → P(Heart ∩ King) = 1/52

Non-Mutually Exclusive: Can be both Heart AND King

P(Heart ∪ King) = P(Heart) + P(King) - P(Heart ∩ King)
P(H ∪ K) = 13/52 + 4/52 - 1/52 = 16/52 = 4/13
```

**Answer:** P(H ∪ K) = **4/13**

---

#### Example 2: Playing Football OR Basketball

**Question:** In a class of 30 students: 15 play football, 12 play basketball, 5 play both sports. What is the probability that a randomly selected student plays football OR basketball?

**Solution:**
```
P(Football) = 15/30
P(Basketball) = 12/30
P(Football ∩ Basketball) = 5/30

Non-Mutually Exclusive: Can play both sports

P(F ∪ B) = P(F) + P(B) - P(F ∩ B)
P(F ∪ B) = 15/30 + 12/30 - 5/30 = 22/30 = 11/15
```

**Answer:** P(F ∪ B) = **11/15**

---

## 📌 COMPLEMENTARY EVENTS

> [!INFO] **Definition: Complementary Events**
> Two events are complementary if they cover **all possible outcomes** and **cannot happen at the same time**.

**Formula:**
```
P(A) + P(A') = 1
P(A') = 1 - P(A)
```

**Example:** Pass/Fail in exam are complementary events.

---

### Example 1: Probability of No Rain

**Question:** The probability of rain tomorrow is 0.3. What is the probability that it does NOT rain tomorrow?

**Solution:**
```
Let R = "rain tomorrow"
P(R) = 0.3

P(R') = 1 - P(R)
P(R') = 1 - 0.3 = 0.7
```

**Answer:** P(R') = **0.7**

---

### Example 2: NOT Rolling a 6

**Question:** A fair six-sided die is rolled. What is the probability of NOT rolling a 6?

**Solution:**
```
Event A: Rolling a 6
P(A) = 1/6

P(A') = 1 - P(A)
P(A') = 1 - 1/6 = 5/6
```

**Answer:** P(A') = **5/6**

---

### Example 3: NOT Drawing a Spade

**Question:** A card is drawn from a standard 52-card deck. What is the probability of NOT drawing a Spade?

**Solution:**
```
Event B: Drawing a Spade
P(B) = 13/52 = 1/4

P(B') = 1 - P(B)
P(B') = 1 - 1/4 = 3/4
```

**Answer:** P(B') = **3/4**

---

## 📌 TYPES OF PROBABILITY

### 1. Marginal Probability

> Probability of an event **without considering** any other event. **P(A)**
> 
> Single variable involved.

---

### 2. Joint Probability

> Probability of **two or more events occurring simultaneously**. **P(A ∩ B)**

---

### 3. Conditional Probability

> [!INFO] **Definition: Conditional Probability**
> The probability of an event **given that** another event has already occurred.
> 
> **P(A|B)** = Probability of A given that B has already occurred

**Formula:**
```
P(A|B) = P(A ∩ B) / P(B)
```

---

#### Example 1: Rolling a 6 Given Even Number

**Question:** You roll a fair six-sided dice. What is the probability that the number rolled is a 6, given that the number rolled is an even number?

**Solution:**
```
Event A: Rolling a 6 → Outcomes: {6}
Event B: Rolling an even number → Outcomes: {2, 4, 6}
A ∩ B = {6}

P(A|B) = P(A ∩ B) / P(B)
P(6|Even) = (1/6) / (3/6)
P(6|Even) = (1/6) × (6/3)
P(6|Even) = 1/3
```

**Answer:** P(6|Even) = **1/3**

---

#### Example 2: King Given Face Card

**Question:** You draw one card from a standard deck of 52 playing cards. What is the probability that the card is a King, given that the card drawn is a face card (King, Queen, or Jack)?

**Solution:**
```
Event A: Drawing a King → Total = 4
Event B: Drawing a face card (K, Q, J) → Total = 3 × 4 = 12

P(King|Face Card) = P(A ∩ B) / P(B)
P(King|Face Card) = (4/52) / (12/52)
P(King|Face Card) = 4/12 = 1/3
```

**Answer:** P(King|Face Card) = **1/3**

---

## 📌 MULTIPLICATION RULE OF PROBABILITY

> Helps calculate the probability that **two events both occur**.

### 1. Independent Events

> **Definition:** Occurring of one event **does NOT affect** occurring of the other event.
> 
> Examples: Tossing a coin, rolling a dice

**Formula:**
```
P(A ∩ B) = P(A) × P(B)
```

---

#### Example 1: Heads AND Rolling a 4

**Question:** You flip a fair coin and roll a fair six-sided die. What is the probability of getting heads on the coin and a 4 on the die?

**Solution:**
```
P(Heads) = 1/2
P(4) = 1/6

P(H ∩ 4) = P(H) × P(4)
P(H ∩ 4) = (1/2) × (1/6) = 1/12
```

**Answer:** P(H ∩ 4) = **1/12**

---

#### Example 2: Both Marbles Red (With Replacement)

**Question:** A bag contains 3 red marbles and 2 blue marbles. You draw a marble, **replace it**, and then draw another marble. What is the probability that both marbles are red?

**Solution:**
```
P(Red first) = P(R₁) = 3/5
P(Red second) = P(R₂) = 3/5 (replaced, so same probability)

P(R₁ ∩ R₂) = P(R₁) × P(R₂)
P(R₁ ∩ R₂) = (3/5) × (3/5) = 9/25
```

**Answer:** P(R₁ ∩ R₂) = **9/25**

---

#### Example 3: Tail AND Number Less Than 3

**Question:** You flip a fair coin and roll a standard six-sided die. What is the probability of flipping a Tail on the coin AND rolling a number less than 3 on the die?

**Solution:**
```
P(T) = 1/2
P(D < 3) = 2/6 = 1/3 (outcomes: {1, 2})

P(T ∩ D) = P(T) × P(D)
P(T ∩ D) = (1/2) × (1/3) = 1/6
```

**Answer:** P(T ∩ D) = **1/6**

---

### 2. Dependent Events

> **Definition:** Probability of one event **affects** probability of other event.
> 
> Example: Drawing a card from a deck **without replacement**

**Formula:**
```
P(A ∩ B) = P(A) × P(B|A)
```

---

#### Example 1: Both Marbles Red (Without Replacement)

**Question:** A bag contains 3 red marbles and 2 blue marbles. You draw a marble **without replacement** and then draw another marble. What is the probability that both marbles are red?

**Solution:**
```
P(R₁) = 3/5
P(R₂|R₁) = 2/4 = 1/2 (only 2 red left out of 4 total)

P(R₁ ∩ R₂) = P(R₁) × P(R₂|R₁)
P(R₁ ∩ R₂) = (3/5) × (1/2) = 3/10
```

**Answer:** P(R₁ ∩ R₂) = **3/10**

---

#### Example 2: Both Cards Hearts (Without Replacement)

**Question:** A standard deck of 52 cards is used. You draw two cards **without replacement**. What is the probability that both cards are hearts?

**Solution:**
```
P(H₁) = 13/52 = 1/4
P(H₂|H₁) = 12/51 = 4/17 (only 12 hearts left out of 51 cards)

P(H₁ ∩ H₂) = P(H₁) × P(H₂|H₁)
P(H₁ ∩ H₂) = (1/4) × (4/17) = 1/17
```

**Answer:** P(H₁ ∩ H₂) = **1/17**

---

#### Example 3: White Ball Then Black Ball

**Question:** A box contains 5 white and 3 black balls. Two balls are drawn **without replacement**. What is the probability that the first ball is white and the second ball is black?

**Solution:**
```
P(W₁) = 5/8
P(B₂|W₁) = 3/7 (3 black balls left out of 7 total)

P(W₁ ∩ B₂) = P(W₁) × P(B₂|W₁)
P(W₁ ∩ B₂) = (5/8) × (3/7) = 15/56
```

**Answer:** P(W₁ ∩ B₂) = **15/56**

---

## 🧠 Key Points

- **Probability range:** 0 to 1 (0 = impossible, 1 = certain)
- **Basic formula:** P(A) = Favorable outcomes / Total outcomes
- **Mutually Exclusive:** P(A ∪ B) = P(A) + P(B)
- **Non-Mutually Exclusive:** P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- **Complementary:** P(A) + P(A') = 1
- **Conditional:** P(A|B) = P(A ∩ B) / P(B)
- **Independent Events:** P(A ∩ B) = P(A) × P(B)
- **Dependent Events:** P(A ∩ B) = P(A) × P(B|A)

---

## ❓ 5 Questions to Test Yourself

> [!QUESTION] Q1: What is the difference between mutually exclusive and non-mutually exclusive events?
>> [!SUCCESS]- Answer
>> **Mutually Exclusive**: Cannot occur at the same time (P(A ∩ B) = 0). **Non-Mutually Exclusive**: Can occur at the same time (P(A ∩ B) ≠ 0).

> [!QUESTION] Q2: If P(A) = 0.6, what is P(A')?
>> [!SUCCESS]- Answer
>> P(A') = 1 - P(A) = 1 - 0.6 = **0.4**

> [!QUESTION] Q3: When do you use P(A ∩ B) = P(A) × P(B)?
>> [!SUCCESS]- Answer
>> When events are **independent** (one event does not affect the other).

> [!QUESTION] Q4: What is conditional probability?
>> [!SUCCESS]- Answer
>> Probability of event A **given that** event B has already occurred. Formula: **P(A|B) = P(A ∩ B) / P(B)**

> [!QUESTION] Q5: Drawing cards without replacement - independent or dependent?
>> [!SUCCESS]- Answer
>> **Dependent** - the first draw affects the probability of the second draw.

---

[[6-Measures-of-Dispersion|← Previous]] | [[Math-AI-ML-Hub|🏠 Hub]]
