class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if min(nr, nc) < 0 or nr==rows or nc==cols or grid[nr][nc]=='0':
                        continue
                    grid[nr][nc]='0'
                    q.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    bfs(i, j)
                    islands += 1
        return islands
                    
                    
            