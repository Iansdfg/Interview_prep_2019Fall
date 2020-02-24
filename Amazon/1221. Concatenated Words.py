class Solution:
    """
    @param words: List[str]
    @return: return List[str]
    """
    def findAllConcatenatedWordsInADict(self, words):
        # write your code here
        words.sort(key = lambda x: -len(x))
        cands = set(words)
        ans = []
        for i in range(0, len(words)):
            cands -= {words[i]}
            if self.wordBreak(words[i], cands):
                if words[i] == '':
                    continue
                ans.append(words[i]) 
        return ans

    def wordBreak(self, s, dict):
        # write your code here
        dict_set = set(dict)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 
        for i in range(n + 1):
            for j in range(i + 1):
                if not dp[j]:
                    continue
                if s[j:i] in dict:
                    dp[i] = 1 
                    break 
        return bool(dp[-1])
