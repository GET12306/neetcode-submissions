class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def bfs(node):
            q = deque()
            q.append(node)
            visit.add(node)

            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in visit:
                        continue
                    q.append(nei)
                    visit.add(nei)

        
        res = 0
        for i in range(n):
            if i in visit:
                continue
            bfs(i)
            res += 1

        return res