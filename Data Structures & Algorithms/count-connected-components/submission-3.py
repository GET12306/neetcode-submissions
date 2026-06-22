class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * n

        def dfs(node):
            if visit[node] is True:
                return
            visit[node] = True
            for nei in adj[node]:
                if nei==node:
                    continue
                dfs(nei)

        part = 0

        for i in range(n):
            if visit[i] is False:
                dfs(i)
                part += 1

        return part