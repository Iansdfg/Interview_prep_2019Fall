class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        return self.helper(prices, k)
    
    def helper(self, prices, k):
        if not prices: return 0
        N = len(prices)
        g = [[0] * (k+1) for _ in range(N)]
        l = [[0] * (k+1) for _ in range(N)]
        for i in range(1, N):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k+1):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
        return g[-1][-1]
