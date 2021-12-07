from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []        
        nodes, output = [root], []

        while nodes:
            output.append(max([node.val for node in nodes]))

            children = []            
            for child in nodes:
                if child.left:
                    children.append(child.left)
                if child.right:
                    children.append(child.right)
                
            nodes = children

        return output
    
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


sol = Solution()
print(sol.largestValues(TreeNode(1)))

for i in range(100):    
    #generate_test(sol)
    pass
