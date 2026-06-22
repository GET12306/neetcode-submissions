class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}

        for i, val in enumerate(nums):
            c[val] = 1 + c.get(val, 0)
        c = dict(sorted(c.items(), key= lambda x: x[1]))
        print(c)

        res = []
        for i in range(k):
            res.append(c.popitem()[0])
        
        return res
