# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self.inorder(root)
        self.counter=0
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.vals.append(node.val)
        self.inorder(node.right)


    def next(self) -> int:
        self.counter+=1
        return self.vals[self.counter-1]

    def hasNext(self) -> bool:
        return self.counter<len(self.vals)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()