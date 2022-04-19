from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        firstNode, secondNode = None, None
        prev = TreeNode(-math.inf)
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if not firstNode and prev.val >= root.val:
                firstNode = prev

            if firstNode and prev.val >= root.val:
                secondNode = root
                
            prev, root = root, root.right
         
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
