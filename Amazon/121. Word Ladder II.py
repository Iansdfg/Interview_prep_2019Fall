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
        distance = {}
        self.bfs(end, distance, dict)
        print(distance)
        result = []
        self.dfs(start, end, distance, dict, [start], result)
        
        return result
        
    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_word(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
                    
    def get_next_word(self, word, dict):
        words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i]+char+word[i+1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
                
                
    def dfs(self, curt, target, distance, dict, path, result):
        if curt == target:
            result.append(path[:])
            return
        
        for word in self.get_next_word(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, result)
            path.pop()
        
   
