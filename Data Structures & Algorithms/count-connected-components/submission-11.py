class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = 0

        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei in visit:
                    continue
                dfs(nei)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res