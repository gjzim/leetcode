from typing import List, Optional
from collections import deque
import random

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def preorder_iter(self, root: 'Node') -> List[int]:
        if root is None: return []

        output, nodes = [], [root]

        while nodes:
            cur = nodes.pop()
            output.append(cur.val)

            if cur.children:
                for child in reversed(cur.children):
                    nodes.append(child)
                    
        return output

    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []

        output = []

        def _traverse(node, output):
            if node is None: return
        
            output.append(node.val)
            if node.children:
                for child in node.children:
                    _traverse(child, output)

        _traverse(root, output)

        return output
        
def pre_order_traversal(root):
    output = []
        
    def _traverse(node, output):
        if node is None: return
        
        output.append(node.val)
        if node.children:
            for child in node.children:
                _traverse(child, output)

    _traverse(root, output)

    return output 
           
    
def create_n_ary_tree(length, numMin, numMax, maxChildren):
    root = TreeNode(random.randint(numMin, numMax))
    nodes = deque([root])

    i = 1
    while i < length:
        try:
            cur = nodes.popleft()
        except:
            return root
        
        childCount = random.randint(0, 8)
        children = []
        
        while len(children) < childCount:
            child = TreeNode(random.randint(numMin, numMax))
            children.append(child)
            nodes.append(child)

        cur.children = children
        i += childCount

    return root
    

def generate_test(sol):
    tree = create_n_ary_tree(1000, 0, 10000, 8)
    if pre_order_traversal(tree) != sol.preorder(tree):
        print('error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
