# ═══════════════════════════════════════
# 📌 [206] - Reverse Linked List
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Reverse a singly linked list.

## 💡 **Key Insight:**
Iterative: Track prev, curr, next. Redirect curr.next to prev.

## 🔧 **Optimal Approach:**
**Algorithm:** Iterative Pointer Manipulation

**Steps:**
- prev = None, curr = head
- While curr: save next, redirect curr.next to prev
- Move prev and curr forward

## 💻 **Code (Run Directly):**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Helper to create and print list
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

# TEST
head = createList([1, 2, 3, 4, 5])
print("Input:", [1, 2, 3, 4, 5])
print("Output:", printList(reverseList(head)))
```

## 🏃 **Dry Run:**
**Example:** 1 -> 2 -> 3 -> None

```
step | prev | curr | next | action
-----|------|------|------|--------
1    | None | 1    | 2    | 1->None
2    | 1    | 2    | 3    | 2->1
3    | 2    | 3    | None | 3->2
4    | 3    | None | -    | done

Result: 3 -> 2 -> 1 -> None
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Linked List, Reversal

## ⚠️ **Gotcha:**
Save next BEFORE redirecting curr.next.
