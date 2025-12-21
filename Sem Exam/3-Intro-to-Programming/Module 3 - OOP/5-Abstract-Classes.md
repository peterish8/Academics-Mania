# 👻 Abstract Classes

## 📌 1. Concept
An abstract class is a blueprint for other classes. It **cannot be instantiated** itself and often contains abstract methods that **must** be implemented by sub-classes.

## 🛠️ 2. Implementation (abc module)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying ${amount} with Credit Card")

class PayPal(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal")

# p = PaymentProcessor() -> Error! Cannot instantiate abstract class
c = CreditCard()
c.pay(50)
```

---

## 🧠 Practice Exercises
1. **Animal Kingdom**: Create an abstract class `Animal` with abstract methods `move()` and `make_sound()`. Implement specific animals like `Snake` and `Eagle`.

---
> [[Sem Exam/3-Intro-to-Programming/Module 3 - OOP/README|🔙 Back to Module 3 Overview]] | [[../Intro-Prog-Hub|🏠 Back to Subject Hub]]
