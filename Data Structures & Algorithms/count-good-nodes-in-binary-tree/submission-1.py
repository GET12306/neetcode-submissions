# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, -200))

        while q:
            node, mval = q.popleft()
            if node.val >= mval:
                res += 1
                mval = node.val
            if node.left:
                q.append((node.left, mval))
            if node.right:
                q.append((node.right, mval))

        return res