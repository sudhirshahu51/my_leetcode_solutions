#problem link https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf') #buying price of stock.
        diff = 0
        for price in prices:
            if price < buy_price: # Finding the min buy_price.
                buy_price = price
            if price - buy_price > diff: #trying to find max diff of buy_price with price of anyday.
                diff = price - buy_price
        return diff