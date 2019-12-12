
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_max = []
        curr_max = height[0]
        for val in height:
            curr_max = max(curr_max, val)
            left_max.append(curr_max)
            
        right_max = []
        curr_max = height[-1]
        for val in height[::-1]:
            curr_max = max(curr_max, val)
            right_max.append(curr_max)
        right_max = right_max[::-1]
        
        water = 0
        for pos in range(len(height)):
            water += (min(right_max[pos], left_max[pos]) - height[pos])
            
        return water
            
        
        

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if heights == []:
            return 0
        left, right = 0, len(heights)-1
        left_max, right_max = heights[left], heights[right]
        water = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
                right -= 1
        return water
