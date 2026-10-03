# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        s = deque()
        s.append((root,1))
        while s:
            a,b = s.popleft()
            if a:
                if a.left:
                    s.append((a.left, b+1))
                if a.right:
                    s.append((a.right,b+1))
            depth = max(depth,b)
        return depth

                

