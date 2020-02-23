from heapq import heappush, heappop
from collections import deque
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        word_to_tup = dict()
        for word in words:
            if word not in word_to_tup:
                word_to_tup[word] = (-1, word)
            else:
                time, word = word_to_tup[word]
                word_to_tup[word] = (time - 1, word)
                
        heap = []
        for key in word_to_tup:
            tup = word_to_tup[key]
            heappush(heap, tup)
        # print(heap)
            
        results = []   
        for _ in range(k):
            time, word = heappop(heap)
            results.append(word)
        return results
