class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        lenth = len(nums)
        if lenth < 2: 
            return nums
            
        left, right = 0, 0
        
        while right < lenth :
            # find the first zero, left point to zero
            while left < lenth and nums[left]:
                left += 1 
            
            # find the first none zero after left
            right = left
            while right < lenth and not nums[right]:
                right += 1
                
            if right < lenth:
                nums[left], nums[right] = nums[right], nums[left]
            
            # print(left, right, nums)
            
