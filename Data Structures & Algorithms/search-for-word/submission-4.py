class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)

        def dfs(r, c, dep, visit: set):
            if dep == n:
                return True

            if min(r,c)<0 or r==rows or c==cols or (r,c) in visit or board[r][c] != word[dep]:
                return False
                    
            visit.add((r,c))
            res = dfs(r+1, c,dep+1, visit) or dfs(r-1, c,dep+1, visit) or dfs(r, c+1,dep+1, visit) or dfs(r, c-1,dep+1, visit)

            visit.remove((r,c))

            return res

        
        for i in range(rows):
             for j in range(cols):
                if dfs(i, j, 0, set()):
                    return True
        
        return False
            