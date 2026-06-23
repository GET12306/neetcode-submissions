class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for i, j, k in triplets:
            if i>target[0] or j>target[1] or k>target[2]:
                continue
            if i==target[0]:
                good.add(0)
            if j==target[1]:
                good.add(1)
            if k==target[2]:
                good.add(2)

        
        return len(good) == 3