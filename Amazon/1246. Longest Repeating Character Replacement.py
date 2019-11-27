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
        ans = 1
        max_count = 0
        length = len(s)
        
        for right in range(length):
            end = s[right]
            char_to_cnt[end] = char_to_cnt.get(end, 0) + 1
            most_frequent = max(char_to_cnt[end], most_frequent)
            print(end, most_frequent)
            
            delta = right - left + 1 - most_frequent
            if delta > k:
                char_to_cnt[s[left]] -= 1
                left += 1
            else:
                ans = max(ans, right - left + 1)
        return ans

            
