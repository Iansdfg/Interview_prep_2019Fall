class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here

        dp = [0 for _ in range(amount+1)]
        for i in range(1, amount+1):
            choice = []
            for coin in coins:
                if coin == 0:
                    continue
                if i - coin < 0:
                    choice.append(float('inf'))
                else:
                    choice.append(dp[i - coin] + 1)
            dp[i] = min(choice)
            # print(i, choice,dp)
        return -1 if dp[-1] == float('inf') else dp[-1]
            
