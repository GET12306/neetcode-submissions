class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dic = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(x,y):
            q = deque()
            q.append((x,y))
            while q:
                r,c = q.popleft()
                grid[r][c] = '0'
                for dr,dc in dic:
                    nr,nc = r+dr, c+dc
                    if min(nr,nc)<0 or nr==rows or nc==cols or grid[nr][nc]=='0':
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = '0'
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    res += 1
                    bfs(i, j)
        return res