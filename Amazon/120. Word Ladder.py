from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = deque([start])
        distance = {start: 1}
        
        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
                
            for next_word in self.get_next_words(word, dict):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1
                
        return 0
                
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in dict and new_word != word:
                    words.append(new_word)
        return words
                
                
        
