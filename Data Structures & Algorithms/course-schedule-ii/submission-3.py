class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        res = []
        finish = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        while q:
            c = q.popleft()
            res.append(c)
            finish += 1
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if finish==numCourses else []