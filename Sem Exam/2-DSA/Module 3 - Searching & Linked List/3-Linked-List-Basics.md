# 🔗 Linked List Basics

## 🎯 **The Node Structure**

> [!SUCCESS] **Definition**: A linear data structure where elements are not stored contiguously. Each element points to the next.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TEST - Create a linked list: 1 -> 2 -> 3 -> None
head = Node(1, Node(2, Node(3)))
print("Linked List Created: 1 -> 2 -> 3 -> None")
```

---

## ⛓️ **Types of Lists**

1.  **Singly Linked List**: `A -> B -> C -> None`
2.  **Doubly Linked List (DLL)**: `None <- A <-> B <-> C -> None` (Prev & Next).
3.  **Circular Linked List**: `A -> B -> C -> A` (Loop).

---

## 🛠️ **Basic Operations**

### **1. Traversal O(n)**
```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TEST - Traverse and print
head = Node(1, Node(2, Node(3)))
curr = head
result = []
while curr:
    result.append(curr.val)
    curr = curr.next
print("Traversal:", result)
```

### **2. Insertion O(1)** (If you have pointer)
```python
# Insert New Node AFTER Prev
new_node.next = prev.next
prev.next = new_node
```

### **3. Deletion O(1)**
```python
# Delete Node AFTER Prev
prev.next = prev.next.next
```

---

## 🏹 **Doubly Linked List (DLL)**

> Has `self.prev`.
> **Pros**: Can traverse backward. Easier to delete (if you have the node, you know its prev).
> **Cons**: More memory (2 pointers).

```python
class DLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Sentinel Node**: A Dummy node at the start (`dummy = Node(0, head)`) solves 90% of edge case headaches (like deleting the head).
> - **Arrows**: Always draw arrows before coding! `A -> B`.
> - **Lost Link**: Never break a chain before connecting new link.

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Time complexity to access the Nth element?
> > [!SUCCESS]- Answer
> > **O(n)**. (Unlike Array O(1)).

> [!QUESTION] **Q2**: Advantage of Linked List over Array?
> > [!SUCCESS]- Answer
> > Dynamic size (easy insertion/deletion) without resizing or shifting elements.

> [!QUESTION] **Q3**: What is a "Circular" list?
> > [!SUCCESS]- Answer
> > The last node's `next` points back to the `head` instead of `None`.

> [!QUESTION] **Q4**: How do you delete a node given ONLY that node (not head)?
> > [!SUCCESS]- Answer
> > Copy the value of the `next` node into the current node, then delete the `next` node. (Works unless it's the tail).

> [!QUESTION] **Q5**: What is a Dummy/Sentinel node?
> > [!SUCCESS]- Answer
> > A fake node placed before the head. It simplifies insertion/deletion logic so you don't need special conditions for the Head.

---

Back to: [[Sem Exam/2-DSA/Module 3 - Searching & Linked List/README|Module 3 Hub]] | [[../DSA-Hub|DSA Hub]]
