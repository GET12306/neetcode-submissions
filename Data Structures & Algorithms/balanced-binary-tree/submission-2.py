# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        lh, rh = self.calh(root.left), self.calh(root.right)
        return abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def calh(self, node):
        if node is None: return 0
        return 1+max(self.calh(node.left), self.calh(node.right))