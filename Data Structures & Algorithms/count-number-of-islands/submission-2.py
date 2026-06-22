class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dic = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        isd = 0
        nr, nc = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c)<0 or r==nr or c==nc or grid[r][c]=='0':
                return
            grid[r][c]='0'
            for dr, dc in dic:
                dfs(r+dr, c+dc)

        for i in range(nr):
            for j in range(nc):
                if grid[i][j]=='1':
                    dfs(i, j)
                    isd+=1
        return isd
