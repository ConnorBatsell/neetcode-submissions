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
        res = {}
        stack = [[1,root]]
        while stack:
            depth,node = stack.pop()
            if node:
                if depth not in res:
                    res[depth]= []
                res[depth].append(node.val)
                stack.append([depth+1, node.right])
                stack.append([depth+1, node.left])
        out = []
        for key in res:
            out.append(res[key][len(res[key])-1])
        return out