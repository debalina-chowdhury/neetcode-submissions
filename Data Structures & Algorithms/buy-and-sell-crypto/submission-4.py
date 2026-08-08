class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for p in prices:
            min_price = min(min_price, p)      # cheapest buy day up to here
            profit = max(profit, p - min_price)  # best sell if we sell today
        return profit