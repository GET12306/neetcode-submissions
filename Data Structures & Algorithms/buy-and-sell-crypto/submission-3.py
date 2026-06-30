class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mbuy = prices[0]
        maxp = 0

        for price in prices:
            if price <= mbuy:
                mbuy = price
            maxp = max(maxp, price-mbuy)
        return maxp
