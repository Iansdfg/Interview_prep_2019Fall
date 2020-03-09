class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        char_to_count = {}
        for char in s:
            if char in char_to_count:
                char_to_count[char] += 1 
            else:
                char_to_count[char] = 1 
                
        for char in t:
            if char in char_to_count:
                char_to_count[char] -= 1 
            else:
                return False 
        for key in char_to_count:
            if char_to_count[key] != 0:
                return False 
        return True
