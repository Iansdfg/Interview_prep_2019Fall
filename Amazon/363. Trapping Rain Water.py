class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        
        left_max = []
        curr_max = float('-inf')
        for height in heights:
            curr_max = max(curr_max, height)
            left_max.append(curr_max)
            
        right_max = []
        curr_max = float('-inf')
        for height in heights[::-1]:
            curr_max = max(curr_max, height)
            right_max.append(curr_max)
        right_max = right_max[::-1]
        
        
        water = 0
        for pos in range(len(heights)):
            water += (min(left_max[pos], right_max[pos]) - heights[pos])
            
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
