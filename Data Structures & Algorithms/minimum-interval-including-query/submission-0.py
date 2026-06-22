class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)

        for i in range(len(queries)):
            minl = 0
            for se in intervals:
                if se[0] >queries[i] or se[1] < queries[i]:
                    continue
                if minl == 0:
                    minl = se[1]-se[0]+1
                else:
                    minl = min(minl, se[1]-se[0]+1)
            res[i] = minl if minl>0 else -1
        return res
            