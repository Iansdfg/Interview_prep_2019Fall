
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left_max = []
        curr_max = height[0]
        for h in height:
            curr_max = max(h, curr_max)
            left_max.append(curr_max)
            
        right_max = []
        curr_max = height[-1]
        for h in reversed(height):
            curr_max = max(h, curr_max)
            right_max.append(curr_max)
        right_max.reverse()
        
        water = 0
        for pos in range(len(height)):
            water += min(left_max[pos], right_max[pos]) - height[pos]
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
