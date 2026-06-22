# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pl = self.t2l(p)
        ql = self.t2l(q)

        if pl == ql:
            return True
        else:
            return False
    
    def t2l(self, root):
        stack = [root]
        tree = []
        while stack:
            node = stack.pop()
            if node:
                tree.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                tree.append(None)

        return tree
        
        