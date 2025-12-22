# 🔗 Linked List - Complete Guide

## 🎯 **Introduction**

> [!SUCCESS] **Definition**: A linear data structure where elements (nodes) are connected using pointers, not continuous memory.

**Each Node stores:**
- `data` - the actual value
- `next` - reference (pointer) to next node

---

## ✅ **Why Use Linked List?**

| Advantage | Explanation |
|-----------|-------------|
| **O(1) Insert/Delete** | At beginning/end (with tail pointer) |
| **Dynamic Size** | No need for contiguous memory |
| **No Shifting** | Unlike arrays, no element shifting needed |

## ❌ **Why It's Not Perfect?**

| Disadvantage | Explanation |
|--------------|-------------|
| **O(n) Access** | Must traverse from head to find element |
| **Extra Memory** | Each node stores pointer (overhead) |
| **No Random Access** | Can't do `arr[5]` like arrays |

---

## 🛠️ **Basic Structure**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
print("Empty List:", ll.print_list())
```

---

## ➕ **Insertion Operations**

### **(A) Insert at Beginning (Head) - O(1)** ⚡
> Fastest operation. Just point new node → old head.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point to old head
        self.head = new_node       # Update head
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
print("After insert at beginning:", ll.print_list())
```

---

### **(B) Insert at End (Tail) - O(n)**
> Must traverse to find last node (unless you maintain tail pointer).

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to last node
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node  # Link last node to new node
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
print("After insert at end:", ll.print_list())
```

---

### **(C) Insert at Any Position - O(n)**
> Position is 0-based index. Traverse to (pos-1) and insert.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_position(self, data, pos):
        # If position is 0, insert at beginning
        if pos == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        curr = self.head
        count = 0
        
        # Traverse to (pos-1)
        while curr is not None and count < pos - 1:
            curr = curr.next
            count += 1
        
        if curr is None:
            raise IndexError("Position out of bounds")
        
        # Insert: new_node points to curr.next, curr points to new_node
        new_node.next = curr.next
        curr.next = new_node
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(3)
ll.insert_at_position(2, 1)  # Insert 2 at position 1
print("After insert at position 1:", ll.print_list())
```

---

## ➖ **Deletion Operations**

### **(A) Delete from Beginning - O(1)** ⚡
> Just move head to next node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_from_beginning(self):
        if self.head is None:
            return  # Empty list
        self.head = self.head.next  # Move head forward
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
print("Before delete:", ll.print_list())
ll.delete_from_beginning()
print("After delete from beginning:", ll.print_list())
```

---

### **(B) Delete from End - O(n)**
> Must traverse to second-last node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_from_end(self):
        if self.head is None:
            return  # Empty list
        
        # Only one node
        if self.head.next is None:
            self.head = None
            return
        
        # Traverse to second-last node
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        curr.next = None  # Remove last node
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
print("Before delete:", ll.print_list())
ll.delete_from_end()
print("After delete from end:", ll.print_list())
```

---

### **(C) Delete from Any Position - O(n)**
> Traverse to (pos-1) and bypass the target node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_from_position(self, pos):
        if self.head is None:
            return
        
        # Delete first node
        if pos == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        count = 0
        
        # Traverse to (pos-1)
        while curr is not None and count < pos - 1:
            curr = curr.next
            count += 1
        
        if curr is None or curr.next is None:
            raise IndexError("Position out of bounds")
        
        # Bypass: curr.next skips over the deleted node
        curr.next = curr.next.next
    
    def print_list(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

# TEST
ll = LinkedList()
ll.insert_at_beginning(4)
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
print("Before delete:", ll.print_list())
ll.delete_from_position(2)  # Delete element at index 2
print("After delete from position 2:", ll.print_list())
```

---

## 📊 **Time Complexity Summary**

| Operation | Time | Notes |
|-----------|------|-------|
| Insert at Beginning | O(1) | Fastest |
| Insert at End | O(n) | O(1) with tail pointer |
| Insert at Position | O(n) | Must traverse |
| Delete from Beginning | O(1) | Fastest |
| Delete from End | O(n) | Need second-last |
| Delete from Position | O(n) | Must traverse |
| Search | O(n) | No random access |

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Insert Beginning** = Point new → old head, update head
> - **Insert End** = Traverse to last, link it
> - **Delete Beginning** = Move head forward
> - **Delete End** = Find second-last, set `.next = None`
> - **Position ops** = Traverse to (pos-1) first!

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: Why is Insert at Beginning O(1)?
> > [!SUCCESS]- Answer
> > No traversal needed. Just update pointers (new_node.next = head, head = new_node).

> [!QUESTION] **Q2**: How to make Insert at End O(1)?
> > [!SUCCESS]- Answer
> > Maintain a **tail pointer** that always points to the last node.

> [!QUESTION] **Q3**: Why traverse to (pos-1) for insert/delete at position?
> > [!SUCCESS]- Answer
> > You need the **previous node** to update its `.next` pointer.

> [!QUESTION] **Q4**: What happens if you delete from an empty list?
> > [!SUCCESS]- Answer
> > Check `if self.head is None: return` to avoid errors.

> [!QUESTION] **Q5**: Why can't we do `arr[5]` in Linked List?
> > [!SUCCESS]- Answer
> > No random access. Nodes aren't stored contiguously in memory. Must traverse from head.

---

Back to: [[Sem Exam/2-DSA/DSA-Hub|DSA Hub]]
