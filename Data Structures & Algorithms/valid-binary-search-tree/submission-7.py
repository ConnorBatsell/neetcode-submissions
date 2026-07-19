# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def dfs(node,l,r):
            if not node:
                return
            if l < node.val < r:
                dfs(node.left, l, node.val)
                dfs(node.right, node.val, r)
            else:
                self.valid = False
                return
        dfs(root, float("-inf"), float("inf"))
        return self.valid
        
            