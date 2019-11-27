class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        if not s or len(s) == 0:
            return 0
            
        
        char_to_cnt = dict()
        left = 0
        max_frquency = 0
        ans = 0
        for right in range(len(s)):
            char = s[right]
            char_to_cnt[char] = char_to_cnt.get(char,0)+1
            max_frquency = max(max_frquency, char_to_cnt[char])
            
            delta = right - left + 1 - max_frquency
            
            if delta > k:
                char_to_cnt[s[left]] -= 1
                left += 1
            else:
                ans = max(ans, right - left + 1)
                
        return ans
            
