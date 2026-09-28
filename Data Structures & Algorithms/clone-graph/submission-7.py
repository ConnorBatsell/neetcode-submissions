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
            if not n:
                return None
            if n in temp:
                return temp[n]
            temp[n] = Node(n.val)
            for neighbor in n.neighbors:
                temp[n].neighbors.append(dfs(neighbor))
            return temp[n]
        return dfs(node)
        
            


