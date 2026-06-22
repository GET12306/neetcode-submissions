# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        leftH = self.calH(root.left)
        leftR = self.calH(root.right)
        
        return max(leftH+leftR, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))


    def calH(self, root: Optional[TreeNode]):
        if root is None: return 0

        return 1 + max(self.calH(root.left), self.calH(root.right))
        
        