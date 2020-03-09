class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res
            
                
            
        
