class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses

        adj = [[] for i in range(numCourses)]

        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        finish = 0
        res = []
        q = deque()

        for i, degree in enumerate(indegree):
            if degree == 0:
                q.append(i)
    
        while q:
            c = q.popleft()
            res.append(c)
            finish += 1
            for c_ad in adj[c]:
                indegree[c_ad] -= 1
                if indegree[c_ad] == 0:
                    q.append(c_ad)

        
        return res if finish==numCourses else []