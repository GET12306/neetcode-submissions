# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        lh = self.cd(root.left)
        rh = self.cd(root.right)
        if abs(lh-rh) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    
    def cd(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        return 1 + max(self.cd(root.left), self.cd(root.right))