# 8️⃣ Linked List Types - Comparison

---

## 📌 Doubly Linked List (DLL)

### Structure
```python
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

### ✅ Advantages
| Advantage | Explanation |
|-----------|-------------|
| **Bidirectional traversal** | Can go forward and backward |
| **Easy deletion** | No need to track previous node |
| **O(1) delete if node given** | Just update prev and next pointers |

### ❌ Disadvantages
| Disadvantage | Explanation |
|--------------|-------------|
| **Extra memory** | Two pointers per node (prev + next) |
| **Complex operations** | More pointers to update |

---

## 📌 Circular Linked List (CLL)

### Structure
- Last node points back to **head** instead of `None`
- No null at end!

```
[A] → [B] → [C] → [A] (back to start)
```

### ✅ Advantages
| Advantage | Explanation |
|-----------|-------------|
| **No null checks** | Can always traverse |
| **Round-robin access** | Good for scheduling (OS) |
| **Any node can be start** | No fixed beginning |

### ❌ Disadvantages
| Disadvantage | Explanation |
|--------------|-------------|
| **Infinite loop risk** | Must track visited nodes |
| **Complex termination** | Need to check if back to start |

---

## 📊 Comparison Table

| Feature | Singly | Doubly | Circular |
|---------|--------|--------|----------|
| **Memory** | 1 pointer | 2 pointers | 1 pointer |
| **Traverse backward** | ❌ No | ✅ Yes | ❌ No |
| **Delete with node** | O(n) | O(1) | O(n) |
| **End detection** | `next == None` | `next == None` | `next == head` |
| **Use case** | Simple lists | Browser history | Scheduling |

---

## 🧠 Key Points
- **DLL**: Extra `prev` pointer, bidirectional
- **CLL**: Last → Head, no null end
- **DLL advantage**: O(1) delete if you have the node
- **CLL advantage**: Circular access, no beginning/end

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
