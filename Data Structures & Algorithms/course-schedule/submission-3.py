class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        while q:
            c = q.popleft()
            finish += 1
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

    
        
        return finish==numCourses
            
            