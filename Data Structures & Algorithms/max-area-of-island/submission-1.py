class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dic = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r, c))
            
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        area = 0

        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i, j))


        return area