from typing import List, Optional
from collections import deque
import random
          
    
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: return []

        output, visited, nodes = [], {}, [root]

        while nodes:
            cur = nodes[-1]
            
            if cur in visited:
                nodes.pop()
                output.append(cur.val)                
            else:
                if cur.children:
                    for child in reversed(cur.children):
                        nodes.append(child)

                visited[cur] = True
        
        return output

    def postorder_recursive(self, root: 'Node') -> List[int]:
        if root is None: return []

        output = []
        
        def _traverse(node, output):
            if node is None: return
                
            if node.children:
                for child in node.children:
                    _traverse(child, output)
            output.append(node.val)

        _traverse(root, output)
        
        return output

def post_order_traversal(root):
    output = []
        
    def _traverse(node, output):
        if node is None: return
                
        if node.children:
            for child in node.children:
                _traverse(child, output)
                
        output.append(node.val)

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
    if post_order_traversal(tree) != sol.postorder(tree):
        print('error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
