class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rstones = [-x for x in stones]
        heapq.heapify(rstones)

        while len(rstones) > 1:
            s1 = heapq.heappop(rstones) * -1
            s2 = heapq.heappop(rstones) * -1
            s = abs(s1-s2)
            if s > 0:
                heapq.heappush(rstones, -s)
        return 0 if len(rstones)==0 else rstones[0]*-1