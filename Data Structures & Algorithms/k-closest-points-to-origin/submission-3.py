class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i, [x, y] in enumerate(points):
            dist.append([x**2+y**2, i])
        
        heapq.heapify(dist)

        res = []
        for i in range(k):
            dis, index = heapq.heappop(dist)
            res.append(points[index])
        return res