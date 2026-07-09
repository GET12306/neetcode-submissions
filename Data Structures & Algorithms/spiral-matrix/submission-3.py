class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, cols - 1
        top, bottom = 0, rows - 1

        res = []

        while left <= right and top <= bottom:
            # 从左向右遍历上边界
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 从上向下遍历右边界
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 可能已经没有剩余行或列
            if left > right or top > bottom:
                break

            # 从右向左遍历下边界
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1

            # 从下向上遍历左边界
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res