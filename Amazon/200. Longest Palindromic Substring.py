class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if len(s)<2:
            return s 
        max_palin = ''
        for i in range(len(s)):
            palin = self.find_pal(i, i, s)
            if len(palin) > len(max_palin):
                max_palin = palin
                
            palin = self.find_pal(i, i + 1, s)
            if len(palin) > len(max_palin):
                max_palin = palin
        return max_palin

    def find_pal(self, left, right, s):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]
