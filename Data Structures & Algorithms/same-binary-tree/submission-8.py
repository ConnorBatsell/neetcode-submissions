# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p,q]]
        while stack:
            a,b = stack.pop()
            if a and b:
                if not a.val==b.val:
                    return False
                stack.append([a.left, b.left])
                stack.append([a.right, b.right])
            if (not a and b) or (not b and a):
                return False
        return True
            