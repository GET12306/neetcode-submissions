class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dric = [[1,0],[-1,0],[0,1],[0,-1]]


        def bfs(r,c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in dric:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc)<0 or nr==rows or nc==cols or grid[nr][nc]=='0':
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'



        isd = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    bfs(i, j)
                    isd += 1
        return isd
        