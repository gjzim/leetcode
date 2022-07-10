from typing import Optional
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, pathMax, pathMin):
            if not node: 
                return pathMax - pathMin
            
            pathMax = max(pathMax, node.val)
            pathMin = min(pathMin, node.val)
                        
            return max(
                helper(node.left, pathMax, pathMin),
                helper(node.right, pathMax, pathMin)
            )        
                    
        return helper(root, -math.inf, math.inf)
