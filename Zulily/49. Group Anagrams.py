class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        code_to_group = {}
        for str in strs:
            code = self.get_code(str)
            if code in code_to_group:
                code_to_group[code].append(str)
            else:
                code_to_group[code] = [str]
        res = []
        for key in code_to_group:
            res.append(code_to_group[key])
        return res
            
    def get_code(self, str):
        code = [0]*26
        for char in str:
            code[ord(char) - ord('a')] += 1
        return tuple(code)
