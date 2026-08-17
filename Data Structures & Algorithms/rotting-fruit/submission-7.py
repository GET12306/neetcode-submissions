class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direction = [[1,0],[-1,0],[0,-1],[0,1]]
        fresh = 0

        rot_q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rot_q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        res = 0

        while rot_q and fresh != 0:
            for _ in range(len(rot_q)):
                r, c = rot_q.popleft()
                for dr, dc in direction:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc)<0 or nr==rows or nc==cols or grid[nr][nc]==0 or grid[nr][nc] == 2:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    rot_q.append((nr, nc))
            res += 1
        
        return res if fresh==0 else -1
        
