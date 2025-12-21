# ═══════════════════════════════════════
# 📌 [876] - Middle of the Linked List
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Find middle node. If two middles, return second.

## 💡 **Key Insight:**
Slow and fast pointers. When fast reaches end, slow is at middle.

## 🔧 **Optimal Approach:**
**Algorithm:** Two Pointers (Tortoise and Hare)

**Steps:**
- slow moves 1 step, fast moves 2 steps
- When fast reaches end, slow is at middle

## 💻 **Code (Run Directly):**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

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

# TEST
head1 = createList([1, 2, 3, 4, 5])
head2 = createList([1, 2, 3, 4, 5, 6])
print("Odd [1,2,3,4,5] middle:", printList(middleNode(head1)))
print("Even [1,2,3,4,5,6] middle:", printList(middleNode(head2)))
```

## 🏃 **Dry Run:**
**Example:** 1 -> 2 -> 3 -> 4 -> 5

```
step | slow | fast
-----|------|------
init | 1    | 1
1    | 2    | 3
2    | 3    | 5
3    | -    | None (fast.next is None)

Return slow = 3
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Linked List, Two Pointers

## ⚠️ **Gotcha:**
Check both fast and fast.next before moving.
