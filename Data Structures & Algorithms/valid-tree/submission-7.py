class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= len(edges): return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        q.append((0,-1))
        visit = set()

        while q:
            node, par = q.popleft()
            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if nei in visit:
                    return False
                q.append((nei, node))
        
        return len(visit)==n

        