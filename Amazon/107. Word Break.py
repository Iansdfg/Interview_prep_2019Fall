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
        
        length = len(s)
        dp = [False] * (length+1)
        dp[0] = True
        
        max_len = max([len(word) for word in dict])
        
        
        for i in range(1, length+1):
            for j in range(1, min(i, max_len)+1):
                if not dp[i-j]:
                    continue
                if s[i-j:i] in dict:
                    dp[i] = True 
                    break 
                
        return dp[-1]
                
            
