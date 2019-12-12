class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        left_max = height[0]
        left_height = []
        for val in height:
            left_max = max(left_max, val)
            left_height.append(left_max)
            
        right_max = height[-1]
        right_height = []
        for val in height[::-1]:
            right_max = max(right_max, val)
            right_height.append(right_max)
            
        right_height = right_height[::-1]
        # print(left_height, right_height)
        water = 0
        for i in range(len(height)):
            water += min(left_height[i],right_height[i])-height[i]
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
