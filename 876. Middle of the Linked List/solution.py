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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:            
            slow = slow.next            
            fast = fast.next.next
        
        return slow

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
    maxLength = 99
    numMin = 1
    numMax = 100
    
    length = random.randint(1, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    l = createLinkedList(nums)
    
    mid = len(nums)//2
    lmid = sol.middleNode(l).val
    if nums[mid] != lmid:
        print(nums, nums[mid], lmid, 'error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
