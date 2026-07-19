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
        stack = deque([root])
        res = []
        while stack:
            farthest = None
            for _ in range(len(stack)):
                node = stack.popleft()
                if node:
                    farthest = node.val
                    stack.append(node.left)
                    stack.append(node.right)
            if farthest:
                res.append(farthest)

        return res
            


            