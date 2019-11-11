class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here

        if sorted(nums[:])[::-1] == nums:
            return nums[::-1]
        
        
        first_down, slightly_large= len(nums)-1, len(nums)-1

        for first_down in range(len(nums)-2, -1, -1):
            if nums[first_down] < nums[first_down + 1]:
                break 

        for slightly_large in range(len(nums)-1, first_down, -1):
            if nums[slightly_large] > nums[first_down]:
                nums[slightly_large], nums[first_down] = nums[first_down], nums[slightly_large]
                break
        nums = nums[:first_down+1] + nums[first_down+1:][::-1]
        
        return nums
            
        
 
