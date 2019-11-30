class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return len(s) == 0
            
        n = len(s)
        dp = [1] + [0] * n
        
        max_len = max([len(word) for word in dict])
        
        for i in range(1, n+1):
            for j in range(1, min(i, max_len) + 1):
                if not dp[i - j]:
                    continue
                if s[i - j:i] in dict:
                    dp[i] = 1
                    break
                
        return bool(dp[-1])
                    
