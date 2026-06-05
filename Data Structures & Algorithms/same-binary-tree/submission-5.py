# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def helper(nodeA, nodeB):
            if not nodeA and not nodeB:
                return
            if not nodeA or not nodeB:
                self.res = False
                return
            if nodeA.val != nodeB.val:
                self.res = False
                return
            helper(nodeA.left, nodeB.left)
            helper(nodeA.right, nodeB.right)
        helper(p, q)
        return self.res