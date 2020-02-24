"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from heapq import heappush, heappop

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        heap = []
        for point in points:
            dis = self.get_distance(point, origin)
            heappush(heap, (dis, point.x, point.y))
            
        res = []
        for i in range(k):
            dis, curr_x, curr_y = heappop(heap)
            res.append(Point(curr_x, curr_y))
        return res
        
    def get_distance(self, point, origin):
        return abs(point.x - origin.x)**2 + abs(point.y - origin.y)**2
        
