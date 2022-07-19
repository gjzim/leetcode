from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        def zerotree(node):
            if not node: return True
            
            leftzero, rightzero = zerotree(node.left), zerotree(node.right)
            if leftzero: node.left = None
            if rightzero: node.right = None
            
            return node.val == 0 and leftzero and rightzero        
        
        return None if zerotree(root) else root
