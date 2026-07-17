# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(a,b):
            if not a and not b:
                return True
            if (not a and b) or (not b and a) or (a.val!=b.val):
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)
        s = [root]
        while s:
            a = s.pop()
            if a:
                s.append(a.left)
                s.append(a.right)
                if dfs(a, subRoot):
                    return True
        return False
            