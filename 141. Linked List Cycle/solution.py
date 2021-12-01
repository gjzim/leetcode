from typing import List
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        
        while head and head not in seen:
            seen[head] = True
            head = head.next
                    
        return head in seen

    def hasCycle_2(self, head: Optional[ListNode]) -> bool:       
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False        
        
        
