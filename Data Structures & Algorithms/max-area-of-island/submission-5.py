class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if min(r,c)<0 or r==rows or c==cols or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            
            return 1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)

        maxa = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxa = max(maxa, dfs(i,j))
        
        return maxa