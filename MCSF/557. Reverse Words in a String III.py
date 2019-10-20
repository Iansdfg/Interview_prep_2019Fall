class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        new_word = []
        s = s + ' '
        for char in s:
            if char != ' ':
                new_word.append(char)
            else:
                ans.append(''.join(new_word[::-1]))
                new_word = []
        return ' '.join(ans)
           
