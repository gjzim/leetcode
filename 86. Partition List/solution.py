from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:                
        bsentinel = ListNode(0, None)
        asentinel = ListNode(0, None)
        before = bsentinel
        after = asentinel
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
                
            head = head.next

        after.next = None
        before.next = asentinel.next        
            
        return bsentinel.next
