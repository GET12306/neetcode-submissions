class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        poss = []

        def dfs(openn, closen):
            if openn == closen == n:
                res.append(''.join(poss))
                return

            if openn < n:
                poss.append('(')
                dfs(openn+1, closen)
                poss.pop()
            if closen < openn:
                poss.append(')')
                dfs(openn, closen+1)
                poss.pop()


        dfs(0, 0)

        return res