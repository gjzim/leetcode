import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes_mine(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result, restail = head, None
        cur, curSum = head, 0
        
        while cur:
            curSum += cur.val
            cur = cur.next
            
            if cur and cur.val == 0:                
                result.val = curSum
                restail = result
                result = result.next
                curSum = 0
            
        restail.next = None
        
        return head
    
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        prev, cur = head, head.next
        
        while cur.next:
            if cur.val != 0:
                prev.val += cur.val                
            else:
                prev.next.val = 0
                prev = prev.next
            
            cur = cur.next
            
        prev.next = None
        
        return head
    
