class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i = 0
        max_profit = 0
        valley, peak = prices[0], prices[0]
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1 
            valley = prices[i]
            
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            print(valley, peak)
            max_profit += (peak - valley)
        return max_profit 
            
            
            
            
            

            
        
