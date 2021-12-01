from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder_mine(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        parents = deque([root])
        children = deque([])
        output, level = [], 0

        while parents:            
            if level >= len(output):
                output.append([])
                
            cur = parents.popleft()
            output[level].append(cur.val)

            if cur.left: children.append(cur.left)
            if cur.right: children.append(cur.right)

            if not parents:
                parents.extend(children)
                children.clear()
                level += 1
        
        return output

    def levelOrder(self, root):
        if not root: return []
        
        output, level = [], [root]
        
        while level:
            output.append([node.val for node in level])

            children = []            
            for node in level:
                children.extend([node.left, node.right])
                   
            level = [child for child in children if child]
            
        return output


def flatten(t):
    return [item for sublist in t for item in sublist]

def create_tree_from_list(nums, limit):
    if not nums: return None

    root = TreeNode(nums[0])
    nodes = deque([root])
    i = 1

    while i < len(nums):
        cur = nodes.popleft()

        if nums[i] <= limit:
            cur.left = TreeNode(nums[i])
            nodes.append(cur.left)

        if i+1 < len(nums) and nums[i+1] <= limit:
            cur.right = TreeNode(nums[i+1])
            nodes.append(cur.right)

        i += 2

    return root  

def generate_test(sol):
    maxLength = 2000
    numMin = -1000
    numMax = 1100
    
    length = random.randint(0, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    nums = [random.randint(1, 100)] + nums
    try:
        tree = create_tree_from_list(nums, 1000)
    except:
        return

    nums = list(filter(lambda x: x<=1000, nums))
    lorder = sol.levelOrder(tree)

    if nums != flatten(lorder):
        print(nums, flatten(lorder))
        print('error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
