class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        def bfs(s, d):
            if d in adj[s]: return True
            visit = set()
            q = deque([s])
            while q:
                course = q.popleft()
                visit.add(course)
                for qc in adj[course]:
                    if qc in visit:
                        continue
                    elif qc != d:
                        q.append(qc)
                    else:
                        return True
            return False

        res = []
        for u, v in queries:
            ures = bfs(u, v)
            res.append(ures)

        return res

