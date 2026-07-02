class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dic = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))

            while q:
                r, c = q.popleft()
                board[r][c] = 'T'
                for dr,dc in dic:
                    nr,nc=r+dr, c+dc
                    if min(nr,nc)<0 or nr==rows or nc==cols or board[nr][nc]=='X' or board[nr][nc]=='T':
                        continue
                    q.append((nr,nc))
        
        for i in range(rows):
            if board[i][0]=='O':
                bfs(i, 0)
            if board[i][cols-1]=='O':
                bfs(i, cols-1)
        for j in range(cols):
            if board[0][j]=='O':
                bfs(0, j)
            if board[rows-1][j]=='O':
                bfs(rows-1, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
        
