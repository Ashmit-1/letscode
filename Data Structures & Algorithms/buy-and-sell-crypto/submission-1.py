class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = float('inf')
        profit = 0
        for i in prices:
            buyingPrice = min(buyingPrice, i)
            profit = max(i - buyingPrice, profit)
        return profit

        