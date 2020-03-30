class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left_maxs = []
        left_max = height[0]
        for h in height:
            left_max = max(h, left_max)
            left_maxs.append(left_max)
        print(left_maxs)
        
        right_maxs = []
        right_max = height[-1]
        for h in reversed(height):
            right_max = max(h, right_max)
            right_maxs.append(right_max)
        right_maxs.reverse()
        print(right_maxs)
        
        water = 0
        for i in range(len(height)):
            water += min(left_maxs[i], right_maxs[i]) - height[i]
        return water
        
