from typing import List, Optional
from collections import deque
import random
          
    
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []

        parents = deque([root])
        children = deque([])
        output, level = [], 0

        while parents:            
            if level >= len(output):
                output.append([])
                
            cur = parents.popleft()
            output[level].append(cur.val)

            if cur.children:
                children.extend(cur.children)

            if not parents:
                parents.extend(children)
                children.clear()
                level += 1
        
        return output
    
    def levelOrder_2(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        output, level = [], [root]
        
        while level:
            output.append([node.val for node in level])

            children = []            
            for node in level:
                if node.children:
                    children.extend(node.children)
                   
            level = [child for child in children if child]
            
        return output

def create_n_ary_tree(length, numMin, numMax, maxChildren):
    root = TreeNode(random.randint(numMin, numMax))
    nodes = deque([root])
    nums = [root.val]

    i = 1
    while i < length:
        try:
            cur = nodes.popleft()
        except:
            return (root, nums)
        
        childCount = random.randint(0, maxChildren)
        children = []
        
        while len(children) < childCount:
            child = TreeNode(random.randint(numMin, numMax))
            children.append(child)
            nodes.append(child)
            nums.append(child.val)

        cur.children = children
        i += childCount

    return (root, nums)
    

def flatten(t):
    return [item for sublist in t for item in sublist]

def generate_test(sol):
    (tree, nums) = create_n_ary_tree(1000, 0, 1000, 8)

    if flatten(sol.levelOrder(tree)) != nums:
        print('error')
    
sol = Solution()
for i in range(1000):    
    generate_test(sol)
