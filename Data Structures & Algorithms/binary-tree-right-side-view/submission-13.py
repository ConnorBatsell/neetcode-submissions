# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = deque()
        s.append(root)
        if not root:
            return []
        while s:
            right = None
            for i in range(len(s)):
                a = s.popleft()
                if a.left:
                    s.append(a.left)
                if a.right:
                    s.append(a.right)
                right = a
            if right:
                res.append(right.val)
        return res
                



            