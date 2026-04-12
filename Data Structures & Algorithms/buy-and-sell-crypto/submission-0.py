class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buying_price = prices[0]
        for price in prices:
            if price > buying_price:
                maxProfit = max(maxProfit, price - buying_price)
            else:
                buying_price = price
        return maxProfit