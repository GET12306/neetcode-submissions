class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= len(edges): return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                dfs(nei, node)
            return True
        
        return dfs(0, -1) and len(visit)==n
        