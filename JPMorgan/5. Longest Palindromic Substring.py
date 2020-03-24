class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        res = ''
        for i in range(1, len(s)):
            curr = self.find_Palindrome(s, i, i)
            if len(curr) > len(res):
                res = curr
            curr = self.find_Palindrome(s, i-1, i)
            if len(curr) > len(res):
                res = curr
        return res
        
    def find_Palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
        
