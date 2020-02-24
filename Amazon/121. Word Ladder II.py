from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        word_to_dis = {}
        self.bfs(end, word_to_dis, dict)
        
        print(word_to_dis)
        result = []
        self.dfs(start, end, dict, word_to_dis, [start], result)
        return result
        
    def bfs(self, start, word_to_dis, dict):
        queue = deque([start])
        word_to_dis[start] = 0
        
        while queue:
            curr = queue.popleft()
            for next_word in self.get_next_words(curr, dict):
                if next_word not in word_to_dis:
                    word_to_dis[next_word] = word_to_dis[curr] + 1 
                    queue.append(next_word)
                    
    def get_next_words(self, word, dict):
        result = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word != word and new_word in dict:
                    result.append(new_word)
        return result
        
    def dfs(self, curr, target, dict, word_to_dis, path, result):
        if curr == target:
            result.append(path[:])
            return
        
        for next_word in self.get_next_words(curr, dict):
            if word_to_dis[next_word] != word_to_dis[curr] - 1:
                continue
            path.append(next_word)
            self.dfs(next_word, target, dict, word_to_dis, path, result)
            path.pop()
        
        
        
        
        
        
