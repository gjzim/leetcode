from typing import List, Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists_recurse(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None: return None
        if l1 is None: return l2
        if l2 is None: return l1        

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_recurse(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recurse(l2.next, l1)
            return l2

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = prev = None

        while l1 is not None and l2 is not None:            
            if l1.val < l2.val:
                cur = l1
                l1 = l1.next
            else:
                cur = l2
                l2 = l2.next

            if merged is None:
                merged = prev = cur
                continue

            prev.next = cur
            prev = cur

        rest = l1 if l1 is not None else l2

        if rest is not None:
            if merged is None:
                merged = rest
            else:
                prev.next = rest
                
        return merged

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
    length = random.randint(1,50)
    nums = random.sample(range(-100, 100), length)
    nums.sort()
    l1 = createLinkedList(nums)

    length = random.randint(1,50)
    nums = random.sample(range(-100, 100), length)
    nums.sort()
    l2 = createLinkedList(nums)

    merged = convertToArr(sol.mergeTwoLists(l1, l2))    
    
    mergedcl = merged[:]
    mergedcl.sort()
    
    if merged != mergedcl:
        print(merged)        
        
            
sol = Solution()
for i in range(100):    
    generate_test(sol)

