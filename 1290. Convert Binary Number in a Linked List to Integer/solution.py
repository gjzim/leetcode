from typing import List, Optional
from functools import reduce
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(convertToArr(self))

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num, m = 0, 1
        cur = head

        while cur.next:            
            cur = cur.next
            m *= 2

        cur = head        
        while cur:
            num += cur.val * m
            m //= 2
            cur = cur.next
            
        return num

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

def get_rand_list(length, start = 0, stop = 100):
    nums = []
    for i in range(length):
        nums.append(random.randint(start, stop))

    return nums
    
def generate_test(sol):
    maxLength = 30
    numMin = 0
    numMax = 1
    
    length = random.randint(1, maxLength)
    nums = get_rand_list(length, numMin, numMax)
        
    bs = str(reduce(lambda a, b: str(a) + str(b), nums))
    out = sol.getDecimalValue(createLinkedList(nums))
    if int(bs, 2) != out:
        print('error', bs, int(bs, 2), out)

sol = Solution()
for i in range(1000):    
    generate_test(sol)    
