class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        pro = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                cur_pro = prices[r] - prices[l]
                pro = max(pro, cur_pro)
            else:
                l = r
            r += 1
        return pro