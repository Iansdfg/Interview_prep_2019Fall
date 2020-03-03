class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        dp = [0 for _ in range(len(A))]
        dp[0] = 1
        
        for i in range(len(A)):
            if not dp[i]:
                continue
                
            steps = A[i]
            for step in range(1, steps+1):
                if i + step >= len(dp) or dp[i + step]:
                    continue
                dp[i + step] = 1 
                
        return bool(dp[-1]) 
