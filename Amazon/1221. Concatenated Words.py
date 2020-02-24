class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x:-len(x))
        word_set = set(words)
        res = []
        for i in range(len(words)):
            target = words[i]
            word_set.discard(target)
            # if target can be seperated with other two in word_set:
            if self.word_break(target, word_set):
                if target == '':
                    continue
                res.append(target)
        return res
    
    def word_break(self, word, words_set):
        length = len(word)
        dp = [0]*(length + 1)
        dp[0] = 1 
        
        for i in range(length + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if word[j:i] in words_set:
                    dp[i] = 1
                    break 
        return dp[-1]
        
