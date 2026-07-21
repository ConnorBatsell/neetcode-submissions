# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.out = float("-inf")
        def dfs(node):
            if not node:
                return 0
            l = max(dfs(node.left),0)
            r = max(dfs(node.right),0)
            self.out = max(self.out, l+node.val+r)
            return node.val + max(l,r)
        dfs(root)
        return self.out
            
            