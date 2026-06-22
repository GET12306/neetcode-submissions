class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()

        def addcell(r, c):
            if (r,c) in visit or min(r, c) < 0 or r==rows or c==cols or grid[r][c]==-1:
                return
            
            visit.add((r,c))
            q.append((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i, j))
                    visit.add((i,j))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r+1, c)
                addcell(r-1, c)
                addcell(r, c+1)
                addcell(r, c-1)
            dist += 1
