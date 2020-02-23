class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
        left_max =  []
        curr_max = heights[0]
        for height in heights:
            curr_max = max(curr_max, height)
            left_max.append(curr_max)
        # print(left_max)
        
        right_max =  []
        curr_max = heights[-1]
        for height in reversed(heights):
            curr_max = max(curr_max, height)
            right_max.append(curr_max)
        right_max.reverse()
        # print(right_max)
        
        water = 0
        for i in range(len(heights)):
            water += min(right_max[i], left_max[i]) - heights[i]
            
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
