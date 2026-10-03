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
                depth = max(depth,b)
                s.append((a.left, b+1))
                s.append((a.right,b+1))
            
        return depth

                

