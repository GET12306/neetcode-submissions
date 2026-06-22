class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        
        distant = [[-(x**2 + y**2), i] for i, (x, y) in enumerate(points)]  # [[dis, i]]

        kheap = []  # [[dis, i]]
        r = 0
        while r < len(points):
            while r < k:
                heapq.heappush(kheap, distant[r])
                r += 1
            if -distant[r][0] < -kheap[0][0]:
                heapq.heappop(kheap)
                heapq.heappush(kheap, distant[r])
            r += 1
            

        res = []
        for _, i in kheap:
            res.append(points[i])
        return res
        
        