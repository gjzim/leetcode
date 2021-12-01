from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True

        return  (root.left and self.isSubtree(root.left, subRoot)) or \
                (root.right and self.isSubtree(root.right, subRoot))
            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return p is None and q is None
            
