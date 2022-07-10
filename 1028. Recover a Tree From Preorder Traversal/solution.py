from typing import Optional
import re

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder_iter(self, traversal: str) -> Optional[TreeNode]:       
        i, n = 0, len(traversal)
        nodes = []
        
        while i < n:
            dashes, val = 0, 0
            
            while i < n and traversal[i] == '-':
                dashes += 1
                i += 1
            
            while i < n and traversal[i].isdigit():
                val = (val * 10) + int(traversal[i])
                i += 1

            node = TreeNode(val)            
            while dashes < len(nodes):
                nodes.pop()            

            if nodes and nodes[-1].left:
                nodes[-1].right = node
            elif nodes:
                nodes[-1].left = node

            nodes.append(node)


        return nodes[0]               

    def recoverFromPreorder(self, traversal):
        vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", traversal)][::-1]

        def helper(level = 0):
            if not vals or level != vals[-1][0]:
                return None
            
            node = TreeNode(vals.pop()[1])            
            node.left = helper(level + 1)
            node.right = helper(level + 1)
            
            return node
        
        return helper()
        
