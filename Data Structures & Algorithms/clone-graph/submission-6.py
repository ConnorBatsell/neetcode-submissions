"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        temp = {}
        
        def dfs(n):
            if n in temp:
                return temp[n]
            if not n:
                return None
            temp[n] = Node(n.val)
            for node in n.neighbors:
                temp[n].neighbors.append(dfs(node))
            return temp[n]
        return dfs(node)
        
            


