
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        # 
        res = '' 
        for char in paragraph:
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or char == ' ':
                res += char.lower()
        arr = res.split()
        word_dic = dict()
        for word in arr:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
                
        max_word = ''
        max_time = 0
        
        for key in word_dic:
            if key not in banned:
                time = word_dic[key]
                max_time = max(time, max_time)
                if time == max_time:
                    max_word = key
                    
        return max_word
            
