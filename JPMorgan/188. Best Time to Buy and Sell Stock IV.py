class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if k >= len(prices):
            return self.helper1(prices)
        return self.helper(prices, k)
    
    def helper1(self, prices):
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
            max_profit += (peak - valley)
        return max_profit 
    
    def helper(self, prices, k):
        N = len(prices)
        g = [[0] * (k+1) for _ in range(N)]
        l = [[0] * (k+1) for _ in range(N)]
        for i in range(1, N):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k+1):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
        return g[-1][-1]

 
