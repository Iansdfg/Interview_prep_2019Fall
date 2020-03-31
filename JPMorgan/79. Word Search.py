class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, word, 0, row, col, visited):
                    return True 
        return False
        
    def dfs(self, board, word, index, x, y, visited):
        # return existx
        if index >= len(word):
            return True 
        
        if not self.is_valid(board, word, index, x, y, visited):
            return False 
        
        visited[x][y] = 1
        res = self.dfs(board, word, index + 1, x + 1, y, visited) or\
              self.dfs(board, word, index + 1, x, y + 1, visited) or\
              self.dfs(board, word, index + 1, x - 1, y, visited) or\
              self.dfs(board, word, index + 1, x, y - 1, visited) 
        visited[x][y] = 0
        
        return res 
    
    
    def is_valid(self, board, word, index, x, y, visited):
        rows, cols = len(board), len(board[0])
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if visited[x][y]:
            return False 
        if board[x][y] != word[index]:
            return False 
        return True 
        

        
