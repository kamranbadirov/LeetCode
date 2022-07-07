class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = 0
        sell = prices[0]
        for price in prices:
            buy = max(buy, price - sell)
            sell = min(sell, price)
        return buy


