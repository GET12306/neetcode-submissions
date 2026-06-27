class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def bfs(node, par):
            q = deque()
            q.append((node, par))
            while q:
                node, par = q.popleft()
                nonlocal visit
                visit.add(node)
                for nei in adj[node]:
                    if nei==par or nei in visit: continue
                    visit.add(nei)
                    q.append((nei, node))
        res = 0
        for i in range(n):
            if i not in visit:
                bfs(i, -1)
                res += 1
        return res

        