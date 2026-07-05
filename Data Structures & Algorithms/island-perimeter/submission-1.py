class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dic = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()

        def bfs(r, c):
            adj = 0
            for dr,dc in dic:
                nr, nc = r+dr, c+dc
                if min(nr,nc)<0 or nr==rows or nc==cols or grid[nr][nc]==0:
                    continue
                adj += 1
            return adj



        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    res += 4 - bfs(i,j)
        return res
        