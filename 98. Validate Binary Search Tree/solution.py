from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False

            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root) 
    
    def isValidBST_alt(self, root: Optional[TreeNode]) -> bool:        
        if root.left and (
           not self.isLesserThan(root.left, root.val) or
           not self.isValidBST(root.left)
        ): return False        

        if root.right and (
           not self.isGreaterThan(root.right, root.val) or
           not self.isValidBST(root.right)
        ): return False

        return True

    def isLesserThan(self, node, value):
        if (node.left and not self.isLesserThan(node.left, value)) or \
           (node.right and not self.isLesserThan(node.right, value)):
            return False

        return node.val < value
            
        
    def isGreaterThan(self, node, value):
        if (node.left and not self.isGreaterThan(node.left, value)) or \
           (node.right and not self.isGreaterThan(node.right, value)):
            return False

        return node.val > value

    
