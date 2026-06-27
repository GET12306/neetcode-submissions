class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)==0: return True
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        
        q = deque()
        q.append([0,-1])

        while q:
            node, par = q.popleft()
            visit.add(node)
            for nei in adj[node]:
                if nei==par: continue
                if nei in visit: return False
                visit.add(nei)
                q.append([nei, node])
        
        return len(visit)==n