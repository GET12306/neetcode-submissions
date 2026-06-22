class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r-l)//2
            cur_time = self.cal_time(piles, m)
            if cur_time > h:
                l = m + 1
            elif cur_time <= h:
                res = m
                r = m-1
        return res


    def cal_time(self, piles, speed):
        time = 0
        for i in piles:
            if i % speed == 0:
                time += i // speed
            else:
                time += (i // speed ) + 1
        return time