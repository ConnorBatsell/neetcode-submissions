# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def helper(node, a, b):
            if not node:
                return
            if a < node.val < b:
                helper(node.left, a, node.val)
                helper(node.right, node.val, b)
            else:
                self.valid = False
                return
        helper(root, -10000000, 10000000)
        return self.valid
            