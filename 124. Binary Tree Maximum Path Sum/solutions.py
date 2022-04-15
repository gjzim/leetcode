from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:       
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = -math.inf
        
        def findMaxPathSum(node):
            if node is None:
                return 0
            
            nonlocal maxPathSum
            
            lmax = max(findMaxPathSum(node.left), 0)
            rmax = max(findMaxPathSum(node.right), 0)
            
            maxPathSum = max(
                maxPathSum, 
                node.val + lmax + rmax
            )
            
            return node.val + max(lmax, rmax)
        
        findMaxPathSum(root)
        
        return maxPathSum
        
