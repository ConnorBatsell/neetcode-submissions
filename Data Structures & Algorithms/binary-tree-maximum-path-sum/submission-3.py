# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res= root.val
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            lMax = max(l,0)
            rMax = max(r,0)
            self.res = max(self.res, lMax + node.val + rMax)
            return node.val + max(lMax, rMax)
        helper(root)
        return self.res