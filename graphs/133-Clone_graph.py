"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldToNew = {}

        def dfsClone(node):
            if node in oldToNew:
                return oldToNew[node]

            cp = Node(node.val)
            oldToNew[node] = cp
            for neighbor in node.neighbors:
                cp.neighbors.append(dfsClone(neighbor))
            return cp
        
        return dfsClone(node)

'''
time O(n)  n=vertices + edges
space O(n)   n=vertices + edges
'''