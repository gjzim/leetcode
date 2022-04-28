from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        sl = None
        s = c = 0
        while l1 and l2:
            c, s = divmod(l1.val + l2.val + c, 10)
            sl = ListNode(s, sl)
            l1, l2 = l1.next, l2.next
        
        while l1:
            c, s = divmod(l1.val + c, 10)
            sl = ListNode(s, sl)
            l1 = l1.next
            
        while l2:
            c, s = divmod(l2.val + c, 10)
            sl = ListNode(s, sl)
            l2 = l2.next            
        
        return ListNode(c, sl) if c else sl
        
        
    def reverseList(self, head):
        prev = None        
        while head:
            head.next, prev, head = prev, head, head.next
            
        return prev
