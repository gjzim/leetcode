from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        prev = None

        while fast:
            fast = fast.next
            if n <= 0:
                prev = slow
                slow = slow.next
            n -= 1

        if prev is None:
            return slow.next
        
        prev.next = slow.next

        return head
    
    def removeNthFromEnd_clean(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next
    
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next            
        
        slow.next = slow.next.next

        return head

def createLinkedList(nums):
    head, prev = None, None

    for n in nums:
        node = ListNode(n)
        if head is None:
            head = node

        if prev is not None:
            prev.next = node

        prev = node

    return head

def convertToArr(node):
    arr = []

    while node:
        arr.append(node.val)
        node = node.next

    return arr

