from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dic = [[1,0],[-1,0],[0,1],[0,-1]]

        visit = set()
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
                
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dic:
                    nr, nc = r+dr, c+dc
                    if min(nr,nc)<0 or nr==rows or nc==cols or (nr, nc) in visit or grid[nr][nc]==-1:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            dist += 1
        