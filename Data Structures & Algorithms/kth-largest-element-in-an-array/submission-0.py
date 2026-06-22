class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mnums = [-x for x in nums]
        heapq.heapify(mnums)

        for i in range(k):
            res = -heapq.heappop(mnums)

        return res