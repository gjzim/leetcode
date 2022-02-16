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
    def isPalindrome_O_n_space(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        
        mid = fast = head
        length, nodes = 0, []

        while head:
            if fast and fast.next:
                nodes.append(mid.val)
            
                mid = mid.next
                fast = fast.next.next

            length += 1
            head = head.next

        if length % 2 == 1:
            mid = mid.next
        
        for i in reversed(nodes):
            if mid.val != i:
                return False

            mid = mid.next
        
        return True

    def isPalindrome_slow_fast_pointers(self, head: Optional[ListNode]) -> bool:
        if head.next is None: return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        result = True
        tail = self.reverseList(slow)

        headcp, tailcp = head, tail
        while headcp and tailcp:
            if headcp.val != tailcp.val:
                result = False
                break

            headcp = headcp.next
            tailcp = tailcp.next        
        
        slow = self.reverseList(tail)
        
        return result

    def reverseList(self, head):
        cur = head
        prev = next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            prev, prev.next, head = head, prev, head.next
        
        tail = head.next if fast else head
        
        isPali = True
        while prev:
            isPali = isPali and prev.val == tail.val
            head, head.next, prev = prev, head, prev.next
            tail = tail.next
            
        return isPali
            

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

sol = Solution()
head = createLinkedList([1,2,3,2,1,7])
sol.isPalindrome(head)

##def generate_test(sol):
##    maxLength = 10000
##    numMin = 0
##    numMax = 9
##    
##    length = random.randint(2, maxLength)
##    nums = get_rand_list(length//2, numMin, numMax)
##
##    pal = bool(random.randint(0,1))
##    if pal:
##        if random.randint(0,1):
##            nums += [random.randint(0,9)] + list(reversed(nums))
##        else: nums += list(reversed(nums))
##    else:
##        nums += get_rand_list(length//2, numMin, numMax)
##
##    if pal != sol.isPalindrome(createLinkedList(nums)):
##        print('error')
##    
##sol = Solution()
##for i in range(1000):    
##    generate_test(sol)
