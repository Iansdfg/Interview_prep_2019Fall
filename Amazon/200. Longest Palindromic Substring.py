class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        max_sub = ''
        for i in range(len(s)):
            sub = self.find_sub(s, i, i)
            if len(sub) > len(max_sub):
                max_sub = sub
            sub = self.find_sub(s, i, i+1)
            if len(sub) > len(max_sub):
                max_sub = sub
        return max_sub
       
    def find_sub(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
            
            
            
