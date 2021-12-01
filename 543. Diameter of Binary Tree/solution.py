from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            lh, rh = 0, 0
            
            if node.left: lh = 1 + height(node.left)                
            if node.right: rh = 1 + height(node.right)
            
            self.diameter = max(self.diameter, lh+rh)

            return max(lh, rh)

        height(root)
        
        return self.diameter

