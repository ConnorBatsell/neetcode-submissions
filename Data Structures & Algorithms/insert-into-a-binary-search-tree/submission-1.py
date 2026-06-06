# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            temp = curr
            if val > curr.val:
                curr = curr.right
                if not curr:
                    temp.right = TreeNode(val)
            else:
                curr = curr.left
                if not curr:
                    temp.left = TreeNode(val)
        return root
            

