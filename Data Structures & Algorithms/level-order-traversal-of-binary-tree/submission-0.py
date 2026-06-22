# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None: return res
        stack = deque()
        stack.append(root)

        while stack:
            # node = stack.pop()
            ql = len(stack)
            levelL = []
            for i in range(ql):
                node = stack.popleft()
                levelL.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(levelL)
        
        return res
