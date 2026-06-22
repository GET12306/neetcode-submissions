class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()

        def addcell(r, c):  # 增加陆地
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == -1:
                return
            
            visit.add((r, c))
            q.append((r, c))

        for r in range(rows):  # 增加宝物
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        dist = 0  # distance
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r+1, c)
                addcell(r-1, c)
                addcell(r, c+1)
                addcell(r, c-1)
            dist += 1