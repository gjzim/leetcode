import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def countGoodNodes(node, maxTill):
            if node is None:
                return
            
            if node.val >= maxTill:
                maxTill = node.val
                self.count += 1
            
            countGoodNodes(node.left, maxTill)
            countGoodNodes(node.right, maxTill)
            
        countGoodNodes(root, -math.inf)
            
        return self.count
        
