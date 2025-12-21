# 🧩 Advanced Linked List Problems

## 🎯 **Classic Patterns**

> [!SUCCESS] **Goal**: Solve common interview problems and understand the pointer gymnastics.

---

## 🔄 **1. Reverse Linked List**

> **Strategy**: 3 Pointers (`prev`, `curr`, `next`).
> Iterate and flip the arrows backwards.

```python
def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next  # Save next
        curr.next = prev  # Flip arrow
        prev = curr       # Move prev
        curr = temp       # Move curr
    return prev # New Head
```

---

## 🐢 **2. Detect Cycle (Runner Method)**

> **Floyd’s Cycle Finding Algorithm**.
> Use `Slow` (+1) and `Fast` (+2). If they collide, there is a loop.

```python
curr = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True # Loop found!
```

---

## ✂️ **3. Remove Nth Node From End**

> **Strategy**:
> 1. Move `Fast` pointer N steps ahead.
> 2. Move `Slow` and `Fast` together until Fast hits end.
> 3. `Slow` is now at the (N+1)th node from end (just before target).
> 4. `slow.next = slow.next.next`

---

## 🤝 **4. Merge Two Sorted Lists**

> Use a Dummy node and stitch them together like a zipper.

```python
dummy = Node()
tail = dummy
while l1 and l2:
    if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next
tail.next = l1 or l2 # Attach remainder
return dummy.next
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Reverse** = "Flip the Arrow" ↩️.
> - **Cycle** = "Track Race" (Fast laps Slow) 🏎️.
> - **From End** = "Head start" (Give Fast a head start of N).

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: What happens if you forget `temp = curr.next` in reversal?
> > [!SUCCESS]- Answer
> > You lose the rest of the list (broken chain) and can't continue traversal.

> [!QUESTION] **Q2**: Time complexity of Cycle Detection?
> > [!SUCCESS]- Answer
> > **O(n)**.

> [!QUESTION] **Q3**: How to find the Middle of a Linked List?
> > [!SUCCESS]- Answer
> > Same Slow/Fast pointers. When Fast hits end, Slow is at middle.

> [!QUESTION] **Q4**: Is merging lists In-Place?
> > [!SUCCESS]- Answer
> > Yes. We only change pointers, we don't create new nodes.

> [!QUESTION] **Q5**: How to check if a LL is Palindrome?
> > [!SUCCESS]- Answer
> > 1. Find Mid. 2. Reverse second half. 3. Compare values of first half and reversed second half.

---

Back to: [[Sem Exam/2-DSA/Module 3 - Searching & Linked List/README|Module 3 Hub]] | [[../DSA-Hub|DSA Hub]]
