from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        firstK = head
        while k > 1:
            firstK, k = firstK.next, k - 1
            
        lastK, cur = head, firstK
        while cur.next:
            lastK, cur = lastK.next, cur.next                    
            
        firstK.val, lastK.val = lastK.val, firstK.val

        return head
            
            
        
            
            
        
