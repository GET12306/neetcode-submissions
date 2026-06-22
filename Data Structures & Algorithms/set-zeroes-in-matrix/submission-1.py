class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row0, col0 = [False] * rows, [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row0[r], col0[c] = True, True
        
        for r in range(rows):
            for c in range(cols):
                if row0[r] or col0[c]:
                    matrix[r][c] = 0

        