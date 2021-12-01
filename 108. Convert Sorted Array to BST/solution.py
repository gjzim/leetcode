from typing import List, Optional
import random

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        output = str(self.val) + ' '

        if self.left is not None:
            output += str(self.left)        

        if self.right is not None:
            output += str(self.right)

        return output

    def height(self):      
        height = 1
        left_height = 0
        right_height = 0
        
        if self.left is not None:
            left_height = self.left.height()

        if self.right is not None:
            right_height = self.right.height()

        return 1 + (left_height if left_height > right_height else right_height)        
        

    def is_balanced(self):
        lh = rh = 0
        if self.left is not None:
            lh = self.left.height()

        if self.right is not None:
            rh = self.right.height()
        
        return abs(lh-rh) < 2
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])

        rootIndex = (len(nums)-1)//2
        root = TreeNode(nums[rootIndex])
        root.left = self.sortedArrayToBST(nums[:rootIndex])
        root.right = self.sortedArrayToBST(nums[rootIndex+1:])

        return root
        

def generate_test():
    length = random.randint(0,10000)
    nums = random.sample(range(-100000, 100000), length)

    nums.sort()
    sol = Solution()
    tree = sol.sortedArrayToBST(nums)

   
    if not tree.is_balanced():
        print('error')

for i in range(1000):
    generate_test()
