from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        
        result = []
        nodes = collections.deque([root])
        
        while nodes:
            result.append(nodes[-1].val)
            levelSize = len(nodes)
            
            for _ in range(levelSize):
                node = nodes.popleft()
                
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
            
        return result
        
        
        
