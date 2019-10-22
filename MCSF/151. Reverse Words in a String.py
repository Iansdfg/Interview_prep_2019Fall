class Solution:
    def reverseWords(self, s: str) -> str:
        s = s+' '
        ans = []
        new_word = []
        for char in s:
            if char != ' ':
                new_word.append(char)
            else:
                if new_word == []:
                    continue
                ans.append(''.join(new_word))
                new_word = []
        ans = ' '.join(ans[::-1])
        return ans
        
        
