from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        
        nodes = collections.deque([root])
        
        while nodes:
            levelSize = len(nodes)
            prev = None
            
            for _ in range(levelSize):
                node = nodes.popleft()
                
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
                
                if prev: prev.next = node
                prev = node            
        
        return root

    def connect_o_1_space(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root

        while root and root.left:
            next = root.left
            
            while root:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                root = root.next
                
            root = next            

        return head
        
        
        
