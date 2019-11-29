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
