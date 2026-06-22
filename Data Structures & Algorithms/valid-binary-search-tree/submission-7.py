# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, l, h):
            if node is None: return True
            if not l < node.val < h:
                return False
            return dfs(node.left, l, node.val) and dfs(node.right, node.val, h)

        return dfs(root, -2000, 2000)
            
