class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key in count.keys():
            count[key] *= -1
        
        minh = []

        for key in count.keys():
            heapq.heappush(minh, (count[key], key))
        
        res = []
        for i in range(k):
            _, key = heapq.heappop(minh)
            res.append(key)
        return res
        
        
        