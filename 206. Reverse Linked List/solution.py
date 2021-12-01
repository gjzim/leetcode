from typing import List, Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(convertToArr(self))

class Solution:
    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        cur = head
        head = self.reverseList(head.next)

        cur.next.next = cur
        cur.next = None        

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

def generate_test(sol):
    maxLength = 1021
    numMin = -5000
    numMax = 5000
    
    length = random.randint(0, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    l = createLinkedList(nums)

    nums.reverse()
    l = sol.reverseList(l)
    
    if convertToArr(l) != nums:
        print('error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
