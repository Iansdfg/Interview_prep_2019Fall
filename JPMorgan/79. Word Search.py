class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        n, m = len(board[0]), len(board)
        visited = [[0 for i in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.search(board, word, 0, i, j, visited): return True
        return False

    def search(self, board, word, depth, i, j, visited):
        if len(word) == depth:
            return True
        n, m = len(board[0]), len(board)
        if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or board[i][j] != word[depth]: return False
        visited[i][j] = 1
        res = self.search(board, word, depth + 1, i+1, j, visited) or \
              self.search(board, word, depth + 1, i-1, j, visited)or \
              self.search(board, word, depth + 1, i, j+1, visited)or \
              self.search(board, word, depth + 1, i, j-1, visited)
        visited[i][j] = 0
        return res