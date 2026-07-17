# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        size = 0
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                a = q.popleft()
                if a:
                    level.append(a.val)
                    q.append(a.left)
                    q.append(a.right)
            if level:
                res.append(level)
        return res


