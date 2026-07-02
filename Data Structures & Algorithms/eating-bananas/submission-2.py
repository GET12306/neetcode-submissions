class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        if h==len(piles): return r
        
        res = r
        while l <= r:
            m = l + (r-l) // 2
            cur = self.calt(piles, m)
            if cur > h:
                l = m+1
            elif cur <= h:
                res = m
                r = m-1
        return res
        


    def calt(self, piles, speed) -> int:
        time: int = 0
        for p in piles:
            if p%speed != 0:
                time += int(p / speed) + 1
            else:
                time += int(p / speed)
        return time