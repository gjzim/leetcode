from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        def fix(node):
            if node and node.left:
                node.left.val = (2 * node.val) + 1
                self.nodes.add(node.left.val)
                fix(node.left)
            
            if node and node.right:
                node.right.val = (2 * node.val) + 2
                self.nodes.add(node.right.val)
                fix(node.right)
        
        self.nodes = set([])
        if root: 
            root.val = 0
            self.nodes.add(0)
            
        fix(root)

    def find(self, target: int) -> bool:                   
        return target in self.nodes
