class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rnums = [-x for x in nums]
        heapq.heapify(rnums)
        for _ in range(k-1):
            heapq.heappop(rnums)
        return heapq.heappop(rnums) * -1