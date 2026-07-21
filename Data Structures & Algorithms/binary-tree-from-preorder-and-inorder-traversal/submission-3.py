# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        cache = defaultdict(int)
        for i,val in enumerate(inorder):
            cache[val] = i
        self.indx = 0
        def dfs(l,r):
            if l>r:
                return None
            rootVal = preorder[self.indx]
            self.indx +=1
            root = TreeNode(rootVal)
            mid = cache[rootVal]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0, len(inorder)-1)


        
            