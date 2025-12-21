# ═══════════════════════════════════════
# 📌 [237] - Delete Node in a Linked List
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Delete a node (given only access to that node, not head).

## 💡 **Key Insight:**
Copy next node's value to current, then delete next node.

## 🔧 **Optimal Approach:**
**Algorithm:** Value Copy

**Steps:**
- Copy next node's value to current node
- Delete next node by skipping it

## 💻 **Code (Run Directly):**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

# Helper functions
def createList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def findNode(head, val):
    while head:
        if head.val == val:
            return head
        head = head.next
    return None

# TEST
head = createList([4, 5, 1, 9])
print("Input:", [4, 5, 1, 9])
node = findNode(head, 5)  # Delete node with value 5
deleteNode(node)
print("After deleting 5:", printList(head))
```

## 🏃 **Dry Run:**
**Example:** 4 -> 5 -> 1 -> 9, delete node 5

```
Before: 4 -> [5] -> 1 -> 9
Step 1: Copy 1 to node -> 4 -> [1] -> 1 -> 9
Step 2: Skip duplicate -> 4 -> [1] -> 9

Result: 4 -> 1 -> 9
```

## ⏱️ **Complexity:**
- **Time:** O(1)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Linked List

## ⚠️ **Gotcha:**
Can't delete tail node with this approach. Problem guarantees not tail.
