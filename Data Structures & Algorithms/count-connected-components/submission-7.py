class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node):
            nonlocal visit
            if node in visit: return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visit:
                res+=1
                dfs(i)
        return res