from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder_reverse(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        result = []
        nodes = deque([root])
        level = 0

        while nodes:
            levelSize = len(nodes)
            currentLevel = []

            for _ in range(levelSize):
                node = nodes.popleft()
                
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)

                currentLevel.append(node.val)

            if level % 2: currentLevel.reverse()
                
            result.append(currentLevel)
            level += 1

        return result

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        result = []
        nodes = deque([root])
        ltor = True

        while nodes:
            levelSize = len(nodes)
            currentLevel = deque()

            for _ in range(levelSize):
                node = nodes.popleft()
                
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)

                if ltor: 
                    currentLevel.append(node.val)
                else:
                    currentLevel.appendleft(node.val)
                
            result.append(currentLevel)
            ltor = not ltor

        return result

        
        
