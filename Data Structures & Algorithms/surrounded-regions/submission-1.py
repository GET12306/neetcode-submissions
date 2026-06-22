class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def cap(r, c):
            if min(r, c) < 0 or r==rows or c==cols or board[r][c]!= 'O':
                return
            
            board[r][c] = 'T'
            cap(r + 1, c)
            cap(r - 1, c)
            cap(r, c + 1)
            cap(r, c - 1)

        for r in range(rows):
            if board[r][0] == 'O':
                cap(r, 0)
            if board[r][cols - 1] == "O":
                cap(r, cols-1)

        for c in range(cols):
            if board[0][c] == 'O':
                cap(0, c)
            if board[rows-1][c] == "O":
                cap(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"