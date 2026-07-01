class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        marea = 0
        dic = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            area = 1
            while q:
                r, c = q.popleft()
                grid[r][c] = 0
                for dr,dc in dic:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc)<0 or nr==rows or nc==cols or grid[nr][nc]==0:
                        continue
                    q.append((nr, nc))
                    area += 1
                    grid[nr][nc]=0
        
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    cur = bfs(i,j)
                    marea = max(marea, cur)
        return marea