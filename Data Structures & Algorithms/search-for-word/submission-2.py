class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols=len(board), len(board[0])

        def dfs(r, c, visit, dep):
            if (r,c) in visit or min(r,c)<0 or r==rows or c==cols:
                return False
            if board[r][c] != word[dep]:
                return False
            if dep+1==len(word):
                return True
            
            visit.add((r,c))
            
            res =  dfs(r+1, c, visit, dep+1) or \
            dfs(r-1, c, visit, dep+1) or \
            dfs(r, c+1, visit, dep+1) or \
            dfs(r, c-1, visit, dep+1)

            visit.remove((r,c))

            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    visit = set()
                    if dfs(i, j, visit, 0):
                        return True
        return False