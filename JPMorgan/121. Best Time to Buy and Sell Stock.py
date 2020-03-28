class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = float('inf')
        max_profit = 0
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)
        return max_profit
            
        
