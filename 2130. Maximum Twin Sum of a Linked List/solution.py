import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(convertToArr(self))
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head: return 0
        
        result = 0
        mid = self.getMid(head)        
        tail, mid.next = self.reverseList(mid.next), None

        while head and tail:
            result = max(result, head.val + tail.val)
            head, tail = head.next, tail.next
        
        return result
    
    def reverseList(self, head):
        prev = None
       
        while head:            
            head.next, prev, head = prev, head, head.next
            
        return prev
        
    def getMid(self, head):
        mid = fast = head
        
        while fast.next.next:
            mid = mid.next
            fast = fast.next.next
            
        return mid

    def pairSum_recursive(self, head: Optional[ListNode]) -> int:
        if not head: return 0

        self.left = head        
        
        return self.maxSum(head, 0)

    def maxSum(self, right, result):
        if not right: return 0

        result = self.maxSum(right.next, result)
        result = max(result, self.left.val + right.val)
        
        self.left = self.left.next
        
        return result
