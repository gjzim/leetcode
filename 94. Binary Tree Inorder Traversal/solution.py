from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        output, visited, nodes = [], {}, [root]

        while nodes:
            cur = nodes[-1]
            
            if cur not in visited and cur.left:
                nodes.append(cur.left)
            else:
                nodes.pop()
                output.append(cur.val)                
                if cur.right:
                    nodes.append(cur.right)

            visited[cur] = True
        
        return output

def in_order_traversal(root):
    output = []
        
    def _traverse(node, output):
        if node is None: return
                
        _traverse(node.left, output)
        output.append(node.val)
        _traverse(node.right, output)

    _traverse(root, output)

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
    maxLength = 100
    numMin = -100
    numMax = 110
    
    length = random.randint(1, maxLength)
    nums = random.sample(range(numMin, numMax), length)
    nums = [random.randint(1, 100)] + nums
    tree = create_tree_from_list(nums, 100)

    if in_order_traversal(tree) != sol.inorderTraversal(tree):
        print('error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
