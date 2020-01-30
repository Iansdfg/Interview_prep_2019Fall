class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1 
            
        start, end  = 0, len(nums)-1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] > target:
                end = mid
                
            elif nums[mid] < target:
                start = mid
                
            else:
                start = mid 
        
        if nums[end] == target:
            return end 
        elif nums[start] == target:
            return start
        return -1
            
