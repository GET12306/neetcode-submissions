class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        pro = 0
        for i in prices:
            if i > minBuy:
                pro = max(pro, i-minBuy)
            else:
                minBuy = i
        
        return pro