class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def bfs(node):
            q = deque()
            visit.add(node)
            q.append(node)

            while q:
                no = q.popleft()
                for nei in adj[no]:
                    if nei in visit:
                        continue
                    q.append(nei)
                    visit.add(nei)


        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                bfs(i)

        return res