class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direction = [[1,0],[-1,0],[0,-1],[0,1]]
        rotq = deque()
        
        fresh = 0
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotq.append((i,j))
        
        while rotq and fresh>0:
            for _ in range(len(rotq)):
                r, c = rotq.popleft()
                for dr, dc in direction:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc)<0 or nr==rows or nc==cols or grid[nr][nc]==0 or grid[nr][nc]==2:
                        continue
                    grid[nr][nc] = 2
                    rotq.append((nr, nc))
                    fresh -= 1
            time += 1
            
        if fresh != 0:
            return -1
        return time