class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) < 0 or nr==rows or nc==cols or grid[nr][nc]==0:
                        continue
                    area += 1
                    grid[nr][nc] = 0
                    q.append((nr, nc))

            return area

        maxarea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    maxarea = max(bfs(i,j), maxarea)
        
        return maxarea

                    
