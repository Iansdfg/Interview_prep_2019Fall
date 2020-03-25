class Solution(object):
    dig_to_char = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        results = []
        self.dfs(digits, 0, [], results)
        return results
    
    def dfs(self, digits, index, path, results):
        if len(path) == len(digits):
            results.append(''.join(path))
            return 
        for dig_pos in range(index, len(digits)):
            chars = self.dig_to_char[digits[dig_pos]]
            for char in chars:
                path.append(char)
                self.dfs(digits, dig_pos + 1, path, results)
                path.pop()
                
        
        
