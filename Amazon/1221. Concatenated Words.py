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
                ans.append(words[i]) 
        return ans

    def wordBreak(self, word, cands):
        if not cands:
            return False
        dp = [False] * (len(word) + 1) #store whether w.substr(0, i) can be formed by existing words
        dp[0] = True #empty string is always valid
        for i in range(1, len(word) + 1):
            for j in reversed(range(0, i)):
                if not dp[j]:
                    continue
                if word[j:i] in cands:
                    dp[i] = True
                    break
        return dp[-1]
 
