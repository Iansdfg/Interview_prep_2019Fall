class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        curr, prev, summ = prices[0], prices[0], 0
        for price in prices:
            prev = curr
            curr = price
            if curr > prev:
                summ += curr - prev
        return summ
            
        
