from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        prev = result
        
        c = 0
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            c, s = divmod(v1 + v2 + c, 10)

            prev.next = ListNode(s)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


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
