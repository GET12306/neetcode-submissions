class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        dic = [[1,0],[-1,0],[0,1],[0,-1]]

        rotq = deque()
        visit = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotq.append((i, j))
                    visit.add((i,j))

        time = 0
        while rotq and fresh!=0:
            for _ in range(len(rotq)):
                r, c = rotq.popleft()
                for dr, dc in dic:
                    nr, nc = r+dr, c+dc
                    if (nr,nc) in visit or min(nr, nc)<0 or nr==rows or nc==cols or grid[nr][nc]==0:
                        continue
                    rotq.append((nr, nc))
                    grid[nr][nc] = 2
                    visit.add((nr,nc))
                    fresh -= 1
            time += 1
        if fresh != 0:
            return -1
        return time
