from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
                
        targetSum = targetSum - root.val
        
        if targetSum == 0 and not root.left and not root.right: 
            return True
                        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
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
    maxLength = 1000
    numMin = -1000
    numMax = 1000
    
    length = random.randint(1, maxLength)
    nums = random.choices(range(numMin, numMax), k=length)
    tree = create_tree_from_list(nums, 900)

    targetSum = random.randint(-1000, 900)

    file.write(str(nums) + '\n' + str(targetSum) + '\n' )


sol = Solution()
for i in range(100):    
    generate_test(sol)

file.close()
