from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pathnum):
            if node is None: return 0
            
            pathnum = (10 * pathnum) + node.val
            
            if not node.left and not node.right:
                return pathnum
            
            return dfs(node.left, pathnum) + dfs(node.right, pathnum)
        
        return dfs(root, 0)
