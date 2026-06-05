# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(node):
            if p.val > node.val and q.val > node.val:
                return helper(node.right)
            elif p.val < node.val and q.val < node.val:
                return helper(node.left)
            else:
                return node
        return helper(root)
        
        
            
            