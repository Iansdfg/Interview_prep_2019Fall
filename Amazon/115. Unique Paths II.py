class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if obstacleGrid == [] or obstacleGrid == [[]]:
            return 0
        if obstacleGrid[0][0]:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        dp[1][1] = 1
        for row in range(rows + 1):
            for col in range(cols + 1):
                if row == 1 and col == 1:
                    continue
                if obstacleGrid[row-1][col-1] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] =  dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]
