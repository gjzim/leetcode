#from typing import List, Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(convertToArr(self))

class Solution:
    def getIntersectionNode_hash(self, headA: ListNode, headB: ListNode) -> ListNode:
        lANodes = {}
        while headA:
            lANodes[headA] = True
            headA = headA.next

        while headB:
            if headB in lANodes:
                return headB

            headB = headB.next

        return None

    def getIntersectionNode_constant_space(self, headA: ListNode, headB: ListNode) -> ListNode:        
        curA, curB = headA, headB
        lAlen = 0 if curA is None else 1
        lBlen = 0 if curB is None else 1

        # Calculate lengths of the lists
        while curA and curA.next:            
            curA = curA.next
            lAlen += 1
            
        while curB and curB.next:            
            curB = curB.next
            lBlen += 1

        # If the end nodes are not the same
        # then they don't have any intersection.
        if curA != curB:
            return None

        curA, curB = headA, headB
        # Advance curA and curB pointers so that
        # they are on the same distance from the
        # intersection.
        while lAlen > lBlen:
            curA = curA.next
            lAlen -= 1

        while lBlen > lAlen:
            curB = curB.next
            lBlen -= 1

        # Advance the pointers until we find the
        # intersection node.
        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA

    # the idea is if you switch head, the possible difference between length would be countered. 
    # On the second traversal, they either hit or miss. 
    # if they meet, pa or pb would be the node we are looking for, 
    # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa, pb = headA, headB        
        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa

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

def appendList(l1, l2):
    head = l1
    while head.next:
        head = head.next

    head.next = l2
    return l1

def generate_test(sol):
    maxLength = 5000
    numMin = 1
    numMax = 10000

    # Create list #1
    length = random.randint(1, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    l1 = createLinkedList(nums)

    # Create list #2
    length = random.randint(1, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    l2 = createLinkedList(nums)

    # Create list #3
    l3 = None
    
    if bool(random.randint(0, 1)):
        length = random.randint(1, maxLength)
        nums = random.sample(range(numMin, numMax), length)
        l3 = createLinkedList(nums)

        l1 = appendList(l1, l3)
        l2 = appendList(l2, l3)

    if l3 != sol.getIntersectionNode(l1, l2):
        print('error')
        print(l1)
        print(l2)
        print(l3)
        
    
sol = Solution()
l1 = createLinkedList([1])
l2 = createLinkedList([1])
print(sol.getIntersectionNode(l1, l2))
for i in range(1000):    
    generate_test(sol)    
