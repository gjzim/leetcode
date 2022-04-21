from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(convertToArr(self))

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head

        sentinel = ListNode(0, head)
        prev, cur = sentinel, head
        pos = 1
        while pos < left:
            prev, cur = cur, cur.next       
            pos += 1

        revPrev, revTail = prev, cur        
        prev = None        
        while pos <= right:
            cur.next, prev, cur = prev, cur, cur.next
            pos += 1

        revPrev.next = prev
        revTail.next = cur
        
        return sentinel.next
