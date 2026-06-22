# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bound = [float('-inf'), float('inf')]

        def dfs(node, lb, rb):
            if node is None: return True

            if node.val <= lb or node.val >= rb:
                return False
            
            return dfs(node.left, lb, node.val) and dfs(node.right, node.val, rb)

        return dfs(root, bound[0], bound[1])