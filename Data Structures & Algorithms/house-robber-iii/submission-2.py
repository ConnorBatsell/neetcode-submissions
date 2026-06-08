# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return (0,0)
            L = helper(node.left)
            R = helper(node.right)

            rob = node.val + L[1] + R[1]
            skip = max(L[0], L[1]) + max(R[0], R[1])

            return (rob, skip)
        return max(helper(root))
            