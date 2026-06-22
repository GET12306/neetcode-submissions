class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxarea = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nc < 0 or nr < 0 or nc >= COLS or nr >= ROWS or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    maxarea = max(area, maxarea)
            
        return maxarea