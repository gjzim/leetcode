from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False

        if p.val != q.val: return False
                        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return p is None and q is None
    
def create_tree_from_list(nums, limit):
    if not nums: return None

    root = TreeNode(nums[0])
    nodes = deque([root])
    i = 1

    while i < len(nums):
        try:
            cur = nodes.popleft()
        except:
            return root

        if nums[i] <= limit:
            cur.left = TreeNode(nums[i])
            nodes.append(cur.left)

        if i+1 < len(nums) and nums[i+1] <= limit:
            cur.right = TreeNode(nums[i+1])
            nodes.append(cur.right)

        i += 2

    return root
            
file = open('input.txt', 'a')
def generate_test(sol):
    maxLength = 99
    numMin = -1000
    numMax = 1000
    
    length = random.randint(2, maxLength)
    nums = random.choices(range(numMin, numMax), k=length)
    p = create_tree_from_list(nums, 900)
    nums2 = nums[::]
    nums2.append(random.randint(numMin, numMax))
    q = create_tree_from_list(nums2, 900)

    file.write(str(nums) + '\n' + str(nums2) + '\n' )

sol = Solution()
for i in range(100):    
    generate_test(sol)

file.close()
