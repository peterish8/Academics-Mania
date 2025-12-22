# 🔗 Linked List - LeetCode Problems

## 🎯 **Two Classic Interview Problems**

> [!SUCCESS] These are frequently asked in interviews and exams!

---

## 1️⃣ **Delete Node in a Linked List (LeetCode 237)**

> **Problem**: You are NOT given the head. You are given the node to delete directly.

### 🤔 **The Trick**

> [!IMPORTANT] **Key Insight**
> You can't reach the previous node (no head given).
> So **copy the next node's data** into current, then **delete the next node**!

**Visual:**
```
Before: [4] → [5] → [1] → [9]  (delete node 5)
Step 1: Copy next value → [4] → [1] → [1] → [9]
Step 2: Skip next node → [4] → [1] → [9]
Done!
```

### 💻 **Code (Runnable)**

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    # Copy next node's value to current
    node.val = node.next.val
    # Skip the next node (delete it)
    node.next = node.next.next

def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# TEST
# Create: 4 -> 5 -> 1 -> 9
head = Node(4, Node(5, Node(1, Node(9))))
node_to_delete = head.next  # Node with value 5

print("Before:", printList(head))
deleteNode(node_to_delete)
print("After deleting 5:", printList(head))
```

### ⚠️ **Important Limitation**

> [!WARNING] This only works if the node is **NOT the last node**!
> (You need a `next` node to copy from)

---

## 2️⃣ **Middle of the Linked List (LeetCode 876)**

> **Problem**: Return the middle node. If even length → return the **second** middle.

### 🐢🐇 **The Technique: Slow & Fast Pointers**

> [!TIP] **Key Insight**
> - `slow` moves **1 step**
> - `fast` moves **2 steps**
> - When `fast` reaches end → `slow` is at **middle**!

**Why it works:**
- Fast jumps twice as fast
- When fast finishes → slow has only walked **half** the distance

**Works for:**
- **Odd length** → exact middle
- **Even length** → second middle (as required by problem)

### 💻 **Code (Runnable)**

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next       # 1 step
        fast = fast.next.next  # 2 steps
    
    return slow

def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# TEST - Odd length: 1 -> 2 -> 3 -> 4 -> 5
head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
mid1 = middleNode(head1)
print("Odd [1,2,3,4,5] - Middle:", mid1.val)

# TEST - Even length: 1 -> 2 -> 3 -> 4 -> 5 -> 6
head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
mid2 = middleNode(head2)
print("Even [1,2,3,4,5,6] - Middle:", mid2.val)
```

---

## 📊 **Quick Summary**

| Problem | Key Technique | Time | Space |
|---------|---------------|------|-------|
| **Delete Node** | Copy next → delete next | O(1) | O(1) |
| **Middle Node** | Slow/Fast pointers | O(n) | O(1) |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Delete Node** (no head): "Become your next, then kill your next" 💀
> - **Middle Node**: "Tortoise 🐢 vs Hare 🐇" - when hare finishes, tortoise is halfway!

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Why can't we delete the last node with the "copy trick"?
> > [!SUCCESS]- Answer
> > There's no `next` node to copy from! `node.next` would be `None`.

> [!QUESTION] **Q2**: What does `while fast and fast.next` check?
> > [!SUCCESS]- Answer
> > Ensures `fast` hasn't reached end AND there's still a node after `fast` (safe to do `fast.next.next`).

> [!QUESTION] **Q3**: For list [1,2,3,4], which node is returned as middle?
> > [!SUCCESS]- Answer
> > Node with value **3** (second middle for even-length lists).

> [!QUESTION] **Q4**: Time complexity of finding middle?
> > [!SUCCESS]- Answer
> > **O(n)** - we traverse the list once (slow walks n/2 steps, fast walks n steps).

> [!QUESTION] **Q5**: What other problems use Slow/Fast pointers?
> > [!SUCCESS]- Answer
> > - **Cycle Detection** (Floyd's Algorithm)
> > - **Find Cycle Start**
> > - **Find nth node from end**

---

Back to: [[Sem Exam/2-DSA/DSA-Hub|DSA Hub]]
