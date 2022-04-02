from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodes = collections.deque([root])
        result = 0
        
        while nodes:
            totalNodes, result = len(nodes), 0
            
            for _ in range(totalNodes):
                node = nodes.popleft()
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
                
                result += node.val
            
        return result

    def deepestLeavesSum_alt(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        result = 0
        
        while nodes:
            children, result = [], 0
            
            for node in nodes:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
                    
                result += node.val
                
            nodes = children
            
        return result 
        
