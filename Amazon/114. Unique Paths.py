class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == 0 or n == 0:
            return 0
        dp = [[ 0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[1][1] = 1
        print(dp)
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if row == 1 and col == 1:
                    continue
                dp[row][col] = dp[row-1][col] + dp[row][col-1] 
        return dp[-1][-1]
                
                
        
