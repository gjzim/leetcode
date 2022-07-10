from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node: return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.moves += abs(left) + abs(right)
            
            return left + right + node.val - 1
        
        self.moves = 0
        helper(root)
        return self.moves
        
