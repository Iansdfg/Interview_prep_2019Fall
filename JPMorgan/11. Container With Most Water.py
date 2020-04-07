class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            val = (right - left) * min(height[left], height[right])
            res = max(val, res)
            
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
                
        return res
