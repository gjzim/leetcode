class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':      
        cloned = {}
        
        def cloneNode(original):
            if original.val in cloned:
                return cloned[original.val]
            
            clone = Node(original.val)
            cloned[original.val] = clone
            
            for neighbor in original.neighbors:
                clone.neighbors.append(cloneNode(neighbor))
            
            return clone
                
        return cloneNode(node) if node else None
