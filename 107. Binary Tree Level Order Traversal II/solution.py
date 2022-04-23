from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        result = deque()
        nodes = deque([root])

        while nodes:
            levelSize = len(nodes)
            currentLevel = []

            for _ in range(levelSize):
                node = nodes.popleft()
                currentLevel.append(node.val)

                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)

            result.appendleft(currentLevel)

        return result
