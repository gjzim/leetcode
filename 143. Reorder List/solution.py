from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(convertToArr(self))

class Solution:
    def reorderList_cryptic(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None: return
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow.next, slow = None, slow.next  
        tail = None  

        while slow:
            tail, slow.next, slow = slow, tail, slow.next

        while tail:
            hnext, tnext = head.next, tail.next
            head.next, tail.next = tail, hnext
            head, tail = hnext, tnext

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None: return

        # Go to middle of the list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the list
        tail = None
        while slow:
            next = slow.next
            slow.next = tail
            tail = slow
            slow = next

        # Insert nodes from the end in reverse order
        while head and tail:
            hnext, tnext = head.next, tail.next
            head.next, tail.next = tail, hnext
            head, tail = hnext, tnext

        # Set the next of the last node to 'None'
        if head: head.next = None

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
