class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = float('inf')
        profit = 0
        for i in prices:
            if i < buyingPrice:
                buyingPrice = i
            if i - buyingPrice > profit:
                profit = i - buyingPrice
        return profit

        