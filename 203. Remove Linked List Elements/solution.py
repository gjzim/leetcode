from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            if cur.val == val:
                if cur == head:
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
                
            cur = cur.next
        
        return head
