import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n, tail = 1, head
        while tail.next:
            tail, n = tail.next, n + 1
            
        k = (n - k) % n
        if k == 0: return head        
        
        rotHead, prev = head, None
        while k:
            prev, rotHead = rotHead, rotHead.next
            k -= 1

        prev.next, tail.next = None, head
                
        return rotHead
