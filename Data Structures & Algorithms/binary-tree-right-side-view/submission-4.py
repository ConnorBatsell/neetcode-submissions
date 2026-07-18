# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            rightMost = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightMost = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightMost:
                res.append(rightMost)
        return res
        
            


            