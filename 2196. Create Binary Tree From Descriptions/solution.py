from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        
        for parent, child, isLeft in descriptions:
            nodes[parent] = nodes.get(parent, [TreeNode(parent), False])
            nodes[child] = nodes.get(child, [TreeNode(child), True])
            
            nodes[child][1] = True
            parent, child = nodes[parent][0], nodes[child][0]            
            
            if isLeft:
                parent.left = child
            else:
                parent.right = child
                               
        for node, hasParent in nodes.values():
            if not hasParent:
                return node
        
        return None
                
