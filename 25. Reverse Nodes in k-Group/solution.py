from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(convertToArr(self))
           
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        prev = sentinel
        nextSeg = head

        while nextSeg and self.hasKNodes(nextSeg, k):
            revHead, revTail, nextSeg = self.reverseKNodes(nextSeg, k)
            
            prev.next = revHead
            prev = revTail
            revTail.next = nextSeg
                    
        return sentinel.next

    def reverseKNodes(self, head, k):
        tail = head
        prev, next = None, head.next

        while k:
            next = head.next
            head.next = prev
            prev = head
            head = next
            k -= 1
        
        return prev, tail, next

    def hasKNodes(self, head, k):       
        while head and k:
            k, head = k - 1, head.next
        else:
            return k == 0
        

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

sol = Solution()
head = createLinkedList([1,2,3,4,5,6,7,8])
print(sol.reverseKGroup(head, 3))

