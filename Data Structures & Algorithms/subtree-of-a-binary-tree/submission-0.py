# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def helper(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False
            if nodeA.val != nodeB.val:
                return False
            return helper(nodeA.left, nodeB.left) and helper(nodeA.right, nodeB.right)
        
        def dfs(node):
            if not node:
                return
            if helper(node, subRoot):
                self.res = True
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res