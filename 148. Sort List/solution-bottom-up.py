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

        length = self.getLen(head)
        sentinel = ListNode(0, head)

        cur, start, size = None, None, 1
       
        while size < length:
            prev = sentinel
            cur = sentinel.next
            
            while cur:
                left = cur
                right = self.splitAndGetNextNode(left, size)
                cur = self.splitAndGetNextNode(right, size)

                prev = self.mergeAndGetTail(left, right, prev)               

            size *= 2

        return sentinel.next

    def splitAndGetNextNode(self, head, size):
        for _ in range(size - 1):
            if not head: break
            
            head = head.next

        if not head: return None
        
        nextNode = head.next
        head.next = None
        
        return nextNode

    def mergeAndGetTail(self, head1, head2, prev):
        cur = prev
        
        while head1 and head2:            
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next

            cur = cur.next

        cur.next = head1 if head1 else head2

        while cur.next:
            cur = cur.next
            
        return cur
    

    def getLen(self, head):
        count = 0
        
        while head:
            head = head.next
            count += 1

        return count
