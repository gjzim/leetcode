class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        
        def calculateSum(node, parent, grandparent):
            if node is None: return
            
            if grandparent and grandparent.val % 2 == 0:
                self.sum += node.val
                
            calculateSum(node.left, node, parent)
            calculateSum(node.right, node, parent)
            
        calculateSum(root, None, None)
        
        return self.sum
        
