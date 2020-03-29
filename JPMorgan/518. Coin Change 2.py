class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount+1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        return dp[-1]
                
                

                
