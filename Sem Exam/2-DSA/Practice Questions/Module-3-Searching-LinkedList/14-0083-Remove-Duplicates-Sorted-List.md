# ═══════════════════════════════════════
# 📌 [83] - Remove Duplicates from Sorted List
# ═══════════════════════════════════════

## 🎯 **Problem Core:**
Remove duplicates from sorted linked list.

## 💡 **Key Insight:**
Since sorted, duplicates are adjacent. Skip nodes with same value.

## 🔧 **Optimal Approach:**
**Algorithm:** Adjacent Comparison

**Steps:**
- Compare curr.val with curr.next.val
- If same, skip curr.next
- Else move to next

## 💻 **Code (Run Directly):**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

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
head = createList([1, 1, 2, 3, 3])
print("Input:", [1, 1, 2, 3, 3])
print("Output:", printList(deleteDuplicates(head)))
```

## 🏃 **Dry Run:**
**Example:** 1 -> 1 -> 2 -> 3 -> 3

```
step | curr | curr.next | action
-----|------|-----------|--------
1    | 1    | 1         | skip (1.next = 2)
2    | 1    | 2         | move (curr = 2)
3    | 2    | 3         | move (curr = 3)
4    | 3    | 3         | skip (3.next = None)
5    | 3    | None      | done

Result: 1 -> 2 -> 3
```

## ⏱️ **Complexity:**
- **Time:** O(n)
- **Space:** O(1)

## 🏷️ **Pattern Tag:** 
Linked List

## ⚠️ **Gotcha:**
Don't advance curr when deleting - there might be more duplicates.
