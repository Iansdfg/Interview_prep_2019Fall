class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        seen = set()
        char_to_pos = dict()
        for pos, char in enumerate(s):
            if char not in char_to_pos:
                char_to_pos[char] = pos

            if char not in seen:
                seen.add(char)
                res.add(pos)
            else:
                res.discard(char_to_pos[char])
            # print(pos,char, res)
        return -1 if len(res) == 0 else min(res)
                
                
            
