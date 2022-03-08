import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head        

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)     

        return self.merge(left, right)
        
    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        sentinel = ListNode(0)
        cur = sentinel
        
        while head1 and head2:            
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next

            cur = cur.next
                
        if head1: cur.next = head1
        if head2: cur.next = head2
            
        return sentinel.next

    def getMid(self, head: ListNode) -> ListNode:
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = head
            head = head.next
            fast = fast.next.next        

        mid = prev.next
        prev.next = None

        return mid
