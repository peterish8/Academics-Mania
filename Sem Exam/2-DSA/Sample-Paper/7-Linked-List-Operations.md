# 7️⃣ Linked List Operations

---

## 📌 Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 📌 Singly Linked List - Insertion

### Insert at Beginning - O(1)
> **Goal**: Add new node at the start of the list.

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Insert at End - O(n)
> **Goal**: Add new node at the end of the list.

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    curr = self.head
    while curr.next:
        curr = curr.next
    curr.next = new_node
```

### Insert at Position k - O(k)
> **Goal**: Insert new node at given position (0-indexed).

```python
def insert_at_position(self, data, k):
    if k == 0:
        self.insert_at_beginning(data)
        return
    new_node = Node(data)
    curr = self.head
    for _ in range(k - 1):
        if curr is None:
            return  # Position out of bounds
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
```

---

## 📌 Singly Linked List - Deletion

### Delete from Beginning - O(1)
> **Goal**: Remove the first node from the list.

```python
def delete_from_beginning(self):
    if self.head is None:
        return
    self.head = self.head.next
```

### Delete from End - O(n)
> **Goal**: Remove the last node from the list.

```python
def delete_from_end(self):
    if self.head is None:
        return
    if self.head.next is None:
        self.head = None
        return
    curr = self.head
    while curr.next.next:
        curr = curr.next
    curr.next = None
```

### Delete from Position k - O(k)
> **Goal**: Remove node at given position (0-indexed).

```python
def delete_from_position(self, k):
    if self.head is None:
        return
    if k == 0:
        self.head = self.head.next
        return
    curr = self.head
    for _ in range(k - 1):
        if curr.next is None:
            return
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
```

---

## 📌 Linked List Problems

### Find Middle Node (Slow-Fast Pointers)
> **Goal**: Return the middle node. For even length, return second middle.

```python
def findMiddle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Detect Cycle (Floyd's Algorithm)
> **Goal**: Check if linked list has a cycle (loop).

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## 🧠 Key Points
- **Insert Beginning**: O(1) - Just update head
- **Insert End**: O(n) - Must traverse (O(1) with tail pointer)
- **Slow-Fast**: Middle = slow when fast reaches end
- **Cycle**: If slow meets fast, cycle exists

---

Back to: [[Sample-Paper-Hub|Sample Paper Hub]]
