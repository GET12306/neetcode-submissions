class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegree = [0] * (n+1)
        indegree = [0] * (n+1)
        for src, dst in trust:
            indegree[dst] += 1
            outdegree[src] += 1
        res = -1
        for i in range(1, n+1):
            if indegree[i] == n-1:
                if outdegree[i] == 0:
                    res = i
                    return res
        return res